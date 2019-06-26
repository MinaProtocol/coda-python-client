# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestCodaClient.test_get_daemon_status 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': 'query { daemonStatus { numAccounts blockCount uptimeSecs ledgerMerkleRoot stagedLedgerHash stateHash peers userCommandsSent runSnarkWorker proposePubkeys consensusTimeNow consensusTimeBestTip consensusMechanism consensusConfiguration { delta k c cTimesK slotsPerEpoch slotDuration epochDuration acceptableNetworkDelay } } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_daemon_version 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': '{ version }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_wallets 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': '{ ownedWallets { publicKey } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_balance 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': 'query($publicKey:String!){ balance(publicKey:$publicKey) }',
                'variables': {
                    'publicKey': 'pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_current_snark_worker 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': '{ currentSnarkWorker{ key fee } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_sync_status 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': '{ syncStatus }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_set_current_snark_worker 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': '{ syncStatus }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_create_wallet_with_args 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': 'mutation($publicKey:String, $privateKey:String){ addWallet(input: { publicKey:$publicKey, privateKey:$privateKey }) { publicKey } }',
                'variables': {
                    'privateKey': 'sk',
                    'publicKey': 'pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_create_wallet_no_args 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': 'mutation($publicKey:String, $privateKey:String){ addWallet(input: { publicKey:$publicKey, privateKey:$privateKey }) { publicKey } }',
                'variables': {
                    'privateKey': '',
                    'publicKey': ''
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_send_payment 1'] = [
    (
        (
            'http://localhost:8080/graphql'
        ,),
        {
            'json': {
                'query': 'mutation($from:String!, $to:String!, $amount:String!, $fee:String!, $memo:String){ sendPayment(input: { from:$from, to:$to, amount:$amount, fee:$fee, memo:$memo }) { payment { id, isDelegation, nonce, from, to, amount, fee, memo } } }',
                'variables': {
                    'amount': 'amount',
                    'fee': 'fee',
                    'from': 'from_pk',
                    'memo': 'memo',
                    'to': 'to_pk'
                }
            }
        }
    ,)
]
