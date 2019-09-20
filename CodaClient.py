#!/usr/bin/python3

import requests
import time
import json
import asyncio
import websockets
import logging

class Client():
  # Implements a GraphQL Client for the Coda Daemon

  def __init__(
      self,
      graphql_protocol: str = "http",
      websocket_protocol: str = "ws",
      graphql_host: str = "localhost",
      graphql_path: str = "/graphql",
      graphql_port: int = 8304,
  ):
    self.endpoint = "{}://{}:{}{}".format(graphql_protocol, graphql_host, graphql_port, graphql_path)
    self.websocket_endpoint = "{}://{}:{}{}".format(websocket_protocol, graphql_host, graphql_port, graphql_path)
    self.logger = logging.getLogger(__name__)

  def _send_query(self, query: str, variables: dict = {}) -> dict:
    """Sends a query to the Coda Daemon's GraphQL Endpoint
    
    Arguments:
        query {str} -- A GraphQL Query
    
    Keyword Arguments:
        variables {dict} -- Optional Variables for the query (default: {{}})
    
    Returns:
        dict -- A Response object from the GraphQL Server.
    """
    return self._graphql_request(query, variables)

  def _send_mutation(self, query: str, variables: dict = {}) -> dict:
    """Sends a mutation to the Coda Daemon's GraphQL Endpoint.
    
    Arguments:
        query {str} -- A GraphQL Mutation
    
    Keyword Arguments:
        variables {dict} -- Variables for the mutation (default: {{}})
    
    Returns:
        dict -- A Response object from the GraphQL Server.
    """
    return self._graphql_request(query, variables)
  
  def _graphql_request(self, query: str, variables: dict = {}):
    """GraphQL queries all look alike, this is a generic function to facilitate a GraphQL Request.
    
    Arguments:
        query {str} -- A GraphQL Query
    
    Keyword Arguments:
        variables {dict} -- Optional Variables for the GraphQL Query (default: {{}})
    
    Raises:
        Exception: Raises an exception if the response is anything other than 200.
    
    Returns:
        dict -- Returns the JSON Response as a Dict.
    """
    # Strip all the whitespace and replace with spaces
    query = " ".join(query.split())
    payload = {'query': query}
    if variables:
      payload = { **payload, 'variables': variables }

    headers = {
      "Accept": "application/json"
    }
    self.logger.debug("Sending a Query: {}".format(payload))
    response = requests.post(self.endpoint, json=payload, headers=headers)
    if response.status_code == 200:
      self.logger.debug("Got a Response: {}".format(response.json()))
      return response.json()
    else:
      print(response.text)
      raise Exception(
          "Query failed -- returned code {}. {}".format(response.status_code, query))
  
  async def _graphql_subscription(self, query: str, variables: dict = {}, callback = None): 
    hello_message = {"type": "connection_init", "payload": {}}

    # Strip all the whitespace and replace with spaces
    query = " ".join(query.split())
    payload = {'query': query}
    if variables:
      payload = { **payload, 'variables': variables }
    
    query_message = {"id": "1", "type": "start", "payload": payload}
    self.logger.info("Listening to GraphQL Subscription...")
    
    uri = self.websocket_endpoint
    async with websockets.client.connect(uri, ping_timeout=None) as websocket:
      # Set up Websocket Connection
      self.logger.debug("WEBSOCKET -- Sending Hello Message: {}".format(hello_message))
      await websocket.send(json.dumps(hello_message))
      resp = await websocket.recv()
      self.logger.debug("WEBSOCKET -- Recieved Response {}".format(resp))
      self.logger.debug("WEBSOCKET -- Sending Subscribe Query: {}".format(query_message))
      await websocket.send(json.dumps(query_message))

      # Wait for and iterate over messages in the connection
      async for message in websocket:
        self.logger.debug("Recieved a message from a Subscription: {}".format(message))
        if callback: 
          await callback(message)
        else:
          print(message)
  
  def get_daemon_status(self) -> dict:
    """Gets the status of the currently configured Coda Daemon.
    
    Returns:
         dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    query {
      daemonStatus {
        numAccounts
        blockchainLength
        highestBlockLengthReceived
        uptimeSecs
        ledgerMerkleRoot
        stateHash
        commitId
        peers
        userCommandsSent
        snarkWorker
        snarkWorkFee
        syncStatus
        proposePubkeys
        consensusTimeBestTip
        consensusTimeNow
        consensusMechanism
        confDir
        commitId
        consensusConfiguration {
          delta
          k
          c
          cTimesK
          slotsPerEpoch
          slotDuration
          epochDuration
          acceptableNetworkDelay
        }
      }
    }
    '''
    res = self._send_query(query)
    return res['data']

  def get_daemon_version(self) -> dict:
    """Gets the version of the currently configured Coda Daemon.
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    {
        version
    }
    '''
    res = self._send_query(query)
    return res["data"]

  def get_wallets(self) -> dict:
    """Gets the wallets that are currently installed in the Coda Daemon.
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    {
      ownedWallets {
        publicKey
        balance {
          total
        }
      }
    }
    '''
    res = self._send_query(query)
    return res["data"]

  def get_wallet(self, pk: str) -> dict:
    """Gets the wallet for the specified Public Key.
    
    Arguments:
        pk {str} -- A Public Key corresponding to a currently installed wallet.
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    query($publicKey:PublicKey!){
      wallet(publicKey:$publicKey) {
        publicKey
    		balance {
    		  total
    		  unknown
    		}
        nonce
        receiptChainHash
        delegate
        votingFor
        stakingActive
        privateKeyPath
      }
    }
    '''
    variables = {
      "publicKey": pk
    }
    res = self._send_query(query, variables)
    return res["data"]

  def get_blocks(self) -> dict:
    """Gets the blocks known to the Coda Daemon. 
    Mostly useful for Archive nodes. 
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    {
      blocks{
        nodes {
          creator
          stateHash
          protocolState {
            previousStateHash
            blockchainState{
              date
              snarkedLedgerHash
              stagedLedgerHash
            }
          }
          transactions {
            userCommands{
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
          snarkJobs {
            prover
            fee
            workIds
          }
        }
        pageInfo {
          hasNextPage
          hasPreviousPage
          firstCursor
          lastCursor
        }
      }
    }
    '''
    res = self._send_query(query)
    return res["data"]    

  def get_current_snark_worker(self) -> dict:
    """Gets the currently configured SNARK Worker from the Coda Daemon. 
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    {
      currentSnarkWorker{
        key
        fee
      }
    }
    '''
    res = self._send_query(query)
    return res["data"]

  def get_sync_status(self) -> dict:
    """Gets the Sync Status of the Coda Daemon.
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    {
      syncStatus
    }
    '''
    res = self._send_query(query)
    return res["data"]

  def set_current_snark_worker(self, worker_pk: str, fee: str) -> dict: 
    """Set the current SNARK Worker preference. 
    
    Arguments:
        worker_pk {str} -- The public key corresponding to the desired SNARK Worker
        fee {str} -- The desired SNARK Work fee
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict
    """
    query = '''
    {
      syncStatus
    }
    '''
    res = self._send_query(query)
    return res["data"]

  def create_wallet(self) -> dict:
    """Creates a new wallet and returns the public key.
    
    Arguments:
      N/A
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict
    """
    query = '''
    mutation{
      addWallet {
        publicKey
      }
    }
    '''
    res = self._send_mutation(query)
    return res["data"]

  def send_payment(self, to_pk: str, from_pk: str, amount: int, fee: int, memo: str) -> dict:
    """Send a payment from the specified wallet to the specified target wallet. 
    
    Arguments:
        to_pk {PublicKey} -- The target wallet where funds should be sent
        from_pk {PublicKey} -- The installed wallet which will finance the payment
        amount {UInt64} -- Tha amount of Coda to send
        fee {UInt64} -- The transaction fee that will be attached to the payment
        memo {str} -- A memo to attach to the payment
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict
    """
    query = '''
    mutation($from:PublicKey!, $to:PublicKey!, $amount:UInt64!, $fee:UInt64!, $memo:String){
      sendPayment(input: {
        from:$from,
        to:$to,
        amount:$amount,
        fee:$fee,
        memo:$memo
      }) {
        payment {
          id,
          isDelegation,
          nonce,
          from,
          to,
          amount,
          fee,
          memo
        }
      }
    }
    '''
    variables = {
      "from": from_pk,
      "to": to_pk,
      "amount": amount,
      "fee": fee,
      "memo": memo
    }
    res = self._send_mutation(query, variables)
    return res["data"]

  def get_pooled_payments(self, pk: str) -> dict:
    """Get the current transactions in the payments pool 
    
    Arguments:
        pk {str} -- The public key corresponding to the installed wallet that will be queried 
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict
    """
    query = '''
    query ($publicKey:String!){
      pooledUserCommands(publicKey:$publicKey) {
        id,
        isDelegation,
        nonce,
        from,
        to,
        amount,
        fee,
        memo
      }
    }
    '''
    variables = {
      "publicKey": pk
    }
    res = self._send_query(query, variables)
    return res["data"]

  def get_transaction_status(self, payment_id: str) -> dict:
    """Get the transaction status for the specified Payment Id.
    
    Arguments:
        payment_id {str} -- A Payment Id corresponding to a UserCommand.
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    query($paymentId:ID!){
      transactionStatus(payment:$paymentId)
    }
    '''
    variables = {
      "paymentId": payment_id
    }
    res = self._send_query(query, variables)
    return res["data"]    

  async def listen_sync_update(self, callback):
    """Creates a subscription for Network Sync Updates
    """
    query = '''
    subscription{
      newSyncUpdate 
    }
    '''
    await self._graphql_subscription(query, {}, callback)
    
  async def listen_block_confirmations(self, callback):
    """Creates a subscription for Block Confirmations
    Calls callback when a new block is recieved. 
    """
    query = '''
    subscription{
      blockConfirmation {
        stateHash
        numConfirmations
      }
    }
    '''
    await self._graphql_subscription(query, {}, callback)

  async def listen_new_blocks(self, pk: str, callback):
    """Creates a subscription for new blocks created by a proposer using a particular private key.
    
    Arguments:
        pk {PublicKey} -- The public key to use to filter blocks
    """
    query = '''
    subscription($pk:PublicKey){
      newBlock(publicKey:$pk){
        creator
        stateHash
        protocolState {
          previousStateHash
          blockchainState {
            date
            snarkedLedgerHash
            stagedLedgerHash
          }
        },
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
    '''
    variables = {
      "pk": pk
    }
    await self._graphql_subscription(query, variables, callback)