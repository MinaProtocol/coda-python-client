#!/usr/bin/python3

import requests

class Client():
  # Implements a GraphQL Client for the Coda Daemon

  def __init__(
      self,
      graphql_protocol: str = "http",
      graphql_host: str = "localhost",
      graphql_path: str = "/graphql",
      graphql_port: int = 8080,
  ):
    self.endpoint = f"{graphql_protocol}://{graphql_host}:{graphql_port}{graphql_path}"

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

  def _send_mutation(self, query: str, variables: dict) -> dict:
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
    payload = {'query': query}
    if variables:
      payload = { **payload, 'variables': variables }
    request = requests.post(self.endpoint, json=payload)
    if request.status_code == 200:
      return request.json()
    else:
      raise Exception(
          f"Query failed -- returned code {request.status_code}. {query}")
  
  def get_daemon_status(self) -> dict:
    """Gets the status of the currently configured Coda Daemon.
    
    Returns:
         dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    query {
      daemonStatus {
        numAccounts
        blockCount
        uptimeSecs
        ledgerMerkleRoot
        stagedLedgerHash
        stateHash
        peers
        userCommandsSent
        runSnarkWorker
        proposePubkeys
        consensusTimeNow
        consensusTimeBestTip
        consensusMechanism
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
    query = '''
    {
      ownedWallets {
        publicKey
      }
    }
    '''
    res = self._send_query(query)
    return res["data"]

  def get_balance(self, pk: str) -> dict:
    """Gets the balance for the specified Public Key.
    
    Arguments:
        pk {str} -- A Public Key corresponding to a currently installed wallet.
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict.
    """
    query = '''
    query($publicKey:String!){
      balance(publicKey:$publicKey)
    }
    '''
    variables = {
      "publicKey": pk
    }
    res = self._send_query(query, variables)
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

  def create_wallet(self, pk: str, sk: str) -> dict:
    """Creates a new wallet with the specified Public and Secret Keys.
    
    Arguments:
        pk {str} -- The private key for the new wallet
        sk {str} -- The secret key for the new wallet
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict
    """
    query = '''
    mutation($publicKey:String, $privateKey:String){
      addWallet(input: {
        publicKey:$publicKey,
        privateKey:$privateKey
      }) {
        publicKey
      }
    }
    '''
    variables = {
      "publicKey": pk,
      "privateKey": sk
    }
    res = self._send_mutation(query, variables)
    return res["data"]

  def send_payment(self, to_pk: str, from_pk: str, amount: str, fee: str, memo: str) -> dict:
    """Send a payment from the specified wallet to the specified tatget wallet. 
    
    Arguments:
        to_pk {str} -- The target wallet where funds should be sent
        from_pk {str} -- The installed wallet which will finance the payment
        amount {str} -- Tha amount of Coda to send
        fee {str} -- The transaction fee that will be attached to the payment
        memo {str} -- A memo to attach to the payment
    
    Returns:
        dict -- Returns the "data" field of the JSON Response as a Dict
    """
    query = '''
    mutation($from:String!, $to:String!, $amount:String!, $fee:String!, $memo:String){
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

  def listen_new_blocks(self, key: str):
    query = '''
      subscription($key:String){
        newBlock(key:$key){
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
      "key": key
    }
    pass

  def listen_block_confirmations(self):
    query = '''
    subscription{
      blockConfirmation {
        stateHash
        numConfirmations
      }
    }
    '''
    pass

  def listen_sync_update(self):
    query = '''
    subscription{
      newSyncUpdate 
    }
    '''
    pass

if __name__ == "__main__":
  client = Client()
  print(client.get_pooled_payments("foo"))
