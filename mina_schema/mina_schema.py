import sgqlc.types


mina_schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean


class ChainReorganizationStatus(sgqlc.types.Enum):
    __schema__ = mina_schema
    __choices__ = ("CHANGED",)


class ExtensionalBlock(sgqlc.types.Scalar):
    __schema__ = mina_schema


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int


class PrecomputedBlock(sgqlc.types.Scalar):
    __schema__ = mina_schema


class PublicKey(sgqlc.types.Scalar):
    __schema__ = mina_schema


String = sgqlc.types.String


class SyncStatus(sgqlc.types.Enum):
    __schema__ = mina_schema
    __choices__ = (
        "CONNECTING",
        "LISTENING",
        "OFFLINE",
        "BOOTSTRAP",
        "SYNCED",
        "CATCHUP",
    )


class TokenId(sgqlc.types.Scalar):
    __schema__ = mina_schema


class TransactionStatus(sgqlc.types.Enum):
    __schema__ = mina_schema
    __choices__ = ("INCLUDED", "PENDING", "UNKNOWN")


class UInt32(sgqlc.types.Scalar):
    __schema__ = mina_schema


class UInt64(sgqlc.types.Scalar):
    __schema__ = mina_schema


class UserCommandKind(sgqlc.types.Scalar):
    __schema__ = mina_schema


class sign(sgqlc.types.Enum):
    __schema__ = mina_schema
    __choices__ = ("PLUS", "MINUS")


########################################################################
# Input Objects
########################################################################
class AddAccountInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("password",)
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="password")


class CreateHDAccountInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("index",)
    index = sgqlc.types.Field(sgqlc.types.non_null(UInt32), graphql_name="index")


class DeleteAccountInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("public_key",)
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )


class LockInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("public_key",)
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )


class NetworkPeer(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("libp2p_port", "host", "peer_id")
    libp2p_port = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="libp2p_port"
    )
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="host")
    peer_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="peer_id")


class SendCreateTokenAccountInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = (
        "nonce",
        "memo",
        "valid_until",
        "fee_payer",
        "fee",
        "receiver",
        "token",
        "token_owner",
    )
    nonce = sgqlc.types.Field(UInt32, graphql_name="nonce")
    memo = sgqlc.types.Field(String, graphql_name="memo")
    valid_until = sgqlc.types.Field(UInt32, graphql_name="validUntil")
    fee_payer = sgqlc.types.Field(PublicKey, graphql_name="feePayer")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    receiver = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="receiver"
    )
    token = sgqlc.types.Field(sgqlc.types.non_null(TokenId), graphql_name="token")
    token_owner = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="tokenOwner"
    )


class SendCreateTokenInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = (
        "nonce",
        "memo",
        "valid_until",
        "fee",
        "token_owner",
        "fee_payer",
    )
    nonce = sgqlc.types.Field(UInt32, graphql_name="nonce")
    memo = sgqlc.types.Field(String, graphql_name="memo")
    valid_until = sgqlc.types.Field(UInt32, graphql_name="validUntil")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    token_owner = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="tokenOwner"
    )
    fee_payer = sgqlc.types.Field(PublicKey, graphql_name="feePayer")


class SendDelegationInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("nonce", "memo", "valid_until", "fee", "to", "from_")
    nonce = sgqlc.types.Field(UInt32, graphql_name="nonce")
    memo = sgqlc.types.Field(String, graphql_name="memo")
    valid_until = sgqlc.types.Field(UInt32, graphql_name="validUntil")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    to = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="to")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="from")


class SendMintTokensInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = (
        "nonce",
        "memo",
        "valid_until",
        "fee",
        "amount",
        "receiver",
        "token",
        "token_owner",
    )
    nonce = sgqlc.types.Field(UInt32, graphql_name="nonce")
    memo = sgqlc.types.Field(String, graphql_name="memo")
    valid_until = sgqlc.types.Field(UInt32, graphql_name="validUntil")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    amount = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="amount")
    receiver = sgqlc.types.Field(PublicKey, graphql_name="receiver")
    token = sgqlc.types.Field(sgqlc.types.non_null(TokenId), graphql_name="token")
    token_owner = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="tokenOwner"
    )


class SendPaymentInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = (
        "nonce",
        "memo",
        "valid_until",
        "fee",
        "amount",
        "token",
        "to",
        "from_",
    )
    nonce = sgqlc.types.Field(UInt32, graphql_name="nonce")
    memo = sgqlc.types.Field(String, graphql_name="memo")
    valid_until = sgqlc.types.Field(UInt32, graphql_name="validUntil")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    amount = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="amount")
    token = sgqlc.types.Field(TokenId, graphql_name="token")
    to = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="to")
    from_ = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="from")


class SetConnectionGatingConfigInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("isolate", "banned_peers", "trusted_peers")
    isolate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="isolate")
    banned_peers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NetworkPeer))),
        graphql_name="bannedPeers",
    )
    trusted_peers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NetworkPeer))),
        graphql_name="trustedPeers",
    )


class SetSnarkWorkFee(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("fee",)
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")


class SetSnarkWorkerInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("public_key",)
    public_key = sgqlc.types.Field(PublicKey, graphql_name="publicKey")


class SetStakingInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("public_keys",)
    public_keys = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicKey))),
        graphql_name="publicKeys",
    )


class SignatureInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("raw_signature", "scalar", "field")
    raw_signature = sgqlc.types.Field(String, graphql_name="rawSignature")
    scalar = sgqlc.types.Field(String, graphql_name="scalar")
    field = sgqlc.types.Field(String, graphql_name="field")


class UnlockInput(sgqlc.types.Input):
    __schema__ = mina_schema
    __field_names__ = ("public_key", "password")
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="password")


########################################################################
# Output Objects and Interfaces
########################################################################
class Account(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "public_key",
        "token",
        "timing",
        "balance",
        "nonce",
        "inferred_nonce",
        "epoch_delegate_account",
        "receipt_chain_hash",
        "delegate",
        "delegate_account",
        "delegators",
        "last_epoch_delegators",
        "voting_for",
        "staking_active",
        "private_key_path",
        "locked",
        "is_token_owner",
        "is_disabled",
    )
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )
    token = sgqlc.types.Field(sgqlc.types.non_null(TokenId), graphql_name="token")
    timing = sgqlc.types.Field(
        sgqlc.types.non_null("AccountTiming"), graphql_name="timing"
    )
    balance = sgqlc.types.Field(
        sgqlc.types.non_null("AnnotatedBalance"), graphql_name="balance"
    )
    nonce = sgqlc.types.Field(String, graphql_name="nonce")
    inferred_nonce = sgqlc.types.Field(String, graphql_name="inferredNonce")
    epoch_delegate_account = sgqlc.types.Field(
        "Account", graphql_name="epochDelegateAccount"
    )
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name="receiptChainHash")
    delegate = sgqlc.types.Field(PublicKey, graphql_name="delegate")
    delegate_account = sgqlc.types.Field("Account", graphql_name="delegateAccount")
    delegators = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("Account")), graphql_name="delegators"
    )
    last_epoch_delegators = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("Account")),
        graphql_name="lastEpochDelegators",
    )
    voting_for = sgqlc.types.Field(String, graphql_name="votingFor")
    staking_active = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="stakingActive"
    )
    private_key_path = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="privateKeyPath"
    )
    locked = sgqlc.types.Field(Boolean, graphql_name="locked")
    is_token_owner = sgqlc.types.Field(Boolean, graphql_name="isTokenOwner")
    is_disabled = sgqlc.types.Field(Boolean, graphql_name="isDisabled")


class AccountTiming(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "initial_mininum_balance",
        "cliff_time",
        "cliff_amount",
        "vesting_period",
        "vesting_increment",
    )
    initial_mininum_balance = sgqlc.types.Field(
        UInt64, graphql_name="initial_mininum_balance"
    )
    cliff_time = sgqlc.types.Field(UInt32, graphql_name="cliff_time")
    cliff_amount = sgqlc.types.Field(UInt64, graphql_name="cliff_amount")
    vesting_period = sgqlc.types.Field(UInt32, graphql_name="vesting_period")
    vesting_increment = sgqlc.types.Field(UInt64, graphql_name="vesting_increment")


class AddAccountPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("public_key", "account")
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="account")


class AddrsAndPorts(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("external_ip", "bind_ip", "peer", "libp2p_port", "client_port")
    external_ip = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="externalIp"
    )
    bind_ip = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="bindIp")
    peer = sgqlc.types.Field("Peer", graphql_name="peer")
    libp2p_port = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="libp2pPort"
    )
    client_port = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="clientPort"
    )


class AnnotatedBalance(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "total",
        "unknown",
        "liquid",
        "locked",
        "block_height",
        "state_hash",
    )
    total = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="total")
    unknown = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="unknown")
    liquid = sgqlc.types.Field(UInt64, graphql_name="liquid")
    locked = sgqlc.types.Field(UInt64, graphql_name="locked")
    block_height = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="blockHeight"
    )
    state_hash = sgqlc.types.Field(String, graphql_name="stateHash")


class Applied(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("applied",)
    applied = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="applied")


class Block(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "creator",
        "creator_account",
        "winner_account",
        "state_hash",
        "state_hash_field",
        "protocol_state",
        "protocol_state_proof",
        "transactions",
        "snark_jobs",
    )
    creator = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="creator")
    creator_account = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="creatorAccount"
    )
    winner_account = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="winnerAccount"
    )
    state_hash = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="stateHash"
    )
    state_hash_field = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="stateHashField"
    )
    protocol_state = sgqlc.types.Field(
        sgqlc.types.non_null("ProtocolState"), graphql_name="protocolState"
    )
    protocol_state_proof = sgqlc.types.Field(
        sgqlc.types.non_null("protocolStateProof"), graphql_name="protocolStateProof"
    )
    transactions = sgqlc.types.Field(
        sgqlc.types.non_null("Transactions"), graphql_name="transactions"
    )
    snark_jobs = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("CompletedWork"))
        ),
        graphql_name="snarkJobs",
    )


class BlockProducerTimings(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "times",
        "global_slot_since_genesis",
        "generated_from_consensus_at",
    )
    times = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("ConsensusTime"))
        ),
        graphql_name="times",
    )
    global_slot_since_genesis = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UInt32))),
        graphql_name="globalSlotSinceGenesis",
    )
    generated_from_consensus_at = sgqlc.types.Field(
        sgqlc.types.non_null("ConsensusTimeGlobalSlot"),
        graphql_name="generatedFromConsensusAt",
    )


class BlockchainState(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("date", "utc_date", "snarked_ledger_hash", "staged_ledger_hash")
    date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="date")
    utc_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="utcDate")
    snarked_ledger_hash = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="snarkedLedgerHash"
    )
    staged_ledger_hash = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="stagedLedgerHash"
    )


class CompletedWork(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("prover", "fee", "work_ids")
    prover = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="prover")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    work_ids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="workIds",
    )


class ConsensusConfiguration(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "delta",
        "k",
        "slots_per_epoch",
        "slot_duration",
        "epoch_duration",
        "genesis_state_timestamp",
        "acceptable_network_delay",
    )
    delta = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="delta")
    k = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="k")
    slots_per_epoch = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="slotsPerEpoch"
    )
    slot_duration = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="slotDuration"
    )
    epoch_duration = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="epochDuration"
    )
    genesis_state_timestamp = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="genesisStateTimestamp"
    )
    acceptable_network_delay = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="acceptableNetworkDelay"
    )


class ConsensusState(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "blockchain_length",
        "block_height",
        "epoch_count",
        "min_window_density",
        "last_vrf_output",
        "total_currency",
        "staking_epoch_data",
        "next_epoch_data",
        "has_ancestor_in_same_checkpoint_window",
        "slot",
        "slot_since_genesis",
        "epoch",
    )
    blockchain_length = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="blockchainLength"
    )
    block_height = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="blockHeight"
    )
    epoch_count = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="epochCount"
    )
    min_window_density = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="minWindowDensity"
    )
    last_vrf_output = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="lastVrfOutput"
    )
    total_currency = sgqlc.types.Field(
        sgqlc.types.non_null(UInt64), graphql_name="totalCurrency"
    )
    staking_epoch_data = sgqlc.types.Field(
        sgqlc.types.non_null("StakingEpochData"), graphql_name="stakingEpochData"
    )
    next_epoch_data = sgqlc.types.Field(
        sgqlc.types.non_null("NextEpochData"), graphql_name="nextEpochData"
    )
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="hasAncestorInSameCheckpointWindow"
    )
    slot = sgqlc.types.Field(sgqlc.types.non_null(UInt32), graphql_name="slot")
    slot_since_genesis = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="slotSinceGenesis"
    )
    epoch = sgqlc.types.Field(sgqlc.types.non_null(UInt32), graphql_name="epoch")


class ConsensusTime(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("epoch", "slot", "global_slot", "start_time", "end_time")
    epoch = sgqlc.types.Field(sgqlc.types.non_null(UInt32), graphql_name="epoch")
    slot = sgqlc.types.Field(sgqlc.types.non_null(UInt32), graphql_name="slot")
    global_slot = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="globalSlot"
    )
    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    end_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="endTime")


class ConsensusTimeGlobalSlot(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("consensus_time", "global_slot_since_genesis")
    consensus_time = sgqlc.types.Field(
        sgqlc.types.non_null(ConsensusTime), graphql_name="consensusTime"
    )
    global_slot_since_genesis = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="globalSlotSinceGenesis"
    )


class DaemonStatus(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "num_accounts",
        "blockchain_length",
        "highest_block_length_received",
        "highest_unvalidated_block_length_received",
        "uptime_secs",
        "ledger_merkle_root",
        "state_hash",
        "chain_id",
        "commit_id",
        "conf_dir",
        "peers",
        "user_commands_sent",
        "snark_worker",
        "snark_work_fee",
        "sync_status",
        "catchup_status",
        "block_production_keys",
        "histograms",
        "consensus_time_best_tip",
        "global_slot_since_genesis_best_tip",
        "next_block_production",
        "consensus_time_now",
        "consensus_mechanism",
        "consensus_configuration",
        "addrs_and_ports",
    )
    num_accounts = sgqlc.types.Field(Int, graphql_name="numAccounts")
    blockchain_length = sgqlc.types.Field(Int, graphql_name="blockchainLength")
    highest_block_length_received = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="highestBlockLengthReceived"
    )
    highest_unvalidated_block_length_received = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="highestUnvalidatedBlockLengthReceived"
    )
    uptime_secs = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="uptimeSecs"
    )
    ledger_merkle_root = sgqlc.types.Field(String, graphql_name="ledgerMerkleRoot")
    state_hash = sgqlc.types.Field(String, graphql_name="stateHash")
    chain_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="chainId")
    commit_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="commitId")
    conf_dir = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="confDir")
    peers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Peer"))),
        graphql_name="peers",
    )
    user_commands_sent = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="userCommandsSent"
    )
    snark_worker = sgqlc.types.Field(String, graphql_name="snarkWorker")
    snark_work_fee = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="snarkWorkFee"
    )
    sync_status = sgqlc.types.Field(
        sgqlc.types.non_null(SyncStatus), graphql_name="syncStatus"
    )
    catchup_status = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="catchupStatus"
    )
    block_production_keys = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="blockProductionKeys",
    )
    histograms = sgqlc.types.Field("Histograms", graphql_name="histograms")
    consensus_time_best_tip = sgqlc.types.Field(
        ConsensusTime, graphql_name="consensusTimeBestTip"
    )
    global_slot_since_genesis_best_tip = sgqlc.types.Field(
        Int, graphql_name="globalSlotSinceGenesisBestTip"
    )
    next_block_production = sgqlc.types.Field(
        BlockProducerTimings, graphql_name="nextBlockProduction"
    )
    consensus_time_now = sgqlc.types.Field(
        sgqlc.types.non_null(ConsensusTime), graphql_name="consensusTimeNow"
    )
    consensus_mechanism = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="consensusMechanism"
    )
    consensus_configuration = sgqlc.types.Field(
        sgqlc.types.non_null(ConsensusConfiguration),
        graphql_name="consensusConfiguration",
    )
    addrs_and_ports = sgqlc.types.Field(
        sgqlc.types.non_null(AddrsAndPorts), graphql_name="addrsAndPorts"
    )


class DeleteAccountPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("public_key",)
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )


class ExportLogsPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("export_logs",)
    export_logs = sgqlc.types.Field(
        sgqlc.types.non_null("TarFile"), graphql_name="exportLogs"
    )


class FeeTransfer(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("recipient", "fee")
    recipient = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="recipient"
    )
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")


class GenesisConstants(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("account_creation_fee", "coinbase")
    account_creation_fee = sgqlc.types.Field(
        sgqlc.types.non_null(UInt64), graphql_name="accountCreationFee"
    )
    coinbase = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="coinbase")


class Histogram(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("values", "intervals", "underflow", "overflow")
    values = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))),
        graphql_name="values",
    )
    intervals = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Interval"))),
        graphql_name="intervals",
    )
    underflow = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="underflow")
    overflow = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="overflow")


class Histograms(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "rpc_timings",
        "external_transition_latency",
        "accepted_transition_local_latency",
        "accepted_transition_remote_latency",
        "snark_worker_transition_time",
        "snark_worker_merge_time",
    )
    rpc_timings = sgqlc.types.Field(
        sgqlc.types.non_null("RpcTimings"), graphql_name="rpcTimings"
    )
    external_transition_latency = sgqlc.types.Field(
        Histogram, graphql_name="externalTransitionLatency"
    )
    accepted_transition_local_latency = sgqlc.types.Field(
        Histogram, graphql_name="acceptedTransitionLocalLatency"
    )
    accepted_transition_remote_latency = sgqlc.types.Field(
        Histogram, graphql_name="acceptedTransitionRemoteLatency"
    )
    snark_worker_transition_time = sgqlc.types.Field(
        Histogram, graphql_name="snarkWorkerTransitionTime"
    )
    snark_worker_merge_time = sgqlc.types.Field(
        Histogram, graphql_name="snarkWorkerMergeTime"
    )


class Interval(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("start", "stop")
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="start")
    stop = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stop")


class LockPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("public_key", "account")
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="account")


class NetworkPeerPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("peer_id", "host", "libp2p_port")
    peer_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="peer_id")
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="host")
    libp2p_port = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="libp2p_port"
    )


class NextEpochData(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "ledger",
        "seed",
        "start_checkpoint",
        "lock_checkpoint",
        "epoch_length",
    )
    ledger = sgqlc.types.Field(
        sgqlc.types.non_null("epochLedger"), graphql_name="ledger"
    )
    seed = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="seed")
    start_checkpoint = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startCheckpoint"
    )
    lock_checkpoint = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="lockCheckpoint"
    )
    epoch_length = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="epochLength"
    )


class Peer(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("host", "libp2p_port", "peer_id")
    host = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="host")
    libp2p_port = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="libp2pPort"
    )
    peer_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="peerId")


class PendingSnarkWork(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("work_bundle",)
    work_bundle = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("WorkDescription"))
        ),
        graphql_name="workBundle",
    )


class ProtocolState(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("previous_state_hash", "blockchain_state", "consensus_state")
    previous_state_hash = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="previousStateHash"
    )
    blockchain_state = sgqlc.types.Field(
        sgqlc.types.non_null(BlockchainState), graphql_name="blockchainState"
    )
    consensus_state = sgqlc.types.Field(
        sgqlc.types.non_null(ConsensusState), graphql_name="consensusState"
    )


class ReloadAccountsPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("success",)
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="success")


class RpcPair(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("dispatch", "impl")
    dispatch = sgqlc.types.Field(Histogram, graphql_name="dispatch")
    impl = sgqlc.types.Field(Histogram, graphql_name="impl")


class RpcTimings(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "get_staged_ledger_aux",
        "answer_sync_ledger_query",
        "get_ancestry",
        "get_transition_chain_proof",
        "get_transition_chain",
    )
    get_staged_ledger_aux = sgqlc.types.Field(
        sgqlc.types.non_null(RpcPair), graphql_name="getStagedLedgerAux"
    )
    answer_sync_ledger_query = sgqlc.types.Field(
        sgqlc.types.non_null(RpcPair), graphql_name="answerSyncLedgerQuery"
    )
    get_ancestry = sgqlc.types.Field(
        sgqlc.types.non_null(RpcPair), graphql_name="getAncestry"
    )
    get_transition_chain_proof = sgqlc.types.Field(
        sgqlc.types.non_null(RpcPair), graphql_name="getTransitionChainProof"
    )
    get_transition_chain = sgqlc.types.Field(
        sgqlc.types.non_null(RpcPair), graphql_name="getTransitionChain"
    )


class SendCreateTokenAccountPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("create_new_token_account",)
    create_new_token_account = sgqlc.types.Field(
        sgqlc.types.non_null("UserCommandNewAccount"),
        graphql_name="createNewTokenAccount",
    )


class SendCreateTokenPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("create_new_token",)
    create_new_token = sgqlc.types.Field(
        sgqlc.types.non_null("UserCommandNewToken"), graphql_name="createNewToken"
    )


class SendDelegationPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("delegation",)
    delegation = sgqlc.types.Field(
        sgqlc.types.non_null("UserCommand"), graphql_name="delegation"
    )


class SendMintTokensPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("mint_tokens",)
    mint_tokens = sgqlc.types.Field(
        sgqlc.types.non_null("UserCommandMintTokens"), graphql_name="mintTokens"
    )


class SendPaymentPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("payment",)
    payment = sgqlc.types.Field(
        sgqlc.types.non_null("UserCommand"), graphql_name="payment"
    )


class SetConnectionGatingConfigPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("trusted_peers", "banned_peers", "isolate")
    trusted_peers = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(NetworkPeerPayload))
        ),
        graphql_name="trustedPeers",
    )
    banned_peers = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(NetworkPeerPayload))
        ),
        graphql_name="bannedPeers",
    )
    isolate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="isolate")


class SetSnarkWorkFeePayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("last_fee",)
    last_fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="lastFee")


class SetSnarkWorkerPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("last_snark_worker",)
    last_snark_worker = sgqlc.types.Field(PublicKey, graphql_name="lastSnarkWorker")


class SetStakingPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("last_staking", "locked_public_keys", "current_staking_keys")
    last_staking = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicKey))),
        graphql_name="lastStaking",
    )
    locked_public_keys = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicKey))),
        graphql_name="lockedPublicKeys",
    )
    current_staking_keys = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicKey))),
        graphql_name="currentStakingKeys",
    )


class SignedFee(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("sign", "fee_magnitude")
    sign = sgqlc.types.Field(sgqlc.types.non_null("sign"), graphql_name="sign")
    fee_magnitude = sgqlc.types.Field(
        sgqlc.types.non_null(UInt64), graphql_name="feeMagnitude"
    )


class SnarkWorker(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("key", "account", "fee")
    key = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="key")
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="account")
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")


class StakingEpochData(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "ledger",
        "seed",
        "start_checkpoint",
        "lock_checkpoint",
        "epoch_length",
    )
    ledger = sgqlc.types.Field(
        sgqlc.types.non_null("epochLedger"), graphql_name="ledger"
    )
    seed = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="seed")
    start_checkpoint = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startCheckpoint"
    )
    lock_checkpoint = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="lockCheckpoint"
    )
    epoch_length = sgqlc.types.Field(
        sgqlc.types.non_null(UInt32), graphql_name="epochLength"
    )


class TarFile(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("tarfile",)
    tarfile = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="tarfile")


class Transactions(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "user_commands",
        "fee_transfer",
        "coinbase",
        "coinbase_receiver_account",
    )
    user_commands = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("UserCommand"))),
        graphql_name="userCommands",
    )
    fee_transfer = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FeeTransfer))),
        graphql_name="feeTransfer",
    )
    coinbase = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="coinbase")
    coinbase_receiver_account = sgqlc.types.Field(
        Account, graphql_name="coinbaseReceiverAccount"
    )


class TrustStatusPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("ip_addr", "peer_id", "trust", "banned_status")
    ip_addr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="ip_addr")
    peer_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="peer_id")
    trust = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="trust")
    banned_status = sgqlc.types.Field(String, graphql_name="banned_status")


class UnlockPayload(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("public_key", "account")
    public_key = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="publicKey"
    )
    account = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="account")


class UserCommand(sgqlc.types.Interface):
    __schema__ = mina_schema
    __field_names__ = (
        "id",
        "hash",
        "kind",
        "nonce",
        "source",
        "receiver",
        "fee_payer",
        "token",
        "amount",
        "fee_token",
        "fee",
        "memo",
        "is_delegation",
        "from_",
        "from_account",
        "to",
        "to_account",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="hash")
    kind = sgqlc.types.Field(sgqlc.types.non_null(UserCommandKind), graphql_name="kind")
    nonce = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="nonce")
    source = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="source")
    receiver = sgqlc.types.Field(sgqlc.types.non_null(Account), graphql_name="receiver")
    fee_payer = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="feePayer"
    )
    token = sgqlc.types.Field(sgqlc.types.non_null(TokenId), graphql_name="token")
    amount = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="amount")
    fee_token = sgqlc.types.Field(
        sgqlc.types.non_null(TokenId), graphql_name="feeToken"
    )
    fee = sgqlc.types.Field(sgqlc.types.non_null(UInt64), graphql_name="fee")
    memo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="memo")
    is_delegation = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isDelegation"
    )
    from_ = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="from")
    from_account = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="fromAccount"
    )
    to = sgqlc.types.Field(sgqlc.types.non_null(PublicKey), graphql_name="to")
    to_account = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="toAccount"
    )


class WorkDescription(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "source_ledger_hash",
        "target_ledger_hash",
        "fee_excess",
        "supply_increase",
        "work_id",
    )
    source_ledger_hash = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="sourceLedgerHash"
    )
    target_ledger_hash = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="targetLedgerHash"
    )
    fee_excess = sgqlc.types.Field(
        sgqlc.types.non_null(SignedFee), graphql_name="feeExcess"
    )
    supply_increase = sgqlc.types.Field(
        sgqlc.types.non_null(UInt64), graphql_name="supplyIncrease"
    )
    work_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="workId")


class epochLedger(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("hash", "total_currency")
    hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="hash")
    total_currency = sgqlc.types.Field(
        sgqlc.types.non_null(UInt64), graphql_name="totalCurrency"
    )


class mutation(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "add_wallet",
        "create_account",
        "create_hdaccount",
        "unlock_account",
        "unlock_wallet",
        "lock_account",
        "lock_wallet",
        "delete_account",
        "delete_wallet",
        "reload_accounts",
        "reload_wallets",
        "send_payment",
        "send_delegation",
        "create_token",
        "create_token_account",
        "mint_tokens",
        "export_logs",
        "set_staking",
        "set_snark_worker",
        "set_snark_work_fee",
        "set_connection_gating_config",
        "add_peers",
        "archive_precomputed_block",
        "archive_extensional_block",
    )
    add_wallet = sgqlc.types.Field(
        sgqlc.types.non_null(AddAccountPayload),
        graphql_name="addWallet",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(AddAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_account = sgqlc.types.Field(
        sgqlc.types.non_null(AddAccountPayload),
        graphql_name="createAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(AddAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_hdaccount = sgqlc.types.Field(
        sgqlc.types.non_null(AddAccountPayload),
        graphql_name="createHDAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(CreateHDAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    unlock_account = sgqlc.types.Field(
        sgqlc.types.non_null(UnlockPayload),
        graphql_name="unlockAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(UnlockInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    unlock_wallet = sgqlc.types.Field(
        sgqlc.types.non_null(UnlockPayload),
        graphql_name="unlockWallet",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(UnlockInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lock_account = sgqlc.types.Field(
        sgqlc.types.non_null(LockPayload),
        graphql_name="lockAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(LockInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lock_wallet = sgqlc.types.Field(
        sgqlc.types.non_null(LockPayload),
        graphql_name="lockWallet",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(LockInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_account = sgqlc.types.Field(
        sgqlc.types.non_null(DeleteAccountPayload),
        graphql_name="deleteAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(DeleteAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_wallet = sgqlc.types.Field(
        sgqlc.types.non_null(DeleteAccountPayload),
        graphql_name="deleteWallet",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(DeleteAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    reload_accounts = sgqlc.types.Field(
        sgqlc.types.non_null(ReloadAccountsPayload), graphql_name="reloadAccounts"
    )
    reload_wallets = sgqlc.types.Field(
        sgqlc.types.non_null(ReloadAccountsPayload), graphql_name="reloadWallets"
    )
    send_payment = sgqlc.types.Field(
        sgqlc.types.non_null(SendPaymentPayload),
        graphql_name="sendPayment",
        args=sgqlc.types.ArgDict(
            (
                (
                    "signature",
                    sgqlc.types.Arg(
                        SignatureInput, graphql_name="signature", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SendPaymentInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    send_delegation = sgqlc.types.Field(
        sgqlc.types.non_null(SendDelegationPayload),
        graphql_name="sendDelegation",
        args=sgqlc.types.ArgDict(
            (
                (
                    "signature",
                    sgqlc.types.Arg(
                        SignatureInput, graphql_name="signature", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SendDelegationInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_token = sgqlc.types.Field(
        sgqlc.types.non_null(SendCreateTokenPayload),
        graphql_name="createToken",
        args=sgqlc.types.ArgDict(
            (
                (
                    "signature",
                    sgqlc.types.Arg(
                        SignatureInput, graphql_name="signature", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SendCreateTokenInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_token_account = sgqlc.types.Field(
        sgqlc.types.non_null(SendCreateTokenAccountPayload),
        graphql_name="createTokenAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "signature",
                    sgqlc.types.Arg(
                        SignatureInput, graphql_name="signature", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SendCreateTokenAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    mint_tokens = sgqlc.types.Field(
        sgqlc.types.non_null(SendMintTokensPayload),
        graphql_name="mintTokens",
        args=sgqlc.types.ArgDict(
            (
                (
                    "signature",
                    sgqlc.types.Arg(
                        SignatureInput, graphql_name="signature", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SendMintTokensInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    export_logs = sgqlc.types.Field(
        sgqlc.types.non_null(ExportLogsPayload),
        graphql_name="exportLogs",
        args=sgqlc.types.ArgDict(
            (
                (
                    "basename",
                    sgqlc.types.Arg(String, graphql_name="basename", default=None),
                ),
            )
        ),
    )
    set_staking = sgqlc.types.Field(
        sgqlc.types.non_null(SetStakingPayload),
        graphql_name="setStaking",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SetStakingInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    set_snark_worker = sgqlc.types.Field(
        sgqlc.types.non_null(SetSnarkWorkerPayload),
        graphql_name="setSnarkWorker",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SetSnarkWorkerInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    set_snark_work_fee = sgqlc.types.Field(
        sgqlc.types.non_null(SetSnarkWorkFeePayload),
        graphql_name="setSnarkWorkFee",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SetSnarkWorkFee),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    set_connection_gating_config = sgqlc.types.Field(
        sgqlc.types.non_null(SetConnectionGatingConfigPayload),
        graphql_name="setConnectionGatingConfig",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SetConnectionGatingConfigInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    add_peers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Peer))),
        graphql_name="addPeers",
        args=sgqlc.types.ArgDict(
            (
                ("seed", sgqlc.types.Arg(Boolean, graphql_name="seed", default=None)),
                (
                    "peers",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(
                            sgqlc.types.list_of(sgqlc.types.non_null(NetworkPeer))
                        ),
                        graphql_name="peers",
                        default=None,
                    ),
                ),
            )
        ),
    )
    archive_precomputed_block = sgqlc.types.Field(
        sgqlc.types.non_null(Applied),
        graphql_name="archivePrecomputedBlock",
        args=sgqlc.types.ArgDict(
            (
                (
                    "block",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(PrecomputedBlock),
                        graphql_name="block",
                        default=None,
                    ),
                ),
            )
        ),
    )
    archive_extensional_block = sgqlc.types.Field(
        sgqlc.types.non_null(Applied),
        graphql_name="archiveExtensionalBlock",
        args=sgqlc.types.ArgDict(
            (
                (
                    "block",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ExtensionalBlock),
                        graphql_name="block",
                        default=None,
                    ),
                ),
            )
        ),
    )


class protocolStateProof(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("base64",)
    base64 = sgqlc.types.Field(String, graphql_name="base64")


class query(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = (
        "sync_status",
        "daemon_status",
        "version",
        "owned_wallets",
        "tracked_accounts",
        "wallet",
        "connection_gating_config",
        "account",
        "accounts",
        "token_owner",
        "current_snark_worker",
        "best_chain",
        "block",
        "genesis_block",
        "initial_peers",
        "get_peers",
        "pooled_user_commands",
        "transaction_status",
        "trust_status",
        "trust_status_all",
        "snark_pool",
        "pending_snark_work",
        "genesis_constants",
        "time_offset",
        "next_available_token",
        "validate_payment",
    )
    sync_status = sgqlc.types.Field(
        sgqlc.types.non_null(SyncStatus), graphql_name="syncStatus"
    )
    daemon_status = sgqlc.types.Field(
        sgqlc.types.non_null(DaemonStatus), graphql_name="daemonStatus"
    )
    version = sgqlc.types.Field(String, graphql_name="version")
    owned_wallets = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))),
        graphql_name="ownedWallets",
    )
    tracked_accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))),
        graphql_name="trackedAccounts",
    )
    wallet = sgqlc.types.Field(
        Account,
        graphql_name="wallet",
        args=sgqlc.types.ArgDict(
            (
                (
                    "public_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(PublicKey),
                        graphql_name="publicKey",
                        default=None,
                    ),
                ),
            )
        ),
    )
    connection_gating_config = sgqlc.types.Field(
        sgqlc.types.non_null(SetConnectionGatingConfigPayload),
        graphql_name="connectionGatingConfig",
    )
    account = sgqlc.types.Field(
        Account,
        graphql_name="account",
        args=sgqlc.types.ArgDict(
            (
                ("token", sgqlc.types.Arg(TokenId, graphql_name="token", default=None)),
                (
                    "public_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(PublicKey),
                        graphql_name="publicKey",
                        default=None,
                    ),
                ),
            )
        ),
    )
    accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))),
        graphql_name="accounts",
        args=sgqlc.types.ArgDict(
            (
                (
                    "public_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(PublicKey),
                        graphql_name="publicKey",
                        default=None,
                    ),
                ),
            )
        ),
    )
    token_owner = sgqlc.types.Field(
        PublicKey,
        graphql_name="tokenOwner",
        args=sgqlc.types.ArgDict(
            (
                (
                    "token",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(TokenId),
                        graphql_name="token",
                        default=None,
                    ),
                ),
            )
        ),
    )
    current_snark_worker = sgqlc.types.Field(
        SnarkWorker, graphql_name="currentSnarkWorker"
    )
    best_chain = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Block)),
        graphql_name="bestChain",
        args=sgqlc.types.ArgDict(
            (
                (
                    "max_length",
                    sgqlc.types.Arg(Int, graphql_name="maxLength", default=None),
                ),
            )
        ),
    )
    block = sgqlc.types.Field(
        sgqlc.types.non_null(Block),
        graphql_name="block",
        args=sgqlc.types.ArgDict(
            (
                ("height", sgqlc.types.Arg(Int, graphql_name="height", default=None)),
                (
                    "state_hash",
                    sgqlc.types.Arg(String, graphql_name="stateHash", default=None),
                ),
            )
        ),
    )
    genesis_block = sgqlc.types.Field(
        sgqlc.types.non_null(Block), graphql_name="genesisBlock"
    )
    initial_peers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="initialPeers",
    )
    get_peers = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Peer))),
        graphql_name="getPeers",
    )
    pooled_user_commands = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UserCommand))),
        graphql_name="pooledUserCommands",
        args=sgqlc.types.ArgDict(
            (
                (
                    "hashes",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(sgqlc.types.non_null(String)),
                        graphql_name="hashes",
                        default=None,
                    ),
                ),
                (
                    "public_key",
                    sgqlc.types.Arg(PublicKey, graphql_name="publicKey", default=None),
                ),
            )
        ),
    )
    transaction_status = sgqlc.types.Field(
        sgqlc.types.non_null(TransactionStatus),
        graphql_name="transactionStatus",
        args=sgqlc.types.ArgDict(
            (
                (
                    "payment",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="payment", default=None
                    ),
                ),
            )
        ),
    )
    trust_status = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(TrustStatusPayload)),
        graphql_name="trustStatus",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ip_address",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="ipAddress",
                        default=None,
                    ),
                ),
            )
        ),
    )
    trust_status_all = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(TrustStatusPayload))
        ),
        graphql_name="trustStatusAll",
    )
    snark_pool = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompletedWork))),
        graphql_name="snarkPool",
    )
    pending_snark_work = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(PendingSnarkWork))
        ),
        graphql_name="pendingSnarkWork",
    )
    genesis_constants = sgqlc.types.Field(
        sgqlc.types.non_null(GenesisConstants), graphql_name="genesisConstants"
    )
    time_offset = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="timeOffset"
    )
    next_available_token = sgqlc.types.Field(
        sgqlc.types.non_null(TokenId), graphql_name="nextAvailableToken"
    )
    validate_payment = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="validatePayment",
        args=sgqlc.types.ArgDict(
            (
                (
                    "signature",
                    sgqlc.types.Arg(
                        SignatureInput, graphql_name="signature", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(SendPaymentInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )


class subscription(sgqlc.types.Type):
    __schema__ = mina_schema
    __field_names__ = ("new_sync_update", "new_block", "chain_reorganization")
    new_sync_update = sgqlc.types.Field(
        sgqlc.types.non_null(SyncStatus), graphql_name="newSyncUpdate"
    )
    new_block = sgqlc.types.Field(
        sgqlc.types.non_null(Block),
        graphql_name="newBlock",
        args=sgqlc.types.ArgDict(
            (
                (
                    "public_key",
                    sgqlc.types.Arg(PublicKey, graphql_name="publicKey", default=None),
                ),
            )
        ),
    )
    chain_reorganization = sgqlc.types.Field(
        sgqlc.types.non_null(ChainReorganizationStatus),
        graphql_name="chainReorganization",
    )


class UserCommandDelegation(sgqlc.types.Type, UserCommand):
    __schema__ = mina_schema
    __field_names__ = ("delegator", "delegatee")
    delegator = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="delegator"
    )
    delegatee = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="delegatee"
    )


class UserCommandMintTokens(sgqlc.types.Type, UserCommand):
    __schema__ = mina_schema
    __field_names__ = ("token_owner",)
    token_owner = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="tokenOwner"
    )


class UserCommandNewAccount(sgqlc.types.Type, UserCommand):
    __schema__ = mina_schema
    __field_names__ = ("token_owner", "disabled")
    token_owner = sgqlc.types.Field(
        sgqlc.types.non_null(Account), graphql_name="tokenOwner"
    )
    disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="disabled")


class UserCommandNewToken(sgqlc.types.Type, UserCommand):
    __schema__ = mina_schema
    __field_names__ = ("token_owner", "new_accounts_disabled")
    token_owner = sgqlc.types.Field(
        sgqlc.types.non_null(PublicKey), graphql_name="tokenOwner"
    )
    new_accounts_disabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="newAccountsDisabled"
    )


class UserCommandPayment(sgqlc.types.Type, UserCommand):
    __schema__ = mina_schema
    __field_names__ = ()


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
mina_schema.query_type = query
mina_schema.mutation_type = mutation
mina_schema.subscription_type = subscription
