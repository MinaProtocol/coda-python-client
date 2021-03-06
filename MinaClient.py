#!/usr/bin/python3

import json
import logging
import random
from enum import Enum

import requests
import sgqlc
import websockets
from sgqlc.operation import Operation

from mina_schema import mina_schema


class CurrencyFormat(Enum):
    """An Enum representing different formats of Currency in mina.

    Constants:
        WHOLE - represents whole mina (1 whole mina == 10^9 nanominas)
        NANO - represents the atomic unit of mina
    """

    WHOLE = 1
    NANO = 2


class CurrencyUnderflow(Exception):
    pass


class Currency:
    """A convenience wrapper around interacting with mina currency values.

    This class supports performing math on Currency values of differing formats.
    Currency instances can be added or subtracted. Currency instances can also
    be scaled through multiplication (either against another Currency instance
    or a int scalar).
    """
    @classmethod
    def __nanominas_from_int(_cls, n):
        return n * 1000000000

    @classmethod
    def __nanominas_from_string(_cls, s):
        segments = s.split(".")
        if len(segments) == 1:
            return int(segments[0])
        elif len(segments) == 2:
            [l, r] = segments
            if len(r) <= 9:
                return int(l + r + ("0" * (9 - len(r))))
            else:
                raise Exception("invalid mina currency format: %s" % s)

    @classmethod
    def random(_cls, lower_bound, upper_bound):
        """Generates a random Currency instance.

        Currency is between a provided lower_bound and upper_bound

        Args:
            lower_bound {Currency} -- A Currency instance representing the lower
              bound for the randomly generated value
            upper_bound {Currency} -- A Currency instance representing the upper
              bound for the randomly generated value

        Returns:
            Currency - A randomly generated Currency instance between the
              lower_bound and upper_bound
        """
        if not (isinstance(lower_bound, Currency)
                and isinstance(upper_bound, Currency)):
            raise Exception(
                "invalid call to Currency.random: lower and upper bound must "
                "be instances of Currency")
        if not upper_bound.nanominas() >= lower_bound.nanominas():
            raise Exception(
                "invalid call to Currency.random: upper_bound is not greater "
                "than lower_bound")
        if lower_bound == upper_bound:
            return lower_bound
        bound_range = upper_bound.nanominas() - lower_bound.nanominas()
        delta = random.randint(0, bound_range)
        return lower_bound + Currency(delta, format=CurrencyFormat.NANO)

    def __init__(self, value, format=CurrencyFormat.WHOLE):
        """Constructs a new Currency instance.

        Values of different CurrencyFormats may be passed in to construct the
        instance.
        In the case of format=CurrencyFormat.WHOLE, then it is interpreted as
        value * 10^9 nanominas.
        In the case of format=CurrencyFormat.NANO, value is only allowed to be
        an int, as there can be no decimal point for nanominas.

        Args:
            value {int|float|string} - The value to construct the Currency
              instance from format {CurrencyFormat} - The representation format
              of the value

        Returns:
            Currency - The newly constructed Currency instance
        """
        if format == CurrencyFormat.WHOLE:
            if isinstance(value, int):
                self.__nanominas = Currency.__nanominas_from_int(value)
            elif isinstance(value, float):
                self.__nanominas = Currency.__nanominas_from_string(str(value))
            elif isinstance(value, str):
                self.__nanominas = Currency.__nanominas_from_string(value)
            else:
                raise Exception("cannot construct whole Currency from %s" %
                                type(value))
        elif format == CurrencyFormat.NANO:
            if isinstance(value, int):
                self.__nanominas = value
            else:
                raise Exception("cannot construct nano Currency from %s" %
                                type(value))
        else:
            raise Exception("invalid Currency format %s" % format)

    def decimal_format(self):
        """Computes string decimal format representation of a Currency instance.

        Returns:
            str - The decimal format representation of the Currency instance
        """
        s = str(self.__nanominas)
        if len(s) > 9:
            return s[:-9] + "." + s[-9:]
        else:
            return "0." + ("0" * (9 - len(s))) + s

    def nanominas(self):
        """Accesses the raw nanominas representation of a Currency instance.

        Returns:
            int - The nanominas of the Currency instance represented as an
              integer
        """
        return self.__nanominas

    def __str__(self):
        return self.decimal_format()

    def __repr__(self):
        return "Currency(%s)" % self.decimal_format()

    def __add__(self, other):
        if isinstance(other, Currency):
            return Currency(self.nanominas() + other.nanominas(),
                            format=CurrencyFormat.NANO)
        else:
            raise Exception("cannot add Currency and %s" % type(other))

    def __sub__(self, other):
        if isinstance(other, Currency):
            new_value = self.nanominas() - other.nanominas()
            if new_value >= 0:
                return Currency(new_value, format=CurrencyFormat.NANO)
            else:
                raise CurrencyUnderflow()
        else:
            raise Exception("cannot subtract Currency and %s" % type(other))

    def __mul__(self, other):
        if isinstance(other, int):
            return Currency(self.nanominas() * other,
                            format=CurrencyFormat.NANO)
        elif isinstance(other, Currency):
            return Currency(self.nanominas() * other.nanominas(),
                            format=CurrencyFormat.NANO)
        else:
            raise Exception("cannot multiply Currency and %s" % type(other))


class Client:
    # Implements a GraphQL Client for the Mina Daemon

    def __init__(
        self,
        graphql_protocol: str = "http",
        websocket_protocol: str = "ws",
        graphql_host: str = "localhost",
        graphql_path: str = "/graphql",
        graphql_port: int = 3085,
    ):
        self.endpoint = "{}://{}:{}{}".format(graphql_protocol, graphql_host,
                                              graphql_port, graphql_path)
        self.websocket_endpoint = "{}://{}:{}{}".format(
            websocket_protocol, graphql_host, graphql_port, graphql_path)
        self.logger = logging.getLogger(__name__)

    def _send_sgqlc_query(self,
                          query: sgqlc.operation.Operation,
                          variables: dict = {}) -> dict:
        """Sends a query to the Mina Daemon's GraphQL Endpoint

        Args:
            query {str} -- A GraphQL Query
            variables {dict} -- Optional Variables for the query (default: {{}})

        Returns:
            dict -- A Response object from the GraphQL Server.
        """
        return self._graphql_request(bytes(query).decode('utf-8'), variables)

    def _send_query(self, query: str, variables: dict = {}) -> dict:
        """Sends a query to the Mina Daemon's GraphQL Endpoint
    
        Args:
            query {str} -- A GraphQL Query
            variables {dict} -- Optional Variables for the query (default: {{}})

        Returns:
            dict -- A Response object from the GraphQL Server.
        """
        return self._graphql_request(query, variables)

    def _send_mutation(self, query: str, variables: dict = {}) -> dict:
        """Sends a mutation to the Mina Daemon's GraphQL Endpoint.
    
        Args:
            query {str} -- A GraphQL Mutation
            variables {dict} -- Variables for the mutation (default: {{}})

        Returns:
            dict -- A Response object from the GraphQL Server.
        """
        return self._graphql_request(query, variables)

    def _graphql_request(self, query: str, variables: dict = {}):
        """Function to facilitate a GraphQL Request.

        GraphQL queries all look alike, this is a generic function to
        facilitate a GraphQL Request.
    
        Args:
            query {str} -- A GraphQL Query
            variables {dict} -- Optional Variables for the GraphQL Query
              (default: {{}})

        Returns:
            dict -- Returns the JSON Response as a Dict.

        Raises:
            Exception: Raises an exception if the response is anything other
              than 200.
        """
        # Strip all the whitespace and replace with spaces
        query = " ".join(query.split())
        #print(query)
        payload = {"query": query}
        if variables:
            payload = {**payload, "variables": variables}

        #print(payload)
        #print(type(payload))

        headers = {"Accept": "application/json"}
        self.logger.debug("Sending a Query: {}".format(payload))
        response = requests.post(self.endpoint, json=payload, headers=headers)
        resp_json = response.json()
        if response.status_code == 200 and "errors" not in resp_json:
            self.logger.debug("Got a Response: {}".format(response.json()))
            return resp_json
        else:
            print(response.text)
            raise Exception(
                "Query failed -- returned code {}. {} -> {}".format(
                    response.status_code, query, response.json()))

    async def _graphql_subscription(self,
                                    query: str,
                                    variables: dict = {},
                                    callback=None):
        hello_message = {"type": "connection_init", "payload": {}}

        # Strip all the whitespace and replace with spaces
        query = " ".join(query.split())
        payload = {"query": query}
        if variables:
            payload = {**payload, "variables": variables}

        query_message = {"id": "1", "type": "start", "payload": payload}
        self.logger.info("Listening to GraphQL Subscription...")

        uri = self.websocket_endpoint
        self.logger.info(uri)
        async with websockets.client.connect(uri,
                                             ping_timeout=None) as websocket:
            # Set up Websocket Connection
            self.logger.debug(
                "WEBSOCKET -- Sending Hello Message: {}".format(hello_message))
            await websocket.send(json.dumps(hello_message))
            resp = await websocket.recv()
            self.logger.debug("WEBSOCKET -- Recieved Response {}".format(resp))
            self.logger.debug(
                "WEBSOCKET -- Sending Subscribe Query: {}".format(
                    query_message))
            await websocket.send(json.dumps(query_message))

            # Wait for and iterate over messages in the connection
            async for message in websocket:
                self.logger.debug(
                    "Recieved a message from a Subscription: {}".format(
                        message))
                if callback:
                    await callback(message)
                else:
                    print(message)

    def get_daemon_status(self, fields: list = None) -> dict:
        """Gets the status of the currently configured Mina Daemon.
    
        Returns:
             dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        if not fields:
            fields = []

        op = Operation(mina_schema.query)
        op.daemon_status().__fields__(*fields)

        res = self._send_sgqlc_query(op)

        return res["data"]

    def get_sync_status(self) -> dict:
        """Gets the Sync Status of the Mina Daemon.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        return self.get_daemon_status(fields=['sync_status'])

    def get_daemon_version(self) -> dict:
        """Gets the version of the currently configured Mina Daemon.
    
        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        op = Operation(mina_schema.query)
        op.version()

        res = self._send_sgqlc_query(op)
        return res["data"]

    def get_wallets(self, fields: list = None) -> dict:
        """Gets the wallets that are currently installed in the Mina Daemon.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """

        default_fields = ['public_key', 'balance']

        fields = [] if isinstance(fields,
                                  list) and not len(fields) else default_fields

        op = Operation(mina_schema.query)
        op.owned_wallets().__fields__(*fields)

        res = self._send_sgqlc_query(op)
        return res["data"]

    def get_wallet(self, pk: str, fields: list = None) -> dict:
        """Gets the wallet for the specified Public Key.
    
        Args:
            pk {str} -- A Public Key corresponding to a currently installed
              wallet.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        default_fields = [
            'balance', 'nonce', 'receipt_chain_hash', 'delegate', 'voting_for',
            'staking_active', 'private_key_path'
        ]

        fields = [] if isinstance(fields,
                                  list) and not len(fields) else default_fields

        op = Operation(mina_schema.query)
        op.wallet(public_key=pk).__fields__(*fields)

        res = self._send_sgqlc_query(op)
        return res["data"]

    def create_wallet(self, password: str) -> dict:
        """Creates a new Wallet.
    
        Args:
            password {str} -- A password for the wallet to unlock.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """

        op = Operation(mina_schema.mutation)
        op.create_account(input={'password': password})
        res = self._send_sgqlc_query(op)
        return res["data"]

    def unlock_wallet(self, pk: str, password: str) -> dict:
        """Unlocks the wallet for the specified Public Key.

        Args:
            pk: Public Key corresponding to a currently installed
              wallet.
            password: password for the wallet to unlock.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        op = Operation(mina_schema.mutation)
        op.unlock_wallet(input={'public_key': pk, 'password': password})
        res = self._send_sgqlc_query(op)
        return res["data"]

    def lock_wallet(self, pk: str, password: str) -> dict:
        """Unlocks the wallet for the specified Public Key.

        Args:
            pk: Public Key corresponding to a currently installed
              wallet.
            password: password for the wallet to unlock.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        op = Operation(mina_schema.mutation)
        op.lock_wallet(input={'public_key': pk, 'password': password})
        res = self._send_sgqlc_query(op)
        return res["data"]

    def get_current_snark_worker(self, fields: list = None) -> dict:
        """Gets the currently configured SNARK Worker from the Mina Daemon.
    
        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        default_fields = ['key', 'fee']

        fields = [] if isinstance(fields,
                                  list) and not len(fields) else default_fields

        op = Operation(mina_schema.query)
        op.current_snark_worker().__fields__(*fields)

        res = self._send_sgqlc_query(op)
        return res["data"]

    def set_current_snark_worker(self, worker_pk: str, fee: int) -> dict:
        """Set the current SNARK Worker preference. 
    
        Args:
            worker_pk: the public key corresponding to the desired SNARK
              Worker
            fee: the desired SNARK Work fee

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict
        """
        op = Operation(mina_schema.mutation)
        op.set_snark_worker(input={'public_key': worker_pk})
        op.set_snark_work_fee(input={'fee': fee})
        res = self._send_sgqlc_query(op)
        return res["data"]

    def send_payment(self, to_pk: str, from_pk: str, amount: Currency,
                     fee: Currency, memo: str) -> dict:
        """Send a payment from the specified wallet to specified target wallet.
    
        Args:
            to_pk: The target wallet where funds should be sent
            from_pk: The installed wallet which will finance the
              payment
            amount: Currency instance. The amount of Mina to send
            fee: Currency instance. The transaction fee that will be attached to
              the payment
            memo:  memo to attach to the payment

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict
        """

        #TODO(Jan): add this once cconnected to a differetn testaccount
        default_fields = [
            'id', 'isDelegation', 'nonce', 'from', 'to', 'amount', 'fee',
            'memo'
        ]

        op = Operation(mina_schema.mutation)
        op.send_payment(
            input={
                "from": from_pk,
                "to": to_pk,
                "fee": fee.nanominas(),
                "memo": memo,
                "amount": amount.nanominas(),
            })
        res = self._send_sgqlc_query(op)

        return res["data"]

    def get_pooled_payments(self, pk: str) -> dict:
        """Get the current transactions in the payments pool.
    
        Args:
            pk: The public key corresponding to the installed wallet
              that will be queried

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict
        """
        query = """
        query($publicKey: String!) {
          pooledUserCommands(publicKey: $publicKey) {
            id
            isDelegation
            nonce
            from
            to
            amount
            fee
            memo
          }
        }
        """
        variables = {"publicKey": pk}
        res = self._send_query(query, variables)
        return res["data"]

    def get_transaction_status(self, payment_id: str) -> dict:
        """Get the transaction status for the specified Payment Id.
    
        Args:
            payment_id: Payment Id corresponding to a UserCommand.

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        query = """
        query($paymentId: ID!) {
          transactionStatus(payment: $paymentId)
        }
        """
        variables = {"paymentId": payment_id}
        res = self._send_query(query, variables)
        return res["data"]

    def get_best_chain(self, max_length: int = 10) -> dict:
        """Get the best blockHeight and stateHash for the canonical chain.

        Returns max_length items in descending order

        Args:
          max_length: defaults to 10

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        query = """
        query ($maxLength: Int!) {
          bestChain(maxLength: $maxLength) {
            protocolState {
              consensusState {
                blockHeight
              }
              previousStateHash
            }
            stateHash
          }
        }
        """
        variables = {"maxLength": max_length}
        res = self._send_query(query, variables)
        return res["data"]

    def get_block_by_height(self, height: int) -> dict:
        """Get the block data by block height.

        Returns stateHash, block creator and snarkJobs

        Args:
          height: block height

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        query = """
        query ($height: Int!) {
          block(height: $height) {
            stateHash
            creator
            snarkJobs {
              fee
              prover
            }
          }
        }
        """
        variables = {"height": height}
        res = self._send_query(query, variables)
        return res["data"]

    def get_block_by_state_hash(self, state_hash: str) -> dict:
        """Get the block data by state hash.

        Returns block height, block creator and snarkJobs

        Args:
          state_hash: state hash

        Returns:
            dict -- Returns the "data" field of the JSON Response as a Dict.
        """
        query = """
        query ($stateHash: String!) {
          block(stateHash: $stateHash) {
            creator
            protocolState {
              consensusState {
                blockHeight
              }
            }
            snarkJobs {
              fee
              prover
            }
          }
        }
        """
        variables = {"stateHash": state_hash}
        res = self._send_query(query, variables)
        return res["data"]

    def send_any_query(self, query, variables=None):
        if not variables:
            variables = {}

        res = self._send_query(query, variables)
        return res["data"]



    async def listen_sync_update(self, callback):
        """Creates a subscription for Network Sync Updates. """
        query = """
        subscription {
          newSyncUpdate
        }
        """
        await self._graphql_subscription(query, {}, callback)

    async def listen_block_confirmations(self, callback):
        """Creates a subscription for Block Confirmations.

        Calls callback when a new block is received.
        """
        query = """
        subscription {
          blockConfirmation {
            stateHash
            numConfirmations
          }
        }
        """
        await self._graphql_subscription(query, {}, callback)

    async def listen_new_blocks(self, callback):
        """Creates a subscription for new blocks.

         Calls `callback` each time the subscription fires.
    
        Args:
            callback(block) {coroutine} -- This coroutine is executed with the
            new block as an argument each time the subscription fires
        """
        query = """
        subscription {
          newBlock {
            creator
            stateHash
            protocolState {
              previousStateHash
              blockchainState {
                date
                snarkedLedgerHash
                stagedLedgerHash
              }
            }
            transactions {
              userCommands {
                id
                isDelegation
                nonce
                from
                to
                amount
                fee
                memo
              }
              feeTransfer {
                recipient
                fee
              }
              coinbase
            }
          }
        }
        """
        variables = {}
        await self._graphql_subscription(query, variables, callback)
