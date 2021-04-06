# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import Snapshot


snapshots = Snapshot()

snapshots['TestMinaClient.test_get_daemon_status 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { daemonStatus { numAccounts blockchainLength highestBlockLengthReceived highestUnvalidatedBlockLengthReceived uptimeSecs ledgerMerkleRoot stateHash chainId commitId confDir peers { host libp2pPort peerId } userCommandsSent snarkWorker snarkWorkFee syncStatus catchupStatus blockProductionKeys histograms { externalTransitionLatency { values underflow overflow } acceptedTransitionLocalLatency { values underflow overflow } acceptedTransitionRemoteLatency { values underflow overflow } snarkWorkerTransitionTime { values underflow overflow } snarkWorkerMergeTime { values underflow overflow } } consensusTimeBestTip { epoch slot globalSlot startTime endTime } globalSlotSinceGenesisBestTip nextBlockProduction { times { epoch slot globalSlot startTime endTime } globalSlotSinceGenesis generatedFromConsensusAt { globalSlotSinceGenesis } } consensusTimeNow { epoch slot globalSlot startTime endTime } consensusMechanism consensusConfiguration { delta k slotsPerEpoch slotDuration epochDuration genesisStateTimestamp acceptableNetworkDelay } addrsAndPorts { externalIp bindIp peer { host libp2pPort peerId } libp2pPort clientPort } } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_daemon_version 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { version }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_wallets 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { ownedWallets { publicKey balance { total unknown liquid locked blockHeight stateHash } } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_current_snark_worker 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { currentSnarkWorker { key fee } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_sync_status 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { daemonStatus { syncStatus } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_set_current_snark_worker 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation { setSnarkWorker(input: {publicKey: "pk"}) { lastSnarkWorker } setSnarkWorkFee(input: {fee: 1}) { lastFee } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_wallet 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { wallet(publicKey: "pk") { balance { total unknown liquid locked blockHeight stateHash } nonce receiptChainHash delegate votingFor stakingActive privateKeyPath } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_transaction_status 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { transactionStatus(payment: "payment_id") }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_create_wallet 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation { createAccount(input: {password: "password"}) { publicKey account { publicKey token nonce inferredNonce receiptChainHash delegate votingFor stakingActive privateKeyPath locked isTokenOwner isDisabled } } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_best_chain 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { bestChain(maxLength: 42) { protocolState { previousStateHash blockchainState { date utcDate snarkedLedgerHash stagedLedgerHash } consensusState { blockchainLength blockHeight epochCount minWindowDensity lastVrfOutput totalCurrency hasAncestorInSameCheckpointWindow slot slotSinceGenesis epoch } } stateHash } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_block_by_height 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { block(height: 42) { stateHash creator snarkJobs { prover fee workIds } } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_get_block_by_state_hash 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'query { block(stateHash: "some_state_hash") { creator protocolState { previousStateHash blockchainState { date utcDate snarkedLedgerHash stagedLedgerHash } consensusState { blockchainLength blockHeight epochCount minWindowDensity lastVrfOutput totalCurrency hasAncestorInSameCheckpointWindow slot slotSinceGenesis epoch } } snarkJobs { prover fee workIds } } }'
            }
        }
    ,)
]

snapshots['TestMinaClient.test_send_payment 1'] = [
    (
        (
            'http://localhost:3085/graphql'
        ,),
        {
            'headers': {
                'Accept': 'application/json'
            },
            'json': {
                'query': 'mutation { sendPayment(input: {memo: "memo", fee: 100000000, amount: 1000000000, to: "to_pk", from: "from_pk"}) { payment { id hash kind nonce token amount feeToken fee memo isDelegation from to } } }'
            }
        }
    ,)
]
