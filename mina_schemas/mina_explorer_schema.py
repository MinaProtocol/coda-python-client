import sgqlc.types
import sgqlc.types.datetime


mina_explorer_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BlockSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('BLOCKHEIGHT_ASC', 'BLOCKHEIGHT_DESC', 'CREATOR_ASC', 'CREATOR_DESC', 'DATETIME_ASC', 'DATETIME_DESC', 'RECEIVEDTIME_ASC', 'RECEIVEDTIME_DESC', 'STATEHASHFIELD_ASC', 'STATEHASHFIELD_DESC', 'STATEHASH_ASC', 'STATEHASH_DESC')


Boolean = sgqlc.types.Boolean

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

Int = sgqlc.types.Int

class Long(sgqlc.types.Scalar):
    __schema__ = mina_explorer_schema


class NextstakeSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('BALANCE_ASC', 'BALANCE_DESC', 'DELEGATE_ASC', 'DELEGATE_DESC', 'LEDGERHASH_ASC', 'LEDGERHASH_DESC', 'NONCE_ASC', 'NONCE_DESC', 'PK_ASC', 'PK_DESC', 'PUBLIC_KEY_ASC', 'PUBLIC_KEY_DESC', 'RECEIPT_CHAIN_HASH_ASC', 'RECEIPT_CHAIN_HASH_DESC', 'TOKEN_ASC', 'TOKEN_DESC', 'VOTING_FOR_ASC', 'VOTING_FOR_DESC')


class ObjectId(sgqlc.types.Scalar):
    __schema__ = mina_explorer_schema


class PayoutSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('BLOCKHEIGHT_ASC', 'BLOCKHEIGHT_DESC', 'COINBASE_ASC', 'COINBASE_DESC', 'DATETIME_ASC', 'DATETIME_DESC', 'EFFECTIVEPOOLSTAKES_ASC', 'EFFECTIVEPOOLSTAKES_DESC', 'EFFECTIVEPOOLWEIGHTING_ASC', 'EFFECTIVEPOOLWEIGHTING_DESC', 'LEDGERHASH_ASC', 'LEDGERHASH_DESC', 'PAYMENTHASH_ASC', 'PAYMENTHASH_DESC', 'PAYMENTID_ASC', 'PAYMENTID_DESC', 'PAYOUT_ASC', 'PAYOUT_DESC', 'PUBLICKEY_ASC', 'PUBLICKEY_DESC', 'STAKINGBALANCE_ASC', 'STAKINGBALANCE_DESC', 'STATEHASH_ASC', 'STATEHASH_DESC', 'SUMEFFECTIVEPOOLSTAKES_ASC', 'SUMEFFECTIVEPOOLSTAKES_DESC', 'SUPERCHARGEDCONTRIBUTION_ASC', 'SUPERCHARGEDCONTRIBUTION_DESC', 'SUPERCHARGEDWEIGHTING_ASC', 'SUPERCHARGEDWEIGHTING_DESC', 'TOTALPOOLSTAKES_ASC', 'TOTALPOOLSTAKES_DESC', 'TOTALREWARDS_ASC', 'TOTALREWARDS_DESC')


class SnarkSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('BLOCKHEIGHT_ASC', 'BLOCKHEIGHT_DESC', 'BLOCKSTATEHASH_ASC', 'BLOCKSTATEHASH_DESC', 'DATETIME_ASC', 'DATETIME_DESC', 'FEE_ASC', 'FEE_DESC', 'PROVER_ASC', 'PROVER_DESC')


class StakeSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('BALANCE_ASC', 'BALANCE_DESC', 'CHAINID_ASC', 'CHAINID_DESC', 'DELEGATE_ASC', 'DELEGATE_DESC', 'EPOCH_ASC', 'EPOCH_DESC', 'LEDGERHASH_ASC', 'LEDGERHASH_DESC', 'NONCE_ASC', 'NONCE_DESC', 'PK_ASC', 'PK_DESC', 'PUBLIC_KEY_ASC', 'PUBLIC_KEY_DESC', 'RECEIPT_CHAIN_HASH_ASC', 'RECEIPT_CHAIN_HASH_DESC', 'TOKEN_ASC', 'TOKEN_DESC', 'VOTING_FOR_ASC', 'VOTING_FOR_DESC')


String = sgqlc.types.String

class TransactionSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('AMOUNT_ASC', 'AMOUNT_DESC', 'BLOCKHEIGHT_ASC', 'BLOCKHEIGHT_DESC', 'BLOCKSTATEHASH_ASC', 'BLOCKSTATEHASH_DESC', 'DATETIME_ASC', 'DATETIME_DESC', 'FAILUREREASON_ASC', 'FAILUREREASON_DESC', 'FEETOKEN_ASC', 'FEETOKEN_DESC', 'FEE_ASC', 'FEE_DESC', 'FROM_ASC', 'FROM_DESC', 'HASH_ASC', 'HASH_DESC', 'ID_ASC', 'ID_DESC', 'KIND_ASC', 'KIND_DESC', 'MEMO_ASC', 'MEMO_DESC', 'NONCE_ASC', 'NONCE_DESC', 'TOKEN_ASC', 'TOKEN_DESC', 'TO_ASC', 'TO_DESC')



########################################################################
# Input Objects
########################################################################
class BlockCreatorAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockCreatorAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('or_', 'public_key_in', 'public_key_gt', 'public_key', 'public_key_lt', 'public_key_lte', 'and_', 'public_key_exists', 'public_key_nin', 'public_key_ne', 'public_key_gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockCreatorAccountQueryInput')), graphql_name='OR')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockCreatorAccountQueryInput')), graphql_name='AND')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')


class BlockCreatorAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class BlockInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('state_hash_field', 'transactions', 'received_time', 'date_time', 'snark_jobs', 'canonical', 'winner_account', 'protocol_state', 'creator', 'creator_account', 'state_hash', 'block_height')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    transactions = sgqlc.types.Field('BlockTransactionInsertInput', graphql_name='transactions')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobInsertInput'), graphql_name='snarkJobs')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    winner_account = sgqlc.types.Field('BlockWinnerAccountInsertInput', graphql_name='winnerAccount')
    protocol_state = sgqlc.types.Field('BlockProtocolStateInsertInput', graphql_name='protocolState')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    creator_account = sgqlc.types.Field(BlockCreatorAccountInsertInput, graphql_name='creatorAccount')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')


class BlockProtocolStateBlockchainStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date', 'snarked_ledger_hash', 'staged_ledger_hash', 'utc_date')
    date = sgqlc.types.Field(Long, graphql_name='date')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')


class BlockProtocolStateBlockchainStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_lte', 'utc_date_lt', 'utc_date_in', 'and_', 'snarked_ledger_hash_lte', 'staged_ledger_hash_lt', 'utc_date_ne', 'utc_date_gt', 'snarked_ledger_hash_in', 'staged_ledger_hash_nin', 'staged_ledger_hash_gt', 'utc_date', 'snarked_ledger_hash_nin', 'or_', 'snarked_ledger_hash_gt', 'snarked_ledger_hash', 'staged_ledger_hash_exists', 'utc_date_exists', 'date', 'snarked_ledger_hash_exists', 'date_nin', 'snarked_ledger_hash_gte', 'snarked_ledger_hash_lt', 'staged_ledger_hash', 'staged_ledger_hash_gte', 'date_gt', 'date_in', 'staged_ledger_hash_lte', 'date_gte', 'staged_ledger_hash_ne', 'utc_date_nin', 'date_ne', 'utc_date_lte', 'staged_ledger_hash_in', 'date_exists', 'snarked_ledger_hash_ne', 'utc_date_gte', 'date_lt')
    date_lte = sgqlc.types.Field(Long, graphql_name='date_lte')
    utc_date_lt = sgqlc.types.Field(Long, graphql_name='utcDate_lt')
    utc_date_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='utcDate_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateBlockchainStateQueryInput')), graphql_name='AND')
    snarked_ledger_hash_lte = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_lte')
    staged_ledger_hash_lt = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_lt')
    utc_date_ne = sgqlc.types.Field(Long, graphql_name='utcDate_ne')
    utc_date_gt = sgqlc.types.Field(Long, graphql_name='utcDate_gt')
    snarked_ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snarkedLedgerHash_in')
    staged_ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagedLedgerHash_nin')
    staged_ledger_hash_gt = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_gt')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')
    snarked_ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snarkedLedgerHash_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateBlockchainStateQueryInput')), graphql_name='OR')
    snarked_ledger_hash_gt = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_gt')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    staged_ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stagedLedgerHash_exists')
    utc_date_exists = sgqlc.types.Field(Boolean, graphql_name='utcDate_exists')
    date = sgqlc.types.Field(Long, graphql_name='date')
    snarked_ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='snarkedLedgerHash_exists')
    date_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='date_nin')
    snarked_ledger_hash_gte = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_gte')
    snarked_ledger_hash_lt = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_lt')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    staged_ledger_hash_gte = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_gte')
    date_gt = sgqlc.types.Field(Long, graphql_name='date_gt')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='date_in')
    staged_ledger_hash_lte = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_lte')
    date_gte = sgqlc.types.Field(Long, graphql_name='date_gte')
    staged_ledger_hash_ne = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_ne')
    utc_date_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='utcDate_nin')
    date_ne = sgqlc.types.Field(Long, graphql_name='date_ne')
    utc_date_lte = sgqlc.types.Field(Long, graphql_name='utcDate_lte')
    staged_ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagedLedgerHash_in')
    date_exists = sgqlc.types.Field(Boolean, graphql_name='date_exists')
    snarked_ledger_hash_ne = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_ne')
    utc_date_gte = sgqlc.types.Field(Long, graphql_name='utcDate_gte')
    date_lt = sgqlc.types.Field(Long, graphql_name='date_lt')


class BlockProtocolStateBlockchainStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('staged_ledger_hash', 'staged_ledger_hash_unset', 'utc_date', 'utc_date_unset', 'date', 'date_unset', 'snarked_ledger_hash', 'snarked_ledger_hash_unset')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    staged_ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stagedLedgerHash_unset')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')
    utc_date_unset = sgqlc.types.Field(Boolean, graphql_name='utcDate_unset')
    date = sgqlc.types.Field(Long, graphql_name='date')
    date_unset = sgqlc.types.Field(Boolean, graphql_name='date_unset')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    snarked_ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='snarkedLedgerHash_unset')


class BlockProtocolStateConsensusStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency', 'last_vrf_output', 'epoch_count', 'staking_epoch_data', 'block_height', 'blockchain_length', 'epoch', 'slot', 'slot_since_genesis', 'min_window_density', 'next_epoch_data', 'has_ancestor_in_same_checkpoint_window')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumInsertInput', graphql_name='stakingEpochData')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    next_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumInsertInput', graphql_name='nextEpochData')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')


class BlockProtocolStateConsensusStateNextEpochDatumInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('start_checkpoint', 'epoch_length', 'ledger', 'lock_checkpoint', 'seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumLedgerInsertInput', graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency_in', 'total_currency_lte', 'total_currency', 'total_currency_lt', 'hash_lt', 'total_currency_gt', 'hash', 'hash_in', 'hash_gte', 'hash_ne', 'hash_exists', 'or_', 'total_currency_exists', 'hash_lte', 'and_', 'hash_nin', 'total_currency_gte', 'total_currency_nin', 'total_currency_ne', 'hash_gt')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput')), graphql_name='OR')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput')), graphql_name='AND')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency_inc', 'total_currency_unset', 'hash', 'hash_unset', 'total_currency')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateNextEpochDatumQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('start_checkpoint_nin', 'and_', 'epoch_length_gt', 'start_checkpoint_gte', 'ledger', 'lock_checkpoint_in', 'start_checkpoint_lte', 'seed_gt', 'epoch_length_exists', 'start_checkpoint_ne', 'seed_exists', 'start_checkpoint_exists', 'epoch_length_lte', 'epoch_length_ne', 'start_checkpoint_lt', 'lock_checkpoint_ne', 'or_', 'lock_checkpoint_exists', 'seed_lt', 'ledger_exists', 'seed_nin', 'start_checkpoint', 'lock_checkpoint_lt', 'epoch_length_in', 'seed_gte', 'lock_checkpoint', 'seed_in', 'start_checkpoint_in', 'epoch_length_nin', 'seed_lte', 'lock_checkpoint_gt', 'epoch_length_gte', 'lock_checkpoint_gte', 'epoch_length_lt', 'seed_ne', 'start_checkpoint_gt', 'lock_checkpoint_lte', 'lock_checkpoint_nin', 'seed', 'epoch_length')
    start_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumQueryInput')), graphql_name='AND')
    epoch_length_gt = sgqlc.types.Field(Int, graphql_name='epochLength_gt')
    start_checkpoint_gte = sgqlc.types.Field(String, graphql_name='startCheckpoint_gte')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput, graphql_name='ledger')
    lock_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_in')
    start_checkpoint_lte = sgqlc.types.Field(String, graphql_name='startCheckpoint_lte')
    seed_gt = sgqlc.types.Field(String, graphql_name='seed_gt')
    epoch_length_exists = sgqlc.types.Field(Boolean, graphql_name='epochLength_exists')
    start_checkpoint_ne = sgqlc.types.Field(String, graphql_name='startCheckpoint_ne')
    seed_exists = sgqlc.types.Field(Boolean, graphql_name='seed_exists')
    start_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_exists')
    epoch_length_lte = sgqlc.types.Field(Int, graphql_name='epochLength_lte')
    epoch_length_ne = sgqlc.types.Field(Int, graphql_name='epochLength_ne')
    start_checkpoint_lt = sgqlc.types.Field(String, graphql_name='startCheckpoint_lt')
    lock_checkpoint_ne = sgqlc.types.Field(String, graphql_name='lockCheckpoint_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumQueryInput')), graphql_name='OR')
    lock_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_exists')
    seed_lt = sgqlc.types.Field(String, graphql_name='seed_lt')
    ledger_exists = sgqlc.types.Field(Boolean, graphql_name='ledger_exists')
    seed_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_nin')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    lock_checkpoint_lt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lt')
    epoch_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_in')
    seed_gte = sgqlc.types.Field(String, graphql_name='seed_gte')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_in')
    start_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_in')
    epoch_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_nin')
    seed_lte = sgqlc.types.Field(String, graphql_name='seed_lte')
    lock_checkpoint_gt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gt')
    epoch_length_gte = sgqlc.types.Field(Int, graphql_name='epochLength_gte')
    lock_checkpoint_gte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gte')
    epoch_length_lt = sgqlc.types.Field(Int, graphql_name='epochLength_lt')
    seed_ne = sgqlc.types.Field(String, graphql_name='seed_ne')
    start_checkpoint_gt = sgqlc.types.Field(String, graphql_name='startCheckpoint_gt')
    lock_checkpoint_lte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lte')
    lock_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_nin')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')


class BlockProtocolStateConsensusStateNextEpochDatumUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('lock_checkpoint_unset', 'seed', 'start_checkpoint_unset', 'lock_checkpoint', 'ledger_unset', 'epoch_length_unset', 'ledger', 'start_checkpoint', 'epoch_length_inc', 'seed_unset', 'epoch_length')
    lock_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_unset')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_unset')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    ledger_unset = sgqlc.types.Field(Boolean, graphql_name='ledger_unset')
    epoch_length_unset = sgqlc.types.Field(Boolean, graphql_name='epochLength_unset')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumLedgerUpdateInput, graphql_name='ledger')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length_inc = sgqlc.types.Field(Int, graphql_name='epochLength_inc')
    seed_unset = sgqlc.types.Field(Boolean, graphql_name='seed_unset')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')


class BlockProtocolStateConsensusStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('last_vrf_output_gt', 'blockchain_length_gt', 'total_currency_gt', 'block_height_nin', 'blockchain_length_nin', 'epoch_count_gte', 'epoch_lte', 'next_epoch_data_exists', 'slot_since_genesis_exists', 'epoch_count', 'total_currency_ne', 'slot_since_genesis_ne', 'total_currency_exists', 'blockchain_length', 'has_ancestor_in_same_checkpoint_window_exists', 'last_vrf_output_gte', 'epoch_gt', 'epoch_in', 'slot_since_genesis_lt', 'has_ancestor_in_same_checkpoint_window_ne', 'block_height_gte', 'slot_since_genesis_gte', 'blockchain_length_gte', 'epoch_count_exists', 'last_vrf_output_lte', 'min_window_density_exists', 'slot_since_genesis_gt', 'min_window_density_lt', 'min_window_density_in', 'total_currency_in', 'slot_gte', 'epoch_exists', 'total_currency_lt', 'staking_epoch_data_exists', 'total_currency_gte', 'slot_lt', 'min_window_density_lte', 'block_height_gt', 'epoch_count_in', 'min_window_density_nin', 'block_height_lt', 'last_vrf_output_nin', 'min_window_density_gte', 'total_currency_lte', 'has_ancestor_in_same_checkpoint_window', 'slot_since_genesis', 'epoch_ne', 'slot_since_genesis_in', 'total_currency_nin', 'staking_epoch_data', 'epoch_count_gt', 'block_height_ne', 'slot_since_genesis_nin', 'min_window_density_gt', 'slot_lte', 'min_window_density', 'last_vrf_output_lt', 'block_height', 'blockchain_length_lt', 'epoch', 'next_epoch_data', 'block_height_in', 'last_vrf_output_ne', 'block_height_lte', 'slot_nin', 'blockchain_length_in', 'or_', 'blockchain_length_lte', 'last_vrf_output', 'epoch_count_ne', 'min_window_density_ne', 'blockchain_length_ne', 'slot_since_genesis_lte', 'epoch_nin', 'slot_in', 'last_vrf_output_in', 'epoch_lt', 'slot_exists', 'slot', 'epoch_gte', 'and_', 'epoch_count_nin', 'slot_gt', 'total_currency', 'slot_ne', 'epoch_count_lte', 'last_vrf_output_exists', 'blockchain_length_exists', 'block_height_exists', 'epoch_count_lt')
    last_vrf_output_gt = sgqlc.types.Field(String, graphql_name='lastVrfOutput_gt')
    blockchain_length_gt = sgqlc.types.Field(Int, graphql_name='blockchainLength_gt')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    blockchain_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockchainLength_nin')
    epoch_count_gte = sgqlc.types.Field(Int, graphql_name='epochCount_gte')
    epoch_lte = sgqlc.types.Field(Int, graphql_name='epoch_lte')
    next_epoch_data_exists = sgqlc.types.Field(Boolean, graphql_name='nextEpochData_exists')
    slot_since_genesis_exists = sgqlc.types.Field(Boolean, graphql_name='slotSinceGenesis_exists')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    slot_since_genesis_ne = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_ne')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    has_ancestor_in_same_checkpoint_window_exists = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_exists')
    last_vrf_output_gte = sgqlc.types.Field(String, graphql_name='lastVrfOutput_gte')
    epoch_gt = sgqlc.types.Field(Int, graphql_name='epoch_gt')
    epoch_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_in')
    slot_since_genesis_lt = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_lt')
    has_ancestor_in_same_checkpoint_window_ne = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_ne')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    slot_since_genesis_gte = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_gte')
    blockchain_length_gte = sgqlc.types.Field(Int, graphql_name='blockchainLength_gte')
    epoch_count_exists = sgqlc.types.Field(Boolean, graphql_name='epochCount_exists')
    last_vrf_output_lte = sgqlc.types.Field(String, graphql_name='lastVrfOutput_lte')
    min_window_density_exists = sgqlc.types.Field(Boolean, graphql_name='minWindowDensity_exists')
    slot_since_genesis_gt = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_gt')
    min_window_density_lt = sgqlc.types.Field(Int, graphql_name='minWindowDensity_lt')
    min_window_density_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minWindowDensity_in')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    slot_gte = sgqlc.types.Field(Int, graphql_name='slot_gte')
    epoch_exists = sgqlc.types.Field(Boolean, graphql_name='epoch_exists')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    staking_epoch_data_exists = sgqlc.types.Field(Boolean, graphql_name='stakingEpochData_exists')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    slot_lt = sgqlc.types.Field(Int, graphql_name='slot_lt')
    min_window_density_lte = sgqlc.types.Field(Int, graphql_name='minWindowDensity_lte')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    epoch_count_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochCount_in')
    min_window_density_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minWindowDensity_nin')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    last_vrf_output_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastVrfOutput_nin')
    min_window_density_gte = sgqlc.types.Field(Int, graphql_name='minWindowDensity_gte')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    epoch_ne = sgqlc.types.Field(Int, graphql_name='epoch_ne')
    slot_since_genesis_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slotSinceGenesis_in')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput', graphql_name='stakingEpochData')
    epoch_count_gt = sgqlc.types.Field(Int, graphql_name='epochCount_gt')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    slot_since_genesis_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slotSinceGenesis_nin')
    min_window_density_gt = sgqlc.types.Field(Int, graphql_name='minWindowDensity_gt')
    slot_lte = sgqlc.types.Field(Int, graphql_name='slot_lte')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    last_vrf_output_lt = sgqlc.types.Field(String, graphql_name='lastVrfOutput_lt')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    blockchain_length_lt = sgqlc.types.Field(Int, graphql_name='blockchainLength_lt')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    next_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumQueryInput, graphql_name='nextEpochData')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    last_vrf_output_ne = sgqlc.types.Field(String, graphql_name='lastVrfOutput_ne')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    slot_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slot_nin')
    blockchain_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockchainLength_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateQueryInput')), graphql_name='OR')
    blockchain_length_lte = sgqlc.types.Field(Int, graphql_name='blockchainLength_lte')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    epoch_count_ne = sgqlc.types.Field(Int, graphql_name='epochCount_ne')
    min_window_density_ne = sgqlc.types.Field(Int, graphql_name='minWindowDensity_ne')
    blockchain_length_ne = sgqlc.types.Field(Int, graphql_name='blockchainLength_ne')
    slot_since_genesis_lte = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_lte')
    epoch_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_nin')
    slot_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slot_in')
    last_vrf_output_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastVrfOutput_in')
    epoch_lt = sgqlc.types.Field(Int, graphql_name='epoch_lt')
    slot_exists = sgqlc.types.Field(Boolean, graphql_name='slot_exists')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    epoch_gte = sgqlc.types.Field(Int, graphql_name='epoch_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateQueryInput')), graphql_name='AND')
    epoch_count_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochCount_nin')
    slot_gt = sgqlc.types.Field(Int, graphql_name='slot_gt')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    slot_ne = sgqlc.types.Field(Int, graphql_name='slot_ne')
    epoch_count_lte = sgqlc.types.Field(Int, graphql_name='epochCount_lte')
    last_vrf_output_exists = sgqlc.types.Field(Boolean, graphql_name='lastVrfOutput_exists')
    blockchain_length_exists = sgqlc.types.Field(Boolean, graphql_name='blockchainLength_exists')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    epoch_count_lt = sgqlc.types.Field(Int, graphql_name='epochCount_lt')


class BlockProtocolStateConsensusStateStakingEpochDatumInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('seed', 'start_checkpoint', 'epoch_length', 'ledger', 'lock_checkpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumLedgerInsertInput', graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency_gt', 'hash_nin', 'hash_in', 'hash_gt', 'total_currency_ne', 'total_currency_nin', 'or_', 'hash_exists', 'total_currency_gte', 'hash_lte', 'hash', 'total_currency_lte', 'total_currency_lt', 'hash_ne', 'total_currency_exists', 'hash_gte', 'total_currency_in', 'hash_lt', 'total_currency', 'and_')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput')), graphql_name='OR')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput')), graphql_name='AND')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'hash_unset', 'total_currency', 'total_currency_unset', 'total_currency_inc')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')


class BlockProtocolStateConsensusStateStakingEpochDatumQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('lock_checkpoint_exists', 'lock_checkpoint_ne', 'seed_in', 'seed_nin', 'start_checkpoint_exists', 'seed_ne', 'lock_checkpoint_gte', 'epoch_length', 'start_checkpoint_lt', 'lock_checkpoint_lte', 'lock_checkpoint', 'ledger', 'seed_gte', 'lock_checkpoint_gt', 'epoch_length_gt', 'seed_lte', 'start_checkpoint_nin', 'epoch_length_lte', 'or_', 'seed', 'start_checkpoint_gte', 'epoch_length_lt', 'epoch_length_exists', 'ledger_exists', 'lock_checkpoint_in', 'lock_checkpoint_lt', 'epoch_length_gte', 'epoch_length_in', 'start_checkpoint_lte', 'seed_gt', 'start_checkpoint_in', 'epoch_length_ne', 'start_checkpoint_ne', 'start_checkpoint_gt', 'seed_lt', 'epoch_length_nin', 'start_checkpoint', 'and_', 'lock_checkpoint_nin', 'seed_exists')
    lock_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_exists')
    lock_checkpoint_ne = sgqlc.types.Field(String, graphql_name='lockCheckpoint_ne')
    seed_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_in')
    seed_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_nin')
    start_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_exists')
    seed_ne = sgqlc.types.Field(String, graphql_name='seed_ne')
    lock_checkpoint_gte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gte')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    start_checkpoint_lt = sgqlc.types.Field(String, graphql_name='startCheckpoint_lt')
    lock_checkpoint_lte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lte')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput, graphql_name='ledger')
    seed_gte = sgqlc.types.Field(String, graphql_name='seed_gte')
    lock_checkpoint_gt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gt')
    epoch_length_gt = sgqlc.types.Field(Int, graphql_name='epochLength_gt')
    seed_lte = sgqlc.types.Field(String, graphql_name='seed_lte')
    start_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_nin')
    epoch_length_lte = sgqlc.types.Field(Int, graphql_name='epochLength_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput')), graphql_name='OR')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint_gte = sgqlc.types.Field(String, graphql_name='startCheckpoint_gte')
    epoch_length_lt = sgqlc.types.Field(Int, graphql_name='epochLength_lt')
    epoch_length_exists = sgqlc.types.Field(Boolean, graphql_name='epochLength_exists')
    ledger_exists = sgqlc.types.Field(Boolean, graphql_name='ledger_exists')
    lock_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_in')
    lock_checkpoint_lt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lt')
    epoch_length_gte = sgqlc.types.Field(Int, graphql_name='epochLength_gte')
    epoch_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_in')
    start_checkpoint_lte = sgqlc.types.Field(String, graphql_name='startCheckpoint_lte')
    seed_gt = sgqlc.types.Field(String, graphql_name='seed_gt')
    start_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_in')
    epoch_length_ne = sgqlc.types.Field(Int, graphql_name='epochLength_ne')
    start_checkpoint_ne = sgqlc.types.Field(String, graphql_name='startCheckpoint_ne')
    start_checkpoint_gt = sgqlc.types.Field(String, graphql_name='startCheckpoint_gt')
    seed_lt = sgqlc.types.Field(String, graphql_name='seed_lt')
    epoch_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_nin')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput')), graphql_name='AND')
    lock_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_nin')
    seed_exists = sgqlc.types.Field(Boolean, graphql_name='seed_exists')


class BlockProtocolStateConsensusStateStakingEpochDatumUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length_unset', 'lock_checkpoint', 'epoch_length_inc', 'seed_unset', 'ledger', 'ledger_unset', 'lock_checkpoint_unset', 'seed', 'start_checkpoint', 'epoch_length', 'start_checkpoint_unset')
    epoch_length_unset = sgqlc.types.Field(Boolean, graphql_name='epochLength_unset')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    epoch_length_inc = sgqlc.types.Field(Int, graphql_name='epochLength_inc')
    seed_unset = sgqlc.types.Field(Boolean, graphql_name='seed_unset')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumLedgerUpdateInput, graphql_name='ledger')
    ledger_unset = sgqlc.types.Field(Boolean, graphql_name='ledger_unset')
    lock_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_unset')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    start_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_unset')


class BlockProtocolStateConsensusStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency_inc', 'total_currency_unset', 'slot_unset', 'has_ancestor_in_same_checkpoint_window', 'total_currency', 'epoch', 'slot_inc', 'next_epoch_data', 'staking_epoch_data', 'blockchain_length_inc', 'block_height_inc', 'epoch_count', 'epoch_count_inc', 'slot_since_genesis', 'last_vrf_output_unset', 'last_vrf_output', 'min_window_density_inc', 'epoch_count_unset', 'epoch_unset', 'slot_since_genesis_unset', 'staking_epoch_data_unset', 'has_ancestor_in_same_checkpoint_window_unset', 'blockchain_length', 'block_height_unset', 'min_window_density_unset', 'next_epoch_data_unset', 'epoch_inc', 'min_window_density', 'slot', 'slot_since_genesis_inc', 'blockchain_length_unset', 'block_height')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    slot_unset = sgqlc.types.Field(Boolean, graphql_name='slot_unset')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    slot_inc = sgqlc.types.Field(Int, graphql_name='slot_inc')
    next_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumUpdateInput, graphql_name='nextEpochData')
    staking_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumUpdateInput, graphql_name='stakingEpochData')
    blockchain_length_inc = sgqlc.types.Field(Int, graphql_name='blockchainLength_inc')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    epoch_count_inc = sgqlc.types.Field(Int, graphql_name='epochCount_inc')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    last_vrf_output_unset = sgqlc.types.Field(Boolean, graphql_name='lastVrfOutput_unset')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    min_window_density_inc = sgqlc.types.Field(Int, graphql_name='minWindowDensity_inc')
    epoch_count_unset = sgqlc.types.Field(Boolean, graphql_name='epochCount_unset')
    epoch_unset = sgqlc.types.Field(Boolean, graphql_name='epoch_unset')
    slot_since_genesis_unset = sgqlc.types.Field(Boolean, graphql_name='slotSinceGenesis_unset')
    staking_epoch_data_unset = sgqlc.types.Field(Boolean, graphql_name='stakingEpochData_unset')
    has_ancestor_in_same_checkpoint_window_unset = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_unset')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    min_window_density_unset = sgqlc.types.Field(Boolean, graphql_name='minWindowDensity_unset')
    next_epoch_data_unset = sgqlc.types.Field(Boolean, graphql_name='nextEpochData_unset')
    epoch_inc = sgqlc.types.Field(Int, graphql_name='epoch_inc')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    slot_since_genesis_inc = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_inc')
    blockchain_length_unset = sgqlc.types.Field(Boolean, graphql_name='blockchainLength_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')


class BlockProtocolStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('consensus_state', 'previous_state_hash', 'blockchain_state')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateInsertInput, graphql_name='consensusState')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateInsertInput, graphql_name='blockchainState')


class BlockProtocolStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('and_', 'blockchain_state_exists', 'previous_state_hash_ne', 'blockchain_state', 'previous_state_hash_lt', 'consensus_state_exists', 'previous_state_hash_gt', 'previous_state_hash_lte', 'previous_state_hash_in', 'previous_state_hash_nin', 'consensus_state', 'previous_state_hash', 'previous_state_hash_exists', 'previous_state_hash_gte', 'or_')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateQueryInput')), graphql_name='AND')
    blockchain_state_exists = sgqlc.types.Field(Boolean, graphql_name='blockchainState_exists')
    previous_state_hash_ne = sgqlc.types.Field(String, graphql_name='previousStateHash_ne')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateQueryInput, graphql_name='blockchainState')
    previous_state_hash_lt = sgqlc.types.Field(String, graphql_name='previousStateHash_lt')
    consensus_state_exists = sgqlc.types.Field(Boolean, graphql_name='consensusState_exists')
    previous_state_hash_gt = sgqlc.types.Field(String, graphql_name='previousStateHash_gt')
    previous_state_hash_lte = sgqlc.types.Field(String, graphql_name='previousStateHash_lte')
    previous_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='previousStateHash_in')
    previous_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='previousStateHash_nin')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateQueryInput, graphql_name='consensusState')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')
    previous_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='previousStateHash_exists')
    previous_state_hash_gte = sgqlc.types.Field(String, graphql_name='previousStateHash_gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateQueryInput')), graphql_name='OR')


class BlockProtocolStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('previous_state_hash_unset', 'blockchain_state', 'blockchain_state_unset', 'consensus_state', 'consensus_state_unset', 'previous_state_hash')
    previous_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='previousStateHash_unset')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateUpdateInput, graphql_name='blockchainState')
    blockchain_state_unset = sgqlc.types.Field(Boolean, graphql_name='blockchainState_unset')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateUpdateInput, graphql_name='consensusState')
    consensus_state_unset = sgqlc.types.Field(Boolean, graphql_name='consensusState_unset')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')


class BlockQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height_nin', 'creator_account', 'and_', 'date_time_lte', 'block_height_lt', 'state_hash_field_gt', 'creator_nin', 'block_height_lte', 'date_time_gt', 'snark_jobs_nin', 'received_time_ne', 'creator_account_exists', 'state_hash_lte', 'state_hash_ne', 'block_height_ne', 'winner_account', 'block_height', 'state_hash_gte', 'state_hash_field_exists', 'state_hash_lt', 'state_hash_gt', 'state_hash', 'protocol_state_exists', 'received_time', 'transactions_exists', 'date_time_exists', 'creator_in', 'creator_exists', 'creator', 'snark_jobs_exists', 'state_hash_field_ne', 'creator_gte', 'state_hash_field', 'state_hash_field_nin', 'date_time_gte', 'transactions', 'winner_account_exists', 'received_time_gte', 'date_time_in', 'block_height_gte', 'date_time', 'canonical', 'state_hash_field_in', 'protocol_state', 'received_time_exists', 'received_time_lt', 'date_time_ne', 'block_height_gt', 'state_hash_in', 'canonical_exists', 'state_hash_exists', 'creator_lte', 'state_hash_field_gte', 'received_time_in', 'creator_ne', 'block_height_in', 'received_time_gt', 'canonical_ne', 'received_time_nin', 'snark_jobs_in', 'state_hash_field_lt', 'date_time_lt', 'creator_lt', 'or_', 'creator_gt', 'received_time_lte', 'snark_jobs', 'state_hash_field_lte', 'state_hash_nin', 'date_time_nin', 'block_height_exists')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    creator_account = sgqlc.types.Field(BlockCreatorAccountQueryInput, graphql_name='creatorAccount')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockQueryInput')), graphql_name='AND')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    state_hash_field_gt = sgqlc.types.Field(String, graphql_name='stateHashField_gt')
    creator_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='creator_nin')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    snark_jobs_nin = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs_nin')
    received_time_ne = sgqlc.types.Field(DateTime, graphql_name='receivedTime_ne')
    creator_account_exists = sgqlc.types.Field(Boolean, graphql_name='creatorAccount_exists')
    state_hash_lte = sgqlc.types.Field(String, graphql_name='stateHash_lte')
    state_hash_ne = sgqlc.types.Field(String, graphql_name='stateHash_ne')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    winner_account = sgqlc.types.Field('BlockWinnerAccountQueryInput', graphql_name='winnerAccount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    state_hash_gte = sgqlc.types.Field(String, graphql_name='stateHash_gte')
    state_hash_field_exists = sgqlc.types.Field(Boolean, graphql_name='stateHashField_exists')
    state_hash_lt = sgqlc.types.Field(String, graphql_name='stateHash_lt')
    state_hash_gt = sgqlc.types.Field(String, graphql_name='stateHash_gt')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    protocol_state_exists = sgqlc.types.Field(Boolean, graphql_name='protocolState_exists')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    transactions_exists = sgqlc.types.Field(Boolean, graphql_name='transactions_exists')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    creator_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='creator_in')
    creator_exists = sgqlc.types.Field(Boolean, graphql_name='creator_exists')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    snark_jobs_exists = sgqlc.types.Field(Boolean, graphql_name='snarkJobs_exists')
    state_hash_field_ne = sgqlc.types.Field(String, graphql_name='stateHashField_ne')
    creator_gte = sgqlc.types.Field(String, graphql_name='creator_gte')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    state_hash_field_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHashField_nin')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    transactions = sgqlc.types.Field('BlockTransactionQueryInput', graphql_name='transactions')
    winner_account_exists = sgqlc.types.Field(Boolean, graphql_name='winnerAccount_exists')
    received_time_gte = sgqlc.types.Field(DateTime, graphql_name='receivedTime_gte')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    state_hash_field_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHashField_in')
    protocol_state = sgqlc.types.Field(BlockProtocolStateQueryInput, graphql_name='protocolState')
    received_time_exists = sgqlc.types.Field(Boolean, graphql_name='receivedTime_exists')
    received_time_lt = sgqlc.types.Field(DateTime, graphql_name='receivedTime_lt')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_in')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    creator_lte = sgqlc.types.Field(String, graphql_name='creator_lte')
    state_hash_field_gte = sgqlc.types.Field(String, graphql_name='stateHashField_gte')
    received_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='receivedTime_in')
    creator_ne = sgqlc.types.Field(String, graphql_name='creator_ne')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    received_time_gt = sgqlc.types.Field(DateTime, graphql_name='receivedTime_gt')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    received_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='receivedTime_nin')
    snark_jobs_in = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs_in')
    state_hash_field_lt = sgqlc.types.Field(String, graphql_name='stateHashField_lt')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    creator_lt = sgqlc.types.Field(String, graphql_name='creator_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockQueryInput')), graphql_name='OR')
    creator_gt = sgqlc.types.Field(String, graphql_name='creator_gt')
    received_time_lte = sgqlc.types.Field(DateTime, graphql_name='receivedTime_lte')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs')
    state_hash_field_lte = sgqlc.types.Field(String, graphql_name='stateHashField_lte')
    state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_nin')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')


class BlockSnarkJobInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_state_hash', 'date_time', 'fee', 'prover', 'work_ids', 'block_height')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')


class BlockSnarkJobQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height_ne', 'block_state_hash_lte', 'fee_nin', 'prover_ne', 'date_time_in', 'fee_ne', 'date_time_gt', 'block_height_lt', 'and_', 'block_height', 'date_time_lt', 'date_time_nin', 'block_state_hash_nin', 'date_time', 'or_', 'block_state_hash_lt', 'date_time_lte', 'fee_lte', 'fee_lt', 'block_state_hash_in', 'fee_in', 'prover_lt', 'block_state_hash_gte', 'block_state_hash_ne', 'block_height_gte', 'block_state_hash', 'prover_exists', 'date_time_ne', 'block_height_lte', 'block_state_hash_gt', 'fee_gt', 'block_height_exists', 'prover', 'work_ids', 'fee_gte', 'prover_nin', 'prover_in', 'block_state_hash_exists', 'prover_gte', 'fee_exists', 'date_time_gte', 'work_ids_nin', 'fee', 'block_height_nin', 'prover_gt', 'block_height_in', 'block_height_gt', 'work_ids_in', 'work_ids_exists', 'date_time_exists', 'prover_lte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    block_state_hash_lte = sgqlc.types.Field(String, graphql_name='blockStateHash_lte')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_nin')
    prover_ne = sgqlc.types.Field(String, graphql_name='prover_ne')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    fee_ne = sgqlc.types.Field(Int, graphql_name='fee_ne')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockSnarkJobQueryInput')), graphql_name='AND')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    block_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_nin')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockSnarkJobQueryInput')), graphql_name='OR')
    block_state_hash_lt = sgqlc.types.Field(String, graphql_name='blockStateHash_lt')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    fee_lte = sgqlc.types.Field(Int, graphql_name='fee_lte')
    fee_lt = sgqlc.types.Field(Int, graphql_name='fee_lt')
    block_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_in')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_in')
    prover_lt = sgqlc.types.Field(String, graphql_name='prover_lt')
    block_state_hash_gte = sgqlc.types.Field(String, graphql_name='blockStateHash_gte')
    block_state_hash_ne = sgqlc.types.Field(String, graphql_name='blockStateHash_ne')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    prover_exists = sgqlc.types.Field(Boolean, graphql_name='prover_exists')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    block_state_hash_gt = sgqlc.types.Field(String, graphql_name='blockStateHash_gt')
    fee_gt = sgqlc.types.Field(Int, graphql_name='fee_gt')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    fee_gte = sgqlc.types.Field(Int, graphql_name='fee_gte')
    prover_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_nin')
    prover_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_in')
    block_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_exists')
    prover_gte = sgqlc.types.Field(String, graphql_name='prover_gte')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    work_ids_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_nin')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    prover_gt = sgqlc.types.Field(String, graphql_name='prover_gt')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    work_ids_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_in')
    work_ids_exists = sgqlc.types.Field(Boolean, graphql_name='workIds_exists')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    prover_lte = sgqlc.types.Field(String, graphql_name='prover_lte')


class BlockSnarkJobUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_time_unset', 'work_ids', 'work_ids_unset', 'block_height_inc', 'block_height', 'fee_inc', 'fee_unset', 'block_state_hash', 'prover', 'fee', 'prover_unset', 'block_height_unset', 'date_time', 'block_state_hash_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    work_ids_unset = sgqlc.types.Field(Boolean, graphql_name='workIds_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    fee_inc = sgqlc.types.Field(Int, graphql_name='fee_inc')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover_unset = sgqlc.types.Field(Boolean, graphql_name='prover_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    block_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_unset')


class BlockTransactionCoinbaseReceiverAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionCoinbaseReceiverAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_exists', 'or_', 'public_key', 'public_key_nin', 'public_key_ne', 'public_key_gte', 'public_key_lt', 'and_', 'public_key_in', 'public_key_gt', 'public_key_lte')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionCoinbaseReceiverAccountQueryInput')), graphql_name='OR')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionCoinbaseReceiverAccountQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')


class BlockTransactionCoinbaseReceiverAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_unset', 'public_key')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionFeeTransferInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee', 'recipient', 'type')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    type = sgqlc.types.Field(String, graphql_name='type')


class BlockTransactionFeeTransferQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('recipient', 'recipient_gte', 'recipient_in', 'type_lt', 'recipient_nin', 'type_gt', 'fee_in', 'recipient_lt', 'type_nin', 'fee', 'or_', 'type_ne', 'fee_lt', 'type', 'type_in', 'fee_ne', 'fee_nin', 'type_exists', 'and_', 'fee_exists', 'recipient_gt', 'fee_gte', 'recipient_ne', 'type_lte', 'recipient_lte', 'fee_gt', 'recipient_exists', 'type_gte', 'fee_lte')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    recipient_gte = sgqlc.types.Field(String, graphql_name='recipient_gte')
    recipient_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipient_in')
    type_lt = sgqlc.types.Field(String, graphql_name='type_lt')
    recipient_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipient_nin')
    type_gt = sgqlc.types.Field(String, graphql_name='type_gt')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_in')
    recipient_lt = sgqlc.types.Field(String, graphql_name='recipient_lt')
    type_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='type_nin')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionFeeTransferQueryInput')), graphql_name='OR')
    type_ne = sgqlc.types.Field(String, graphql_name='type_ne')
    fee_lt = sgqlc.types.Field(Long, graphql_name='fee_lt')
    type = sgqlc.types.Field(String, graphql_name='type')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='type_in')
    fee_ne = sgqlc.types.Field(Long, graphql_name='fee_ne')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_nin')
    type_exists = sgqlc.types.Field(Boolean, graphql_name='type_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionFeeTransferQueryInput')), graphql_name='AND')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    recipient_gt = sgqlc.types.Field(String, graphql_name='recipient_gt')
    fee_gte = sgqlc.types.Field(Long, graphql_name='fee_gte')
    recipient_ne = sgqlc.types.Field(String, graphql_name='recipient_ne')
    type_lte = sgqlc.types.Field(String, graphql_name='type_lte')
    recipient_lte = sgqlc.types.Field(String, graphql_name='recipient_lte')
    fee_gt = sgqlc.types.Field(Long, graphql_name='fee_gt')
    recipient_exists = sgqlc.types.Field(Boolean, graphql_name='recipient_exists')
    type_gte = sgqlc.types.Field(String, graphql_name='type_gte')
    fee_lte = sgqlc.types.Field(Long, graphql_name='fee_lte')


class BlockTransactionFeeTransferUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('recipient_unset', 'type', 'type_unset', 'fee', 'fee_unset', 'recipient')
    recipient_unset = sgqlc.types.Field(Boolean, graphql_name='recipient_unset')
    type = sgqlc.types.Field(String, graphql_name='type')
    type_unset = sgqlc.types.Field(Boolean, graphql_name='type_unset')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')


class BlockTransactionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('coinbase', 'coinbase_receiver_account', 'fee_transfer', 'user_commands')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountInsertInput, graphql_name='coinbaseReceiverAccount')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferInsertInput), graphql_name='feeTransfer')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandInsertInput'), graphql_name='userCommands')


class BlockTransactionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('user_commands_in', 'coinbase_gte', 'coinbase_receiver_account', 'coinbase_nin', 'coinbase_gt', 'coinbase_receiver_account_exists', 'or_', 'coinbase_lt', 'user_commands_exists', 'coinbase_lte', 'fee_transfer', 'user_commands', 'user_commands_nin', 'coinbase_in', 'coinbase_exists', 'coinbase_ne', 'and_', 'fee_transfer_exists', 'coinbase', 'fee_transfer_in', 'fee_transfer_nin')
    user_commands_in = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands_in')
    coinbase_gte = sgqlc.types.Field(Long, graphql_name='coinbase_gte')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountQueryInput, graphql_name='coinbaseReceiverAccount')
    coinbase_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='coinbase_nin')
    coinbase_gt = sgqlc.types.Field(Long, graphql_name='coinbase_gt')
    coinbase_receiver_account_exists = sgqlc.types.Field(Boolean, graphql_name='coinbaseReceiverAccount_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionQueryInput')), graphql_name='OR')
    coinbase_lt = sgqlc.types.Field(Long, graphql_name='coinbase_lt')
    user_commands_exists = sgqlc.types.Field(Boolean, graphql_name='userCommands_exists')
    coinbase_lte = sgqlc.types.Field(Long, graphql_name='coinbase_lte')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands')
    user_commands_nin = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands_nin')
    coinbase_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='coinbase_in')
    coinbase_exists = sgqlc.types.Field(Boolean, graphql_name='coinbase_exists')
    coinbase_ne = sgqlc.types.Field(Long, graphql_name='coinbase_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionQueryInput')), graphql_name='AND')
    fee_transfer_exists = sgqlc.types.Field(Boolean, graphql_name='feeTransfer_exists')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    fee_transfer_in = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer_in')
    fee_transfer_nin = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer_nin')


class BlockTransactionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('coinbase_receiver_account', 'coinbase_receiver_account_unset', 'fee_transfer', 'fee_transfer_unset', 'user_commands', 'user_commands_unset', 'coinbase', 'coinbase_unset')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountUpdateInput, graphql_name='coinbaseReceiverAccount')
    coinbase_receiver_account_unset = sgqlc.types.Field(Boolean, graphql_name='coinbaseReceiverAccount_unset')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferUpdateInput), graphql_name='feeTransfer')
    fee_transfer_unset = sgqlc.types.Field(Boolean, graphql_name='feeTransfer_unset')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandUpdateInput'), graphql_name='userCommands')
    user_commands_unset = sgqlc.types.Field(Boolean, graphql_name='userCommands_unset')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_unset = sgqlc.types.Field(Boolean, graphql_name='coinbase_unset')


class BlockTransactionUserCommandFeePayerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandFeePayerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_nin', 'or_', 'token_ne', 'token_gt', 'token_lte', 'token_in', 'token_exists', 'token_gte', 'token_lt', 'and_')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFeePayerQueryInput')), graphql_name='OR')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFeePayerQueryInput')), graphql_name='AND')


class BlockTransactionUserCommandFeePayerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class BlockTransactionUserCommandFromAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandFromAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gt', 'token_gte', 'token_lte', 'token_in', 'token_exists', 'and_', 'or_', 'token', 'token_nin', 'token_ne', 'token_lt')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFromAccountQueryInput')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFromAccountQueryInput')), graphql_name='OR')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')


class BlockTransactionUserCommandFromAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class BlockTransactionUserCommandInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('source', 'nonce', 'amount', 'receiver', 'block_height', 'id', 'from_', 'memo', 'to_account', 'failure_reason', 'fee', 'block_state_hash', 'fee_token', 'hash', 'kind', 'to', 'is_delegation', 'from_account', 'date_time', 'fee_payer', 'token')
    source = sgqlc.types.Field('BlockTransactionUserCommandSourceInsertInput', graphql_name='source')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiverInsertInput', graphql_name='receiver')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    id = sgqlc.types.Field(String, graphql_name='id')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccountInsertInput', graphql_name='toAccount')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    to = sgqlc.types.Field(String, graphql_name='to')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountInsertInput, graphql_name='fromAccount')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerInsertInput, graphql_name='feePayer')
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_state_hash', 'failure_reason_lt', 'nonce_gt', 'nonce_lt', 'id_lt', 'kind_nin', 'fee_token_in', 'fee_gt', 'block_state_hash_nin', 'is_delegation_exists', 'hash_lt', 'hash_in', 'is_delegation_ne', 'fee_payer', 'kind_gt', 'hash', 'token_lt', 'hash_lte', 'token_in', 'token_gt', 'amount', 'block_height', 'from_account_exists', 'fee_token_ne', 'failure_reason_ne', 'fee_token', 'to_gte', 'kind_ne', 'fee_gte', 'to_gt', 'amount_ne', 'date_time_lt', 'fee_token_lte', 'fee_in', 'memo_nin', 'from_gte', 'id_lte', 'fee', 'to_exists', 'from_nin', 'nonce_in', 'kind_exists', 'failure_reason_exists', 'date_time_lte', 'memo_exists', 'amount_in', 'failure_reason_in', 'from_lt', 'memo_lt', 'from_in', 'fee_nin', 'from_', 'to_nin', 'memo', 'and_', 'amount_exists', 'kind_lte', 'failure_reason_nin', 'from_exists', 'date_time_nin', 'fee_token_lt', 'to_account_exists', 'block_height_gte', 'kind_gte', 'hash_gt', 'fee_payer_exists', 'fee_token_gt', 'block_height_lte', 'date_time', 'block_height_gt', 'failure_reason_gt', 'token_nin', 'hash_nin', 'id', 'memo_gt', 'to_lt', 'hash_exists', 'to_ne', 'amount_gt', 'kind_in', 'nonce_exists', 'fee_lte', 'from_gt', 'to_lte', 'memo_gte', 'nonce_ne', 'hash_gte', 'id_gte', 'block_height_exists', 'to', 'block_state_hash_lte', 'block_height_in', 'amount_lt', 'token_exists', 'id_gt', 'id_in', 'date_time_in', 'source', 'fee_token_gte', 'memo_in', 'receiver_exists', 'failure_reason', 'amount_lte', 'fee_token_exists', 'kind', 'memo_ne', 'id_nin', 'id_ne', 'fee_ne', 'block_height_ne', 'block_state_hash_gt', 'from_account', 'fee_lt', 'token', 'from_ne', 'block_state_hash_lt', 'id_exists', 'to_account', 'block_state_hash_in', 'or_', 'token_gte', 'token_ne', 'date_time_exists', 'date_time_gte', 'failure_reason_lte', 'source_exists', 'failure_reason_gte', 'from_lte', 'amount_gte', 'block_height_nin', 'fee_token_nin', 'token_lte', 'kind_lt', 'fee_exists', 'block_state_hash_ne', 'block_height_lt', 'date_time_gt', 'receiver', 'date_time_ne', 'nonce_lte', 'to_in', 'amount_nin', 'block_state_hash_exists', 'block_state_hash_gte', 'memo_lte', 'nonce_gte', 'hash_ne', 'nonce', 'nonce_nin', 'is_delegation')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    failure_reason_lt = sgqlc.types.Field(String, graphql_name='failureReason_lt')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    kind_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_nin')
    fee_token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_in')
    fee_gt = sgqlc.types.Field(Float, graphql_name='fee_gt')
    block_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_nin')
    is_delegation_exists = sgqlc.types.Field(Boolean, graphql_name='isDelegation_exists')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    is_delegation_ne = sgqlc.types.Field(Boolean, graphql_name='isDelegation_ne')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerQueryInput, graphql_name='feePayer')
    kind_gt = sgqlc.types.Field(String, graphql_name='kind_gt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    from_account_exists = sgqlc.types.Field(Boolean, graphql_name='fromAccount_exists')
    fee_token_ne = sgqlc.types.Field(Int, graphql_name='feeToken_ne')
    failure_reason_ne = sgqlc.types.Field(String, graphql_name='failureReason_ne')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    kind_ne = sgqlc.types.Field(String, graphql_name='kind_ne')
    fee_gte = sgqlc.types.Field(Float, graphql_name='fee_gte')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    amount_ne = sgqlc.types.Field(Float, graphql_name='amount_ne')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    fee_token_lte = sgqlc.types.Field(Int, graphql_name='feeToken_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_in')
    memo_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_nin')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    to_exists = sgqlc.types.Field(Boolean, graphql_name='to_exists')
    from_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_nin')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    kind_exists = sgqlc.types.Field(Boolean, graphql_name='kind_exists')
    failure_reason_exists = sgqlc.types.Field(Boolean, graphql_name='failureReason_exists')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    memo_exists = sgqlc.types.Field(Boolean, graphql_name='memo_exists')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='amount_in')
    failure_reason_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_in')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    memo_lt = sgqlc.types.Field(String, graphql_name='memo_lt')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_in')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_nin')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    to_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_nin')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandQueryInput')), graphql_name='AND')
    amount_exists = sgqlc.types.Field(Boolean, graphql_name='amount_exists')
    kind_lte = sgqlc.types.Field(String, graphql_name='kind_lte')
    failure_reason_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_nin')
    from_exists = sgqlc.types.Field(Boolean, graphql_name='from_exists')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    fee_token_lt = sgqlc.types.Field(Int, graphql_name='feeToken_lt')
    to_account_exists = sgqlc.types.Field(Boolean, graphql_name='toAccount_exists')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    kind_gte = sgqlc.types.Field(String, graphql_name='kind_gte')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    fee_payer_exists = sgqlc.types.Field(Boolean, graphql_name='feePayer_exists')
    fee_token_gt = sgqlc.types.Field(Int, graphql_name='feeToken_gt')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    failure_reason_gt = sgqlc.types.Field(String, graphql_name='failureReason_gt')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    id = sgqlc.types.Field(String, graphql_name='id')
    memo_gt = sgqlc.types.Field(String, graphql_name='memo_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    to_ne = sgqlc.types.Field(String, graphql_name='to_ne')
    amount_gt = sgqlc.types.Field(Float, graphql_name='amount_gt')
    kind_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_in')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    fee_lte = sgqlc.types.Field(Float, graphql_name='fee_lte')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    memo_gte = sgqlc.types.Field(String, graphql_name='memo_gte')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    to = sgqlc.types.Field(String, graphql_name='to')
    block_state_hash_lte = sgqlc.types.Field(String, graphql_name='blockStateHash_lte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    amount_lt = sgqlc.types.Field(Float, graphql_name='amount_lt')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_in')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    source = sgqlc.types.Field('BlockTransactionUserCommandSourceQueryInput', graphql_name='source')
    fee_token_gte = sgqlc.types.Field(Int, graphql_name='feeToken_gte')
    memo_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_in')
    receiver_exists = sgqlc.types.Field(Boolean, graphql_name='receiver_exists')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    amount_lte = sgqlc.types.Field(Float, graphql_name='amount_lte')
    fee_token_exists = sgqlc.types.Field(Boolean, graphql_name='feeToken_exists')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    memo_ne = sgqlc.types.Field(String, graphql_name='memo_ne')
    id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_nin')
    id_ne = sgqlc.types.Field(String, graphql_name='id_ne')
    fee_ne = sgqlc.types.Field(Float, graphql_name='fee_ne')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    block_state_hash_gt = sgqlc.types.Field(String, graphql_name='blockStateHash_gt')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountQueryInput, graphql_name='fromAccount')
    fee_lt = sgqlc.types.Field(Float, graphql_name='fee_lt')
    token = sgqlc.types.Field(Int, graphql_name='token')
    from_ne = sgqlc.types.Field(String, graphql_name='from_ne')
    block_state_hash_lt = sgqlc.types.Field(String, graphql_name='blockStateHash_lt')
    id_exists = sgqlc.types.Field(Boolean, graphql_name='id_exists')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccountQueryInput', graphql_name='toAccount')
    block_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandQueryInput')), graphql_name='OR')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    failure_reason_lte = sgqlc.types.Field(String, graphql_name='failureReason_lte')
    source_exists = sgqlc.types.Field(Boolean, graphql_name='source_exists')
    failure_reason_gte = sgqlc.types.Field(String, graphql_name='failureReason_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    amount_gte = sgqlc.types.Field(Float, graphql_name='amount_gte')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    fee_token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_nin')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    kind_lt = sgqlc.types.Field(String, graphql_name='kind_lt')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    block_state_hash_ne = sgqlc.types.Field(String, graphql_name='blockStateHash_ne')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiverQueryInput', graphql_name='receiver')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_in')
    amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='amount_nin')
    block_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_exists')
    block_state_hash_gte = sgqlc.types.Field(String, graphql_name='blockStateHash_gte')
    memo_lte = sgqlc.types.Field(String, graphql_name='memo_lte')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')


class BlockTransactionUserCommandReceiverInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandReceiverQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_lte', 'public_key_gte', 'public_key_lt', 'public_key_in', 'public_key_ne', 'public_key_gt', 'public_key_exists', 'public_key_nin', 'and_', 'or_', 'public_key')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandReceiverQueryInput')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandReceiverQueryInput')), graphql_name='OR')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandReceiverUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_unset', 'public_key')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandSourceInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandSourceQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_exists', 'public_key_gte', 'public_key_lt', 'public_key_in', 'public_key_ne', 'public_key_lte', 'and_', 'public_key', 'public_key_gt', 'public_key_nin', 'or_')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandSourceQueryInput')), graphql_name='AND')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandSourceQueryInput')), graphql_name='OR')


class BlockTransactionUserCommandSourceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class BlockTransactionUserCommandToAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandToAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('and_', 'token_lte', 'token', 'token_in', 'token_ne', 'token_gte', 'or_', 'token_nin', 'token_exists', 'token_gt', 'token_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandToAccountQueryInput')), graphql_name='AND')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandToAccountQueryInput')), graphql_name='OR')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')


class BlockTransactionUserCommandToAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class BlockTransactionUserCommandUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('nonce', 'to_account_unset', 'failure_reason_unset', 'block_height_inc', 'nonce_unset', 'block_state_hash', 'to_unset', 'block_height', 'from_account_unset', 'token', 'failure_reason', 'amount_unset', 'date_time_unset', 'amount_inc', 'id', 'fee_unset', 'kind_unset', 'to', 'source_unset', 'fee_token_unset', 'is_delegation', 'fee_payer_unset', 'memo_unset', 'token_unset', 'fee_inc', 'block_height_unset', 'from_account', 'is_delegation_unset', 'fee_token', 'from_', 'to_account', 'hash', 'memo', 'hash_unset', 'id_unset', 'receiver_unset', 'source', 'block_state_hash_unset', 'nonce_inc', 'from_unset', 'fee_payer', 'date_time', 'kind', 'fee', 'fee_token_inc', 'amount', 'token_inc', 'receiver')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    to_account_unset = sgqlc.types.Field(Boolean, graphql_name='toAccount_unset')
    failure_reason_unset = sgqlc.types.Field(Boolean, graphql_name='failureReason_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    to_unset = sgqlc.types.Field(Boolean, graphql_name='to_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    from_account_unset = sgqlc.types.Field(Boolean, graphql_name='fromAccount_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    amount_unset = sgqlc.types.Field(Boolean, graphql_name='amount_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    amount_inc = sgqlc.types.Field(Float, graphql_name='amount_inc')
    id = sgqlc.types.Field(String, graphql_name='id')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    kind_unset = sgqlc.types.Field(Boolean, graphql_name='kind_unset')
    to = sgqlc.types.Field(String, graphql_name='to')
    source_unset = sgqlc.types.Field(Boolean, graphql_name='source_unset')
    fee_token_unset = sgqlc.types.Field(Boolean, graphql_name='feeToken_unset')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    fee_payer_unset = sgqlc.types.Field(Boolean, graphql_name='feePayer_unset')
    memo_unset = sgqlc.types.Field(Boolean, graphql_name='memo_unset')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    fee_inc = sgqlc.types.Field(Float, graphql_name='fee_inc')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountUpdateInput, graphql_name='fromAccount')
    is_delegation_unset = sgqlc.types.Field(Boolean, graphql_name='isDelegation_unset')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    to_account = sgqlc.types.Field(BlockTransactionUserCommandToAccountUpdateInput, graphql_name='toAccount')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    id_unset = sgqlc.types.Field(Boolean, graphql_name='id_unset')
    receiver_unset = sgqlc.types.Field(Boolean, graphql_name='receiver_unset')
    source = sgqlc.types.Field(BlockTransactionUserCommandSourceUpdateInput, graphql_name='source')
    block_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_unset')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    from_unset = sgqlc.types.Field(Boolean, graphql_name='from_unset')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerUpdateInput, graphql_name='feePayer')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    fee_token_inc = sgqlc.types.Field(Int, graphql_name='feeToken_inc')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    receiver = sgqlc.types.Field(BlockTransactionUserCommandReceiverUpdateInput, graphql_name='receiver')


class BlockUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'winner_account', 'creator', 'block_height_unset', 'received_time_unset', 'creator_account', 'date_time', 'date_time_unset', 'state_hash_field', 'canonical_unset', 'state_hash', 'canonical', 'winner_account_unset', 'block_height_inc', 'snark_jobs_unset', 'state_hash_unset', 'protocol_state_unset', 'transactions', 'protocol_state', 'received_time', 'creator_unset', 'snark_jobs', 'state_hash_field_unset', 'creator_account_unset', 'transactions_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    winner_account = sgqlc.types.Field('BlockWinnerAccountUpdateInput', graphql_name='winnerAccount')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    received_time_unset = sgqlc.types.Field(Boolean, graphql_name='receivedTime_unset')
    creator_account = sgqlc.types.Field(BlockCreatorAccountUpdateInput, graphql_name='creatorAccount')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    winner_account_unset = sgqlc.types.Field(Boolean, graphql_name='winnerAccount_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    snark_jobs_unset = sgqlc.types.Field(Boolean, graphql_name='snarkJobs_unset')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    protocol_state_unset = sgqlc.types.Field(Boolean, graphql_name='protocolState_unset')
    transactions = sgqlc.types.Field(BlockTransactionUpdateInput, graphql_name='transactions')
    protocol_state = sgqlc.types.Field(BlockProtocolStateUpdateInput, graphql_name='protocolState')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    creator_unset = sgqlc.types.Field(Boolean, graphql_name='creator_unset')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of(BlockSnarkJobUpdateInput), graphql_name='snarkJobs')
    state_hash_field_unset = sgqlc.types.Field(Boolean, graphql_name='stateHashField_unset')
    creator_account_unset = sgqlc.types.Field(Boolean, graphql_name='creatorAccount_unset')
    transactions_unset = sgqlc.types.Field(Boolean, graphql_name='transactions_unset')


class BlockWinnerAccountBalanceInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('liquid', 'locked', 'state_hash', 'total', 'unknown', 'block_height')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    total = sgqlc.types.Field(Long, graphql_name='total')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')


class BlockWinnerAccountBalanceQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('unknown_lt', 'total_in', 'locked_exists', 'and_', 'locked_in', 'block_height_ne', 'unknown_gte', 'liquid_lt', 'state_hash_nin', 'state_hash_ne', 'block_height', 'liquid_gte', 'total_gte', 'total_lte', 'liquid_gt', 'state_hash_exists', 'state_hash_lte', 'total_gt', 'block_height_exists', 'unknown_in', 'locked', 'or_', 'block_height_lte', 'locked_gt', 'block_height_gte', 'block_height_lt', 'total_nin', 'block_height_gt', 'state_hash_gt', 'state_hash_in', 'block_height_nin', 'liquid_in', 'block_height_in', 'total', 'liquid_lte', 'locked_ne', 'unknown_ne', 'locked_lt', 'liquid_exists', 'locked_nin', 'liquid', 'unknown', 'unknown_lte', 'state_hash_gte', 'liquid_nin', 'unknown_exists', 'total_ne', 'liquid_ne', 'unknown_nin', 'unknown_gt', 'total_exists', 'locked_gte', 'total_lt', 'state_hash', 'state_hash_lt', 'locked_lte')
    unknown_lt = sgqlc.types.Field(Long, graphql_name='unknown_lt')
    total_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='total_in')
    locked_exists = sgqlc.types.Field(Boolean, graphql_name='locked_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountBalanceQueryInput')), graphql_name='AND')
    locked_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='locked_in')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    unknown_gte = sgqlc.types.Field(Long, graphql_name='unknown_gte')
    liquid_lt = sgqlc.types.Field(Int, graphql_name='liquid_lt')
    state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_nin')
    state_hash_ne = sgqlc.types.Field(String, graphql_name='stateHash_ne')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    liquid_gte = sgqlc.types.Field(Int, graphql_name='liquid_gte')
    total_gte = sgqlc.types.Field(Long, graphql_name='total_gte')
    total_lte = sgqlc.types.Field(Long, graphql_name='total_lte')
    liquid_gt = sgqlc.types.Field(Int, graphql_name='liquid_gt')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    state_hash_lte = sgqlc.types.Field(String, graphql_name='stateHash_lte')
    total_gt = sgqlc.types.Field(Long, graphql_name='total_gt')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    unknown_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='unknown_in')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountBalanceQueryInput')), graphql_name='OR')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    locked_gt = sgqlc.types.Field(Long, graphql_name='locked_gt')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    total_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='total_nin')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    state_hash_gt = sgqlc.types.Field(String, graphql_name='stateHash_gt')
    state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_in')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    liquid_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='liquid_in')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    total = sgqlc.types.Field(Long, graphql_name='total')
    liquid_lte = sgqlc.types.Field(Int, graphql_name='liquid_lte')
    locked_ne = sgqlc.types.Field(Long, graphql_name='locked_ne')
    unknown_ne = sgqlc.types.Field(Long, graphql_name='unknown_ne')
    locked_lt = sgqlc.types.Field(Long, graphql_name='locked_lt')
    liquid_exists = sgqlc.types.Field(Boolean, graphql_name='liquid_exists')
    locked_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='locked_nin')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    unknown_lte = sgqlc.types.Field(Long, graphql_name='unknown_lte')
    state_hash_gte = sgqlc.types.Field(String, graphql_name='stateHash_gte')
    liquid_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='liquid_nin')
    unknown_exists = sgqlc.types.Field(Boolean, graphql_name='unknown_exists')
    total_ne = sgqlc.types.Field(Long, graphql_name='total_ne')
    liquid_ne = sgqlc.types.Field(Int, graphql_name='liquid_ne')
    unknown_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='unknown_nin')
    unknown_gt = sgqlc.types.Field(Long, graphql_name='unknown_gt')
    total_exists = sgqlc.types.Field(Boolean, graphql_name='total_exists')
    locked_gte = sgqlc.types.Field(Long, graphql_name='locked_gte')
    total_lt = sgqlc.types.Field(Long, graphql_name='total_lt')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    state_hash_lt = sgqlc.types.Field(String, graphql_name='stateHash_lt')
    locked_lte = sgqlc.types.Field(Long, graphql_name='locked_lte')


class BlockWinnerAccountBalanceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('liquid', 'block_height', 'locked', 'total_unset', 'unknown', 'unknown_unset', 'locked_unset', 'state_hash_unset', 'block_height_inc', 'state_hash', 'liquid_unset', 'total', 'liquid_inc', 'block_height_unset')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    total_unset = sgqlc.types.Field(Boolean, graphql_name='total_unset')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    unknown_unset = sgqlc.types.Field(Boolean, graphql_name='unknown_unset')
    locked_unset = sgqlc.types.Field(Boolean, graphql_name='locked_unset')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    liquid_unset = sgqlc.types.Field(Boolean, graphql_name='liquid_unset')
    total = sgqlc.types.Field(Long, graphql_name='total')
    liquid_inc = sgqlc.types.Field(Int, graphql_name='liquid_inc')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')


class BlockWinnerAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'balance')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceInsertInput, graphql_name='balance')


class BlockWinnerAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_ne', 'public_key_gt', 'public_key', 'public_key_in', 'balance', 'public_key_lte', 'public_key_gte', 'public_key_exists', 'or_', 'balance_exists', 'public_key_lt', 'public_key_nin', 'and_')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceQueryInput, graphql_name='balance')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountQueryInput')), graphql_name='OR')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountQueryInput')), graphql_name='AND')


class BlockWinnerAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'balance_unset', 'public_key', 'public_key_unset')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceUpdateInput, graphql_name='balance')
    balance_unset = sgqlc.types.Field(Boolean, graphql_name='balance_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class NextstakeInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'delegate', 'nonce', 'permissions', 'receipt_chain_hash', 'timing', 'pk', 'token', 'voting_for', 'ledger_hash', 'public_key')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('NextstakePermissionInsertInput', graphql_name='permissions')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    timing = sgqlc.types.Field('NextstakeTimingInsertInput', graphql_name='timing')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    token = sgqlc.types.Field(Int, graphql_name='token')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')


class NextstakePermissionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('edit_state', 'send', 'set_delegate', 'set_permissions', 'set_verification_key', 'stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')


class NextstakePermissionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('set_delegate', 'set_verification_key_gte', 'stake_exists', 'set_delegate_exists', 'set_delegate_nin', 'set_permissions_in', 'and_', 'set_permissions_exists', 'send', 'edit_state', 'set_permissions', 'or_', 'set_delegate_lte', 'set_verification_key_exists', 'set_permissions_nin', 'set_delegate_lt', 'edit_state_lt', 'set_verification_key_nin', 'set_verification_key_ne', 'set_verification_key_lte', 'send_ne', 'send_in', 'set_verification_key_gt', 'edit_state_gte', 'set_delegate_gt', 'set_permissions_ne', 'edit_state_nin', 'set_verification_key_lt', 'send_gte', 'set_permissions_lte', 'set_delegate_in', 'send_gt', 'edit_state_in', 'send_exists', 'edit_state_ne', 'send_nin', 'edit_state_lte', 'send_lte', 'stake', 'set_permissions_gte', 'set_permissions_gt', 'set_delegate_gte', 'edit_state_exists', 'send_lt', 'set_delegate_ne', 'edit_state_gt', 'set_verification_key', 'set_verification_key_in', 'stake_ne', 'set_permissions_lt')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_verification_key_gte = sgqlc.types.Field(String, graphql_name='set_verification_key_gte')
    stake_exists = sgqlc.types.Field(Boolean, graphql_name='stake_exists')
    set_delegate_exists = sgqlc.types.Field(Boolean, graphql_name='set_delegate_exists')
    set_delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_nin')
    set_permissions_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NextstakePermissionQueryInput')), graphql_name='AND')
    set_permissions_exists = sgqlc.types.Field(Boolean, graphql_name='set_permissions_exists')
    send = sgqlc.types.Field(String, graphql_name='send')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NextstakePermissionQueryInput')), graphql_name='OR')
    set_delegate_lte = sgqlc.types.Field(String, graphql_name='set_delegate_lte')
    set_verification_key_exists = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_exists')
    set_permissions_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_nin')
    set_delegate_lt = sgqlc.types.Field(String, graphql_name='set_delegate_lt')
    edit_state_lt = sgqlc.types.Field(String, graphql_name='edit_state_lt')
    set_verification_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_nin')
    set_verification_key_ne = sgqlc.types.Field(String, graphql_name='set_verification_key_ne')
    set_verification_key_lte = sgqlc.types.Field(String, graphql_name='set_verification_key_lte')
    send_ne = sgqlc.types.Field(String, graphql_name='send_ne')
    send_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_in')
    set_verification_key_gt = sgqlc.types.Field(String, graphql_name='set_verification_key_gt')
    edit_state_gte = sgqlc.types.Field(String, graphql_name='edit_state_gte')
    set_delegate_gt = sgqlc.types.Field(String, graphql_name='set_delegate_gt')
    set_permissions_ne = sgqlc.types.Field(String, graphql_name='set_permissions_ne')
    edit_state_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_nin')
    set_verification_key_lt = sgqlc.types.Field(String, graphql_name='set_verification_key_lt')
    send_gte = sgqlc.types.Field(String, graphql_name='send_gte')
    set_permissions_lte = sgqlc.types.Field(String, graphql_name='set_permissions_lte')
    set_delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_in')
    send_gt = sgqlc.types.Field(String, graphql_name='send_gt')
    edit_state_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_in')
    send_exists = sgqlc.types.Field(Boolean, graphql_name='send_exists')
    edit_state_ne = sgqlc.types.Field(String, graphql_name='edit_state_ne')
    send_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_nin')
    edit_state_lte = sgqlc.types.Field(String, graphql_name='edit_state_lte')
    send_lte = sgqlc.types.Field(String, graphql_name='send_lte')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    set_permissions_gte = sgqlc.types.Field(String, graphql_name='set_permissions_gte')
    set_permissions_gt = sgqlc.types.Field(String, graphql_name='set_permissions_gt')
    set_delegate_gte = sgqlc.types.Field(String, graphql_name='set_delegate_gte')
    edit_state_exists = sgqlc.types.Field(Boolean, graphql_name='edit_state_exists')
    send_lt = sgqlc.types.Field(String, graphql_name='send_lt')
    set_delegate_ne = sgqlc.types.Field(String, graphql_name='set_delegate_ne')
    edit_state_gt = sgqlc.types.Field(String, graphql_name='edit_state_gt')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    set_verification_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_in')
    stake_ne = sgqlc.types.Field(Boolean, graphql_name='stake_ne')
    set_permissions_lt = sgqlc.types.Field(String, graphql_name='set_permissions_lt')


class NextstakePermissionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('send', 'set_verification_key', 'send_unset', 'set_delegate', 'set_delegate_unset', 'set_permissions', 'set_verification_key_unset', 'stake_unset', 'set_permissions_unset', 'edit_state_unset', 'stake', 'edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    send_unset = sgqlc.types.Field(Boolean, graphql_name='send_unset')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_delegate_unset = sgqlc.types.Field(Boolean, graphql_name='set_delegate_unset')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key_unset = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_unset')
    stake_unset = sgqlc.types.Field(Boolean, graphql_name='stake_unset')
    set_permissions_unset = sgqlc.types.Field(Boolean, graphql_name='set_permissions_unset')
    edit_state_unset = sgqlc.types.Field(Boolean, graphql_name='edit_state_unset')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')


class NextstakeQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('pk_ne', 'voting_for_exists', 'token_lte', 'ledger_hash_exists', 'pk_gte', 'nonce_gte', 'delegate', 'token_exists', 'permissions', 'balance_ne', 'ledger_hash_ne', 'ledger_hash_nin', 'pk', 'public_key_gte', 'receipt_chain_hash_in', 'permissions_exists', 'nonce_nin', 'balance_nin', 'and_', 'voting_for_nin', 'public_key', 'public_key_in', 'receipt_chain_hash_ne', 'timing_exists', 'pk_in', 'token_ne', 'ledger_hash_gt', 'public_key_lt', 'balance_gt', 'balance_exists', 'pk_lt', 'pk_nin', 'receipt_chain_hash_exists', 'token_nin', 'ledger_hash_lte', 'voting_for_ne', 'or_', 'nonce_exists', 'delegate_exists', 'ledger_hash_gte', 'nonce_lt', 'voting_for_lte', 'nonce', 'delegate_nin', 'nonce_lte', 'receipt_chain_hash_lte', 'receipt_chain_hash_lt', 'pk_exists', 'nonce_in', 'receipt_chain_hash', 'delegate_lte', 'ledger_hash', 'ledger_hash_in', 'balance', 'token_lt', 'voting_for', 'voting_for_gt', 'nonce_gt', 'delegate_gte', 'balance_gte', 'ledger_hash_lt', 'receipt_chain_hash_gte', 'token_gt', 'public_key_exists', 'public_key_gt', 'delegate_lt', 'receipt_chain_hash_gt', 'balance_lte', 'delegate_gt', 'pk_lte', 'public_key_nin', 'voting_for_gte', 'pk_gt', 'balance_lt', 'voting_for_in', 'public_key_ne', 'receipt_chain_hash_nin', 'token_in', 'delegate_in', 'token', 'timing', 'nonce_ne', 'balance_in', 'voting_for_lt', 'token_gte', 'public_key_lte', 'delegate_ne')
    pk_ne = sgqlc.types.Field(String, graphql_name='pk_ne')
    voting_for_exists = sgqlc.types.Field(Boolean, graphql_name='voting_for_exists')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_exists')
    pk_gte = sgqlc.types.Field(String, graphql_name='pk_gte')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    permissions = sgqlc.types.Field(NextstakePermissionQueryInput, graphql_name='permissions')
    balance_ne = sgqlc.types.Field(Float, graphql_name='balance_ne')
    ledger_hash_ne = sgqlc.types.Field(String, graphql_name='ledgerHash_ne')
    ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_nin')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    public_key_gte = sgqlc.types.Field(String, graphql_name='public_key_gte')
    receipt_chain_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_in')
    permissions_exists = sgqlc.types.Field(Boolean, graphql_name='permissions_exists')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NextstakeQueryInput')), graphql_name='AND')
    voting_for_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_nin')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_in')
    receipt_chain_hash_ne = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_ne')
    timing_exists = sgqlc.types.Field(Boolean, graphql_name='timing_exists')
    pk_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pk_in')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    ledger_hash_gt = sgqlc.types.Field(String, graphql_name='ledgerHash_gt')
    public_key_lt = sgqlc.types.Field(String, graphql_name='public_key_lt')
    balance_gt = sgqlc.types.Field(Float, graphql_name='balance_gt')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')
    pk_lt = sgqlc.types.Field(String, graphql_name='pk_lt')
    pk_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pk_nin')
    receipt_chain_hash_exists = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_exists')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    ledger_hash_lte = sgqlc.types.Field(String, graphql_name='ledgerHash_lte')
    voting_for_ne = sgqlc.types.Field(String, graphql_name='voting_for_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NextstakeQueryInput')), graphql_name='OR')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    delegate_exists = sgqlc.types.Field(Boolean, graphql_name='delegate_exists')
    ledger_hash_gte = sgqlc.types.Field(String, graphql_name='ledgerHash_gte')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    voting_for_lte = sgqlc.types.Field(String, graphql_name='voting_for_lte')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_nin')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    receipt_chain_hash_lte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lte')
    receipt_chain_hash_lt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lt')
    pk_exists = sgqlc.types.Field(Boolean, graphql_name='pk_exists')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    delegate_lte = sgqlc.types.Field(String, graphql_name='delegate_lte')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_in')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    voting_for_gt = sgqlc.types.Field(String, graphql_name='voting_for_gt')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    delegate_gte = sgqlc.types.Field(String, graphql_name='delegate_gte')
    balance_gte = sgqlc.types.Field(Float, graphql_name='balance_gte')
    ledger_hash_lt = sgqlc.types.Field(String, graphql_name='ledgerHash_lt')
    receipt_chain_hash_gte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='public_key_exists')
    public_key_gt = sgqlc.types.Field(String, graphql_name='public_key_gt')
    delegate_lt = sgqlc.types.Field(String, graphql_name='delegate_lt')
    receipt_chain_hash_gt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gt')
    balance_lte = sgqlc.types.Field(Float, graphql_name='balance_lte')
    delegate_gt = sgqlc.types.Field(String, graphql_name='delegate_gt')
    pk_lte = sgqlc.types.Field(String, graphql_name='pk_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_nin')
    voting_for_gte = sgqlc.types.Field(String, graphql_name='voting_for_gte')
    pk_gt = sgqlc.types.Field(String, graphql_name='pk_gt')
    balance_lt = sgqlc.types.Field(Float, graphql_name='balance_lt')
    voting_for_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_in')
    public_key_ne = sgqlc.types.Field(String, graphql_name='public_key_ne')
    receipt_chain_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_nin')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_in')
    token = sgqlc.types.Field(Int, graphql_name='token')
    timing = sgqlc.types.Field('NextstakeTimingQueryInput', graphql_name='timing')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_in')
    voting_for_lt = sgqlc.types.Field(String, graphql_name='voting_for_lt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    public_key_lte = sgqlc.types.Field(String, graphql_name='public_key_lte')
    delegate_ne = sgqlc.types.Field(String, graphql_name='delegate_ne')


class NextstakeTimingInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('vesting_increment', 'vesting_period', 'cliff_amount', 'cliff_time', 'initial_minimum_balance')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')


class NextstakeTimingQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('vesting_period_ne', 'and_', 'vesting_period_gte', 'initial_minimum_balance', 'initial_minimum_balance_lt', 'cliff_time', 'cliff_time_gte', 'cliff_amount_lte', 'vesting_period_gt', 'or_', 'cliff_amount_gt', 'vesting_increment_gte', 'cliff_time_ne', 'cliff_amount_lt', 'vesting_increment', 'cliff_time_exists', 'initial_minimum_balance_gte', 'vesting_increment_exists', 'initial_minimum_balance_lte', 'initial_minimum_balance_gt', 'vesting_period_exists', 'cliff_time_lt', 'vesting_period_lt', 'vesting_period_nin', 'initial_minimum_balance_nin', 'initial_minimum_balance_in', 'initial_minimum_balance_ne', 'vesting_increment_gt', 'vesting_increment_in', 'cliff_amount_ne', 'cliff_time_nin', 'vesting_period_in', 'cliff_amount_nin', 'cliff_time_lte', 'cliff_amount_in', 'vesting_increment_lte', 'cliff_amount', 'cliff_amount_gte', 'vesting_increment_ne', 'initial_minimum_balance_exists', 'cliff_amount_exists', 'vesting_increment_lt', 'cliff_time_in', 'vesting_period', 'vesting_increment_nin', 'vesting_period_lte', 'cliff_time_gt')
    vesting_period_ne = sgqlc.types.Field(Int, graphql_name='vesting_period_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NextstakeTimingQueryInput')), graphql_name='AND')
    vesting_period_gte = sgqlc.types.Field(Int, graphql_name='vesting_period_gte')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    initial_minimum_balance_lt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lt')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    cliff_time_gte = sgqlc.types.Field(Int, graphql_name='cliff_time_gte')
    cliff_amount_lte = sgqlc.types.Field(Float, graphql_name='cliff_amount_lte')
    vesting_period_gt = sgqlc.types.Field(Int, graphql_name='vesting_period_gt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('NextstakeTimingQueryInput')), graphql_name='OR')
    cliff_amount_gt = sgqlc.types.Field(Float, graphql_name='cliff_amount_gt')
    vesting_increment_gte = sgqlc.types.Field(Float, graphql_name='vesting_increment_gte')
    cliff_time_ne = sgqlc.types.Field(Int, graphql_name='cliff_time_ne')
    cliff_amount_lt = sgqlc.types.Field(Float, graphql_name='cliff_amount_lt')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    cliff_time_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_time_exists')
    initial_minimum_balance_gte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gte')
    vesting_increment_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_exists')
    initial_minimum_balance_lte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lte')
    initial_minimum_balance_gt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gt')
    vesting_period_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_period_exists')
    cliff_time_lt = sgqlc.types.Field(Int, graphql_name='cliff_time_lt')
    vesting_period_lt = sgqlc.types.Field(Int, graphql_name='vesting_period_lt')
    vesting_period_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_nin')
    initial_minimum_balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_nin')
    initial_minimum_balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_in')
    initial_minimum_balance_ne = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_ne')
    vesting_increment_gt = sgqlc.types.Field(Float, graphql_name='vesting_increment_gt')
    vesting_increment_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_in')
    cliff_amount_ne = sgqlc.types.Field(Float, graphql_name='cliff_amount_ne')
    cliff_time_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_nin')
    vesting_period_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_in')
    cliff_amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_nin')
    cliff_time_lte = sgqlc.types.Field(Int, graphql_name='cliff_time_lte')
    cliff_amount_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_in')
    vesting_increment_lte = sgqlc.types.Field(Float, graphql_name='vesting_increment_lte')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    cliff_amount_gte = sgqlc.types.Field(Float, graphql_name='cliff_amount_gte')
    vesting_increment_ne = sgqlc.types.Field(Float, graphql_name='vesting_increment_ne')
    initial_minimum_balance_exists = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_exists')
    cliff_amount_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_exists')
    vesting_increment_lt = sgqlc.types.Field(Float, graphql_name='vesting_increment_lt')
    cliff_time_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_in')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    vesting_increment_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_nin')
    vesting_period_lte = sgqlc.types.Field(Int, graphql_name='vesting_period_lte')
    cliff_time_gt = sgqlc.types.Field(Int, graphql_name='cliff_time_gt')


class NextstakeTimingUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('vesting_increment', 'initial_minimum_balance', 'vesting_period_inc', 'initial_minimum_balance_inc', 'cliff_time_unset', 'cliff_amount_inc', 'cliff_amount_unset', 'cliff_time_inc', 'vesting_increment_inc', 'vesting_increment_unset', 'vesting_period_unset', 'cliff_time', 'vesting_period', 'cliff_amount', 'initial_minimum_balance_unset')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    vesting_period_inc = sgqlc.types.Field(Int, graphql_name='vesting_period_inc')
    initial_minimum_balance_inc = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_inc')
    cliff_time_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_time_unset')
    cliff_amount_inc = sgqlc.types.Field(Float, graphql_name='cliff_amount_inc')
    cliff_amount_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_unset')
    cliff_time_inc = sgqlc.types.Field(Int, graphql_name='cliff_time_inc')
    vesting_increment_inc = sgqlc.types.Field(Float, graphql_name='vesting_increment_inc')
    vesting_increment_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_unset')
    vesting_period_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_period_unset')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    initial_minimum_balance_unset = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_unset')


class NextstakeUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'nonce', 'permissions_unset', 'delegate', 'token_inc', 'balance', 'ledger_hash', 'delegate_unset', 'permissions', 'voting_for_unset', 'balance_inc', 'pk', 'receipt_chain_hash_unset', 'nonce_unset', 'token', 'receipt_chain_hash', 'pk_unset', 'nonce_inc', 'public_key', 'balance_unset', 'public_key_unset', 'timing', 'voting_for', 'ledger_hash_unset', 'timing_unset')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions_unset = sgqlc.types.Field(Boolean, graphql_name='permissions_unset')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    delegate_unset = sgqlc.types.Field(Boolean, graphql_name='delegate_unset')
    permissions = sgqlc.types.Field(NextstakePermissionUpdateInput, graphql_name='permissions')
    voting_for_unset = sgqlc.types.Field(Boolean, graphql_name='voting_for_unset')
    balance_inc = sgqlc.types.Field(Float, graphql_name='balance_inc')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    receipt_chain_hash_unset = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_unset')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    pk_unset = sgqlc.types.Field(Boolean, graphql_name='pk_unset')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    balance_unset = sgqlc.types.Field(Boolean, graphql_name='balance_unset')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='public_key_unset')
    timing = sgqlc.types.Field(NextstakeTimingUpdateInput, graphql_name='timing')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_unset')
    timing_unset = sgqlc.types.Field(Boolean, graphql_name='timing_unset')


class PayoutInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('ledger_hash', 'staking_balance', 'foundation', 'public_key', 'payment_id', 'sum_effective_pool_stakes', 'super_charged_weighting', 'payout', 'block_height', 'coinbase', 'date_time', 'supercharged_contribution', 'effective_pool_weighting', 'payment_hash', 'state_hash', 'total_pool_stakes', 'total_rewards', 'effective_pool_stakes')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    staking_balance = sgqlc.types.Field(Float, graphql_name='stakingBalance')
    foundation = sgqlc.types.Field(Boolean, graphql_name='foundation')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    payment_id = sgqlc.types.Field(String, graphql_name='paymentId')
    sum_effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes')
    super_charged_weighting = sgqlc.types.Field(Float, graphql_name='superChargedWeighting')
    payout = sgqlc.types.Field(Float, graphql_name='payout')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    coinbase = sgqlc.types.Field(Float, graphql_name='coinbase')
    date_time = sgqlc.types.Field(String, graphql_name='dateTime')
    supercharged_contribution = sgqlc.types.Field(Float, graphql_name='superchargedContribution')
    effective_pool_weighting = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting')
    payment_hash = sgqlc.types.Field('PayoutPaymentHashRelationInput', graphql_name='paymentHash')
    state_hash = sgqlc.types.Field('PayoutStateHashRelationInput', graphql_name='stateHash')
    total_pool_stakes = sgqlc.types.Field(Float, graphql_name='totalPoolStakes')
    total_rewards = sgqlc.types.Field(Float, graphql_name='totalRewards')
    effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes')


class PayoutPaymentHashRelationInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('create', 'link')
    create = sgqlc.types.Field('TransactionInsertInput', graphql_name='create')
    link = sgqlc.types.Field(String, graphql_name='link')


class PayoutQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_ne', 'effective_pool_stakes_ne', 'state_hash', 'coinbase_gt', 'super_charged_weighting_in', 'block_height_nin', 'public_key_exists', 'total_pool_stakes_lt', 'effective_pool_stakes', 'super_charged_weighting_lte', 'date_time_gt', 'staking_balance_nin', 'public_key_lte', 'effective_pool_stakes_gt', 'payout_gte', 'payment_id_exists', 'super_charged_weighting_gt', 'super_charged_weighting_ne', 'public_key_gte', 'staking_balance_in', 'effective_pool_weighting_in', 'coinbase', 'block_height_gt', 'supercharged_contribution_ne', 'date_time', 'payment_id_gt', 'payment_id_nin', 'staking_balance_ne', 'coinbase_nin', 'effective_pool_stakes_nin', 'ledger_hash_lte', 'super_charged_weighting_exists', 'coinbase_ne', 'total_pool_stakes_exists', 'supercharged_contribution_in', 'block_height_gte', 'date_time_nin', 'ledger_hash_gte', 'sum_effective_pool_stakes', 'sum_effective_pool_stakes_gt', 'total_rewards_lt', 'sum_effective_pool_stakes_gte', 'total_pool_stakes_lte', 'effective_pool_weighting_lte', 'effective_pool_weighting', 'payment_id_ne', 'payout_exists', 'staking_balance_lte', 'sum_effective_pool_stakes_lte', 'total_pool_stakes_nin', 'payout', 'ledger_hash_nin', 'state_hash_exists', 'date_time_ne', 'date_time_lte', 'sum_effective_pool_stakes_in', 'effective_pool_stakes_exists', 'super_charged_weighting', 'sum_effective_pool_stakes_nin', 'staking_balance_gte', 'payment_hash', 'total_pool_stakes_gte', 'block_height_in', 'supercharged_contribution_lt', 'date_time_in', 'payment_id_lte', 'public_key', 'effective_pool_stakes_gte', 'sum_effective_pool_stakes_exists', 'total_pool_stakes_gt', 'date_time_gte', 'payment_id', 'block_height_lt', 'foundation_ne', 'super_charged_weighting_lt', 'ledger_hash_ne', 'coinbase_in', 'block_height_lte', 'effective_pool_weighting_exists', 'ledger_hash_exists', 'supercharged_contribution_exists', 'payout_lt', 'block_height_exists', 'foundation', 'total_rewards_exists', 'coinbase_gte', 'public_key_lt', 'staking_balance', 'payout_gt', 'payment_id_gte', 'total_rewards_gte', 'sum_effective_pool_stakes_lt', 'and_', 'date_time_lt', 'payout_nin', 'payment_hash_exists', 'foundation_exists', 'total_rewards', 'sum_effective_pool_stakes_ne', 'effective_pool_weighting_ne', 'staking_balance_lt', 'ledger_hash', 'supercharged_contribution_gt', 'supercharged_contribution', 'payment_id_in', 'coinbase_exists', 'coinbase_lt', 'payout_lte', 'coinbase_lte', 'payout_ne', 'payment_id_lt', 'super_charged_weighting_nin', 'effective_pool_weighting_nin', 'staking_balance_exists', 'total_rewards_nin', 'total_rewards_ne', 'date_time_exists', 'total_pool_stakes', 'ledger_hash_lt', 'total_pool_stakes_ne', 'block_height_ne', 'total_pool_stakes_in', 'supercharged_contribution_nin', 'staking_balance_gt', 'total_rewards_gt', 'super_charged_weighting_gte', 'supercharged_contribution_lte', 'supercharged_contribution_gte', 'effective_pool_weighting_gte', 'ledger_hash_in', 'total_rewards_lte', 'effective_pool_weighting_gt', 'effective_pool_stakes_in', 'effective_pool_weighting_lt', 'ledger_hash_gt', 'effective_pool_stakes_lt', 'public_key_gt', 'effective_pool_stakes_lte', 'public_key_nin', 'block_height', 'public_key_in', 'or_', 'total_rewards_in', 'payout_in')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    effective_pool_stakes_ne = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes_ne')
    state_hash = sgqlc.types.Field(BlockQueryInput, graphql_name='stateHash')
    coinbase_gt = sgqlc.types.Field(Float, graphql_name='coinbase_gt')
    super_charged_weighting_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='superChargedWeighting_in')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    total_pool_stakes_lt = sgqlc.types.Field(Float, graphql_name='totalPoolStakes_lt')
    effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes')
    super_charged_weighting_lte = sgqlc.types.Field(Float, graphql_name='superChargedWeighting_lte')
    date_time_gt = sgqlc.types.Field(String, graphql_name='dateTime_gt')
    staking_balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='stakingBalance_nin')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    effective_pool_stakes_gt = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes_gt')
    payout_gte = sgqlc.types.Field(Float, graphql_name='payout_gte')
    payment_id_exists = sgqlc.types.Field(Boolean, graphql_name='paymentId_exists')
    super_charged_weighting_gt = sgqlc.types.Field(Float, graphql_name='superChargedWeighting_gt')
    super_charged_weighting_ne = sgqlc.types.Field(Float, graphql_name='superChargedWeighting_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    staking_balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='stakingBalance_in')
    effective_pool_weighting_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='effectivePoolWeighting_in')
    coinbase = sgqlc.types.Field(Float, graphql_name='coinbase')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    supercharged_contribution_ne = sgqlc.types.Field(Float, graphql_name='superchargedContribution_ne')
    date_time = sgqlc.types.Field(String, graphql_name='dateTime')
    payment_id_gt = sgqlc.types.Field(String, graphql_name='paymentId_gt')
    payment_id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='paymentId_nin')
    staking_balance_ne = sgqlc.types.Field(Float, graphql_name='stakingBalance_ne')
    coinbase_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='coinbase_nin')
    effective_pool_stakes_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='effectivePoolStakes_nin')
    ledger_hash_lte = sgqlc.types.Field(String, graphql_name='ledgerHash_lte')
    super_charged_weighting_exists = sgqlc.types.Field(Boolean, graphql_name='superChargedWeighting_exists')
    coinbase_ne = sgqlc.types.Field(Float, graphql_name='coinbase_ne')
    total_pool_stakes_exists = sgqlc.types.Field(Boolean, graphql_name='totalPoolStakes_exists')
    supercharged_contribution_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='superchargedContribution_in')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='dateTime_nin')
    ledger_hash_gte = sgqlc.types.Field(String, graphql_name='ledgerHash_gte')
    sum_effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes')
    sum_effective_pool_stakes_gt = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes_gt')
    total_rewards_lt = sgqlc.types.Field(Float, graphql_name='totalRewards_lt')
    sum_effective_pool_stakes_gte = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes_gte')
    total_pool_stakes_lte = sgqlc.types.Field(Float, graphql_name='totalPoolStakes_lte')
    effective_pool_weighting_lte = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting_lte')
    effective_pool_weighting = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting')
    payment_id_ne = sgqlc.types.Field(String, graphql_name='paymentId_ne')
    payout_exists = sgqlc.types.Field(Boolean, graphql_name='payout_exists')
    staking_balance_lte = sgqlc.types.Field(Float, graphql_name='stakingBalance_lte')
    sum_effective_pool_stakes_lte = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes_lte')
    total_pool_stakes_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalPoolStakes_nin')
    payout = sgqlc.types.Field(Float, graphql_name='payout')
    ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_nin')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    date_time_ne = sgqlc.types.Field(String, graphql_name='dateTime_ne')
    date_time_lte = sgqlc.types.Field(String, graphql_name='dateTime_lte')
    sum_effective_pool_stakes_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='sumEffectivePoolStakes_in')
    effective_pool_stakes_exists = sgqlc.types.Field(Boolean, graphql_name='effectivePoolStakes_exists')
    super_charged_weighting = sgqlc.types.Field(Float, graphql_name='superChargedWeighting')
    sum_effective_pool_stakes_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='sumEffectivePoolStakes_nin')
    staking_balance_gte = sgqlc.types.Field(Float, graphql_name='stakingBalance_gte')
    payment_hash = sgqlc.types.Field('TransactionQueryInput', graphql_name='paymentHash')
    total_pool_stakes_gte = sgqlc.types.Field(Float, graphql_name='totalPoolStakes_gte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    supercharged_contribution_lt = sgqlc.types.Field(Float, graphql_name='superchargedContribution_lt')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='dateTime_in')
    payment_id_lte = sgqlc.types.Field(String, graphql_name='paymentId_lte')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    effective_pool_stakes_gte = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes_gte')
    sum_effective_pool_stakes_exists = sgqlc.types.Field(Boolean, graphql_name='sumEffectivePoolStakes_exists')
    total_pool_stakes_gt = sgqlc.types.Field(Float, graphql_name='totalPoolStakes_gt')
    date_time_gte = sgqlc.types.Field(String, graphql_name='dateTime_gte')
    payment_id = sgqlc.types.Field(String, graphql_name='paymentId')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    foundation_ne = sgqlc.types.Field(Boolean, graphql_name='foundation_ne')
    super_charged_weighting_lt = sgqlc.types.Field(Float, graphql_name='superChargedWeighting_lt')
    ledger_hash_ne = sgqlc.types.Field(String, graphql_name='ledgerHash_ne')
    coinbase_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='coinbase_in')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    effective_pool_weighting_exists = sgqlc.types.Field(Boolean, graphql_name='effectivePoolWeighting_exists')
    ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_exists')
    supercharged_contribution_exists = sgqlc.types.Field(Boolean, graphql_name='superchargedContribution_exists')
    payout_lt = sgqlc.types.Field(Float, graphql_name='payout_lt')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    foundation = sgqlc.types.Field(Boolean, graphql_name='foundation')
    total_rewards_exists = sgqlc.types.Field(Boolean, graphql_name='totalRewards_exists')
    coinbase_gte = sgqlc.types.Field(Float, graphql_name='coinbase_gte')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    staking_balance = sgqlc.types.Field(Float, graphql_name='stakingBalance')
    payout_gt = sgqlc.types.Field(Float, graphql_name='payout_gt')
    payment_id_gte = sgqlc.types.Field(String, graphql_name='paymentId_gte')
    total_rewards_gte = sgqlc.types.Field(Float, graphql_name='totalRewards_gte')
    sum_effective_pool_stakes_lt = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PayoutQueryInput')), graphql_name='AND')
    date_time_lt = sgqlc.types.Field(String, graphql_name='dateTime_lt')
    payout_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='payout_nin')
    payment_hash_exists = sgqlc.types.Field(Boolean, graphql_name='paymentHash_exists')
    foundation_exists = sgqlc.types.Field(Boolean, graphql_name='foundation_exists')
    total_rewards = sgqlc.types.Field(Float, graphql_name='totalRewards')
    sum_effective_pool_stakes_ne = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes_ne')
    effective_pool_weighting_ne = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting_ne')
    staking_balance_lt = sgqlc.types.Field(Float, graphql_name='stakingBalance_lt')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    supercharged_contribution_gt = sgqlc.types.Field(Float, graphql_name='superchargedContribution_gt')
    supercharged_contribution = sgqlc.types.Field(Float, graphql_name='superchargedContribution')
    payment_id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='paymentId_in')
    coinbase_exists = sgqlc.types.Field(Boolean, graphql_name='coinbase_exists')
    coinbase_lt = sgqlc.types.Field(Float, graphql_name='coinbase_lt')
    payout_lte = sgqlc.types.Field(Float, graphql_name='payout_lte')
    coinbase_lte = sgqlc.types.Field(Float, graphql_name='coinbase_lte')
    payout_ne = sgqlc.types.Field(Float, graphql_name='payout_ne')
    payment_id_lt = sgqlc.types.Field(String, graphql_name='paymentId_lt')
    super_charged_weighting_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='superChargedWeighting_nin')
    effective_pool_weighting_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='effectivePoolWeighting_nin')
    staking_balance_exists = sgqlc.types.Field(Boolean, graphql_name='stakingBalance_exists')
    total_rewards_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalRewards_nin')
    total_rewards_ne = sgqlc.types.Field(Float, graphql_name='totalRewards_ne')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    total_pool_stakes = sgqlc.types.Field(Float, graphql_name='totalPoolStakes')
    ledger_hash_lt = sgqlc.types.Field(String, graphql_name='ledgerHash_lt')
    total_pool_stakes_ne = sgqlc.types.Field(Float, graphql_name='totalPoolStakes_ne')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    total_pool_stakes_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalPoolStakes_in')
    supercharged_contribution_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='superchargedContribution_nin')
    staking_balance_gt = sgqlc.types.Field(Float, graphql_name='stakingBalance_gt')
    total_rewards_gt = sgqlc.types.Field(Float, graphql_name='totalRewards_gt')
    super_charged_weighting_gte = sgqlc.types.Field(Float, graphql_name='superChargedWeighting_gte')
    supercharged_contribution_lte = sgqlc.types.Field(Float, graphql_name='superchargedContribution_lte')
    supercharged_contribution_gte = sgqlc.types.Field(Float, graphql_name='superchargedContribution_gte')
    effective_pool_weighting_gte = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting_gte')
    ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_in')
    total_rewards_lte = sgqlc.types.Field(Float, graphql_name='totalRewards_lte')
    effective_pool_weighting_gt = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting_gt')
    effective_pool_stakes_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='effectivePoolStakes_in')
    effective_pool_weighting_lt = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting_lt')
    ledger_hash_gt = sgqlc.types.Field(String, graphql_name='ledgerHash_gt')
    effective_pool_stakes_lt = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes_lt')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    effective_pool_stakes_lte = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PayoutQueryInput')), graphql_name='OR')
    total_rewards_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalRewards_in')
    payout_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='payout_in')


class PayoutStateHashRelationInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('create', 'link')
    create = sgqlc.types.Field(BlockInsertInput, graphql_name='create')
    link = sgqlc.types.Field(String, graphql_name='link')


class PayoutUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('state_hash_unset', 'total_rewards_unset', 'sum_effective_pool_stakes_inc', 'super_charged_weighting_unset', 'total_pool_stakes_inc', 'effective_pool_weighting', 'effective_pool_weighting_unset', 'payment_hash', 'total_pool_stakes_unset', 'payment_id_unset', 'total_rewards', 'effective_pool_stakes_unset', 'super_charged_weighting', 'total_rewards_inc', 'sum_effective_pool_stakes', 'effective_pool_stakes', 'coinbase_inc', 'staking_balance_inc', 'supercharged_contribution_inc', 'payout_inc', 'sum_effective_pool_stakes_unset', 'block_height_unset', 'block_height_inc', 'date_time_unset', 'supercharged_contribution', 'supercharged_contribution_unset', 'public_key', 'staking_balance', 'effective_pool_stakes_inc', 'date_time', 'payout', 'effective_pool_weighting_inc', 'payment_hash_unset', 'ledger_hash', 'super_charged_weighting_inc', 'block_height', 'coinbase_unset', 'ledger_hash_unset', 'staking_balance_unset', 'coinbase', 'foundation_unset', 'state_hash', 'payout_unset', 'public_key_unset', 'total_pool_stakes', 'foundation', 'payment_id')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    total_rewards_unset = sgqlc.types.Field(Boolean, graphql_name='totalRewards_unset')
    sum_effective_pool_stakes_inc = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes_inc')
    super_charged_weighting_unset = sgqlc.types.Field(Boolean, graphql_name='superChargedWeighting_unset')
    total_pool_stakes_inc = sgqlc.types.Field(Float, graphql_name='totalPoolStakes_inc')
    effective_pool_weighting = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting')
    effective_pool_weighting_unset = sgqlc.types.Field(Boolean, graphql_name='effectivePoolWeighting_unset')
    payment_hash = sgqlc.types.Field(PayoutPaymentHashRelationInput, graphql_name='paymentHash')
    total_pool_stakes_unset = sgqlc.types.Field(Boolean, graphql_name='totalPoolStakes_unset')
    payment_id_unset = sgqlc.types.Field(Boolean, graphql_name='paymentId_unset')
    total_rewards = sgqlc.types.Field(Float, graphql_name='totalRewards')
    effective_pool_stakes_unset = sgqlc.types.Field(Boolean, graphql_name='effectivePoolStakes_unset')
    super_charged_weighting = sgqlc.types.Field(Float, graphql_name='superChargedWeighting')
    total_rewards_inc = sgqlc.types.Field(Float, graphql_name='totalRewards_inc')
    sum_effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes')
    effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes')
    coinbase_inc = sgqlc.types.Field(Float, graphql_name='coinbase_inc')
    staking_balance_inc = sgqlc.types.Field(Float, graphql_name='stakingBalance_inc')
    supercharged_contribution_inc = sgqlc.types.Field(Float, graphql_name='superchargedContribution_inc')
    payout_inc = sgqlc.types.Field(Float, graphql_name='payout_inc')
    sum_effective_pool_stakes_unset = sgqlc.types.Field(Boolean, graphql_name='sumEffectivePoolStakes_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    supercharged_contribution = sgqlc.types.Field(Float, graphql_name='superchargedContribution')
    supercharged_contribution_unset = sgqlc.types.Field(Boolean, graphql_name='superchargedContribution_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    staking_balance = sgqlc.types.Field(Float, graphql_name='stakingBalance')
    effective_pool_stakes_inc = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes_inc')
    date_time = sgqlc.types.Field(String, graphql_name='dateTime')
    payout = sgqlc.types.Field(Float, graphql_name='payout')
    effective_pool_weighting_inc = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting_inc')
    payment_hash_unset = sgqlc.types.Field(Boolean, graphql_name='paymentHash_unset')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    super_charged_weighting_inc = sgqlc.types.Field(Float, graphql_name='superChargedWeighting_inc')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    coinbase_unset = sgqlc.types.Field(Boolean, graphql_name='coinbase_unset')
    ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_unset')
    staking_balance_unset = sgqlc.types.Field(Boolean, graphql_name='stakingBalance_unset')
    coinbase = sgqlc.types.Field(Float, graphql_name='coinbase')
    foundation_unset = sgqlc.types.Field(Boolean, graphql_name='foundation_unset')
    state_hash = sgqlc.types.Field(PayoutStateHashRelationInput, graphql_name='stateHash')
    payout_unset = sgqlc.types.Field(Boolean, graphql_name='payout_unset')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')
    total_pool_stakes = sgqlc.types.Field(Float, graphql_name='totalPoolStakes')
    foundation = sgqlc.types.Field(Boolean, graphql_name='foundation')
    payment_id = sgqlc.types.Field(String, graphql_name='paymentId')


class SnarkBlockStateHashRelationInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('link', 'create')
    link = sgqlc.types.Field(String, graphql_name='link')
    create = sgqlc.types.Field(BlockInsertInput, graphql_name='create')


class SnarkInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'block', 'canonical', 'date_time', 'fee', 'prover', 'work_ids')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block = sgqlc.types.Field(SnarkBlockStateHashRelationInput, graphql_name='block')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')


class SnarkQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee_lt', 'prover_nin', 'block_height_nin', 'fee_lte', 'block_height_ne', 'work_ids_in', 'canonical_ne', 'date_time_ne', 'work_ids', 'fee_ne', 'date_time_nin', 'date_time_exists', 'block_height_lt', 'and_', 'prover_in', 'prover', 'block_height_exists', 'fee_gt', 'work_ids_nin', 'prover_ne', 'prover_lte', 'prover_gte', 'block_height_lte', 'fee_gte', 'fee_exists', 'block_height', 'block_height_in', 'prover_gt', 'block_height_gte', 'date_time_gt', 'fee', 'fee_nin', 'date_time', 'prover_lt', 'date_time_lte', 'canonical_exists', 'block_exists', 'or_', 'fee_in', 'block_height_gt', 'work_ids_exists', 'date_time_gte', 'block', 'prover_exists', 'canonical', 'date_time_lt', 'date_time_in')
    fee_lt = sgqlc.types.Field(Float, graphql_name='fee_lt')
    prover_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_nin')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    fee_lte = sgqlc.types.Field(Float, graphql_name='fee_lte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    work_ids_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_in')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    fee_ne = sgqlc.types.Field(Float, graphql_name='fee_ne')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SnarkQueryInput')), graphql_name='AND')
    prover_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_in')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    fee_gt = sgqlc.types.Field(Float, graphql_name='fee_gt')
    work_ids_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_nin')
    prover_ne = sgqlc.types.Field(String, graphql_name='prover_ne')
    prover_lte = sgqlc.types.Field(String, graphql_name='prover_lte')
    prover_gte = sgqlc.types.Field(String, graphql_name='prover_gte')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    fee_gte = sgqlc.types.Field(Float, graphql_name='fee_gte')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    prover_gt = sgqlc.types.Field(String, graphql_name='prover_gt')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_nin')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    prover_lt = sgqlc.types.Field(String, graphql_name='prover_lt')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    block_exists = sgqlc.types.Field(Boolean, graphql_name='block_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SnarkQueryInput')), graphql_name='OR')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_in')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    work_ids_exists = sgqlc.types.Field(Boolean, graphql_name='workIds_exists')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    block = sgqlc.types.Field(BlockQueryInput, graphql_name='block')
    prover_exists = sgqlc.types.Field(Boolean, graphql_name='prover_exists')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')


class SnarkUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_unset', 'canonical_unset', 'fee', 'block_height', 'date_time', 'canonical', 'fee_inc', 'fee_unset', 'work_ids_unset', 'block_height_unset', 'prover', 'date_time_unset', 'prover_unset', 'work_ids', 'block_height_inc', 'block')
    block_unset = sgqlc.types.Field(Boolean, graphql_name='block_unset')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    fee_inc = sgqlc.types.Field(Float, graphql_name='fee_inc')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    work_ids_unset = sgqlc.types.Field(Boolean, graphql_name='workIds_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    prover_unset = sgqlc.types.Field(Boolean, graphql_name='prover_unset')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block = sgqlc.types.Field(SnarkBlockStateHashRelationInput, graphql_name='block')


class StakeInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('voting_for', 'nonce', 'permissions', 'chain_id', 'delegate', 'pk', 'token', 'balance', 'epoch', 'receipt_chain_hash', 'ledger_hash', 'timing', 'public_key')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('StakePermissionInsertInput', graphql_name='permissions')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    token = sgqlc.types.Field(Int, graphql_name='token')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    timing = sgqlc.types.Field('StakeTimingInsertInput', graphql_name='timing')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')


class StakePermissionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('set_delegate', 'set_permissions', 'set_verification_key', 'stake', 'edit_state', 'send')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')


class StakePermissionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('set_verification_key_gt', 'set_delegate_gt', 'edit_state_nin', 'send_ne', 'send_lte', 'set_verification_key', 'edit_state_lte', 'edit_state_gte', 'and_', 'or_', 'send_nin', 'stake_ne', 'set_permissions_lte', 'set_permissions_in', 'send', 'send_exists', 'set_delegate_lte', 'set_delegate_gte', 'set_verification_key_ne', 'set_permissions', 'set_verification_key_lt', 'set_verification_key_exists', 'set_delegate_ne', 'set_verification_key_in', 'set_verification_key_nin', 'edit_state_in', 'send_gt', 'set_delegate_in', 'set_delegate_exists', 'edit_state', 'send_in', 'send_gte', 'set_permissions_exists', 'edit_state_lt', 'set_permissions_gte', 'set_delegate', 'edit_state_ne', 'send_lt', 'set_permissions_ne', 'set_verification_key_lte', 'stake', 'edit_state_gt', 'set_delegate_lt', 'set_permissions_nin', 'stake_exists', 'set_permissions_gt', 'set_verification_key_gte', 'edit_state_exists', 'set_delegate_nin', 'set_permissions_lt')
    set_verification_key_gt = sgqlc.types.Field(String, graphql_name='set_verification_key_gt')
    set_delegate_gt = sgqlc.types.Field(String, graphql_name='set_delegate_gt')
    edit_state_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_nin')
    send_ne = sgqlc.types.Field(String, graphql_name='send_ne')
    send_lte = sgqlc.types.Field(String, graphql_name='send_lte')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    edit_state_lte = sgqlc.types.Field(String, graphql_name='edit_state_lte')
    edit_state_gte = sgqlc.types.Field(String, graphql_name='edit_state_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakePermissionQueryInput')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakePermissionQueryInput')), graphql_name='OR')
    send_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_nin')
    stake_ne = sgqlc.types.Field(Boolean, graphql_name='stake_ne')
    set_permissions_lte = sgqlc.types.Field(String, graphql_name='set_permissions_lte')
    set_permissions_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_in')
    send = sgqlc.types.Field(String, graphql_name='send')
    send_exists = sgqlc.types.Field(Boolean, graphql_name='send_exists')
    set_delegate_lte = sgqlc.types.Field(String, graphql_name='set_delegate_lte')
    set_delegate_gte = sgqlc.types.Field(String, graphql_name='set_delegate_gte')
    set_verification_key_ne = sgqlc.types.Field(String, graphql_name='set_verification_key_ne')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key_lt = sgqlc.types.Field(String, graphql_name='set_verification_key_lt')
    set_verification_key_exists = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_exists')
    set_delegate_ne = sgqlc.types.Field(String, graphql_name='set_delegate_ne')
    set_verification_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_in')
    set_verification_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_nin')
    edit_state_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_in')
    send_gt = sgqlc.types.Field(String, graphql_name='send_gt')
    set_delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_in')
    set_delegate_exists = sgqlc.types.Field(Boolean, graphql_name='set_delegate_exists')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_in')
    send_gte = sgqlc.types.Field(String, graphql_name='send_gte')
    set_permissions_exists = sgqlc.types.Field(Boolean, graphql_name='set_permissions_exists')
    edit_state_lt = sgqlc.types.Field(String, graphql_name='edit_state_lt')
    set_permissions_gte = sgqlc.types.Field(String, graphql_name='set_permissions_gte')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    edit_state_ne = sgqlc.types.Field(String, graphql_name='edit_state_ne')
    send_lt = sgqlc.types.Field(String, graphql_name='send_lt')
    set_permissions_ne = sgqlc.types.Field(String, graphql_name='set_permissions_ne')
    set_verification_key_lte = sgqlc.types.Field(String, graphql_name='set_verification_key_lte')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    edit_state_gt = sgqlc.types.Field(String, graphql_name='edit_state_gt')
    set_delegate_lt = sgqlc.types.Field(String, graphql_name='set_delegate_lt')
    set_permissions_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_nin')
    stake_exists = sgqlc.types.Field(Boolean, graphql_name='stake_exists')
    set_permissions_gt = sgqlc.types.Field(String, graphql_name='set_permissions_gt')
    set_verification_key_gte = sgqlc.types.Field(String, graphql_name='set_verification_key_gte')
    edit_state_exists = sgqlc.types.Field(Boolean, graphql_name='edit_state_exists')
    set_delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_nin')
    set_permissions_lt = sgqlc.types.Field(String, graphql_name='set_permissions_lt')


class StakePermissionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('set_verification_key_unset', 'stake', 'send', 'set_verification_key', 'set_delegate_unset', 'send_unset', 'set_delegate', 'set_permissions_unset', 'edit_state_unset', 'set_permissions', 'stake_unset', 'edit_state')
    set_verification_key_unset = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_unset')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    set_delegate_unset = sgqlc.types.Field(Boolean, graphql_name='set_delegate_unset')
    send_unset = sgqlc.types.Field(Boolean, graphql_name='send_unset')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions_unset = sgqlc.types.Field(Boolean, graphql_name='set_permissions_unset')
    edit_state_unset = sgqlc.types.Field(Boolean, graphql_name='edit_state_unset')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    stake_unset = sgqlc.types.Field(Boolean, graphql_name='stake_unset')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')


class StakeQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receipt_chain_hash_ne', 'ledger_hash_lte', 'receipt_chain_hash_in', 'receipt_chain_hash_gte', 'balance_ne', 'public_key_exists', 'ledger_hash_gte', 'receipt_chain_hash', 'balance_lte', 'delegate', 'epoch_gte', 'chain_id_in', 'balance_gte', 'epoch_in', 'voting_for_gte', 'permissions', 'delegate_nin', 'token_in', 'epoch_exists', 'pk_ne', 'nonce_lte', 'timing_exists', 'voting_for_exists', 'epoch_nin', 'ledger_hash_lt', 'public_key_in', 'nonce_nin', 'epoch_lte', 'ledger_hash_in', 'chain_id_nin', 'nonce_in', 'public_key_ne', 'receipt_chain_hash_lte', 'ledger_hash_ne', 'public_key_gt', 'receipt_chain_hash_lt', 'chain_id_lt', 'delegate_exists', 'public_key', 'pk', 'voting_for_lte', 'delegate_gte', 'delegate_lte', 'chain_id_lte', 'token_gte', 'chain_id_ne', 'token_exists', 'permissions_exists', 'delegate_in', 'receipt_chain_hash_exists', 'public_key_gte', 'token', 'balance_exists', 'and_', 'nonce', 'token_ne', 'pk_lt', 'voting_for', 'or_', 'voting_for_gt', 'balance', 'nonce_lt', 'chain_id', 'chain_id_gte', 'pk_gte', 'receipt_chain_hash_gt', 'balance_nin', 'voting_for_nin', 'pk_gt', 'pk_nin', 'nonce_exists', 'chain_id_exists', 'epoch', 'epoch_gt', 'ledger_hash_gt', 'public_key_lte', 'token_lt', 'public_key_nin', 'chain_id_gt', 'delegate_ne', 'pk_exists', 'ledger_hash_nin', 'token_nin', 'pk_lte', 'voting_for_lt', 'token_gt', 'epoch_ne', 'nonce_gte', 'ledger_hash_exists', 'receipt_chain_hash_nin', 'balance_in', 'token_lte', 'ledger_hash', 'nonce_gt', 'balance_lt', 'nonce_ne', 'epoch_lt', 'balance_gt', 'delegate_lt', 'delegate_gt', 'timing', 'voting_for_in', 'pk_in', 'public_key_lt', 'voting_for_ne')
    receipt_chain_hash_ne = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_ne')
    ledger_hash_lte = sgqlc.types.Field(String, graphql_name='ledgerHash_lte')
    receipt_chain_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_in')
    receipt_chain_hash_gte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gte')
    balance_ne = sgqlc.types.Field(Float, graphql_name='balance_ne')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='public_key_exists')
    ledger_hash_gte = sgqlc.types.Field(String, graphql_name='ledgerHash_gte')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    balance_lte = sgqlc.types.Field(Float, graphql_name='balance_lte')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    epoch_gte = sgqlc.types.Field(Int, graphql_name='epoch_gte')
    chain_id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chainId_in')
    balance_gte = sgqlc.types.Field(Float, graphql_name='balance_gte')
    epoch_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_in')
    voting_for_gte = sgqlc.types.Field(String, graphql_name='voting_for_gte')
    permissions = sgqlc.types.Field(StakePermissionQueryInput, graphql_name='permissions')
    delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_nin')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    epoch_exists = sgqlc.types.Field(Boolean, graphql_name='epoch_exists')
    pk_ne = sgqlc.types.Field(String, graphql_name='pk_ne')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    timing_exists = sgqlc.types.Field(Boolean, graphql_name='timing_exists')
    voting_for_exists = sgqlc.types.Field(Boolean, graphql_name='voting_for_exists')
    epoch_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_nin')
    ledger_hash_lt = sgqlc.types.Field(String, graphql_name='ledgerHash_lt')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_in')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    epoch_lte = sgqlc.types.Field(Int, graphql_name='epoch_lte')
    ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_in')
    chain_id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chainId_nin')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    public_key_ne = sgqlc.types.Field(String, graphql_name='public_key_ne')
    receipt_chain_hash_lte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lte')
    ledger_hash_ne = sgqlc.types.Field(String, graphql_name='ledgerHash_ne')
    public_key_gt = sgqlc.types.Field(String, graphql_name='public_key_gt')
    receipt_chain_hash_lt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lt')
    chain_id_lt = sgqlc.types.Field(String, graphql_name='chainId_lt')
    delegate_exists = sgqlc.types.Field(Boolean, graphql_name='delegate_exists')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    voting_for_lte = sgqlc.types.Field(String, graphql_name='voting_for_lte')
    delegate_gte = sgqlc.types.Field(String, graphql_name='delegate_gte')
    delegate_lte = sgqlc.types.Field(String, graphql_name='delegate_lte')
    chain_id_lte = sgqlc.types.Field(String, graphql_name='chainId_lte')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    chain_id_ne = sgqlc.types.Field(String, graphql_name='chainId_ne')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    permissions_exists = sgqlc.types.Field(Boolean, graphql_name='permissions_exists')
    delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_in')
    receipt_chain_hash_exists = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_exists')
    public_key_gte = sgqlc.types.Field(String, graphql_name='public_key_gte')
    token = sgqlc.types.Field(Int, graphql_name='token')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeQueryInput')), graphql_name='AND')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    pk_lt = sgqlc.types.Field(String, graphql_name='pk_lt')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeQueryInput')), graphql_name='OR')
    voting_for_gt = sgqlc.types.Field(String, graphql_name='voting_for_gt')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    chain_id_gte = sgqlc.types.Field(String, graphql_name='chainId_gte')
    pk_gte = sgqlc.types.Field(String, graphql_name='pk_gte')
    receipt_chain_hash_gt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gt')
    balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_nin')
    voting_for_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_nin')
    pk_gt = sgqlc.types.Field(String, graphql_name='pk_gt')
    pk_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pk_nin')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    chain_id_exists = sgqlc.types.Field(Boolean, graphql_name='chainId_exists')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    epoch_gt = sgqlc.types.Field(Int, graphql_name='epoch_gt')
    ledger_hash_gt = sgqlc.types.Field(String, graphql_name='ledgerHash_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='public_key_lte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_nin')
    chain_id_gt = sgqlc.types.Field(String, graphql_name='chainId_gt')
    delegate_ne = sgqlc.types.Field(String, graphql_name='delegate_ne')
    pk_exists = sgqlc.types.Field(Boolean, graphql_name='pk_exists')
    ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_nin')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    pk_lte = sgqlc.types.Field(String, graphql_name='pk_lte')
    voting_for_lt = sgqlc.types.Field(String, graphql_name='voting_for_lt')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    epoch_ne = sgqlc.types.Field(Int, graphql_name='epoch_ne')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_exists')
    receipt_chain_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_nin')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_in')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    balance_lt = sgqlc.types.Field(Float, graphql_name='balance_lt')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    epoch_lt = sgqlc.types.Field(Int, graphql_name='epoch_lt')
    balance_gt = sgqlc.types.Field(Float, graphql_name='balance_gt')
    delegate_lt = sgqlc.types.Field(String, graphql_name='delegate_lt')
    delegate_gt = sgqlc.types.Field(String, graphql_name='delegate_gt')
    timing = sgqlc.types.Field('StakeTimingQueryInput', graphql_name='timing')
    voting_for_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_in')
    pk_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pk_in')
    public_key_lt = sgqlc.types.Field(String, graphql_name='public_key_lt')
    voting_for_ne = sgqlc.types.Field(String, graphql_name='voting_for_ne')


class StakeTimingInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('timed_epoch_end', 'cliff_time', 'initial_minimum_balance', 'vesting_period', 'untimed_slot', 'vesting_increment', 'timed_in_epoch', 'cliff_amount', 'timed_weighting')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')


class StakeTimingQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('untimed_slot', 'untimed_slot_in', 'timed_weighting_lte', 'vesting_period_in', 'untimed_slot_lt', 'vesting_increment_gt', 'vesting_increment_exists', 'timed_in_epoch_ne', 'cliff_amount_nin', 'vesting_increment_in', 'cliff_amount_ne', 'untimed_slot_exists', 'untimed_slot_nin', 'vesting_increment_nin', 'cliff_time_gt', 'untimed_slot_lte', 'cliff_time_gte', 'initial_minimum_balance_in', 'vesting_increment', 'cliff_amount_lt', 'timed_weighting', 'vesting_period_ne', 'vesting_period_gt', 'cliff_time_ne', 'vesting_increment_ne', 'vesting_period_nin', 'cliff_time_lte', 'initial_minimum_balance_lte', 'initial_minimum_balance', 'initial_minimum_balance_exists', 'cliff_amount_gte', 'timed_epoch_end_ne', 'initial_minimum_balance_ne', 'cliff_time', 'cliff_time_in', 'cliff_amount_gt', 'timed_weighting_in', 'timed_weighting_exists', 'initial_minimum_balance_gt', 'timed_weighting_ne', 'cliff_time_nin', 'vesting_period', 'timed_weighting_gt', 'vesting_period_lt', 'vesting_period_lte', 'cliff_amount_lte', 'initial_minimum_balance_lt', 'cliff_amount', 'vesting_period_exists', 'and_', 'cliff_time_lt', 'timed_weighting_nin', 'untimed_slot_gt', 'or_', 'initial_minimum_balance_gte', 'timed_weighting_lt', 'timed_in_epoch_exists', 'cliff_time_exists', 'untimed_slot_ne', 'cliff_amount_exists', 'timed_epoch_end_exists', 'timed_in_epoch', 'vesting_increment_gte', 'timed_epoch_end', 'vesting_increment_lte', 'initial_minimum_balance_nin', 'cliff_amount_in', 'vesting_period_gte', 'vesting_increment_lt', 'untimed_slot_gte', 'timed_weighting_gte')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    untimed_slot_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='untimed_slot_in')
    timed_weighting_lte = sgqlc.types.Field(Float, graphql_name='timed_weighting_lte')
    vesting_period_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_in')
    untimed_slot_lt = sgqlc.types.Field(Int, graphql_name='untimed_slot_lt')
    vesting_increment_gt = sgqlc.types.Field(Float, graphql_name='vesting_increment_gt')
    vesting_increment_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_exists')
    timed_in_epoch_ne = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_ne')
    cliff_amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_nin')
    vesting_increment_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_in')
    cliff_amount_ne = sgqlc.types.Field(Float, graphql_name='cliff_amount_ne')
    untimed_slot_exists = sgqlc.types.Field(Boolean, graphql_name='untimed_slot_exists')
    untimed_slot_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='untimed_slot_nin')
    vesting_increment_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_nin')
    cliff_time_gt = sgqlc.types.Field(Int, graphql_name='cliff_time_gt')
    untimed_slot_lte = sgqlc.types.Field(Int, graphql_name='untimed_slot_lte')
    cliff_time_gte = sgqlc.types.Field(Int, graphql_name='cliff_time_gte')
    initial_minimum_balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_in')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    cliff_amount_lt = sgqlc.types.Field(Float, graphql_name='cliff_amount_lt')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    vesting_period_ne = sgqlc.types.Field(Int, graphql_name='vesting_period_ne')
    vesting_period_gt = sgqlc.types.Field(Int, graphql_name='vesting_period_gt')
    cliff_time_ne = sgqlc.types.Field(Int, graphql_name='cliff_time_ne')
    vesting_increment_ne = sgqlc.types.Field(Float, graphql_name='vesting_increment_ne')
    vesting_period_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_nin')
    cliff_time_lte = sgqlc.types.Field(Int, graphql_name='cliff_time_lte')
    initial_minimum_balance_lte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lte')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    initial_minimum_balance_exists = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_exists')
    cliff_amount_gte = sgqlc.types.Field(Float, graphql_name='cliff_amount_gte')
    timed_epoch_end_ne = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_ne')
    initial_minimum_balance_ne = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_ne')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    cliff_time_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_in')
    cliff_amount_gt = sgqlc.types.Field(Float, graphql_name='cliff_amount_gt')
    timed_weighting_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='timed_weighting_in')
    timed_weighting_exists = sgqlc.types.Field(Boolean, graphql_name='timed_weighting_exists')
    initial_minimum_balance_gt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gt')
    timed_weighting_ne = sgqlc.types.Field(Float, graphql_name='timed_weighting_ne')
    cliff_time_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_nin')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    timed_weighting_gt = sgqlc.types.Field(Float, graphql_name='timed_weighting_gt')
    vesting_period_lt = sgqlc.types.Field(Int, graphql_name='vesting_period_lt')
    vesting_period_lte = sgqlc.types.Field(Int, graphql_name='vesting_period_lte')
    cliff_amount_lte = sgqlc.types.Field(Float, graphql_name='cliff_amount_lte')
    initial_minimum_balance_lt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lt')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    vesting_period_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_period_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeTimingQueryInput')), graphql_name='AND')
    cliff_time_lt = sgqlc.types.Field(Int, graphql_name='cliff_time_lt')
    timed_weighting_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='timed_weighting_nin')
    untimed_slot_gt = sgqlc.types.Field(Int, graphql_name='untimed_slot_gt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeTimingQueryInput')), graphql_name='OR')
    initial_minimum_balance_gte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gte')
    timed_weighting_lt = sgqlc.types.Field(Float, graphql_name='timed_weighting_lt')
    timed_in_epoch_exists = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_exists')
    cliff_time_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_time_exists')
    untimed_slot_ne = sgqlc.types.Field(Int, graphql_name='untimed_slot_ne')
    cliff_amount_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_exists')
    timed_epoch_end_exists = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_exists')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    vesting_increment_gte = sgqlc.types.Field(Float, graphql_name='vesting_increment_gte')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    vesting_increment_lte = sgqlc.types.Field(Float, graphql_name='vesting_increment_lte')
    initial_minimum_balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_nin')
    cliff_amount_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_in')
    vesting_period_gte = sgqlc.types.Field(Int, graphql_name='vesting_period_gte')
    vesting_increment_lt = sgqlc.types.Field(Float, graphql_name='vesting_increment_lt')
    untimed_slot_gte = sgqlc.types.Field(Int, graphql_name='untimed_slot_gte')
    timed_weighting_gte = sgqlc.types.Field(Float, graphql_name='timed_weighting_gte')


class StakeTimingUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('timed_in_epoch_unset', 'vesting_period_inc', 'cliff_time', 'initial_minimum_balance_inc', 'initial_minimum_balance', 'timed_weighting', 'untimed_slot_unset', 'vesting_period_unset', 'cliff_amount_unset', 'timed_epoch_end', 'untimed_slot_inc', 'cliff_amount', 'timed_epoch_end_unset', 'cliff_time_unset', 'timed_in_epoch', 'vesting_period', 'vesting_increment', 'vesting_increment_unset', 'cliff_amount_inc', 'cliff_time_inc', 'untimed_slot', 'initial_minimum_balance_unset', 'timed_weighting_inc', 'timed_weighting_unset', 'vesting_increment_inc')
    timed_in_epoch_unset = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_unset')
    vesting_period_inc = sgqlc.types.Field(Int, graphql_name='vesting_period_inc')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    initial_minimum_balance_inc = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_inc')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    untimed_slot_unset = sgqlc.types.Field(Boolean, graphql_name='untimed_slot_unset')
    vesting_period_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_period_unset')
    cliff_amount_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_unset')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    untimed_slot_inc = sgqlc.types.Field(Int, graphql_name='untimed_slot_inc')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    timed_epoch_end_unset = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_unset')
    cliff_time_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_time_unset')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    vesting_increment_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_unset')
    cliff_amount_inc = sgqlc.types.Field(Float, graphql_name='cliff_amount_inc')
    cliff_time_inc = sgqlc.types.Field(Int, graphql_name='cliff_time_inc')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    initial_minimum_balance_unset = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_unset')
    timed_weighting_inc = sgqlc.types.Field(Float, graphql_name='timed_weighting_inc')
    timed_weighting_unset = sgqlc.types.Field(Boolean, graphql_name='timed_weighting_unset')
    vesting_increment_inc = sgqlc.types.Field(Float, graphql_name='vesting_increment_inc')


class StakeUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'chain_id_unset', 'receipt_chain_hash', 'token_unset', 'ledger_hash', 'epoch_unset', 'epoch', 'balance_unset', 'voting_for', 'balance_inc', 'nonce_unset', 'timing', 'voting_for_unset', 'balance', 'delegate_unset', 'public_key', 'nonce', 'permissions', 'nonce_inc', 'pk_unset', 'ledger_hash_unset', 'public_key_unset', 'timing_unset', 'permissions_unset', 'token_inc', 'epoch_inc', 'receipt_chain_hash_unset', 'pk', 'chain_id', 'delegate')
    token = sgqlc.types.Field(Int, graphql_name='token')
    chain_id_unset = sgqlc.types.Field(Boolean, graphql_name='chainId_unset')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    epoch_unset = sgqlc.types.Field(Boolean, graphql_name='epoch_unset')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    balance_unset = sgqlc.types.Field(Boolean, graphql_name='balance_unset')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    balance_inc = sgqlc.types.Field(Float, graphql_name='balance_inc')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    timing = sgqlc.types.Field(StakeTimingUpdateInput, graphql_name='timing')
    voting_for_unset = sgqlc.types.Field(Boolean, graphql_name='voting_for_unset')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    delegate_unset = sgqlc.types.Field(Boolean, graphql_name='delegate_unset')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field(StakePermissionUpdateInput, graphql_name='permissions')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    pk_unset = sgqlc.types.Field(Boolean, graphql_name='pk_unset')
    ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_unset')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='public_key_unset')
    timing_unset = sgqlc.types.Field(Boolean, graphql_name='timing_unset')
    permissions_unset = sgqlc.types.Field(Boolean, graphql_name='permissions_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    epoch_inc = sgqlc.types.Field(Int, graphql_name='epoch_inc')
    receipt_chain_hash_unset = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_unset')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')


class TransactionBlockStateHashRelationInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('create', 'link')
    create = sgqlc.types.Field(BlockInsertInput, graphql_name='create')
    link = sgqlc.types.Field(String, graphql_name='link')


class TransactionFeePayerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionFeePayerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_lte', 'token_in', 'token_exists', 'token_gte', 'token_lt', 'and_', 'token_nin', 'or_', 'token', 'token_ne', 'token_gt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFeePayerQueryInput')), graphql_name='AND')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFeePayerQueryInput')), graphql_name='OR')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')


class TransactionFeePayerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'token', 'token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')


class TransactionFromAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionFromAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_lte', 'token_nin', 'token_exists', 'token', 'token_gt', 'and_', 'token_lt', 'or_', 'token_ne', 'token_gte', 'token_in')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFromAccountQueryInput')), graphql_name='AND')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFromAccountQueryInput')), graphql_name='OR')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')


class TransactionFromAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class TransactionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receiver', 'amount', 'from_', 'source', 'token', 'fee', 'nonce', 'from_account', 'block_height', 'kind', 'is_delegation', 'hash', 'block', 'failure_reason', 'date_time', 'fee_token', 'to_account', 'memo', 'canonical', 'fee_payer', 'id', 'to')
    receiver = sgqlc.types.Field('TransactionReceiverInsertInput', graphql_name='receiver')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    source = sgqlc.types.Field('TransactionSourceInsertInput', graphql_name='source')
    token = sgqlc.types.Field(Int, graphql_name='token')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    from_account = sgqlc.types.Field(TransactionFromAccountInsertInput, graphql_name='fromAccount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    block = sgqlc.types.Field(TransactionBlockStateHashRelationInput, graphql_name='block')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    to_account = sgqlc.types.Field('TransactionToAccountInsertInput', graphql_name='toAccount')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    fee_payer = sgqlc.types.Field(TransactionFeePayerInsertInput, graphql_name='feePayer')
    id = sgqlc.types.Field(String, graphql_name='id')
    to = sgqlc.types.Field(String, graphql_name='to')


class TransactionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gte', 'to_exists', 'fee_gt', 'id_nin', 'kind', 'nonce_ne', 'is_delegation_exists', 'fee_token_nin', 'from_lte', 'token_nin', 'and_', 'failure_reason', 'memo_in', 'id_lte', 'hash_lte', 'fee_payer_exists', 'memo', 'token_in', 'hash_gt', 'to_account_exists', 'kind_lt', 'fee_lt', 'failure_reason_in', 'hash_ne', 'nonce_gt', 'canonical', 'from_account_exists', 'memo_nin', 'kind_lte', 'fee_lte', 'to_lte', 'id_lt', 'kind_nin', 'date_time_gte', 'token_gt', 'kind_in', 'from_exists', 'is_delegation_ne', 'from_gte', 'block_height_ne', 'id_exists', 'fee_token_gt', 'token_exists', 'nonce_lte', 'to_gt', 'to', 'amount_nin', 'fee_token_in', 'amount_lt', 'memo_ne', 'failure_reason_nin', 'from_ne', 'amount_lte', 'memo_gte', 'date_time_lte', 'date_time', 'amount_gte', 'fee', 'date_time_lt', 'to_ne', 'from_gt', 'memo_exists', 'fee_token', 'to_gte', 'date_time_in', 'block_height_in', 'memo_lte', 'date_time_nin', 'date_time_gt', 'to_lt', 'nonce_exists', 'block_exists', 'fee_token_gte', 'date_time_exists', 'failure_reason_gt', 'fee_token_lt', 'amount_gt', 'fee_token_exists', 'block_height_lt', 'block_height_gt', 'id', 'block_height_exists', 'kind_gt', 'nonce_nin', 'hash_nin', 'failure_reason_lt', 'from_account', 'from_lt', 'fee_payer', 'hash_gte', 'memo_gt', 'hash', 'hash_exists', 'id_in', 'hash_lt', 'block', 'from_nin', 'block_height_nin', 'nonce_lt', 'hash_in', 'fee_token_lte', 'token', 'amount', 'token_lt', 'from_', 'is_delegation', 'canonical_exists', 'nonce', 'token_lte', 'from_in', 'id_gte', 'failure_reason_lte', 'or_', 'amount_exists', 'failure_reason_gte', 'fee_exists', 'receiver_exists', 'block_height_lte', 'source_exists', 'nonce_in', 'fee_token_ne', 'to_in', 'id_gt', 'amount_ne', 'to_nin', 'block_height_gte', 'failure_reason_ne', 'fee_gte', 'nonce_gte', 'kind_gte', 'amount_in', 'id_ne', 'source', 'memo_lt', 'kind_exists', 'date_time_ne', 'fee_in', 'canonical_ne', 'token_ne', 'fee_nin', 'receiver', 'to_account', 'block_height', 'fee_ne', 'failure_reason_exists', 'kind_ne')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    to_exists = sgqlc.types.Field(Boolean, graphql_name='to_exists')
    fee_gt = sgqlc.types.Field(Float, graphql_name='fee_gt')
    id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_nin')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    is_delegation_exists = sgqlc.types.Field(Boolean, graphql_name='isDelegation_exists')
    fee_token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_nin')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionQueryInput')), graphql_name='AND')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    memo_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_in')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    fee_payer_exists = sgqlc.types.Field(Boolean, graphql_name='feePayer_exists')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    to_account_exists = sgqlc.types.Field(Boolean, graphql_name='toAccount_exists')
    kind_lt = sgqlc.types.Field(String, graphql_name='kind_lt')
    fee_lt = sgqlc.types.Field(Float, graphql_name='fee_lt')
    failure_reason_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_in')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    from_account_exists = sgqlc.types.Field(Boolean, graphql_name='fromAccount_exists')
    memo_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_nin')
    kind_lte = sgqlc.types.Field(String, graphql_name='kind_lte')
    fee_lte = sgqlc.types.Field(Float, graphql_name='fee_lte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    kind_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_nin')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    kind_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_in')
    from_exists = sgqlc.types.Field(Boolean, graphql_name='from_exists')
    is_delegation_ne = sgqlc.types.Field(Boolean, graphql_name='isDelegation_ne')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    id_exists = sgqlc.types.Field(Boolean, graphql_name='id_exists')
    fee_token_gt = sgqlc.types.Field(Int, graphql_name='feeToken_gt')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to = sgqlc.types.Field(String, graphql_name='to')
    amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='amount_nin')
    fee_token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_in')
    amount_lt = sgqlc.types.Field(Float, graphql_name='amount_lt')
    memo_ne = sgqlc.types.Field(String, graphql_name='memo_ne')
    failure_reason_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_nin')
    from_ne = sgqlc.types.Field(String, graphql_name='from_ne')
    amount_lte = sgqlc.types.Field(Float, graphql_name='amount_lte')
    memo_gte = sgqlc.types.Field(String, graphql_name='memo_gte')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    amount_gte = sgqlc.types.Field(Float, graphql_name='amount_gte')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    to_ne = sgqlc.types.Field(String, graphql_name='to_ne')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    memo_exists = sgqlc.types.Field(Boolean, graphql_name='memo_exists')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    memo_lte = sgqlc.types.Field(String, graphql_name='memo_lte')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    block_exists = sgqlc.types.Field(Boolean, graphql_name='block_exists')
    fee_token_gte = sgqlc.types.Field(Int, graphql_name='feeToken_gte')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    failure_reason_gt = sgqlc.types.Field(String, graphql_name='failureReason_gt')
    fee_token_lt = sgqlc.types.Field(Int, graphql_name='feeToken_lt')
    amount_gt = sgqlc.types.Field(Float, graphql_name='amount_gt')
    fee_token_exists = sgqlc.types.Field(Boolean, graphql_name='feeToken_exists')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    id = sgqlc.types.Field(String, graphql_name='id')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    kind_gt = sgqlc.types.Field(String, graphql_name='kind_gt')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    failure_reason_lt = sgqlc.types.Field(String, graphql_name='failureReason_lt')
    from_account = sgqlc.types.Field(TransactionFromAccountQueryInput, graphql_name='fromAccount')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    fee_payer = sgqlc.types.Field(TransactionFeePayerQueryInput, graphql_name='feePayer')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    memo_gt = sgqlc.types.Field(String, graphql_name='memo_gt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_in')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    block = sgqlc.types.Field(BlockQueryInput, graphql_name='block')
    from_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_nin')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    fee_token_lte = sgqlc.types.Field(Int, graphql_name='feeToken_lte')
    token = sgqlc.types.Field(Int, graphql_name='token')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_in')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    failure_reason_lte = sgqlc.types.Field(String, graphql_name='failureReason_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionQueryInput')), graphql_name='OR')
    amount_exists = sgqlc.types.Field(Boolean, graphql_name='amount_exists')
    failure_reason_gte = sgqlc.types.Field(String, graphql_name='failureReason_gte')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    receiver_exists = sgqlc.types.Field(Boolean, graphql_name='receiver_exists')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    source_exists = sgqlc.types.Field(Boolean, graphql_name='source_exists')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    fee_token_ne = sgqlc.types.Field(Int, graphql_name='feeToken_ne')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_in')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    amount_ne = sgqlc.types.Field(Float, graphql_name='amount_ne')
    to_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_nin')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    failure_reason_ne = sgqlc.types.Field(String, graphql_name='failureReason_ne')
    fee_gte = sgqlc.types.Field(Float, graphql_name='fee_gte')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    kind_gte = sgqlc.types.Field(String, graphql_name='kind_gte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='amount_in')
    id_ne = sgqlc.types.Field(String, graphql_name='id_ne')
    source = sgqlc.types.Field('TransactionSourceQueryInput', graphql_name='source')
    memo_lt = sgqlc.types.Field(String, graphql_name='memo_lt')
    kind_exists = sgqlc.types.Field(Boolean, graphql_name='kind_exists')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_in')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_nin')
    receiver = sgqlc.types.Field('TransactionReceiverQueryInput', graphql_name='receiver')
    to_account = sgqlc.types.Field('TransactionToAccountQueryInput', graphql_name='toAccount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    fee_ne = sgqlc.types.Field(Float, graphql_name='fee_ne')
    failure_reason_exists = sgqlc.types.Field(Boolean, graphql_name='failureReason_exists')
    kind_ne = sgqlc.types.Field(String, graphql_name='kind_ne')


class TransactionReceiverInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionReceiverQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_exists', 'public_key_gte', 'and_', 'public_key_in', 'public_key_gt', 'public_key_lt', 'public_key_lte', 'public_key_nin', 'public_key_ne', 'or_')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionReceiverQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionReceiverQueryInput')), graphql_name='OR')


class TransactionReceiverUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class TransactionSourceInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionSourceQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('or_', 'public_key_gt', 'public_key_lt', 'and_', 'public_key_in', 'public_key_nin', 'public_key_gte', 'public_key_lte', 'public_key', 'public_key_ne', 'public_key_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionSourceQueryInput')), graphql_name='OR')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionSourceQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')


class TransactionSourceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class TransactionToAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionToAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gt', 'token', 'token_gte', 'token_lte', 'or_', 'token_exists', 'token_ne', 'token_in', 'token_nin', 'and_', 'token_lt')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionToAccountQueryInput')), graphql_name='OR')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionToAccountQueryInput')), graphql_name='AND')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')


class TransactionToAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_inc', 'token_unset', 'token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'canonical', 'date_time', 'block_height', 'from_', 'id_unset', 'block_unset', 'nonce_unset', 'canonical_unset', 'token_inc', 'block', 'to_account', 'amount_inc', 'memo_unset', 'from_unset', 'date_time_unset', 'receiver', 'kind', 'token', 'nonce_inc', 'fee_inc', 'amount_unset', 'is_delegation', 'fee_unset', 'hash_unset', 'memo', 'fee_payer_unset', 'receiver_unset', 'nonce', 'from_account', 'hash', 'block_height_inc', 'failure_reason', 'is_delegation_unset', 'fee_payer', 'fee_token_unset', 'source', 'fee_token', 'failure_reason_unset', 'to', 'kind_unset', 'amount', 'from_account_unset', 'to_account_unset', 'block_height_unset', 'fee_token_inc', 'id', 'fee', 'source_unset', 'to_unset')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    id_unset = sgqlc.types.Field(Boolean, graphql_name='id_unset')
    block_unset = sgqlc.types.Field(Boolean, graphql_name='block_unset')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    block = sgqlc.types.Field(TransactionBlockStateHashRelationInput, graphql_name='block')
    to_account = sgqlc.types.Field(TransactionToAccountUpdateInput, graphql_name='toAccount')
    amount_inc = sgqlc.types.Field(Float, graphql_name='amount_inc')
    memo_unset = sgqlc.types.Field(Boolean, graphql_name='memo_unset')
    from_unset = sgqlc.types.Field(Boolean, graphql_name='from_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    receiver = sgqlc.types.Field(TransactionReceiverUpdateInput, graphql_name='receiver')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    token = sgqlc.types.Field(Int, graphql_name='token')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    fee_inc = sgqlc.types.Field(Float, graphql_name='fee_inc')
    amount_unset = sgqlc.types.Field(Boolean, graphql_name='amount_unset')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    fee_payer_unset = sgqlc.types.Field(Boolean, graphql_name='feePayer_unset')
    receiver_unset = sgqlc.types.Field(Boolean, graphql_name='receiver_unset')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    from_account = sgqlc.types.Field(TransactionFromAccountUpdateInput, graphql_name='fromAccount')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    is_delegation_unset = sgqlc.types.Field(Boolean, graphql_name='isDelegation_unset')
    fee_payer = sgqlc.types.Field(TransactionFeePayerUpdateInput, graphql_name='feePayer')
    fee_token_unset = sgqlc.types.Field(Boolean, graphql_name='feeToken_unset')
    source = sgqlc.types.Field(TransactionSourceUpdateInput, graphql_name='source')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    failure_reason_unset = sgqlc.types.Field(Boolean, graphql_name='failureReason_unset')
    to = sgqlc.types.Field(String, graphql_name='to')
    kind_unset = sgqlc.types.Field(Boolean, graphql_name='kind_unset')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    from_account_unset = sgqlc.types.Field(Boolean, graphql_name='fromAccount_unset')
    to_account_unset = sgqlc.types.Field(Boolean, graphql_name='toAccount_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    fee_token_inc = sgqlc.types.Field(Int, graphql_name='feeToken_inc')
    id = sgqlc.types.Field(String, graphql_name='id')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    source_unset = sgqlc.types.Field(Boolean, graphql_name='source_unset')
    to_unset = sgqlc.types.Field(Boolean, graphql_name='to_unset')



########################################################################
# Output Objects and Interfaces
########################################################################
class Block(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'canonical', 'creator', 'creator_account', 'date_time', 'protocol_state', 'received_time', 'snark_fees', 'snark_jobs', 'state_hash', 'state_hash_field', 'transactions', 'tx_fees', 'winner_account')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    creator_account = sgqlc.types.Field('BlockCreatorAccount', graphql_name='creatorAccount')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    protocol_state = sgqlc.types.Field('BlockProtocolState', graphql_name='protocolState')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    snark_fees = sgqlc.types.Field(Long, graphql_name='snarkFees')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJob'), graphql_name='snarkJobs')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    transactions = sgqlc.types.Field('BlockTransaction', graphql_name='transactions')
    tx_fees = sgqlc.types.Field(Long, graphql_name='txFees')
    winner_account = sgqlc.types.Field('BlockWinnerAccount', graphql_name='winnerAccount')


class BlockCreatorAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockProtocolState(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('blockchain_state', 'consensus_state', 'previous_state_hash')
    blockchain_state = sgqlc.types.Field('BlockProtocolStateBlockchainState', graphql_name='blockchainState')
    consensus_state = sgqlc.types.Field('BlockProtocolStateConsensusState', graphql_name='consensusState')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')


class BlockProtocolStateBlockchainState(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date', 'snarked_ledger_hash', 'staged_ledger_hash', 'utc_date')
    date = sgqlc.types.Field(Long, graphql_name='date')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')


class BlockProtocolStateConsensusState(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'blockchain_length', 'epoch', 'epoch_count', 'has_ancestor_in_same_checkpoint_window', 'last_vrf_output', 'min_window_density', 'next_epoch_data', 'slot', 'slot_since_genesis', 'staking_epoch_data', 'total_currency')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    next_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatum', graphql_name='nextEpochData')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatum', graphql_name='stakingEpochData')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateNextEpochDatum(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length', 'ledger', 'lock_checkpoint', 'seed', 'start_checkpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumLedger', graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')


class BlockProtocolStateConsensusStateNextEpochDatumLedger(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateStakingEpochDatum(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length', 'ledger', 'lock_checkpoint', 'seed', 'start_checkpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumLedger', graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')


class BlockProtocolStateConsensusStateStakingEpochDatumLedger(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockSnarkJob(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'block_state_hash', 'date_time', 'fee', 'prover', 'work_ids')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')


class BlockTransaction(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('coinbase', 'coinbase_receiver_account', 'fee_transfer', 'user_commands')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_receiver_account = sgqlc.types.Field('BlockTransactionCoinbaseReceiverAccount', graphql_name='coinbaseReceiverAccount')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionFeeTransfer'), graphql_name='feeTransfer')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommand'), graphql_name='userCommands')


class BlockTransactionCoinbaseReceiverAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionFeeTransfer(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee', 'recipient', 'type')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    type = sgqlc.types.Field(String, graphql_name='type')


class BlockTransactionUserCommand(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('amount', 'block_height', 'block_state_hash', 'date_time', 'failure_reason', 'fee', 'fee_payer', 'fee_token', 'from_', 'from_account', 'hash', 'id', 'is_delegation', 'kind', 'memo', 'nonce', 'receiver', 'source', 'to', 'to_account', 'token')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    fee_payer = sgqlc.types.Field('BlockTransactionUserCommandFeePayer', graphql_name='feePayer')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_account = sgqlc.types.Field('BlockTransactionUserCommandFromAccount', graphql_name='fromAccount')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    id = sgqlc.types.Field(String, graphql_name='id')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiver', graphql_name='receiver')
    source = sgqlc.types.Field('BlockTransactionUserCommandSource', graphql_name='source')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccount', graphql_name='toAccount')
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandFeePayer(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandFromAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandReceiver(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandSource(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandToAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockWinnerAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'public_key')
    balance = sgqlc.types.Field('BlockWinnerAccountBalance', graphql_name='balance')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockWinnerAccountBalance(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'liquid', 'locked', 'state_hash', 'total', 'unknown')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    total = sgqlc.types.Field(Long, graphql_name='total')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')


class DelegationTotal(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('count_delegates', 'total_delegated')
    count_delegates = sgqlc.types.Field(Int, graphql_name='countDelegates')
    total_delegated = sgqlc.types.Field(Float, graphql_name='totalDelegated')


class DeleteManyPayload(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('deleted_count',)
    deleted_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletedCount')


class InsertManyPayload(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('inserted_ids',)
    inserted_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ObjectId)), graphql_name='insertedIds')


class Mutation(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('delete_many_blocks', 'delete_many_nextstakes', 'delete_many_payouts', 'delete_many_snarks', 'delete_many_stakes', 'delete_many_transactions', 'delete_one_block', 'delete_one_nextstake', 'delete_one_payout', 'delete_one_snark', 'delete_one_stake', 'delete_one_transaction', 'insert_many_blocks', 'insert_many_nextstakes', 'insert_many_payouts', 'insert_many_snarks', 'insert_many_stakes', 'insert_many_transactions', 'insert_one_block', 'insert_one_nextstake', 'insert_one_payout', 'insert_one_snark', 'insert_one_stake', 'insert_one_transaction', 'replace_one_block', 'replace_one_nextstake', 'replace_one_payout', 'replace_one_snark', 'replace_one_stake', 'replace_one_transaction', 'update_many_blocks', 'update_many_nextstakes', 'update_many_payouts', 'update_many_snarks', 'update_many_stakes', 'update_many_transactions', 'update_one_block', 'update_one_nextstake', 'update_one_payout', 'update_one_snark', 'update_one_stake', 'update_one_transaction', 'upsert_one_block', 'upsert_one_nextstake', 'upsert_one_payout', 'upsert_one_snark', 'upsert_one_stake', 'upsert_one_transaction')
    delete_many_blocks = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManyBlocks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
))
    )
    delete_many_nextstakes = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManyNextstakes', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
))
    )
    delete_many_payouts = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManyPayouts', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
))
    )
    delete_many_snarks = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManySnarks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
))
    )
    delete_many_stakes = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManyStakes', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
))
    )
    delete_many_transactions = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManyTransactions', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
))
    )
    delete_one_block = sgqlc.types.Field(Block, graphql_name='deleteOneBlock', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(BlockQueryInput), graphql_name='query', default=None)),
))
    )
    delete_one_nextstake = sgqlc.types.Field('Nextstake', graphql_name='deleteOneNextstake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(NextstakeQueryInput), graphql_name='query', default=None)),
))
    )
    delete_one_payout = sgqlc.types.Field('Payout', graphql_name='deleteOnePayout', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(PayoutQueryInput), graphql_name='query', default=None)),
))
    )
    delete_one_snark = sgqlc.types.Field('Snark', graphql_name='deleteOneSnark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(SnarkQueryInput), graphql_name='query', default=None)),
))
    )
    delete_one_stake = sgqlc.types.Field('Stake', graphql_name='deleteOneStake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(StakeQueryInput), graphql_name='query', default=None)),
))
    )
    delete_one_transaction = sgqlc.types.Field('Transaction', graphql_name='deleteOneTransaction', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(TransactionQueryInput), graphql_name='query', default=None)),
))
    )
    insert_many_blocks = sgqlc.types.Field(InsertManyPayload, graphql_name='insertManyBlocks', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BlockInsertInput))), graphql_name='data', default=None)),
))
    )
    insert_many_nextstakes = sgqlc.types.Field(InsertManyPayload, graphql_name='insertManyNextstakes', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NextstakeInsertInput))), graphql_name='data', default=None)),
))
    )
    insert_many_payouts = sgqlc.types.Field(InsertManyPayload, graphql_name='insertManyPayouts', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PayoutInsertInput))), graphql_name='data', default=None)),
))
    )
    insert_many_snarks = sgqlc.types.Field(InsertManyPayload, graphql_name='insertManySnarks', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SnarkInsertInput))), graphql_name='data', default=None)),
))
    )
    insert_many_stakes = sgqlc.types.Field(InsertManyPayload, graphql_name='insertManyStakes', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StakeInsertInput))), graphql_name='data', default=None)),
))
    )
    insert_many_transactions = sgqlc.types.Field(InsertManyPayload, graphql_name='insertManyTransactions', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TransactionInsertInput))), graphql_name='data', default=None)),
))
    )
    insert_one_block = sgqlc.types.Field(Block, graphql_name='insertOneBlock', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(BlockInsertInput), graphql_name='data', default=None)),
))
    )
    insert_one_nextstake = sgqlc.types.Field('Nextstake', graphql_name='insertOneNextstake', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(NextstakeInsertInput), graphql_name='data', default=None)),
))
    )
    insert_one_payout = sgqlc.types.Field('Payout', graphql_name='insertOnePayout', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(PayoutInsertInput), graphql_name='data', default=None)),
))
    )
    insert_one_snark = sgqlc.types.Field('Snark', graphql_name='insertOneSnark', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(SnarkInsertInput), graphql_name='data', default=None)),
))
    )
    insert_one_stake = sgqlc.types.Field('Stake', graphql_name='insertOneStake', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(StakeInsertInput), graphql_name='data', default=None)),
))
    )
    insert_one_transaction = sgqlc.types.Field('Transaction', graphql_name='insertOneTransaction', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(TransactionInsertInput), graphql_name='data', default=None)),
))
    )
    replace_one_block = sgqlc.types.Field(Block, graphql_name='replaceOneBlock', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(BlockInsertInput), graphql_name='data', default=None)),
))
    )
    replace_one_nextstake = sgqlc.types.Field('Nextstake', graphql_name='replaceOneNextstake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(NextstakeInsertInput), graphql_name='data', default=None)),
))
    )
    replace_one_payout = sgqlc.types.Field('Payout', graphql_name='replaceOnePayout', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(PayoutInsertInput), graphql_name='data', default=None)),
))
    )
    replace_one_snark = sgqlc.types.Field('Snark', graphql_name='replaceOneSnark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(SnarkInsertInput), graphql_name='data', default=None)),
))
    )
    replace_one_stake = sgqlc.types.Field('Stake', graphql_name='replaceOneStake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(StakeInsertInput), graphql_name='data', default=None)),
))
    )
    replace_one_transaction = sgqlc.types.Field('Transaction', graphql_name='replaceOneTransaction', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(TransactionInsertInput), graphql_name='data', default=None)),
))
    )
    update_many_blocks = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManyBlocks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(BlockUpdateInput), graphql_name='set', default=None)),
))
    )
    update_many_nextstakes = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManyNextstakes', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(NextstakeUpdateInput), graphql_name='set', default=None)),
))
    )
    update_many_payouts = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManyPayouts', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(PayoutUpdateInput), graphql_name='set', default=None)),
))
    )
    update_many_snarks = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManySnarks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(SnarkUpdateInput), graphql_name='set', default=None)),
))
    )
    update_many_stakes = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManyStakes', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(StakeUpdateInput), graphql_name='set', default=None)),
))
    )
    update_many_transactions = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManyTransactions', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(TransactionUpdateInput), graphql_name='set', default=None)),
))
    )
    update_one_block = sgqlc.types.Field(Block, graphql_name='updateOneBlock', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(BlockUpdateInput), graphql_name='set', default=None)),
))
    )
    update_one_nextstake = sgqlc.types.Field('Nextstake', graphql_name='updateOneNextstake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(NextstakeUpdateInput), graphql_name='set', default=None)),
))
    )
    update_one_payout = sgqlc.types.Field('Payout', graphql_name='updateOnePayout', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(PayoutUpdateInput), graphql_name='set', default=None)),
))
    )
    update_one_snark = sgqlc.types.Field('Snark', graphql_name='updateOneSnark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(SnarkUpdateInput), graphql_name='set', default=None)),
))
    )
    update_one_stake = sgqlc.types.Field('Stake', graphql_name='updateOneStake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(StakeUpdateInput), graphql_name='set', default=None)),
))
    )
    update_one_transaction = sgqlc.types.Field('Transaction', graphql_name='updateOneTransaction', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(TransactionUpdateInput), graphql_name='set', default=None)),
))
    )
    upsert_one_block = sgqlc.types.Field(Block, graphql_name='upsertOneBlock', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(BlockInsertInput), graphql_name='data', default=None)),
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
))
    )
    upsert_one_nextstake = sgqlc.types.Field('Nextstake', graphql_name='upsertOneNextstake', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(NextstakeInsertInput), graphql_name='data', default=None)),
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
))
    )
    upsert_one_payout = sgqlc.types.Field('Payout', graphql_name='upsertOnePayout', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(PayoutInsertInput), graphql_name='data', default=None)),
))
    )
    upsert_one_snark = sgqlc.types.Field('Snark', graphql_name='upsertOneSnark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(SnarkInsertInput), graphql_name='data', default=None)),
))
    )
    upsert_one_stake = sgqlc.types.Field('Stake', graphql_name='upsertOneStake', args=sgqlc.types.ArgDict((
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(StakeInsertInput), graphql_name='data', default=None)),
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
))
    )
    upsert_one_transaction = sgqlc.types.Field('Transaction', graphql_name='upsertOneTransaction', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(TransactionInsertInput), graphql_name='data', default=None)),
))
    )


class NextDelegationTotal(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('count_delegates', 'total_delegated')
    count_delegates = sgqlc.types.Field(Int, graphql_name='countDelegates')
    total_delegated = sgqlc.types.Field(Float, graphql_name='totalDelegated')


class Nextstake(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'delegate', 'ledger_hash', 'next_delegation_totals', 'nonce', 'permissions', 'pk', 'public_key', 'receipt_chain_hash', 'timing', 'token', 'voting_for')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    next_delegation_totals = sgqlc.types.Field(NextDelegationTotal, graphql_name='nextDelegationTotals')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('NextstakePermission', graphql_name='permissions')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    timing = sgqlc.types.Field('NextstakeTiming', graphql_name='timing')
    token = sgqlc.types.Field(Int, graphql_name='token')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')


class NextstakePermission(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('edit_state', 'send', 'set_delegate', 'set_permissions', 'set_verification_key', 'stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')


class NextstakeTiming(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('cliff_amount', 'cliff_time', 'initial_minimum_balance', 'vesting_increment', 'vesting_period')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')


class Payout(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'coinbase', 'date_time', 'effective_pool_stakes', 'effective_pool_weighting', 'foundation', 'ledger_hash', 'payment_hash', 'payment_id', 'payout', 'public_key', 'staking_balance', 'state_hash', 'sum_effective_pool_stakes', 'super_charged_weighting', 'supercharged_contribution', 'total_pool_stakes', 'total_rewards')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    coinbase = sgqlc.types.Field(Float, graphql_name='coinbase')
    date_time = sgqlc.types.Field(String, graphql_name='dateTime')
    effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='effectivePoolStakes')
    effective_pool_weighting = sgqlc.types.Field(Float, graphql_name='effectivePoolWeighting')
    foundation = sgqlc.types.Field(Boolean, graphql_name='foundation')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    payment_hash = sgqlc.types.Field('Transaction', graphql_name='paymentHash')
    payment_id = sgqlc.types.Field(String, graphql_name='paymentId')
    payout = sgqlc.types.Field(Float, graphql_name='payout')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    staking_balance = sgqlc.types.Field(Float, graphql_name='stakingBalance')
    state_hash = sgqlc.types.Field(Block, graphql_name='stateHash')
    sum_effective_pool_stakes = sgqlc.types.Field(Float, graphql_name='sumEffectivePoolStakes')
    super_charged_weighting = sgqlc.types.Field(Float, graphql_name='superChargedWeighting')
    supercharged_contribution = sgqlc.types.Field(Float, graphql_name='superchargedContribution')
    total_pool_stakes = sgqlc.types.Field(Float, graphql_name='totalPoolStakes')
    total_rewards = sgqlc.types.Field(Float, graphql_name='totalRewards')


class Query(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block', 'blocks', 'nextstake', 'nextstakes', 'payout', 'payouts', 'snark', 'snarks', 'stake', 'stakes', 'transaction', 'transactions')
    block = sgqlc.types.Field(Block, graphql_name='block', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
))
    )
    blocks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Block)), graphql_name='blocks', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(BlockSortByInput, graphql_name='sortBy', default=None)),
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
))
    )
    nextstake = sgqlc.types.Field(Nextstake, graphql_name='nextstake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
))
    )
    nextstakes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Nextstake)), graphql_name='nextstakes', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(NextstakeQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(NextstakeSortByInput, graphql_name='sortBy', default=None)),
))
    )
    payout = sgqlc.types.Field(Payout, graphql_name='payout', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
))
    )
    payouts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Payout)), graphql_name='payouts', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(PayoutQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(PayoutSortByInput, graphql_name='sortBy', default=None)),
))
    )
    snark = sgqlc.types.Field('Snark', graphql_name='snark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
))
    )
    snarks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Snark')), graphql_name='snarks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(SnarkSortByInput, graphql_name='sortBy', default=None)),
))
    )
    stake = sgqlc.types.Field('Stake', graphql_name='stake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
))
    )
    stakes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Stake')), graphql_name='stakes', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(StakeSortByInput, graphql_name='sortBy', default=None)),
))
    )
    transaction = sgqlc.types.Field('Transaction', graphql_name='transaction', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
))
    )
    transactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Transaction')), graphql_name='transactions', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(TransactionSortByInput, graphql_name='sortBy', default=None)),
))
    )


class Snark(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block', 'block_height', 'canonical', 'date_time', 'fee', 'prover', 'work_ids')
    block = sgqlc.types.Field(Block, graphql_name='block')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')


class Stake(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'chain_id', 'delegate', 'delegation_totals', 'epoch', 'ledger_hash', 'nonce', 'permissions', 'pk', 'public_key', 'receipt_chain_hash', 'timing', 'token', 'voting_for')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    delegation_totals = sgqlc.types.Field(DelegationTotal, graphql_name='delegationTotals')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('StakePermission', graphql_name='permissions')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    timing = sgqlc.types.Field('StakeTiming', graphql_name='timing')
    token = sgqlc.types.Field(Int, graphql_name='token')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')


class StakePermission(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('edit_state', 'send', 'set_delegate', 'set_permissions', 'set_verification_key', 'stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')


class StakeTiming(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('cliff_amount', 'cliff_time', 'initial_minimum_balance', 'timed_epoch_end', 'timed_in_epoch', 'timed_weighting', 'untimed_slot', 'vesting_increment', 'vesting_period')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')


class Transaction(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('amount', 'block', 'block_height', 'canonical', 'date_time', 'failure_reason', 'fee', 'fee_payer', 'fee_token', 'from_', 'from_account', 'hash', 'id', 'is_delegation', 'kind', 'memo', 'nonce', 'receiver', 'source', 'to', 'to_account', 'token')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    block = sgqlc.types.Field(Block, graphql_name='block')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    fee_payer = sgqlc.types.Field('TransactionFeePayer', graphql_name='feePayer')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_account = sgqlc.types.Field('TransactionFromAccount', graphql_name='fromAccount')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    id = sgqlc.types.Field(String, graphql_name='id')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    receiver = sgqlc.types.Field('TransactionReceiver', graphql_name='receiver')
    source = sgqlc.types.Field('TransactionSource', graphql_name='source')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_account = sgqlc.types.Field('TransactionToAccount', graphql_name='toAccount')
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionFeePayer(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionFromAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionReceiver(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionSource(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionToAccount(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class UpdateManyPayload(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('matched_count', 'modified_count')
    matched_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchedCount')
    modified_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='modifiedCount')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
mina_explorer_schema.query_type = Query
mina_explorer_schema.mutation_type = Mutation
mina_explorer_schema.subscription_type = None

