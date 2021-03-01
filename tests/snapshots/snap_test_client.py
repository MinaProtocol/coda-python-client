# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestCodaClient.test_get_daemon_status 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { daemonStatus { addrsAndPorts { bindIp clientPort externalIp libp2pPort peer { host libp2pPort peerId } } blockProductionKeys blockchainLength commitId confDir consensusConfiguration { acceptableNetworkDelay delta epochDuration genesisStateTimestamp k slotDuration slotsPerEpoch } consensusMechanism consensusTimeBestTip { endTime epoch globalSlot slot startTime } consensusTimeNow { endTime epoch globalSlot slot startTime } highestBlockLengthReceived ledgerMerkleRoot nextBlockProduction { times { endTime epoch globalSlot slot startTime } } numAccounts peers snarkWorkFee snarkWorker stateHash syncStatus uptimeSecs userCommandsSent } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_daemon_version 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ version }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_wallets 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ ownedWallets { publicKey balance { total } } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_current_snark_worker 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ currentSnarkWorker { key fee } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_sync_status 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': '{ daemonStatus { syncStatus } }'
            }
        }
    ,)
]

snapshots['TestCodaClient.test_set_current_snark_worker 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation($worker_pk: PublicKey!, $fee: UInt64!) { setSnarkWorker(input: { publicKey: $worker_pk }) { lastSnarkWorker } setSnarkWorkFee(input: { fee: $fee }) }',
                'variables': {
                    'fee': 1,
                    'worker_pk': 'pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_wallet 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query($publicKey: PublicKey!) { wallet(publicKey: $publicKey) { publicKey balance { total unknown } nonce receiptChainHash delegate votingFor stakingActive privateKeyPath } }',
                'variables': {
                    'publicKey': 'pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_transaction_status 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query($paymentId: ID!) { transactionStatus(payment: $paymentId) }',
                'variables': {
                    'paymentId': 'payment_id'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_create_wallet 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation($password: String!) { createAccount(input: { password: $password }) { publicKey } }',
                'variables': {
                    'password': 'password'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_send_payment 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation( $from: PublicKey! $to: PublicKey! $amount: UInt64! $fee: UInt64! $memo: String ) { sendPayment( input: { from: $from, to: $to, amount: $amount, fee: $fee, memo: $memo } ) { payment { id isDelegation nonce from to amount fee memo } } }',
                'variables': {
                    'amount': 1000000000,
                    'fee': 100000000,
                    'from': 'from_pk',
                    'memo': 'memo',
                    'to': 'to_pk'
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_best_chain 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query ($maxLength: Int!) { bestChain(maxLength: $maxLength) { protocolState { consensusState { blockHeight } previousStateHash } stateHash } }',
                'variables': {
                    'maxLength': 42
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_block_by_height 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query ($height: Int!) { block(height: $height) { stateHash creator snarkJobs { fee prover } } }',
                'variables': {
                    'height': 42
                }
            }
        }
    ,)
]

snapshots['TestCodaClient.test_get_block_by_state_hash 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query ($stateHash: String!) { block(stateHash: $stateHash) { creator protocolState { consensusState { blockHeight } } snarkJobs { fee prover } } }',
                'variables': {
                    'stateHash': 'some_state_hash'
                }
            }
        }
    ,)
]
