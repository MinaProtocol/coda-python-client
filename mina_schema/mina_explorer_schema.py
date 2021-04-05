import sgqlc.types
import sgqlc.types.datetime


mina_explorer_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BlockSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('CREATOR_ASC', 'CREATOR_DESC', 'STATEHASH_ASC', 'STATEHASH_DESC', 'STATEHASHFIELD_ASC', 'STATEHASHFIELD_DESC', 'BLOCKHEIGHT_DESC', 'DATETIME_ASC', 'DATETIME_DESC', 'RECEIVEDTIME_ASC', 'RECEIVEDTIME_DESC', 'BLOCKHEIGHT_ASC')


Boolean = sgqlc.types.Boolean

DateTime = sgqlc.types.datetime.DateTime

Float = sgqlc.types.Float

Int = sgqlc.types.Int

class Long(sgqlc.types.Scalar):
    __schema__ = mina_explorer_schema


class ObjectId(sgqlc.types.Scalar):
    __schema__ = mina_explorer_schema


class SnarkSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('FEE_DESC', 'PROVER_ASC', 'PROVER_DESC', 'BLOCKHEIGHT_ASC', 'BLOCKHEIGHT_DESC', 'BLOCKSTATEHASH_ASC', 'DATETIME_ASC', 'DATETIME_DESC', 'FEE_ASC', 'BLOCKSTATEHASH_DESC')


class StakeSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('CHAINID_ASC', 'EPOCH_ASC', 'EPOCH_DESC', 'BALANCE_ASC', 'NONCE_ASC', 'PUBLIC_KEY_DESC', 'VOTING_FOR_ASC', 'TOKEN_DESC', 'DELEGATE_ASC', 'DELEGATE_DESC', 'NONCE_DESC', 'PUBLIC_KEY_ASC', 'RECEIPT_CHAIN_HASH_DESC', 'LEDGERHASH_ASC', 'CHAINID_DESC', 'RECEIPT_CHAIN_HASH_ASC', 'VOTING_FOR_DESC', 'LEDGERHASH_DESC', 'TOKEN_ASC', 'BALANCE_DESC')


String = sgqlc.types.String

class TransactionSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('HASH_ASC', 'FEE_ASC', 'BLOCKSTATEHASH_DESC', 'TO_ASC', 'TOKEN_ASC', 'AMOUNT_ASC', 'NONCE_DESC', 'FEE_DESC', 'DATETIME_ASC', 'FAILUREREASON_ASC', 'TOKEN_DESC', 'ID_ASC', 'ID_DESC', 'DATETIME_DESC', 'TO_DESC', 'BLOCKSTATEHASH_ASC', 'AMOUNT_DESC', 'KIND_ASC', 'KIND_DESC', 'HASH_DESC', 'FAILUREREASON_DESC', 'FROM_ASC', 'FROM_DESC', 'MEMO_DESC', 'BLOCKHEIGHT_ASC', 'NONCE_ASC', 'MEMO_ASC', 'BLOCKHEIGHT_DESC', 'FEETOKEN_ASC', 'FEETOKEN_DESC')



########################################################################
# Input Objects
########################################################################
class BlockCreatorAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockCreatorAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('and_', 'public_key', 'public_key_ne', 'public_key_gt', 'public_key_nin', 'public_key_exists', 'public_key_in', 'public_key_gte', 'public_key_lt', 'public_key_lte', 'or_')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockCreatorAccountQueryInput')), graphql_name='AND')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockCreatorAccountQueryInput')), graphql_name='OR')


class BlockCreatorAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class BlockInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('protocol_state', 'date_time', 'winner_account', 'state_hash', 'block_height', 'transactions', 'creator', 'snark_jobs', 'received_time', 'state_hash_field', 'creator_account', 'canonical')
    protocol_state = sgqlc.types.Field('BlockProtocolStateInsertInput', graphql_name='protocolState')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    winner_account = sgqlc.types.Field('BlockWinnerAccountInsertInput', graphql_name='winnerAccount')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    transactions = sgqlc.types.Field('BlockTransactionInsertInput', graphql_name='transactions')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobInsertInput'), graphql_name='snarkJobs')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    creator_account = sgqlc.types.Field(BlockCreatorAccountInsertInput, graphql_name='creatorAccount')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')


class BlockProtocolStateBlockchainStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date', 'snarked_ledger_hash', 'staged_ledger_hash', 'utc_date')
    date = sgqlc.types.Field(Long, graphql_name='date')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')


class BlockProtocolStateBlockchainStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('staged_ledger_hash_lte', 'and_', 'date_gt', 'snarked_ledger_hash_exists', 'date_in', 'staged_ledger_hash_ne', 'date_ne', 'staged_ledger_hash_in', 'snarked_ledger_hash_lt', 'utc_date_ne', 'staged_ledger_hash_gte', 'staged_ledger_hash', 'snarked_ledger_hash_nin', 'snarked_ledger_hash_ne', 'snarked_ledger_hash_gt', 'date_lte', 'staged_ledger_hash_lt', 'snarked_ledger_hash', 'utc_date_gt', 'utc_date_exists', 'date_lt', 'utc_date_lt', 'staged_ledger_hash_nin', 'date_gte', 'staged_ledger_hash_gt', 'date_exists', 'utc_date_nin', 'utc_date_gte', 'utc_date_lte', 'staged_ledger_hash_exists', 'date', 'snarked_ledger_hash_lte', 'date_nin', 'or_', 'utc_date_in', 'utc_date', 'snarked_ledger_hash_gte', 'snarked_ledger_hash_in')
    staged_ledger_hash_lte = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateBlockchainStateQueryInput')), graphql_name='AND')
    date_gt = sgqlc.types.Field(Long, graphql_name='date_gt')
    snarked_ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='snarkedLedgerHash_exists')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='date_in')
    staged_ledger_hash_ne = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_ne')
    date_ne = sgqlc.types.Field(Long, graphql_name='date_ne')
    staged_ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagedLedgerHash_in')
    snarked_ledger_hash_lt = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_lt')
    utc_date_ne = sgqlc.types.Field(Long, graphql_name='utcDate_ne')
    staged_ledger_hash_gte = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_gte')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    snarked_ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snarkedLedgerHash_nin')
    snarked_ledger_hash_ne = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_ne')
    snarked_ledger_hash_gt = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_gt')
    date_lte = sgqlc.types.Field(Long, graphql_name='date_lte')
    staged_ledger_hash_lt = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_lt')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    utc_date_gt = sgqlc.types.Field(Long, graphql_name='utcDate_gt')
    utc_date_exists = sgqlc.types.Field(Boolean, graphql_name='utcDate_exists')
    date_lt = sgqlc.types.Field(Long, graphql_name='date_lt')
    utc_date_lt = sgqlc.types.Field(Long, graphql_name='utcDate_lt')
    staged_ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagedLedgerHash_nin')
    date_gte = sgqlc.types.Field(Long, graphql_name='date_gte')
    staged_ledger_hash_gt = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_gt')
    date_exists = sgqlc.types.Field(Boolean, graphql_name='date_exists')
    utc_date_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='utcDate_nin')
    utc_date_gte = sgqlc.types.Field(Long, graphql_name='utcDate_gte')
    utc_date_lte = sgqlc.types.Field(Long, graphql_name='utcDate_lte')
    staged_ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stagedLedgerHash_exists')
    date = sgqlc.types.Field(Long, graphql_name='date')
    snarked_ledger_hash_lte = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_lte')
    date_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='date_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateBlockchainStateQueryInput')), graphql_name='OR')
    utc_date_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='utcDate_in')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')
    snarked_ledger_hash_gte = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_gte')
    snarked_ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snarkedLedgerHash_in')


class BlockProtocolStateBlockchainStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_unset', 'snarked_ledger_hash', 'snarked_ledger_hash_unset', 'staged_ledger_hash', 'staged_ledger_hash_unset', 'utc_date', 'utc_date_unset', 'date')
    date_unset = sgqlc.types.Field(Boolean, graphql_name='date_unset')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    snarked_ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='snarkedLedgerHash_unset')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    staged_ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stagedLedgerHash_unset')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')
    utc_date_unset = sgqlc.types.Field(Boolean, graphql_name='utcDate_unset')
    date = sgqlc.types.Field(Long, graphql_name='date')


class BlockProtocolStateConsensusStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('staking_epoch_data', 'total_currency', 'blockchain_length', 'min_window_density', 'epoch_count', 'slot', 'slot_since_genesis', 'epoch', 'next_epoch_data', 'has_ancestor_in_same_checkpoint_window', 'last_vrf_output', 'block_height')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumInsertInput', graphql_name='stakingEpochData')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    next_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumInsertInput', graphql_name='nextEpochData')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')


class BlockProtocolStateConsensusStateNextEpochDatumInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length', 'ledger', 'lock_checkpoint', 'seed', 'start_checkpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumLedgerInsertInput', graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency', 'hash')
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')
    hash = sgqlc.types.Field(String, graphql_name='hash')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency_exists', 'total_currency_gt', 'total_currency', 'hash_lte', 'hash_nin', 'hash_ne', 'hash_exists', 'total_currency_ne', 'total_currency_in', 'or_', 'total_currency_lt', 'hash_gt', 'hash_in', 'hash', 'hash_gte', 'total_currency_lte', 'total_currency_nin', 'and_', 'hash_lt', 'total_currency_gte')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    total_currency_gt = sgqlc.types.Field(Long, graphql_name='totalCurrency_gt')
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    total_currency_ne = sgqlc.types.Field(Long, graphql_name='totalCurrency_ne')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='totalCurrency_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput')), graphql_name='OR')
    total_currency_lt = sgqlc.types.Field(Long, graphql_name='totalCurrency_lt')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    total_currency_lte = sgqlc.types.Field(Long, graphql_name='totalCurrency_lte')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='totalCurrency_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput')), graphql_name='AND')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    total_currency_gte = sgqlc.types.Field(Long, graphql_name='totalCurrency_gte')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash_unset', 'total_currency', 'total_currency_unset', 'hash')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')


class BlockProtocolStateConsensusStateNextEpochDatumQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('seed_lt', 'start_checkpoint_lt', 'or_', 'lock_checkpoint', 'epoch_length_gte', 'start_checkpoint_exists', 'lock_checkpoint_lt', 'start_checkpoint', 'seed_in', 'lock_checkpoint_gt', 'seed_gt', 'lock_checkpoint_gte', 'seed_ne', 'start_checkpoint_in', 'start_checkpoint_gt', 'seed_lte', 'start_checkpoint_gte', 'lock_checkpoint_in', 'ledger_exists', 'and_', 'seed', 'epoch_length_ne', 'start_checkpoint_ne', 'epoch_length_exists', 'epoch_length_nin', 'seed_gte', 'start_checkpoint_lte', 'seed_exists', 'ledger', 'start_checkpoint_nin', 'epoch_length_in', 'lock_checkpoint_exists', 'epoch_length_lt', 'lock_checkpoint_ne', 'epoch_length_gt', 'lock_checkpoint_lte', 'seed_nin', 'epoch_length', 'epoch_length_lte', 'lock_checkpoint_nin')
    seed_lt = sgqlc.types.Field(String, graphql_name='seed_lt')
    start_checkpoint_lt = sgqlc.types.Field(String, graphql_name='startCheckpoint_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumQueryInput')), graphql_name='OR')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    epoch_length_gte = sgqlc.types.Field(Int, graphql_name='epochLength_gte')
    start_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_exists')
    lock_checkpoint_lt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lt')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    seed_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_in')
    lock_checkpoint_gt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gt')
    seed_gt = sgqlc.types.Field(String, graphql_name='seed_gt')
    lock_checkpoint_gte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gte')
    seed_ne = sgqlc.types.Field(String, graphql_name='seed_ne')
    start_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_in')
    start_checkpoint_gt = sgqlc.types.Field(String, graphql_name='startCheckpoint_gt')
    seed_lte = sgqlc.types.Field(String, graphql_name='seed_lte')
    start_checkpoint_gte = sgqlc.types.Field(String, graphql_name='startCheckpoint_gte')
    lock_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_in')
    ledger_exists = sgqlc.types.Field(Boolean, graphql_name='ledger_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumQueryInput')), graphql_name='AND')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    epoch_length_ne = sgqlc.types.Field(Int, graphql_name='epochLength_ne')
    start_checkpoint_ne = sgqlc.types.Field(String, graphql_name='startCheckpoint_ne')
    epoch_length_exists = sgqlc.types.Field(Boolean, graphql_name='epochLength_exists')
    epoch_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_nin')
    seed_gte = sgqlc.types.Field(String, graphql_name='seed_gte')
    start_checkpoint_lte = sgqlc.types.Field(String, graphql_name='startCheckpoint_lte')
    seed_exists = sgqlc.types.Field(Boolean, graphql_name='seed_exists')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput, graphql_name='ledger')
    start_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_nin')
    epoch_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_in')
    lock_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_exists')
    epoch_length_lt = sgqlc.types.Field(Int, graphql_name='epochLength_lt')
    lock_checkpoint_ne = sgqlc.types.Field(String, graphql_name='lockCheckpoint_ne')
    epoch_length_gt = sgqlc.types.Field(Int, graphql_name='epochLength_gt')
    lock_checkpoint_lte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lte')
    seed_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_nin')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    epoch_length_lte = sgqlc.types.Field(Int, graphql_name='epochLength_lte')
    lock_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_nin')


class BlockProtocolStateConsensusStateNextEpochDatumUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length_unset', 'seed', 'start_checkpoint_unset', 'start_checkpoint', 'epoch_length', 'ledger_unset', 'lock_checkpoint_unset', 'epoch_length_inc', 'ledger', 'seed_unset', 'lock_checkpoint')
    epoch_length_unset = sgqlc.types.Field(Boolean, graphql_name='epochLength_unset')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_unset')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger_unset = sgqlc.types.Field(Boolean, graphql_name='ledger_unset')
    lock_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_unset')
    epoch_length_inc = sgqlc.types.Field(Int, graphql_name='epochLength_inc')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumLedgerUpdateInput, graphql_name='ledger')
    seed_unset = sgqlc.types.Field(Boolean, graphql_name='seed_unset')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')


class BlockProtocolStateConsensusStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('slot_gt', 'total_currency_gt', 'slot_since_genesis_lte', 'blockchain_length_nin', 'epoch_count_ne', 'last_vrf_output_exists', 'last_vrf_output', 'epoch_count_exists', 'min_window_density_gt', 'min_window_density_ne', 'blockchain_length_gt', 'slot_in', 'blockchain_length_lte', 'block_height_lt', 'total_currency_exists', 'min_window_density_lte', 'blockchain_length_ne', 'epoch_count_gte', 'slot_exists', 'min_window_density_lt', 'slot_since_genesis_gte', 'epoch_in', 'last_vrf_output_nin', 'slot_since_genesis_in', 'epoch_lte', 'blockchain_length_in', 'epoch_ne', 'blockchain_length_gte', 'staking_epoch_data_exists', 'epoch_count_lt', 'slot', 'epoch_nin', 'min_window_density_nin', 'last_vrf_output_in', 'epoch_gt', 'total_currency_lte', 'epoch_count_lte', 'or_', 'total_currency_in', 'slot_since_genesis_lt', 'has_ancestor_in_same_checkpoint_window_exists', 'epoch_count_in', 'total_currency', 'slot_lte', 'total_currency_gte', 'epoch_lt', 'last_vrf_output_lte', 'epoch_count', 'block_height', 'epoch_gte', 'blockchain_length', 'epoch_count_nin', 'has_ancestor_in_same_checkpoint_window_ne', 'block_height_in', 'slot_since_genesis_exists', 'slot_lt', 'slot_since_genesis_ne', 'epoch_count_gt', 'last_vrf_output_lt', 'min_window_density', 'total_currency_ne', 'block_height_nin', 'slot_gte', 'slot_nin', 'slot_since_genesis', 'min_window_density_gte', 'total_currency_nin', 'block_height_gt', 'has_ancestor_in_same_checkpoint_window', 'slot_ne', 'and_', 'slot_since_genesis_gt', 'last_vrf_output_gt', 'next_epoch_data', 'total_currency_lt', 'last_vrf_output_ne', 'min_window_density_in', 'block_height_ne', 'block_height_gte', 'block_height_lte', 'block_height_exists', 'slot_since_genesis_nin', 'staking_epoch_data', 'min_window_density_exists', 'blockchain_length_exists', 'last_vrf_output_gte', 'next_epoch_data_exists', 'epoch', 'blockchain_length_lt', 'epoch_exists')
    slot_gt = sgqlc.types.Field(Int, graphql_name='slot_gt')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')
    slot_since_genesis_lte = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_lte')
    blockchain_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockchainLength_nin')
    epoch_count_ne = sgqlc.types.Field(Int, graphql_name='epochCount_ne')
    last_vrf_output_exists = sgqlc.types.Field(Boolean, graphql_name='lastVrfOutput_exists')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    epoch_count_exists = sgqlc.types.Field(Boolean, graphql_name='epochCount_exists')
    min_window_density_gt = sgqlc.types.Field(Int, graphql_name='minWindowDensity_gt')
    min_window_density_ne = sgqlc.types.Field(Int, graphql_name='minWindowDensity_ne')
    blockchain_length_gt = sgqlc.types.Field(Int, graphql_name='blockchainLength_gt')
    slot_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slot_in')
    blockchain_length_lte = sgqlc.types.Field(Int, graphql_name='blockchainLength_lte')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    min_window_density_lte = sgqlc.types.Field(Int, graphql_name='minWindowDensity_lte')
    blockchain_length_ne = sgqlc.types.Field(Int, graphql_name='blockchainLength_ne')
    epoch_count_gte = sgqlc.types.Field(Int, graphql_name='epochCount_gte')
    slot_exists = sgqlc.types.Field(Boolean, graphql_name='slot_exists')
    min_window_density_lt = sgqlc.types.Field(Int, graphql_name='minWindowDensity_lt')
    slot_since_genesis_gte = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_gte')
    epoch_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_in')
    last_vrf_output_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastVrfOutput_nin')
    slot_since_genesis_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slotSinceGenesis_in')
    epoch_lte = sgqlc.types.Field(Int, graphql_name='epoch_lte')
    blockchain_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockchainLength_in')
    epoch_ne = sgqlc.types.Field(Int, graphql_name='epoch_ne')
    blockchain_length_gte = sgqlc.types.Field(Int, graphql_name='blockchainLength_gte')
    staking_epoch_data_exists = sgqlc.types.Field(Boolean, graphql_name='stakingEpochData_exists')
    epoch_count_lt = sgqlc.types.Field(Int, graphql_name='epochCount_lt')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    epoch_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_nin')
    min_window_density_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minWindowDensity_nin')
    last_vrf_output_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastVrfOutput_in')
    epoch_gt = sgqlc.types.Field(Int, graphql_name='epoch_gt')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    epoch_count_lte = sgqlc.types.Field(Int, graphql_name='epochCount_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateQueryInput')), graphql_name='OR')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    slot_since_genesis_lt = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_lt')
    has_ancestor_in_same_checkpoint_window_exists = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_exists')
    epoch_count_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochCount_in')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    slot_lte = sgqlc.types.Field(Int, graphql_name='slot_lte')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    epoch_lt = sgqlc.types.Field(Int, graphql_name='epoch_lt')
    last_vrf_output_lte = sgqlc.types.Field(String, graphql_name='lastVrfOutput_lte')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    epoch_gte = sgqlc.types.Field(Int, graphql_name='epoch_gte')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    epoch_count_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochCount_nin')
    has_ancestor_in_same_checkpoint_window_ne = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_ne')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    slot_since_genesis_exists = sgqlc.types.Field(Boolean, graphql_name='slotSinceGenesis_exists')
    slot_lt = sgqlc.types.Field(Int, graphql_name='slot_lt')
    slot_since_genesis_ne = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_ne')
    epoch_count_gt = sgqlc.types.Field(Int, graphql_name='epochCount_gt')
    last_vrf_output_lt = sgqlc.types.Field(String, graphql_name='lastVrfOutput_lt')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    slot_gte = sgqlc.types.Field(Int, graphql_name='slot_gte')
    slot_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slot_nin')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    min_window_density_gte = sgqlc.types.Field(Int, graphql_name='minWindowDensity_gte')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    slot_ne = sgqlc.types.Field(Int, graphql_name='slot_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateQueryInput')), graphql_name='AND')
    slot_since_genesis_gt = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_gt')
    last_vrf_output_gt = sgqlc.types.Field(String, graphql_name='lastVrfOutput_gt')
    next_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumQueryInput, graphql_name='nextEpochData')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    last_vrf_output_ne = sgqlc.types.Field(String, graphql_name='lastVrfOutput_ne')
    min_window_density_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minWindowDensity_in')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    slot_since_genesis_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slotSinceGenesis_nin')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput', graphql_name='stakingEpochData')
    min_window_density_exists = sgqlc.types.Field(Boolean, graphql_name='minWindowDensity_exists')
    blockchain_length_exists = sgqlc.types.Field(Boolean, graphql_name='blockchainLength_exists')
    last_vrf_output_gte = sgqlc.types.Field(String, graphql_name='lastVrfOutput_gte')
    next_epoch_data_exists = sgqlc.types.Field(Boolean, graphql_name='nextEpochData_exists')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    blockchain_length_lt = sgqlc.types.Field(Int, graphql_name='blockchainLength_lt')
    epoch_exists = sgqlc.types.Field(Boolean, graphql_name='epoch_exists')


class BlockProtocolStateConsensusStateStakingEpochDatumInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('lock_checkpoint', 'seed', 'start_checkpoint', 'epoch_length', 'ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumLedgerInsertInput', graphql_name='ledger')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency_gte', 'hash_exists', 'and_', 'hash_ne', 'or_', 'hash_nin', 'total_currency', 'total_currency_nin', 'hash_gte', 'total_currency_lt', 'total_currency_lte', 'total_currency_in', 'hash_lt', 'hash_in', 'total_currency_ne', 'hash_lte', 'total_currency_gt', 'total_currency_exists', 'hash_gt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput')), graphql_name='AND')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput')), graphql_name='OR')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash_unset', 'total_currency', 'total_currency_inc', 'total_currency_unset', 'hash')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')


class BlockProtocolStateConsensusStateStakingEpochDatumQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length_lte', 'and_', 'start_checkpoint', 'seed_exists', 'seed_lte', 'lock_checkpoint_nin', 'lock_checkpoint_lte', 'epoch_length_nin', 'epoch_length', 'or_', 'ledger', 'lock_checkpoint', 'start_checkpoint_gte', 'start_checkpoint_in', 'start_checkpoint_gt', 'lock_checkpoint_ne', 'seed_nin', 'epoch_length_lt', 'seed', 'epoch_length_in', 'lock_checkpoint_lt', 'start_checkpoint_nin', 'lock_checkpoint_in', 'epoch_length_gte', 'lock_checkpoint_gte', 'epoch_length_exists', 'start_checkpoint_lt', 'epoch_length_ne', 'ledger_exists', 'seed_lt', 'start_checkpoint_lte', 'lock_checkpoint_exists', 'seed_gte', 'lock_checkpoint_gt', 'seed_gt', 'epoch_length_gt', 'start_checkpoint_ne', 'seed_in', 'seed_ne', 'start_checkpoint_exists')
    epoch_length_lte = sgqlc.types.Field(Int, graphql_name='epochLength_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput')), graphql_name='AND')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    seed_exists = sgqlc.types.Field(Boolean, graphql_name='seed_exists')
    seed_lte = sgqlc.types.Field(String, graphql_name='seed_lte')
    lock_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_nin')
    lock_checkpoint_lte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lte')
    epoch_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_nin')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput')), graphql_name='OR')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput, graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    start_checkpoint_gte = sgqlc.types.Field(String, graphql_name='startCheckpoint_gte')
    start_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_in')
    start_checkpoint_gt = sgqlc.types.Field(String, graphql_name='startCheckpoint_gt')
    lock_checkpoint_ne = sgqlc.types.Field(String, graphql_name='lockCheckpoint_ne')
    seed_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_nin')
    epoch_length_lt = sgqlc.types.Field(Int, graphql_name='epochLength_lt')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    epoch_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_in')
    lock_checkpoint_lt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lt')
    start_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_nin')
    lock_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_in')
    epoch_length_gte = sgqlc.types.Field(Int, graphql_name='epochLength_gte')
    lock_checkpoint_gte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gte')
    epoch_length_exists = sgqlc.types.Field(Boolean, graphql_name='epochLength_exists')
    start_checkpoint_lt = sgqlc.types.Field(String, graphql_name='startCheckpoint_lt')
    epoch_length_ne = sgqlc.types.Field(Int, graphql_name='epochLength_ne')
    ledger_exists = sgqlc.types.Field(Boolean, graphql_name='ledger_exists')
    seed_lt = sgqlc.types.Field(String, graphql_name='seed_lt')
    start_checkpoint_lte = sgqlc.types.Field(String, graphql_name='startCheckpoint_lte')
    lock_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_exists')
    seed_gte = sgqlc.types.Field(String, graphql_name='seed_gte')
    lock_checkpoint_gt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gt')
    seed_gt = sgqlc.types.Field(String, graphql_name='seed_gt')
    epoch_length_gt = sgqlc.types.Field(Int, graphql_name='epochLength_gt')
    start_checkpoint_ne = sgqlc.types.Field(String, graphql_name='startCheckpoint_ne')
    seed_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_in')
    seed_ne = sgqlc.types.Field(String, graphql_name='seed_ne')
    start_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_exists')


class BlockProtocolStateConsensusStateStakingEpochDatumUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length', 'epoch_length_unset', 'lock_checkpoint_unset', 'seed', 'ledger', 'lock_checkpoint', 'seed_unset', 'start_checkpoint', 'ledger_unset', 'start_checkpoint_unset', 'epoch_length_inc')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    epoch_length_unset = sgqlc.types.Field(Boolean, graphql_name='epochLength_unset')
    lock_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_unset')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumLedgerUpdateInput, graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed_unset = sgqlc.types.Field(Boolean, graphql_name='seed_unset')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    ledger_unset = sgqlc.types.Field(Boolean, graphql_name='ledger_unset')
    start_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_unset')
    epoch_length_inc = sgqlc.types.Field(Int, graphql_name='epochLength_inc')


class BlockProtocolStateConsensusStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('has_ancestor_in_same_checkpoint_window_unset', 'last_vrf_output', 'next_epoch_data', 'slot_unset', 'block_height', 'slot_inc', 'next_epoch_data_unset', 'last_vrf_output_unset', 'epoch_count_unset', 'block_height_unset', 'blockchain_length', 'min_window_density', 'epoch_count_inc', 'epoch', 'slot_since_genesis_unset', 'staking_epoch_data_unset', 'epoch_count', 'total_currency_unset', 'slot', 'min_window_density_inc', 'total_currency_inc', 'blockchain_length_unset', 'min_window_density_unset', 'total_currency', 'epoch_unset', 'has_ancestor_in_same_checkpoint_window', 'block_height_inc', 'epoch_inc', 'slot_since_genesis', 'staking_epoch_data', 'slot_since_genesis_inc', 'blockchain_length_inc')
    has_ancestor_in_same_checkpoint_window_unset = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_unset')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    next_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumUpdateInput, graphql_name='nextEpochData')
    slot_unset = sgqlc.types.Field(Boolean, graphql_name='slot_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    slot_inc = sgqlc.types.Field(Int, graphql_name='slot_inc')
    next_epoch_data_unset = sgqlc.types.Field(Boolean, graphql_name='nextEpochData_unset')
    last_vrf_output_unset = sgqlc.types.Field(Boolean, graphql_name='lastVrfOutput_unset')
    epoch_count_unset = sgqlc.types.Field(Boolean, graphql_name='epochCount_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    epoch_count_inc = sgqlc.types.Field(Int, graphql_name='epochCount_inc')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    slot_since_genesis_unset = sgqlc.types.Field(Boolean, graphql_name='slotSinceGenesis_unset')
    staking_epoch_data_unset = sgqlc.types.Field(Boolean, graphql_name='stakingEpochData_unset')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    min_window_density_inc = sgqlc.types.Field(Int, graphql_name='minWindowDensity_inc')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')
    blockchain_length_unset = sgqlc.types.Field(Boolean, graphql_name='blockchainLength_unset')
    min_window_density_unset = sgqlc.types.Field(Boolean, graphql_name='minWindowDensity_unset')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    epoch_unset = sgqlc.types.Field(Boolean, graphql_name='epoch_unset')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    epoch_inc = sgqlc.types.Field(Int, graphql_name='epoch_inc')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    staking_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumUpdateInput, graphql_name='stakingEpochData')
    slot_since_genesis_inc = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_inc')
    blockchain_length_inc = sgqlc.types.Field(Int, graphql_name='blockchainLength_inc')


class BlockProtocolStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('blockchain_state', 'consensus_state', 'previous_state_hash')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateInsertInput, graphql_name='blockchainState')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateInsertInput, graphql_name='consensusState')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')


class BlockProtocolStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('blockchain_state', 'previous_state_hash_gt', 'consensus_state_exists', 'previous_state_hash_lte', 'previous_state_hash_in', 'previous_state_hash_nin', 'blockchain_state_exists', 'consensus_state', 'previous_state_hash_ne', 'or_', 'and_', 'previous_state_hash_exists', 'previous_state_hash_gte', 'previous_state_hash_lt', 'previous_state_hash')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateQueryInput, graphql_name='blockchainState')
    previous_state_hash_gt = sgqlc.types.Field(String, graphql_name='previousStateHash_gt')
    consensus_state_exists = sgqlc.types.Field(Boolean, graphql_name='consensusState_exists')
    previous_state_hash_lte = sgqlc.types.Field(String, graphql_name='previousStateHash_lte')
    previous_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='previousStateHash_in')
    previous_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='previousStateHash_nin')
    blockchain_state_exists = sgqlc.types.Field(Boolean, graphql_name='blockchainState_exists')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateQueryInput, graphql_name='consensusState')
    previous_state_hash_ne = sgqlc.types.Field(String, graphql_name='previousStateHash_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateQueryInput')), graphql_name='OR')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateQueryInput')), graphql_name='AND')
    previous_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='previousStateHash_exists')
    previous_state_hash_gte = sgqlc.types.Field(String, graphql_name='previousStateHash_gte')
    previous_state_hash_lt = sgqlc.types.Field(String, graphql_name='previousStateHash_lt')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')


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
    __field_names__ = ('block_height_lte', 'state_hash_field_exists', 'received_time_in', 'date_time_lt', 'state_hash_field_nin', 'snark_jobs_nin', 'canonical_exists', 'protocol_state', 'winner_account_exists', 'creator_ne', 'received_time', 'state_hash', 'protocol_state_exists', 'state_hash_nin', 'block_height_gte', 'state_hash_ne', 'received_time_exists', 'date_time_gte', 'block_height_ne', 'creator_in', 'received_time_gt', 'canonical_ne', 'state_hash_field_ne', 'creator_gt', 'date_time_ne', 'state_hash_exists', 'block_height', 'date_time_nin', 'or_', 'state_hash_field_lt', 'transactions_exists', 'canonical', 'creator_gte', 'received_time_nin', 'block_height_exists', 'received_time_gte', 'creator', 'state_hash_in', 'creator_lt', 'creator_exists', 'snark_jobs', 'date_time_lte', 'state_hash_gt', 'state_hash_gte', 'block_height_in', 'date_time_gt', 'winner_account', 'state_hash_lt', 'state_hash_field_lte', 'state_hash_field_gt', 'state_hash_field_in', 'block_height_lt', 'transactions', 'block_height_nin', 'state_hash_lte', 'creator_nin', 'state_hash_field', 'state_hash_field_gte', 'and_', 'received_time_lte', 'block_height_gt', 'snark_jobs_in', 'snark_jobs_exists', 'received_time_lt', 'date_time', 'date_time_exists', 'creator_account', 'date_time_in', 'received_time_ne', 'creator_lte', 'creator_account_exists')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    state_hash_field_exists = sgqlc.types.Field(Boolean, graphql_name='stateHashField_exists')
    received_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='receivedTime_in')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    state_hash_field_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHashField_nin')
    snark_jobs_nin = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs_nin')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    protocol_state = sgqlc.types.Field(BlockProtocolStateQueryInput, graphql_name='protocolState')
    winner_account_exists = sgqlc.types.Field(Boolean, graphql_name='winnerAccount_exists')
    creator_ne = sgqlc.types.Field(String, graphql_name='creator_ne')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    protocol_state_exists = sgqlc.types.Field(Boolean, graphql_name='protocolState_exists')
    state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_nin')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    state_hash_ne = sgqlc.types.Field(String, graphql_name='stateHash_ne')
    received_time_exists = sgqlc.types.Field(Boolean, graphql_name='receivedTime_exists')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    creator_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='creator_in')
    received_time_gt = sgqlc.types.Field(DateTime, graphql_name='receivedTime_gt')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    state_hash_field_ne = sgqlc.types.Field(String, graphql_name='stateHashField_ne')
    creator_gt = sgqlc.types.Field(String, graphql_name='creator_gt')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockQueryInput')), graphql_name='OR')
    state_hash_field_lt = sgqlc.types.Field(String, graphql_name='stateHashField_lt')
    transactions_exists = sgqlc.types.Field(Boolean, graphql_name='transactions_exists')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    creator_gte = sgqlc.types.Field(String, graphql_name='creator_gte')
    received_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='receivedTime_nin')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    received_time_gte = sgqlc.types.Field(DateTime, graphql_name='receivedTime_gte')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_in')
    creator_lt = sgqlc.types.Field(String, graphql_name='creator_lt')
    creator_exists = sgqlc.types.Field(Boolean, graphql_name='creator_exists')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    state_hash_gt = sgqlc.types.Field(String, graphql_name='stateHash_gt')
    state_hash_gte = sgqlc.types.Field(String, graphql_name='stateHash_gte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    winner_account = sgqlc.types.Field('BlockWinnerAccountQueryInput', graphql_name='winnerAccount')
    state_hash_lt = sgqlc.types.Field(String, graphql_name='stateHash_lt')
    state_hash_field_lte = sgqlc.types.Field(String, graphql_name='stateHashField_lte')
    state_hash_field_gt = sgqlc.types.Field(String, graphql_name='stateHashField_gt')
    state_hash_field_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHashField_in')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    transactions = sgqlc.types.Field('BlockTransactionQueryInput', graphql_name='transactions')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    state_hash_lte = sgqlc.types.Field(String, graphql_name='stateHash_lte')
    creator_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='creator_nin')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    state_hash_field_gte = sgqlc.types.Field(String, graphql_name='stateHashField_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockQueryInput')), graphql_name='AND')
    received_time_lte = sgqlc.types.Field(DateTime, graphql_name='receivedTime_lte')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    snark_jobs_in = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs_in')
    snark_jobs_exists = sgqlc.types.Field(Boolean, graphql_name='snarkJobs_exists')
    received_time_lt = sgqlc.types.Field(DateTime, graphql_name='receivedTime_lt')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    creator_account = sgqlc.types.Field(BlockCreatorAccountQueryInput, graphql_name='creatorAccount')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    received_time_ne = sgqlc.types.Field(DateTime, graphql_name='receivedTime_ne')
    creator_lte = sgqlc.types.Field(String, graphql_name='creator_lte')
    creator_account_exists = sgqlc.types.Field(Boolean, graphql_name='creatorAccount_exists')


class BlockSnarkJobInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee', 'prover', 'work_ids', 'block_height', 'block_state_hash', 'date_time')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')


class BlockSnarkJobQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_time', 'prover_gt', 'fee_gte', 'date_time_exists', 'block_height_gt', 'fee_exists', 'block_state_hash_exists', 'block_height_lt', 'block_state_hash_in', 'date_time_gt', 'block_height_exists', 'and_', 'fee_lte', 'prover_nin', 'block_state_hash_gte', 'work_ids_exists', 'date_time_in', 'prover_lt', 'work_ids_nin', 'block_height_ne', 'block_height_nin', 'block_state_hash_nin', 'date_time_nin', 'block_height', 'fee', 'fee_in', 'prover_in', 'work_ids_in', 'block_state_hash_ne', 'prover_exists', 'prover_ne', 'work_ids', 'fee_nin', 'block_height_lte', 'date_time_ne', 'prover_gte', 'block_state_hash_lt', 'prover', 'block_state_hash_gt', 'prover_lte', 'block_height_gte', 'fee_ne', 'fee_gt', 'block_state_hash', 'block_state_hash_lte', 'fee_lt', 'date_time_lte', 'date_time_lt', 'block_height_in', 'date_time_gte', 'or_')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    prover_gt = sgqlc.types.Field(String, graphql_name='prover_gt')
    fee_gte = sgqlc.types.Field(Int, graphql_name='fee_gte')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    block_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_exists')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    block_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_in')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockSnarkJobQueryInput')), graphql_name='AND')
    fee_lte = sgqlc.types.Field(Int, graphql_name='fee_lte')
    prover_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_nin')
    block_state_hash_gte = sgqlc.types.Field(String, graphql_name='blockStateHash_gte')
    work_ids_exists = sgqlc.types.Field(Boolean, graphql_name='workIds_exists')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    prover_lt = sgqlc.types.Field(String, graphql_name='prover_lt')
    work_ids_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_nin')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    block_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_nin')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_in')
    prover_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_in')
    work_ids_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_in')
    block_state_hash_ne = sgqlc.types.Field(String, graphql_name='blockStateHash_ne')
    prover_exists = sgqlc.types.Field(Boolean, graphql_name='prover_exists')
    prover_ne = sgqlc.types.Field(String, graphql_name='prover_ne')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_nin')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    prover_gte = sgqlc.types.Field(String, graphql_name='prover_gte')
    block_state_hash_lt = sgqlc.types.Field(String, graphql_name='blockStateHash_lt')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    block_state_hash_gt = sgqlc.types.Field(String, graphql_name='blockStateHash_gt')
    prover_lte = sgqlc.types.Field(String, graphql_name='prover_lte')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    fee_ne = sgqlc.types.Field(Int, graphql_name='fee_ne')
    fee_gt = sgqlc.types.Field(Int, graphql_name='fee_gt')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    block_state_hash_lte = sgqlc.types.Field(String, graphql_name='blockStateHash_lte')
    fee_lt = sgqlc.types.Field(Int, graphql_name='fee_lt')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockSnarkJobQueryInput')), graphql_name='OR')


class BlockSnarkJobUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_state_hash_unset', 'block_height_inc', 'date_time_unset', 'date_time', 'block_state_hash', 'block_height_unset', 'fee_inc', 'block_height', 'work_ids_unset', 'work_ids', 'fee', 'fee_unset', 'prover', 'prover_unset')
    block_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    fee_inc = sgqlc.types.Field(Int, graphql_name='fee_inc')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    work_ids_unset = sgqlc.types.Field(Boolean, graphql_name='workIds_unset')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    prover_unset = sgqlc.types.Field(Boolean, graphql_name='prover_unset')


class BlockTransactionCoinbaseReceiverAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionCoinbaseReceiverAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('and_', 'public_key_ne', 'public_key_gte', 'public_key_in', 'public_key', 'public_key_lt', 'public_key_nin', 'or_', 'public_key_lte', 'public_key_gt', 'public_key_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionCoinbaseReceiverAccountQueryInput')), graphql_name='AND')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionCoinbaseReceiverAccountQueryInput')), graphql_name='OR')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')


class BlockTransactionCoinbaseReceiverAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class BlockTransactionFeeTransferInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee', 'recipient', 'type')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    type = sgqlc.types.Field(String, graphql_name='type')


class BlockTransactionFeeTransferQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('or_', 'fee_gt', 'fee_exists', 'type_in', 'fee', 'fee_gte', 'recipient_ne', 'and_', 'type_ne', 'fee_nin', 'type_lt', 'type_lte', 'recipient_in', 'recipient_lt', 'recipient_gt', 'recipient_lte', 'fee_in', 'type', 'recipient_nin', 'type_gte', 'fee_ne', 'recipient_gte', 'type_gt', 'recipient_exists', 'recipient', 'type_nin', 'fee_lte', 'fee_lt', 'type_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionFeeTransferQueryInput')), graphql_name='OR')
    fee_gt = sgqlc.types.Field(Long, graphql_name='fee_gt')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='type_in')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    fee_gte = sgqlc.types.Field(Long, graphql_name='fee_gte')
    recipient_ne = sgqlc.types.Field(String, graphql_name='recipient_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionFeeTransferQueryInput')), graphql_name='AND')
    type_ne = sgqlc.types.Field(String, graphql_name='type_ne')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_nin')
    type_lt = sgqlc.types.Field(String, graphql_name='type_lt')
    type_lte = sgqlc.types.Field(String, graphql_name='type_lte')
    recipient_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipient_in')
    recipient_lt = sgqlc.types.Field(String, graphql_name='recipient_lt')
    recipient_gt = sgqlc.types.Field(String, graphql_name='recipient_gt')
    recipient_lte = sgqlc.types.Field(String, graphql_name='recipient_lte')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_in')
    type = sgqlc.types.Field(String, graphql_name='type')
    recipient_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipient_nin')
    type_gte = sgqlc.types.Field(String, graphql_name='type_gte')
    fee_ne = sgqlc.types.Field(Long, graphql_name='fee_ne')
    recipient_gte = sgqlc.types.Field(String, graphql_name='recipient_gte')
    type_gt = sgqlc.types.Field(String, graphql_name='type_gt')
    recipient_exists = sgqlc.types.Field(Boolean, graphql_name='recipient_exists')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    type_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='type_nin')
    fee_lte = sgqlc.types.Field(Long, graphql_name='fee_lte')
    fee_lt = sgqlc.types.Field(Long, graphql_name='fee_lt')
    type_exists = sgqlc.types.Field(Boolean, graphql_name='type_exists')


class BlockTransactionFeeTransferUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee', 'fee_unset', 'recipient', 'recipient_unset', 'type', 'type_unset')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    recipient_unset = sgqlc.types.Field(Boolean, graphql_name='recipient_unset')
    type = sgqlc.types.Field(String, graphql_name='type')
    type_unset = sgqlc.types.Field(Boolean, graphql_name='type_unset')


class BlockTransactionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee_transfer', 'user_commands', 'coinbase', 'coinbase_receiver_account')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferInsertInput), graphql_name='feeTransfer')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandInsertInput'), graphql_name='userCommands')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountInsertInput, graphql_name='coinbaseReceiverAccount')


class BlockTransactionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('coinbase_in', 'fee_transfer_in', 'and_', 'fee_transfer', 'fee_transfer_nin', 'user_commands', 'coinbase_receiver_account_exists', 'coinbase', 'coinbase_gt', 'coinbase_gte', 'user_commands_exists', 'coinbase_lt', 'coinbase_exists', 'user_commands_in', 'user_commands_nin', 'coinbase_lte', 'coinbase_nin', 'fee_transfer_exists', 'coinbase_receiver_account', 'or_', 'coinbase_ne')
    coinbase_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='coinbase_in')
    fee_transfer_in = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionQueryInput')), graphql_name='AND')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer')
    fee_transfer_nin = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer_nin')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands')
    coinbase_receiver_account_exists = sgqlc.types.Field(Boolean, graphql_name='coinbaseReceiverAccount_exists')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_gt = sgqlc.types.Field(Long, graphql_name='coinbase_gt')
    coinbase_gte = sgqlc.types.Field(Long, graphql_name='coinbase_gte')
    user_commands_exists = sgqlc.types.Field(Boolean, graphql_name='userCommands_exists')
    coinbase_lt = sgqlc.types.Field(Long, graphql_name='coinbase_lt')
    coinbase_exists = sgqlc.types.Field(Boolean, graphql_name='coinbase_exists')
    user_commands_in = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands_in')
    user_commands_nin = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands_nin')
    coinbase_lte = sgqlc.types.Field(Long, graphql_name='coinbase_lte')
    coinbase_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='coinbase_nin')
    fee_transfer_exists = sgqlc.types.Field(Boolean, graphql_name='feeTransfer_exists')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountQueryInput, graphql_name='coinbaseReceiverAccount')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionQueryInput')), graphql_name='OR')
    coinbase_ne = sgqlc.types.Field(Long, graphql_name='coinbase_ne')


class BlockTransactionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('coinbase_unset', 'coinbase_receiver_account', 'coinbase_receiver_account_unset', 'fee_transfer', 'fee_transfer_unset', 'user_commands', 'user_commands_unset', 'coinbase')
    coinbase_unset = sgqlc.types.Field(Boolean, graphql_name='coinbase_unset')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountUpdateInput, graphql_name='coinbaseReceiverAccount')
    coinbase_receiver_account_unset = sgqlc.types.Field(Boolean, graphql_name='coinbaseReceiverAccount_unset')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferUpdateInput), graphql_name='feeTransfer')
    fee_transfer_unset = sgqlc.types.Field(Boolean, graphql_name='feeTransfer_unset')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandUpdateInput'), graphql_name='userCommands')
    user_commands_unset = sgqlc.types.Field(Boolean, graphql_name='userCommands_unset')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')


class BlockTransactionUserCommandFeePayerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandFeePayerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gt', 'token_lte', 'or_', 'token_gte', 'token_exists', 'and_', 'token_ne', 'token_lt', 'token_nin', 'token_in', 'token')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFeePayerQueryInput')), graphql_name='OR')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFeePayerQueryInput')), graphql_name='AND')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token = sgqlc.types.Field(Int, graphql_name='token')


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
    __field_names__ = ('and_', 'token_lte', 'token_in', 'token_nin', 'token_gt', 'token_gte', 'or_', 'token', 'token_lt', 'token_exists', 'token_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFromAccountQueryInput')), graphql_name='AND')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFromAccountQueryInput')), graphql_name='OR')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')


class BlockTransactionUserCommandFromAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_unset', 'token_inc')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')


class BlockTransactionUserCommandInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee_token', 'receiver', 'block_height', 'from_account', 'hash', 'block_state_hash', 'date_time', 'amount', 'id', 'to', 'source', 'token', 'fee', 'from_', 'failure_reason', 'memo', 'kind', 'fee_payer', 'nonce', 'to_account', 'is_delegation')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiverInsertInput', graphql_name='receiver')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountInsertInput, graphql_name='fromAccount')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    id = sgqlc.types.Field(String, graphql_name='id')
    to = sgqlc.types.Field(String, graphql_name='to')
    source = sgqlc.types.Field('BlockTransactionUserCommandSourceInsertInput', graphql_name='source')
    token = sgqlc.types.Field(Int, graphql_name='token')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerInsertInput, graphql_name='feePayer')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccountInsertInput', graphql_name='toAccount')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')


class BlockTransactionUserCommandQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('memo_ne', 'amount_lte', 'hash_gte', 'fee_lt', 'hash_lte', 'from_gt', 'token_gt', 'date_time_in', 'receiver', 'memo_exists', 'block_state_hash_lte', 'from_in', 'failure_reason_in', 'hash_nin', 'to', 'fee_nin', 'hash_exists', 'to_account_exists', 'from_', 'date_time_gte', 'token_lte', 'fee_token_ne', 'kind_exists', 'fee_payer_exists', 'block_height_exists', 'from_exists', 'nonce_ne', 'block_height_lte', 'kind_gt', 'block_state_hash_gte', 'fee_token_exists', 'date_time_nin', 'block_state_hash_lt', 'block_height_in', 'nonce_gt', 'fee', 'from_account_exists', 'amount_in', 'nonce_lt', 'fee_token_nin', 'token_lt', 'date_time', 'amount', 'fee_lte', 'memo_gte', 'failure_reason_gte', 'token_nin', 'fee_token_in', 'id_gt', 'id_exists', 'to_gte', 'nonce_lte', 'memo_lte', 'nonce_exists', 'date_time_lt', 'id_nin', 'source_exists', 'source', 'from_ne', 'hash_gt', 'from_account', 'fee_ne', 'failure_reason_nin', 'hash', 'date_time_gt', 'kind', 'failure_reason_gt', 'id', 'id_gte', 'nonce', 'amount_gte', 'from_nin', 'block_height', 'block_state_hash', 'hash_ne', 'token_in', 'failure_reason_exists', 'id_lte', 'fee_gt', 'memo_nin', 'is_delegation_ne', 'amount_nin', 'amount_gt', 'memo', 'block_height_lt', 'block_state_hash_exists', 'fee_token', 'to_gt', 'date_time_lte', 'kind_lt', 'hash_lt', 'fee_exists', 'block_height_nin', 'amount_lt', 'failure_reason', 'date_time_exists', 'nonce_gte', 'memo_in', 'to_lt', 'to_exists', 'block_height_gt', 'kind_gte', 'kind_nin', 'memo_gt', 'fee_token_gte', 'id_lt', 'hash_in', 'block_height_ne', 'id_ne', 'block_state_hash_nin', 'to_in', 'failure_reason_lte', 'to_ne', 'token_exists', 'kind_lte', 'fee_token_lt', 'block_height_gte', 'token_ne', 'kind_in', 'fee_payer', 'amount_exists', 'is_delegation_exists', 'block_state_hash_gt', 'date_time_ne', 'token', 'fee_token_lte', 'failure_reason_ne', 'id_in', 'fee_token_gt', 'receiver_exists', 'token_gte', 'block_state_hash_ne', 'nonce_nin', 'from_lt', 'block_state_hash_in', 'from_lte', 'memo_lt', 'amount_ne', 'to_nin', 'or_', 'to_lte', 'and_', 'fee_gte', 'to_account', 'is_delegation', 'kind_ne', 'nonce_in', 'from_gte', 'failure_reason_lt', 'fee_in')
    memo_ne = sgqlc.types.Field(String, graphql_name='memo_ne')
    amount_lte = sgqlc.types.Field(Int, graphql_name='amount_lte')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    fee_lt = sgqlc.types.Field(Int, graphql_name='fee_lt')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiverQueryInput', graphql_name='receiver')
    memo_exists = sgqlc.types.Field(Boolean, graphql_name='memo_exists')
    block_state_hash_lte = sgqlc.types.Field(String, graphql_name='blockStateHash_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_in')
    failure_reason_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_in')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    to = sgqlc.types.Field(String, graphql_name='to')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_nin')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    to_account_exists = sgqlc.types.Field(Boolean, graphql_name='toAccount_exists')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    fee_token_ne = sgqlc.types.Field(Int, graphql_name='feeToken_ne')
    kind_exists = sgqlc.types.Field(Boolean, graphql_name='kind_exists')
    fee_payer_exists = sgqlc.types.Field(Boolean, graphql_name='feePayer_exists')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    from_exists = sgqlc.types.Field(Boolean, graphql_name='from_exists')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    kind_gt = sgqlc.types.Field(String, graphql_name='kind_gt')
    block_state_hash_gte = sgqlc.types.Field(String, graphql_name='blockStateHash_gte')
    fee_token_exists = sgqlc.types.Field(Boolean, graphql_name='feeToken_exists')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    block_state_hash_lt = sgqlc.types.Field(String, graphql_name='blockStateHash_lt')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    from_account_exists = sgqlc.types.Field(Boolean, graphql_name='fromAccount_exists')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='amount_in')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    fee_token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_nin')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    fee_lte = sgqlc.types.Field(Int, graphql_name='fee_lte')
    memo_gte = sgqlc.types.Field(String, graphql_name='memo_gte')
    failure_reason_gte = sgqlc.types.Field(String, graphql_name='failureReason_gte')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    fee_token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_in')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    id_exists = sgqlc.types.Field(Boolean, graphql_name='id_exists')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    memo_lte = sgqlc.types.Field(String, graphql_name='memo_lte')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_nin')
    source_exists = sgqlc.types.Field(Boolean, graphql_name='source_exists')
    source = sgqlc.types.Field('BlockTransactionUserCommandSourceQueryInput', graphql_name='source')
    from_ne = sgqlc.types.Field(String, graphql_name='from_ne')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountQueryInput, graphql_name='fromAccount')
    fee_ne = sgqlc.types.Field(Int, graphql_name='fee_ne')
    failure_reason_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_nin')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    failure_reason_gt = sgqlc.types.Field(String, graphql_name='failureReason_gt')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    amount_gte = sgqlc.types.Field(Int, graphql_name='amount_gte')
    from_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_nin')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    failure_reason_exists = sgqlc.types.Field(Boolean, graphql_name='failureReason_exists')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    fee_gt = sgqlc.types.Field(Int, graphql_name='fee_gt')
    memo_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_nin')
    is_delegation_ne = sgqlc.types.Field(Boolean, graphql_name='isDelegation_ne')
    amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='amount_nin')
    amount_gt = sgqlc.types.Field(Int, graphql_name='amount_gt')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    block_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_exists')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    kind_lt = sgqlc.types.Field(String, graphql_name='kind_lt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    amount_lt = sgqlc.types.Field(Int, graphql_name='amount_lt')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    memo_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_in')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_exists = sgqlc.types.Field(Boolean, graphql_name='to_exists')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    kind_gte = sgqlc.types.Field(String, graphql_name='kind_gte')
    kind_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_nin')
    memo_gt = sgqlc.types.Field(String, graphql_name='memo_gt')
    fee_token_gte = sgqlc.types.Field(Int, graphql_name='feeToken_gte')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    id_ne = sgqlc.types.Field(String, graphql_name='id_ne')
    block_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_nin')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_in')
    failure_reason_lte = sgqlc.types.Field(String, graphql_name='failureReason_lte')
    to_ne = sgqlc.types.Field(String, graphql_name='to_ne')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    kind_lte = sgqlc.types.Field(String, graphql_name='kind_lte')
    fee_token_lt = sgqlc.types.Field(Int, graphql_name='feeToken_lt')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    kind_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_in')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerQueryInput, graphql_name='feePayer')
    amount_exists = sgqlc.types.Field(Boolean, graphql_name='amount_exists')
    is_delegation_exists = sgqlc.types.Field(Boolean, graphql_name='isDelegation_exists')
    block_state_hash_gt = sgqlc.types.Field(String, graphql_name='blockStateHash_gt')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    token = sgqlc.types.Field(Int, graphql_name='token')
    fee_token_lte = sgqlc.types.Field(Int, graphql_name='feeToken_lte')
    failure_reason_ne = sgqlc.types.Field(String, graphql_name='failureReason_ne')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_in')
    fee_token_gt = sgqlc.types.Field(Int, graphql_name='feeToken_gt')
    receiver_exists = sgqlc.types.Field(Boolean, graphql_name='receiver_exists')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    block_state_hash_ne = sgqlc.types.Field(String, graphql_name='blockStateHash_ne')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    block_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_in')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    memo_lt = sgqlc.types.Field(String, graphql_name='memo_lt')
    amount_ne = sgqlc.types.Field(Int, graphql_name='amount_ne')
    to_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandQueryInput')), graphql_name='OR')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandQueryInput')), graphql_name='AND')
    fee_gte = sgqlc.types.Field(Int, graphql_name='fee_gte')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccountQueryInput', graphql_name='toAccount')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    kind_ne = sgqlc.types.Field(String, graphql_name='kind_ne')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    failure_reason_lt = sgqlc.types.Field(String, graphql_name='failureReason_lt')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_in')


class BlockTransactionUserCommandReceiverInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandReceiverQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_ne', 'public_key_gte', 'and_', 'public_key', 'public_key_nin', 'public_key_lte', 'or_', 'public_key_gt', 'public_key_exists', 'public_key_lt', 'public_key_in')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandReceiverQueryInput')), graphql_name='AND')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandReceiverQueryInput')), graphql_name='OR')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')


class BlockTransactionUserCommandReceiverUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class BlockTransactionUserCommandSourceInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandSourceQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_gt', 'or_', 'public_key_exists', 'public_key_lt', 'public_key_ne', 'public_key_lte', 'public_key_gte', 'and_', 'public_key_in', 'public_key_nin', 'public_key')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandSourceQueryInput')), graphql_name='OR')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandSourceQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


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
    __field_names__ = ('token', 'token_lte', 'and_', 'token_lt', 'token_ne', 'or_', 'token_exists', 'token_in', 'token_gt', 'token_gte', 'token_nin')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandToAccountQueryInput')), graphql_name='AND')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandToAccountQueryInput')), graphql_name='OR')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')


class BlockTransactionUserCommandToAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class BlockTransactionUserCommandUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee_payer', 'source_unset', 'kind_unset', 'amount_unset', 'block_height', 'block_state_hash_unset', 'from_account_unset', 'source', 'date_time', 'amount_inc', 'block_height_unset', 'nonce', 'fee_token', 'is_delegation', 'hash_unset', 'from_account', 'token_inc', 'receiver_unset', 'date_time_unset', 'kind', 'to_unset', 'block_state_hash', 'memo', 'memo_unset', 'fee_unset', 'fee_token_unset', 'nonce_inc', 'fee_token_inc', 'is_delegation_unset', 'failure_reason', 'failure_reason_unset', 'receiver', 'token_unset', 'nonce_unset', 'to', 'token', 'fee', 'fee_inc', 'id_unset', 'block_height_inc', 'from_unset', 'id', 'amount', 'to_account', 'from_', 'fee_payer_unset', 'hash', 'to_account_unset')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerUpdateInput, graphql_name='feePayer')
    source_unset = sgqlc.types.Field(Boolean, graphql_name='source_unset')
    kind_unset = sgqlc.types.Field(Boolean, graphql_name='kind_unset')
    amount_unset = sgqlc.types.Field(Boolean, graphql_name='amount_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_unset')
    from_account_unset = sgqlc.types.Field(Boolean, graphql_name='fromAccount_unset')
    source = sgqlc.types.Field(BlockTransactionUserCommandSourceUpdateInput, graphql_name='source')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    amount_inc = sgqlc.types.Field(Int, graphql_name='amount_inc')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountUpdateInput, graphql_name='fromAccount')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    receiver_unset = sgqlc.types.Field(Boolean, graphql_name='receiver_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    to_unset = sgqlc.types.Field(Boolean, graphql_name='to_unset')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    memo_unset = sgqlc.types.Field(Boolean, graphql_name='memo_unset')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    fee_token_unset = sgqlc.types.Field(Boolean, graphql_name='feeToken_unset')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    fee_token_inc = sgqlc.types.Field(Int, graphql_name='feeToken_inc')
    is_delegation_unset = sgqlc.types.Field(Boolean, graphql_name='isDelegation_unset')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    failure_reason_unset = sgqlc.types.Field(Boolean, graphql_name='failureReason_unset')
    receiver = sgqlc.types.Field(BlockTransactionUserCommandReceiverUpdateInput, graphql_name='receiver')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    to = sgqlc.types.Field(String, graphql_name='to')
    token = sgqlc.types.Field(Int, graphql_name='token')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    fee_inc = sgqlc.types.Field(Int, graphql_name='fee_inc')
    id_unset = sgqlc.types.Field(Boolean, graphql_name='id_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    from_unset = sgqlc.types.Field(Boolean, graphql_name='from_unset')
    id = sgqlc.types.Field(String, graphql_name='id')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    to_account = sgqlc.types.Field(BlockTransactionUserCommandToAccountUpdateInput, graphql_name='toAccount')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    fee_payer_unset = sgqlc.types.Field(Boolean, graphql_name='feePayer_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    to_account_unset = sgqlc.types.Field(Boolean, graphql_name='toAccount_unset')


class BlockUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_time_unset', 'creator_unset', 'canonical_unset', 'protocol_state_unset', 'transactions', 'protocol_state', 'snark_jobs_unset', 'state_hash_unset', 'winner_account', 'winner_account_unset', 'creator_account', 'state_hash_field', 'date_time', 'snark_jobs', 'state_hash', 'received_time', 'received_time_unset', 'canonical', 'state_hash_field_unset', 'block_height', 'transactions_unset', 'block_height_inc', 'block_height_unset', 'creator', 'creator_account_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    creator_unset = sgqlc.types.Field(Boolean, graphql_name='creator_unset')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    protocol_state_unset = sgqlc.types.Field(Boolean, graphql_name='protocolState_unset')
    transactions = sgqlc.types.Field(BlockTransactionUpdateInput, graphql_name='transactions')
    protocol_state = sgqlc.types.Field(BlockProtocolStateUpdateInput, graphql_name='protocolState')
    snark_jobs_unset = sgqlc.types.Field(Boolean, graphql_name='snarkJobs_unset')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    winner_account = sgqlc.types.Field('BlockWinnerAccountUpdateInput', graphql_name='winnerAccount')
    winner_account_unset = sgqlc.types.Field(Boolean, graphql_name='winnerAccount_unset')
    creator_account = sgqlc.types.Field(BlockCreatorAccountUpdateInput, graphql_name='creatorAccount')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of(BlockSnarkJobUpdateInput), graphql_name='snarkJobs')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    received_time_unset = sgqlc.types.Field(Boolean, graphql_name='receivedTime_unset')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    state_hash_field_unset = sgqlc.types.Field(Boolean, graphql_name='stateHashField_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    transactions_unset = sgqlc.types.Field(Boolean, graphql_name='transactions_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    creator_account_unset = sgqlc.types.Field(Boolean, graphql_name='creatorAccount_unset')


class BlockWinnerAccountBalanceInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height', 'liquid', 'locked', 'state_hash', 'total', 'unknown')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    total = sgqlc.types.Field(Long, graphql_name='total')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')


class BlockWinnerAccountBalanceQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('and_', 'unknown_gt', 'total', 'locked_in', 'total_lt', 'liquid_lte', 'state_hash', 'unknown_in', 'state_hash_lt', 'unknown_lte', 'liquid_exists', 'locked_lt', 'liquid_nin', 'state_hash_in', 'block_height_lt', 'block_height_gt', 'unknown_lt', 'block_height_lte', 'liquid', 'block_height_exists', 'state_hash_gte', 'liquid_in', 'total_lte', 'total_gte', 'block_height_nin', 'liquid_ne', 'total_nin', 'unknown_gte', 'total_gt', 'locked_gt', 'total_ne', 'block_height_ne', 'block_height_gte', 'total_in', 'locked_ne', 'unknown_nin', 'unknown', 'state_hash_ne', 'locked_exists', 'locked_lte', 'locked_gte', 'unknown_ne', 'liquid_gt', 'liquid_gte', 'unknown_exists', 'block_height_in', 'locked_nin', 'locked', 'state_hash_lte', 'state_hash_exists', 'state_hash_gt', 'total_exists', 'block_height', 'state_hash_nin', 'liquid_lt', 'or_')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountBalanceQueryInput')), graphql_name='AND')
    unknown_gt = sgqlc.types.Field(Long, graphql_name='unknown_gt')
    total = sgqlc.types.Field(Long, graphql_name='total')
    locked_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='locked_in')
    total_lt = sgqlc.types.Field(Long, graphql_name='total_lt')
    liquid_lte = sgqlc.types.Field(Int, graphql_name='liquid_lte')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    unknown_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='unknown_in')
    state_hash_lt = sgqlc.types.Field(String, graphql_name='stateHash_lt')
    unknown_lte = sgqlc.types.Field(Long, graphql_name='unknown_lte')
    liquid_exists = sgqlc.types.Field(Boolean, graphql_name='liquid_exists')
    locked_lt = sgqlc.types.Field(Long, graphql_name='locked_lt')
    liquid_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='liquid_nin')
    state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_in')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    unknown_lt = sgqlc.types.Field(Long, graphql_name='unknown_lt')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    state_hash_gte = sgqlc.types.Field(String, graphql_name='stateHash_gte')
    liquid_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='liquid_in')
    total_lte = sgqlc.types.Field(Long, graphql_name='total_lte')
    total_gte = sgqlc.types.Field(Long, graphql_name='total_gte')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    liquid_ne = sgqlc.types.Field(Int, graphql_name='liquid_ne')
    total_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='total_nin')
    unknown_gte = sgqlc.types.Field(Long, graphql_name='unknown_gte')
    total_gt = sgqlc.types.Field(Long, graphql_name='total_gt')
    locked_gt = sgqlc.types.Field(Long, graphql_name='locked_gt')
    total_ne = sgqlc.types.Field(Long, graphql_name='total_ne')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    total_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='total_in')
    locked_ne = sgqlc.types.Field(Long, graphql_name='locked_ne')
    unknown_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='unknown_nin')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    state_hash_ne = sgqlc.types.Field(String, graphql_name='stateHash_ne')
    locked_exists = sgqlc.types.Field(Boolean, graphql_name='locked_exists')
    locked_lte = sgqlc.types.Field(Long, graphql_name='locked_lte')
    locked_gte = sgqlc.types.Field(Long, graphql_name='locked_gte')
    unknown_ne = sgqlc.types.Field(Long, graphql_name='unknown_ne')
    liquid_gt = sgqlc.types.Field(Int, graphql_name='liquid_gt')
    liquid_gte = sgqlc.types.Field(Int, graphql_name='liquid_gte')
    unknown_exists = sgqlc.types.Field(Boolean, graphql_name='unknown_exists')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    locked_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='locked_nin')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    state_hash_lte = sgqlc.types.Field(String, graphql_name='stateHash_lte')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    state_hash_gt = sgqlc.types.Field(String, graphql_name='stateHash_gt')
    total_exists = sgqlc.types.Field(Boolean, graphql_name='total_exists')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_nin')
    liquid_lt = sgqlc.types.Field(Int, graphql_name='liquid_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountBalanceQueryInput')), graphql_name='OR')


class BlockWinnerAccountBalanceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('locked_unset', 'total', 'block_height_unset', 'state_hash_unset', 'liquid_unset', 'liquid', 'locked', 'block_height_inc', 'block_height', 'unknown', 'liquid_inc', 'unknown_unset', 'total_unset', 'state_hash')
    locked_unset = sgqlc.types.Field(Boolean, graphql_name='locked_unset')
    total = sgqlc.types.Field(Long, graphql_name='total')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    liquid_unset = sgqlc.types.Field(Boolean, graphql_name='liquid_unset')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    liquid_inc = sgqlc.types.Field(Int, graphql_name='liquid_inc')
    unknown_unset = sgqlc.types.Field(Boolean, graphql_name='unknown_unset')
    total_unset = sgqlc.types.Field(Boolean, graphql_name='total_unset')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')


class BlockWinnerAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'public_key')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceInsertInput, graphql_name='balance')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockWinnerAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_lt', 'public_key_ne', 'or_', 'balance', 'public_key', 'public_key_gte', 'and_', 'public_key_lte', 'public_key_nin', 'public_key_gt', 'public_key_in', 'public_key_exists', 'balance_exists')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountQueryInput')), graphql_name='OR')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceQueryInput, graphql_name='balance')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountQueryInput')), graphql_name='AND')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')


class BlockWinnerAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'balance_unset', 'public_key', 'public_key_unset')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceUpdateInput, graphql_name='balance')
    balance_unset = sgqlc.types.Field(Boolean, graphql_name='balance_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class SnarkBlockStateHashRelationInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('link', 'create')
    link = sgqlc.types.Field(String, graphql_name='link')
    create = sgqlc.types.Field(BlockInsertInput, graphql_name='create')


class SnarkInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('prover', 'work_ids', 'block_height', 'block', 'canonical', 'date_time', 'fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block = sgqlc.types.Field(SnarkBlockStateHashRelationInput, graphql_name='block')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Int, graphql_name='fee')


class SnarkQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('prover_ne', 'date_time_gte', 'fee_lte', 'work_ids_exists', 'block_height_nin', 'canonical', 'canonical_ne', 'block_height_ne', 'date_time_ne', 'block_height_exists', 'fee', 'work_ids_in', 'block_height_gte', 'prover_in', 'fee_gt', 'date_time', 'fee_exists', 'fee_lt', 'fee_gte', 'prover_lt', 'canonical_exists', 'date_time_in', 'prover_nin', 'work_ids', 'block_height_lte', 'prover_gte', 'block_height_in', 'prover_lte', 'date_time_gt', 'prover_gt', 'prover_exists', 'date_time_lt', 'block_height', 'date_time_exists', 'fee_ne', 'work_ids_nin', 'or_', 'date_time_nin', 'block_height_gt', 'block_height_lt', 'date_time_lte', 'fee_nin', 'block_exists', 'fee_in', 'prover', 'block', 'and_')
    prover_ne = sgqlc.types.Field(String, graphql_name='prover_ne')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    fee_lte = sgqlc.types.Field(Int, graphql_name='fee_lte')
    work_ids_exists = sgqlc.types.Field(Boolean, graphql_name='workIds_exists')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    work_ids_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_in')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    prover_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_in')
    fee_gt = sgqlc.types.Field(Int, graphql_name='fee_gt')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    fee_lt = sgqlc.types.Field(Int, graphql_name='fee_lt')
    fee_gte = sgqlc.types.Field(Int, graphql_name='fee_gte')
    prover_lt = sgqlc.types.Field(String, graphql_name='prover_lt')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    prover_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_nin')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    prover_gte = sgqlc.types.Field(String, graphql_name='prover_gte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    prover_lte = sgqlc.types.Field(String, graphql_name='prover_lte')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    prover_gt = sgqlc.types.Field(String, graphql_name='prover_gt')
    prover_exists = sgqlc.types.Field(Boolean, graphql_name='prover_exists')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    fee_ne = sgqlc.types.Field(Int, graphql_name='fee_ne')
    work_ids_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SnarkQueryInput')), graphql_name='OR')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_nin')
    block_exists = sgqlc.types.Field(Boolean, graphql_name='block_exists')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_in')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    block = sgqlc.types.Field(BlockQueryInput, graphql_name='block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SnarkQueryInput')), graphql_name='AND')


class SnarkUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height_inc', 'block', 'canonical_unset', 'date_time', 'canonical', 'fee', 'prover_unset', 'block_height_unset', 'block_unset', 'work_ids', 'block_height', 'date_time_unset', 'fee_inc', 'fee_unset', 'prover', 'work_ids_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block = sgqlc.types.Field(SnarkBlockStateHashRelationInput, graphql_name='block')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover_unset = sgqlc.types.Field(Boolean, graphql_name='prover_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    block_unset = sgqlc.types.Field(Boolean, graphql_name='block_unset')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    fee_inc = sgqlc.types.Field(Int, graphql_name='fee_inc')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids_unset = sgqlc.types.Field(Boolean, graphql_name='workIds_unset')


class StakeInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receipt_chain_hash', 'epoch', 'ledger_hash', 'balance', 'delegate', 'timing', 'chain_id', 'public_key', 'voting_for', 'token', 'nonce', 'permissions')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    timing = sgqlc.types.Field('StakeTimingInsertInput', graphql_name='timing')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    token = sgqlc.types.Field(Int, graphql_name='token')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('StakePermissionInsertInput', graphql_name='permissions')


class StakePermissionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('edit_state', 'send', 'set_delegate', 'set_permissions', 'set_verification_key', 'stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')


class StakePermissionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('send', 'set_delegate_lte', 'set_permissions_in', 'or_', 'stake_exists', 'set_delegate_lt', 'set_permissions_nin', 'edit_state_in', 'edit_state_gte', 'send_gt', 'set_verification_key_ne', 'set_delegate', 'stake', 'edit_state', 'set_delegate_in', 'edit_state_gt', 'set_delegate_nin', 'set_permissions_gt', 'send_gte', 'send_lt', 'set_delegate_gte', 'set_permissions_lt', 'set_verification_key_gt', 'set_permissions_lte', 'set_verification_key_exists', 'set_verification_key_gte', 'set_permissions_ne', 'set_delegate_exists', 'set_permissions_exists', 'send_lte', 'set_verification_key_nin', 'send_nin', 'set_verification_key_in', 'edit_state_lt', 'edit_state_ne', 'set_delegate_ne', 'set_verification_key', 'set_verification_key_lt', 'set_permissions', 'and_', 'send_exists', 'send_in', 'edit_state_nin', 'set_delegate_gt', 'edit_state_lte', 'edit_state_exists', 'send_ne', 'set_verification_key_lte', 'set_permissions_gte', 'stake_ne')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_delegate_lte = sgqlc.types.Field(String, graphql_name='set_delegate_lte')
    set_permissions_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakePermissionQueryInput')), graphql_name='OR')
    stake_exists = sgqlc.types.Field(Boolean, graphql_name='stake_exists')
    set_delegate_lt = sgqlc.types.Field(String, graphql_name='set_delegate_lt')
    set_permissions_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_nin')
    edit_state_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_in')
    edit_state_gte = sgqlc.types.Field(String, graphql_name='edit_state_gte')
    send_gt = sgqlc.types.Field(String, graphql_name='send_gt')
    set_verification_key_ne = sgqlc.types.Field(String, graphql_name='set_verification_key_ne')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    set_delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_in')
    edit_state_gt = sgqlc.types.Field(String, graphql_name='edit_state_gt')
    set_delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_nin')
    set_permissions_gt = sgqlc.types.Field(String, graphql_name='set_permissions_gt')
    send_gte = sgqlc.types.Field(String, graphql_name='send_gte')
    send_lt = sgqlc.types.Field(String, graphql_name='send_lt')
    set_delegate_gte = sgqlc.types.Field(String, graphql_name='set_delegate_gte')
    set_permissions_lt = sgqlc.types.Field(String, graphql_name='set_permissions_lt')
    set_verification_key_gt = sgqlc.types.Field(String, graphql_name='set_verification_key_gt')
    set_permissions_lte = sgqlc.types.Field(String, graphql_name='set_permissions_lte')
    set_verification_key_exists = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_exists')
    set_verification_key_gte = sgqlc.types.Field(String, graphql_name='set_verification_key_gte')
    set_permissions_ne = sgqlc.types.Field(String, graphql_name='set_permissions_ne')
    set_delegate_exists = sgqlc.types.Field(Boolean, graphql_name='set_delegate_exists')
    set_permissions_exists = sgqlc.types.Field(Boolean, graphql_name='set_permissions_exists')
    send_lte = sgqlc.types.Field(String, graphql_name='send_lte')
    set_verification_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_nin')
    send_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_nin')
    set_verification_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_in')
    edit_state_lt = sgqlc.types.Field(String, graphql_name='edit_state_lt')
    edit_state_ne = sgqlc.types.Field(String, graphql_name='edit_state_ne')
    set_delegate_ne = sgqlc.types.Field(String, graphql_name='set_delegate_ne')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    set_verification_key_lt = sgqlc.types.Field(String, graphql_name='set_verification_key_lt')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakePermissionQueryInput')), graphql_name='AND')
    send_exists = sgqlc.types.Field(Boolean, graphql_name='send_exists')
    send_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_in')
    edit_state_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_nin')
    set_delegate_gt = sgqlc.types.Field(String, graphql_name='set_delegate_gt')
    edit_state_lte = sgqlc.types.Field(String, graphql_name='edit_state_lte')
    edit_state_exists = sgqlc.types.Field(Boolean, graphql_name='edit_state_exists')
    send_ne = sgqlc.types.Field(String, graphql_name='send_ne')
    set_verification_key_lte = sgqlc.types.Field(String, graphql_name='set_verification_key_lte')
    set_permissions_gte = sgqlc.types.Field(String, graphql_name='set_permissions_gte')
    stake_ne = sgqlc.types.Field(Boolean, graphql_name='stake_ne')


class StakePermissionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('set_delegate_unset', 'stake', 'send', 'set_verification_key_unset', 'edit_state', 'edit_state_unset', 'set_delegate', 'set_permissions', 'set_permissions_unset', 'set_verification_key', 'send_unset', 'stake_unset')
    set_delegate_unset = sgqlc.types.Field(Boolean, graphql_name='set_delegate_unset')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_verification_key_unset = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_unset')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    edit_state_unset = sgqlc.types.Field(Boolean, graphql_name='edit_state_unset')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_permissions_unset = sgqlc.types.Field(Boolean, graphql_name='set_permissions_unset')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    send_unset = sgqlc.types.Field(Boolean, graphql_name='send_unset')
    stake_unset = sgqlc.types.Field(Boolean, graphql_name='stake_unset')


class StakeQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gt', 'voting_for_in', 'receipt_chain_hash', 'balance_gt', 'receipt_chain_hash_lt', 'balance_lte', 'ledger_hash_nin', 'nonce', 'voting_for_lt', 'receipt_chain_hash_ne', 'token_lt', 'delegate_lte', 'balance_nin', 'public_key_gte', 'delegate_lt', 'token_lte', 'nonce_gt', 'voting_for_lte', 'chain_id_lte', 'epoch_lt', 'epoch', 'receipt_chain_hash_lte', 'receipt_chain_hash_gte', 'token_gte', 'ledger_hash_gte', 'permissions', 'delegate_ne', 'ledger_hash_lte', 'balance_gte', 'public_key_ne', 'balance_ne', 'receipt_chain_hash_nin', 'nonce_lte', 'ledger_hash_ne', 'token_exists', 'nonce_lt', 'epoch_gt', 'balance_in', 'delegate_gte', 'token_ne', 'balance', 'delegate_in', 'timing_exists', 'receipt_chain_hash_exists', 'public_key_nin', 'permissions_exists', 'voting_for', 'chain_id_lt', 'public_key_gt', 'chain_id', 'public_key', 'balance_exists', 'delegate_nin', 'receipt_chain_hash_in', 'epoch_ne', 'public_key_lte', 'receipt_chain_hash_gt', 'chain_id_ne', 'ledger_hash_in', 'token', 'chain_id_gte', 'timing', 'voting_for_exists', 'token_nin', 'voting_for_ne', 'and_', 'chain_id_in', 'public_key_lt', 'voting_for_gt', 'or_', 'nonce_exists', 'epoch_exists', 'public_key_exists', 'nonce_in', 'voting_for_nin', 'ledger_hash_exists', 'chain_id_nin', 'token_in', 'ledger_hash_gt', 'balance_lt', 'nonce_nin', 'epoch_in', 'public_key_in', 'delegate_gt', 'chain_id_gt', 'epoch_nin', 'epoch_gte', 'delegate', 'nonce_gte', 'delegate_exists', 'epoch_lte', 'ledger_hash', 'chain_id_exists', 'nonce_ne', 'ledger_hash_lt', 'voting_for_gte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    voting_for_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_in')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    balance_gt = sgqlc.types.Field(Float, graphql_name='balance_gt')
    receipt_chain_hash_lt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lt')
    balance_lte = sgqlc.types.Field(Float, graphql_name='balance_lte')
    ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_nin')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    voting_for_lt = sgqlc.types.Field(String, graphql_name='voting_for_lt')
    receipt_chain_hash_ne = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_ne')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    delegate_lte = sgqlc.types.Field(String, graphql_name='delegate_lte')
    balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_nin')
    public_key_gte = sgqlc.types.Field(String, graphql_name='public_key_gte')
    delegate_lt = sgqlc.types.Field(String, graphql_name='delegate_lt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    voting_for_lte = sgqlc.types.Field(String, graphql_name='voting_for_lte')
    chain_id_lte = sgqlc.types.Field(String, graphql_name='chainId_lte')
    epoch_lt = sgqlc.types.Field(Int, graphql_name='epoch_lt')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    receipt_chain_hash_lte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lte')
    receipt_chain_hash_gte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gte')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    ledger_hash_gte = sgqlc.types.Field(String, graphql_name='ledgerHash_gte')
    permissions = sgqlc.types.Field(StakePermissionQueryInput, graphql_name='permissions')
    delegate_ne = sgqlc.types.Field(String, graphql_name='delegate_ne')
    ledger_hash_lte = sgqlc.types.Field(String, graphql_name='ledgerHash_lte')
    balance_gte = sgqlc.types.Field(Float, graphql_name='balance_gte')
    public_key_ne = sgqlc.types.Field(String, graphql_name='public_key_ne')
    balance_ne = sgqlc.types.Field(Float, graphql_name='balance_ne')
    receipt_chain_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_nin')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    ledger_hash_ne = sgqlc.types.Field(String, graphql_name='ledgerHash_ne')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    epoch_gt = sgqlc.types.Field(Int, graphql_name='epoch_gt')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_in')
    delegate_gte = sgqlc.types.Field(String, graphql_name='delegate_gte')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_in')
    timing_exists = sgqlc.types.Field(Boolean, graphql_name='timing_exists')
    receipt_chain_hash_exists = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_exists')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_nin')
    permissions_exists = sgqlc.types.Field(Boolean, graphql_name='permissions_exists')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    chain_id_lt = sgqlc.types.Field(String, graphql_name='chainId_lt')
    public_key_gt = sgqlc.types.Field(String, graphql_name='public_key_gt')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')
    delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_nin')
    receipt_chain_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_in')
    epoch_ne = sgqlc.types.Field(Int, graphql_name='epoch_ne')
    public_key_lte = sgqlc.types.Field(String, graphql_name='public_key_lte')
    receipt_chain_hash_gt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gt')
    chain_id_ne = sgqlc.types.Field(String, graphql_name='chainId_ne')
    ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_in')
    token = sgqlc.types.Field(Int, graphql_name='token')
    chain_id_gte = sgqlc.types.Field(String, graphql_name='chainId_gte')
    timing = sgqlc.types.Field('StakeTimingQueryInput', graphql_name='timing')
    voting_for_exists = sgqlc.types.Field(Boolean, graphql_name='voting_for_exists')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    voting_for_ne = sgqlc.types.Field(String, graphql_name='voting_for_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeQueryInput')), graphql_name='AND')
    chain_id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chainId_in')
    public_key_lt = sgqlc.types.Field(String, graphql_name='public_key_lt')
    voting_for_gt = sgqlc.types.Field(String, graphql_name='voting_for_gt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeQueryInput')), graphql_name='OR')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    epoch_exists = sgqlc.types.Field(Boolean, graphql_name='epoch_exists')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='public_key_exists')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    voting_for_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_nin')
    ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_exists')
    chain_id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chainId_nin')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    ledger_hash_gt = sgqlc.types.Field(String, graphql_name='ledgerHash_gt')
    balance_lt = sgqlc.types.Field(Float, graphql_name='balance_lt')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    epoch_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_in')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_in')
    delegate_gt = sgqlc.types.Field(String, graphql_name='delegate_gt')
    chain_id_gt = sgqlc.types.Field(String, graphql_name='chainId_gt')
    epoch_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_nin')
    epoch_gte = sgqlc.types.Field(Int, graphql_name='epoch_gte')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    delegate_exists = sgqlc.types.Field(Boolean, graphql_name='delegate_exists')
    epoch_lte = sgqlc.types.Field(Int, graphql_name='epoch_lte')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    chain_id_exists = sgqlc.types.Field(Boolean, graphql_name='chainId_exists')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    ledger_hash_lt = sgqlc.types.Field(String, graphql_name='ledgerHash_lt')
    voting_for_gte = sgqlc.types.Field(String, graphql_name='voting_for_gte')


class StakeTimingInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('timed_epoch_end', 'cliff_time', 'cliff_amount', 'untimed_slot', 'vesting_increment', 'timed_weighting', 'vesting_period', 'timed_in_epoch', 'initial_minimum_balance')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')


class StakeTimingQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('untimed_slot_gt', 'initial_minimum_balance_lte', 'untimed_slot_lte', 'initial_minimum_balance', 'untimed_slot_exists', 'vesting_increment_gt', 'timed_weighting_in', 'cliff_amount_gt', 'or_', 'vesting_period', 'vesting_period_gt', 'timed_epoch_end_exists', 'cliff_amount_ne', 'timed_weighting_nin', 'cliff_time_gte', 'vesting_increment_gte', 'cliff_amount_nin', 'cliff_time_ne', 'cliff_time_lte', 'vesting_period_lte', 'cliff_time_lt', 'vesting_increment_lte', 'cliff_amount_lt', 'initial_minimum_balance_exists', 'cliff_time_gt', 'vesting_period_gte', 'timed_epoch_end_ne', 'vesting_period_nin', 'vesting_period_lt', 'untimed_slot', 'timed_weighting_ne', 'initial_minimum_balance_gte', 'untimed_slot_gte', 'initial_minimum_balance_ne', 'vesting_increment_in', 'timed_weighting_gt', 'untimed_slot_lt', 'vesting_increment_ne', 'cliff_amount_gte', 'cliff_amount_lte', 'timed_weighting', 'vesting_increment', 'vesting_increment_lt', 'cliff_time_in', 'timed_epoch_end', 'vesting_period_ne', 'vesting_increment_nin', 'timed_weighting_exists', 'initial_minimum_balance_in', 'timed_in_epoch_exists', 'timed_in_epoch', 'cliff_amount_exists', 'vesting_period_exists', 'vesting_period_in', 'timed_weighting_lte', 'timed_weighting_gte', 'and_', 'cliff_time_nin', 'timed_weighting_lt', 'untimed_slot_in', 'cliff_amount_in', 'initial_minimum_balance_nin', 'cliff_time_exists', 'initial_minimum_balance_gt', 'initial_minimum_balance_lt', 'untimed_slot_ne', 'vesting_increment_exists', 'cliff_time', 'untimed_slot_nin', 'timed_in_epoch_ne', 'cliff_amount')
    untimed_slot_gt = sgqlc.types.Field(Int, graphql_name='untimed_slot_gt')
    initial_minimum_balance_lte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lte')
    untimed_slot_lte = sgqlc.types.Field(Int, graphql_name='untimed_slot_lte')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    untimed_slot_exists = sgqlc.types.Field(Boolean, graphql_name='untimed_slot_exists')
    vesting_increment_gt = sgqlc.types.Field(Float, graphql_name='vesting_increment_gt')
    timed_weighting_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='timed_weighting_in')
    cliff_amount_gt = sgqlc.types.Field(Float, graphql_name='cliff_amount_gt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeTimingQueryInput')), graphql_name='OR')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    vesting_period_gt = sgqlc.types.Field(Int, graphql_name='vesting_period_gt')
    timed_epoch_end_exists = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_exists')
    cliff_amount_ne = sgqlc.types.Field(Float, graphql_name='cliff_amount_ne')
    timed_weighting_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='timed_weighting_nin')
    cliff_time_gte = sgqlc.types.Field(Int, graphql_name='cliff_time_gte')
    vesting_increment_gte = sgqlc.types.Field(Float, graphql_name='vesting_increment_gte')
    cliff_amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_nin')
    cliff_time_ne = sgqlc.types.Field(Int, graphql_name='cliff_time_ne')
    cliff_time_lte = sgqlc.types.Field(Int, graphql_name='cliff_time_lte')
    vesting_period_lte = sgqlc.types.Field(Int, graphql_name='vesting_period_lte')
    cliff_time_lt = sgqlc.types.Field(Int, graphql_name='cliff_time_lt')
    vesting_increment_lte = sgqlc.types.Field(Float, graphql_name='vesting_increment_lte')
    cliff_amount_lt = sgqlc.types.Field(Float, graphql_name='cliff_amount_lt')
    initial_minimum_balance_exists = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_exists')
    cliff_time_gt = sgqlc.types.Field(Int, graphql_name='cliff_time_gt')
    vesting_period_gte = sgqlc.types.Field(Int, graphql_name='vesting_period_gte')
    timed_epoch_end_ne = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_ne')
    vesting_period_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_nin')
    vesting_period_lt = sgqlc.types.Field(Int, graphql_name='vesting_period_lt')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    timed_weighting_ne = sgqlc.types.Field(Float, graphql_name='timed_weighting_ne')
    initial_minimum_balance_gte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gte')
    untimed_slot_gte = sgqlc.types.Field(Int, graphql_name='untimed_slot_gte')
    initial_minimum_balance_ne = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_ne')
    vesting_increment_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_in')
    timed_weighting_gt = sgqlc.types.Field(Float, graphql_name='timed_weighting_gt')
    untimed_slot_lt = sgqlc.types.Field(Int, graphql_name='untimed_slot_lt')
    vesting_increment_ne = sgqlc.types.Field(Float, graphql_name='vesting_increment_ne')
    cliff_amount_gte = sgqlc.types.Field(Float, graphql_name='cliff_amount_gte')
    cliff_amount_lte = sgqlc.types.Field(Float, graphql_name='cliff_amount_lte')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    vesting_increment_lt = sgqlc.types.Field(Float, graphql_name='vesting_increment_lt')
    cliff_time_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_in')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    vesting_period_ne = sgqlc.types.Field(Int, graphql_name='vesting_period_ne')
    vesting_increment_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_nin')
    timed_weighting_exists = sgqlc.types.Field(Boolean, graphql_name='timed_weighting_exists')
    initial_minimum_balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_in')
    timed_in_epoch_exists = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_exists')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    cliff_amount_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_exists')
    vesting_period_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_period_exists')
    vesting_period_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_in')
    timed_weighting_lte = sgqlc.types.Field(Float, graphql_name='timed_weighting_lte')
    timed_weighting_gte = sgqlc.types.Field(Float, graphql_name='timed_weighting_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeTimingQueryInput')), graphql_name='AND')
    cliff_time_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_nin')
    timed_weighting_lt = sgqlc.types.Field(Float, graphql_name='timed_weighting_lt')
    untimed_slot_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='untimed_slot_in')
    cliff_amount_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_in')
    initial_minimum_balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_nin')
    cliff_time_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_time_exists')
    initial_minimum_balance_gt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gt')
    initial_minimum_balance_lt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lt')
    untimed_slot_ne = sgqlc.types.Field(Int, graphql_name='untimed_slot_ne')
    vesting_increment_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_exists')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    untimed_slot_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='untimed_slot_nin')
    timed_in_epoch_ne = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_ne')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')


class StakeTimingUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('vesting_increment_inc', 'timed_in_epoch_unset', 'cliff_amount', 'initial_minimum_balance_inc', 'vesting_period', 'cliff_time_inc', 'initial_minimum_balance', 'vesting_period_unset', 'untimed_slot_inc', 'untimed_slot', 'timed_weighting', 'vesting_increment_unset', 'cliff_amount_unset', 'timed_in_epoch', 'vesting_period_inc', 'initial_minimum_balance_unset', 'vesting_increment', 'untimed_slot_unset', 'timed_weighting_inc', 'timed_epoch_end', 'cliff_time_unset', 'timed_weighting_unset', 'timed_epoch_end_unset', 'cliff_amount_inc', 'cliff_time')
    vesting_increment_inc = sgqlc.types.Field(Float, graphql_name='vesting_increment_inc')
    timed_in_epoch_unset = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_unset')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    initial_minimum_balance_inc = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_inc')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    cliff_time_inc = sgqlc.types.Field(Int, graphql_name='cliff_time_inc')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    vesting_period_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_period_unset')
    untimed_slot_inc = sgqlc.types.Field(Int, graphql_name='untimed_slot_inc')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    vesting_increment_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_unset')
    cliff_amount_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_unset')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    vesting_period_inc = sgqlc.types.Field(Int, graphql_name='vesting_period_inc')
    initial_minimum_balance_unset = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_unset')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    untimed_slot_unset = sgqlc.types.Field(Boolean, graphql_name='untimed_slot_unset')
    timed_weighting_inc = sgqlc.types.Field(Float, graphql_name='timed_weighting_inc')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    cliff_time_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_time_unset')
    timed_weighting_unset = sgqlc.types.Field(Boolean, graphql_name='timed_weighting_unset')
    timed_epoch_end_unset = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_unset')
    cliff_amount_inc = sgqlc.types.Field(Float, graphql_name='cliff_amount_inc')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')


class StakeUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_inc', 'token', 'chain_id', 'token_unset', 'receipt_chain_hash', 'receipt_chain_hash_unset', 'public_key', 'voting_for', 'epoch', 'balance_unset', 'nonce', 'nonce_unset', 'voting_for_unset', 'delegate', 'public_key_unset', 'timing', 'chain_id_unset', 'ledger_hash', 'nonce_inc', 'permissions', 'balance', 'balance_inc', 'permissions_unset', 'timing_unset', 'ledger_hash_unset', 'delegate_unset', 'token_inc', 'epoch_unset')
    epoch_inc = sgqlc.types.Field(Int, graphql_name='epoch_inc')
    token = sgqlc.types.Field(Int, graphql_name='token')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    receipt_chain_hash_unset = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_unset')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    balance_unset = sgqlc.types.Field(Boolean, graphql_name='balance_unset')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    voting_for_unset = sgqlc.types.Field(Boolean, graphql_name='voting_for_unset')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='public_key_unset')
    timing = sgqlc.types.Field(StakeTimingUpdateInput, graphql_name='timing')
    chain_id_unset = sgqlc.types.Field(Boolean, graphql_name='chainId_unset')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    permissions = sgqlc.types.Field(StakePermissionUpdateInput, graphql_name='permissions')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    balance_inc = sgqlc.types.Field(Float, graphql_name='balance_inc')
    permissions_unset = sgqlc.types.Field(Boolean, graphql_name='permissions_unset')
    timing_unset = sgqlc.types.Field(Boolean, graphql_name='timing_unset')
    ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_unset')
    delegate_unset = sgqlc.types.Field(Boolean, graphql_name='delegate_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    epoch_unset = sgqlc.types.Field(Boolean, graphql_name='epoch_unset')


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
    __field_names__ = ('and_', 'token', 'token_gte', 'token_in', 'token_lt', 'token_lte', 'token_nin', 'or_', 'token_exists', 'token_ne', 'token_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFeePayerQueryInput')), graphql_name='AND')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFeePayerQueryInput')), graphql_name='OR')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')


class TransactionFeePayerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class TransactionFromAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionFromAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_in', 'token', 'token_lte', 'or_', 'token_lt', 'token_nin', 'token_exists', 'token_ne', 'token_gte', 'token_gt', 'and_')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFromAccountQueryInput')), graphql_name='OR')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFromAccountQueryInput')), graphql_name='AND')


class TransactionFromAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class TransactionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('failure_reason', 'source', 'fee_token', 'from_account', 'nonce', 'amount', 'is_delegation', 'to', 'kind', 'block_height', 'hash', 'memo', 'receiver', 'from_', 'date_time', 'id', 'to_account', 'fee_payer', 'block', 'canonical', 'fee', 'token')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    source = sgqlc.types.Field('TransactionSourceInsertInput', graphql_name='source')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    from_account = sgqlc.types.Field(TransactionFromAccountInsertInput, graphql_name='fromAccount')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    to = sgqlc.types.Field(String, graphql_name='to')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    receiver = sgqlc.types.Field('TransactionReceiverInsertInput', graphql_name='receiver')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    id = sgqlc.types.Field(String, graphql_name='id')
    to_account = sgqlc.types.Field('TransactionToAccountInsertInput', graphql_name='toAccount')
    fee_payer = sgqlc.types.Field(TransactionFeePayerInsertInput, graphql_name='feePayer')
    block = sgqlc.types.Field(TransactionBlockStateHashRelationInput, graphql_name='block')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_time_ne', 'memo_nin', 'hash_gt', 'token_ne', 'nonce', 'date_time_nin', 'memo', 'token_exists', 'kind_gt', 'amount_gt', 'canonical_exists', 'date_time_in', 'date_time_gt', 'date_time_lt', 'failure_reason_gte', 'fee_token_gte', 'fee_token_nin', 'failure_reason', 'fee_in', 'fee_token_lt', 'from_account', 'canonical_ne', 'to_account_exists', 'id', 'failure_reason_nin', 'fee_lt', 'date_time', 'memo_gt', 'token_gte', 'memo_lte', 'id_gte', 'token_lte', 'from_', 'fee_token_ne', 'id_ne', 'from_account_exists', 'failure_reason_in', 'fee_token', 'amount_gte', 'block_height_gte', 'token_gt', 'hash_ne', 'amount_ne', 'to_ne', 'kind_in', 'date_time_gte', 'hash_gte', 'to_gt', 'to_exists', 'block_exists', 'kind_gte', 'fee_payer', 'hash_lte', 'token_in', 'fee_gte', 'amount_lt', 'is_delegation_ne', 'block_height_gt', 'id_nin', 'source', 'nonce_lte', 'kind_ne', 'is_delegation_exists', 'kind_exists', 'from_exists', 'amount_lte', 'kind_nin', 'hash', 'block_height_in', 'id_lt', 'amount', 'fee_token_in', 'token_lt', 'or_', 'fee_nin', 'from_ne', 'id_exists', 'canonical', 'nonce_in', 'hash_nin', 'hash_exists', 'token_nin', 'id_gt', 'kind', 'fee_token_gt', 'amount_exists', 'from_in', 'id_in', 'nonce_gte', 'from_nin', 'fee_exists', 'amount_in', 'amount_nin', 'nonce_exists', 'memo_exists', 'block_height_nin', 'token', 'receiver', 'kind_lt', 'to_in', 'nonce_gt', 'memo_lt', 'fee', 'block_height_ne', 'to_lt', 'fee_ne', 'fee_token_lte', 'date_time_lte', 'fee_gt', 'nonce_nin', 'from_lte', 'block_height', 'fee_lte', 'fee_payer_exists', 'is_delegation', 'block_height_lt', 'receiver_exists', 'and_', 'to_nin', 'source_exists', 'failure_reason_exists', 'from_gte', 'failure_reason_lt', 'to_gte', 'block_height_lte', 'id_lte', 'to_account', 'from_lt', 'failure_reason_lte', 'fee_token_exists', 'failure_reason_ne', 'hash_in', 'block_height_exists', 'to', 'nonce_ne', 'to_lte', 'memo_in', 'from_gt', 'hash_lt', 'failure_reason_gt', 'block', 'date_time_exists', 'kind_lte', 'memo_gte', 'nonce_lt', 'memo_ne')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    memo_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_nin')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    kind_gt = sgqlc.types.Field(String, graphql_name='kind_gt')
    amount_gt = sgqlc.types.Field(Long, graphql_name='amount_gt')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    failure_reason_gte = sgqlc.types.Field(String, graphql_name='failureReason_gte')
    fee_token_gte = sgqlc.types.Field(Int, graphql_name='feeToken_gte')
    fee_token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_nin')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_in')
    fee_token_lt = sgqlc.types.Field(Int, graphql_name='feeToken_lt')
    from_account = sgqlc.types.Field(TransactionFromAccountQueryInput, graphql_name='fromAccount')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    to_account_exists = sgqlc.types.Field(Boolean, graphql_name='toAccount_exists')
    id = sgqlc.types.Field(String, graphql_name='id')
    failure_reason_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_nin')
    fee_lt = sgqlc.types.Field(Long, graphql_name='fee_lt')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    memo_gt = sgqlc.types.Field(String, graphql_name='memo_gt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    memo_lte = sgqlc.types.Field(String, graphql_name='memo_lte')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    fee_token_ne = sgqlc.types.Field(Int, graphql_name='feeToken_ne')
    id_ne = sgqlc.types.Field(String, graphql_name='id_ne')
    from_account_exists = sgqlc.types.Field(Boolean, graphql_name='fromAccount_exists')
    failure_reason_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_in')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    amount_gte = sgqlc.types.Field(Long, graphql_name='amount_gte')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    amount_ne = sgqlc.types.Field(Long, graphql_name='amount_ne')
    to_ne = sgqlc.types.Field(String, graphql_name='to_ne')
    kind_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_in')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_exists = sgqlc.types.Field(Boolean, graphql_name='to_exists')
    block_exists = sgqlc.types.Field(Boolean, graphql_name='block_exists')
    kind_gte = sgqlc.types.Field(String, graphql_name='kind_gte')
    fee_payer = sgqlc.types.Field(TransactionFeePayerQueryInput, graphql_name='feePayer')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    fee_gte = sgqlc.types.Field(Long, graphql_name='fee_gte')
    amount_lt = sgqlc.types.Field(Long, graphql_name='amount_lt')
    is_delegation_ne = sgqlc.types.Field(Boolean, graphql_name='isDelegation_ne')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_nin')
    source = sgqlc.types.Field('TransactionSourceQueryInput', graphql_name='source')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    kind_ne = sgqlc.types.Field(String, graphql_name='kind_ne')
    is_delegation_exists = sgqlc.types.Field(Boolean, graphql_name='isDelegation_exists')
    kind_exists = sgqlc.types.Field(Boolean, graphql_name='kind_exists')
    from_exists = sgqlc.types.Field(Boolean, graphql_name='from_exists')
    amount_lte = sgqlc.types.Field(Long, graphql_name='amount_lte')
    kind_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_nin')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    fee_token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_in')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionQueryInput')), graphql_name='OR')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_nin')
    from_ne = sgqlc.types.Field(String, graphql_name='from_ne')
    id_exists = sgqlc.types.Field(Boolean, graphql_name='id_exists')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    fee_token_gt = sgqlc.types.Field(Int, graphql_name='feeToken_gt')
    amount_exists = sgqlc.types.Field(Boolean, graphql_name='amount_exists')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_in')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_in')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    from_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_nin')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='amount_in')
    amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='amount_nin')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    memo_exists = sgqlc.types.Field(Boolean, graphql_name='memo_exists')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    token = sgqlc.types.Field(Int, graphql_name='token')
    receiver = sgqlc.types.Field('TransactionReceiverQueryInput', graphql_name='receiver')
    kind_lt = sgqlc.types.Field(String, graphql_name='kind_lt')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_in')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    memo_lt = sgqlc.types.Field(String, graphql_name='memo_lt')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    fee_ne = sgqlc.types.Field(Long, graphql_name='fee_ne')
    fee_token_lte = sgqlc.types.Field(Int, graphql_name='feeToken_lte')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    fee_gt = sgqlc.types.Field(Long, graphql_name='fee_gt')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    fee_lte = sgqlc.types.Field(Long, graphql_name='fee_lte')
    fee_payer_exists = sgqlc.types.Field(Boolean, graphql_name='feePayer_exists')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    receiver_exists = sgqlc.types.Field(Boolean, graphql_name='receiver_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionQueryInput')), graphql_name='AND')
    to_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_nin')
    source_exists = sgqlc.types.Field(Boolean, graphql_name='source_exists')
    failure_reason_exists = sgqlc.types.Field(Boolean, graphql_name='failureReason_exists')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    failure_reason_lt = sgqlc.types.Field(String, graphql_name='failureReason_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    to_account = sgqlc.types.Field('TransactionToAccountQueryInput', graphql_name='toAccount')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    failure_reason_lte = sgqlc.types.Field(String, graphql_name='failureReason_lte')
    fee_token_exists = sgqlc.types.Field(Boolean, graphql_name='feeToken_exists')
    failure_reason_ne = sgqlc.types.Field(String, graphql_name='failureReason_ne')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    to = sgqlc.types.Field(String, graphql_name='to')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    memo_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_in')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    failure_reason_gt = sgqlc.types.Field(String, graphql_name='failureReason_gt')
    block = sgqlc.types.Field(BlockQueryInput, graphql_name='block')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    kind_lte = sgqlc.types.Field(String, graphql_name='kind_lte')
    memo_gte = sgqlc.types.Field(String, graphql_name='memo_gte')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    memo_ne = sgqlc.types.Field(String, graphql_name='memo_ne')


class TransactionReceiverInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionReceiverQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_lt', 'public_key', 'public_key_gte', 'public_key_exists', 'or_', 'public_key_gt', 'public_key_lte', 'public_key_nin', 'public_key_ne', 'and_', 'public_key_in')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionReceiverQueryInput')), graphql_name='OR')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionReceiverQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')


class TransactionReceiverUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_unset', 'public_key')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionSourceInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionSourceQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_nin', 'public_key_lt', 'public_key_exists', 'public_key_gt', 'and_', 'public_key_in', 'or_', 'public_key', 'public_key_gte', 'public_key_lte', 'public_key_ne')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionSourceQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionSourceQueryInput')), graphql_name='OR')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')


class TransactionSourceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_unset', 'public_key')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionToAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class TransactionToAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gte', 'token_in', 'or_', 'token_lte', 'token_gt', 'token_ne', 'token', 'token_exists', 'token_lt', 'and_', 'token_nin')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionToAccountQueryInput')), graphql_name='OR')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionToAccountQueryInput')), graphql_name='AND')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')


class TransactionToAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'token', 'token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')


class TransactionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('source', 'token_unset', 'token_inc', 'fee_unset', 'from_unset', 'block_height_inc', 'nonce', 'date_time_unset', 'fee_token', 'amount', 'fee_payer', 'from_', 'fee_payer_unset', 'block_height_unset', 'block', 'memo_unset', 'token', 'nonce_unset', 'block_unset', 'canonical_unset', 'from_account', 'from_account_unset', 'fee', 'failure_reason', 'kind', 'fee_token_inc', 'canonical', 'failure_reason_unset', 'hash_unset', 'to_account', 'is_delegation', 'to_account_unset', 'amount_unset', 'fee_token_unset', 'is_delegation_unset', 'receiver', 'nonce_inc', 'block_height', 'receiver_unset', 'kind_unset', 'to_unset', 'memo', 'to', 'hash', 'date_time', 'id', 'id_unset', 'source_unset')
    source = sgqlc.types.Field(TransactionSourceUpdateInput, graphql_name='source')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    from_unset = sgqlc.types.Field(Boolean, graphql_name='from_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    fee_payer = sgqlc.types.Field(TransactionFeePayerUpdateInput, graphql_name='feePayer')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    fee_payer_unset = sgqlc.types.Field(Boolean, graphql_name='feePayer_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    block = sgqlc.types.Field(TransactionBlockStateHashRelationInput, graphql_name='block')
    memo_unset = sgqlc.types.Field(Boolean, graphql_name='memo_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    block_unset = sgqlc.types.Field(Boolean, graphql_name='block_unset')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    from_account = sgqlc.types.Field(TransactionFromAccountUpdateInput, graphql_name='fromAccount')
    from_account_unset = sgqlc.types.Field(Boolean, graphql_name='fromAccount_unset')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    fee_token_inc = sgqlc.types.Field(Int, graphql_name='feeToken_inc')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    failure_reason_unset = sgqlc.types.Field(Boolean, graphql_name='failureReason_unset')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    to_account = sgqlc.types.Field(TransactionToAccountUpdateInput, graphql_name='toAccount')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    to_account_unset = sgqlc.types.Field(Boolean, graphql_name='toAccount_unset')
    amount_unset = sgqlc.types.Field(Boolean, graphql_name='amount_unset')
    fee_token_unset = sgqlc.types.Field(Boolean, graphql_name='feeToken_unset')
    is_delegation_unset = sgqlc.types.Field(Boolean, graphql_name='isDelegation_unset')
    receiver = sgqlc.types.Field(TransactionReceiverUpdateInput, graphql_name='receiver')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    receiver_unset = sgqlc.types.Field(Boolean, graphql_name='receiver_unset')
    kind_unset = sgqlc.types.Field(Boolean, graphql_name='kind_unset')
    to_unset = sgqlc.types.Field(Boolean, graphql_name='to_unset')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    to = sgqlc.types.Field(String, graphql_name='to')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    id = sgqlc.types.Field(String, graphql_name='id')
    id_unset = sgqlc.types.Field(Boolean, graphql_name='id_unset')
    source_unset = sgqlc.types.Field(Boolean, graphql_name='source_unset')



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
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')


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
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
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
    __field_names__ = ('delete_many_blocks', 'delete_many_snarks', 'delete_many_stakes', 'delete_many_transactions', 'delete_one_block', 'delete_one_snark', 'delete_one_stake', 'delete_one_transaction', 'insert_many_blocks', 'insert_many_snarks', 'insert_many_stakes', 'insert_many_transactions', 'insert_one_block', 'insert_one_snark', 'insert_one_stake', 'insert_one_transaction', 'replace_one_block', 'replace_one_snark', 'replace_one_stake', 'replace_one_transaction', 'update_many_blocks', 'update_many_snarks', 'update_many_stakes', 'update_many_transactions', 'update_one_block', 'update_one_snark', 'update_one_stake', 'update_one_transaction', 'upsert_one_block', 'upsert_one_snark', 'upsert_one_stake', 'upsert_one_transaction')
    delete_many_blocks = sgqlc.types.Field(DeleteManyPayload, graphql_name='deleteManyBlocks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
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
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(BlockUpdateInput), graphql_name='set', default=None)),
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
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
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(TransactionUpdateInput), graphql_name='set', default=None)),
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
))
    )
    upsert_one_block = sgqlc.types.Field(Block, graphql_name='upsertOneBlock', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(BlockInsertInput), graphql_name='data', default=None)),
))
    )
    upsert_one_snark = sgqlc.types.Field('Snark', graphql_name='upsertOneSnark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(SnarkInsertInput), graphql_name='data', default=None)),
))
    )
    upsert_one_stake = sgqlc.types.Field('Stake', graphql_name='upsertOneStake', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(StakeQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(StakeInsertInput), graphql_name='data', default=None)),
))
    )
    upsert_one_transaction = sgqlc.types.Field('Transaction', graphql_name='upsertOneTransaction', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(TransactionInsertInput), graphql_name='data', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block', 'blocks', 'snark', 'snarks', 'stake', 'stakes', 'transaction', 'transactions')
    block = sgqlc.types.Field(Block, graphql_name='block', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
))
    )
    blocks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Block)), graphql_name='blocks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
        ('sort_by', sgqlc.types.Arg(BlockSortByInput, graphql_name='sortBy', default=None)),
))
    )
    snark = sgqlc.types.Field('Snark', graphql_name='snark', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
))
    )
    snarks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Snark')), graphql_name='snarks', args=sgqlc.types.ArgDict((
        ('sort_by', sgqlc.types.Arg(SnarkSortByInput, graphql_name='sortBy', default=None)),
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=100)),
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
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')


class Stake(sgqlc.types.Type):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance', 'chain_id', 'delegate', 'delegation_totals', 'epoch', 'ledger_hash', 'nonce', 'permissions', 'public_key', 'receipt_chain_hash', 'timing', 'token', 'voting_for')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    delegation_totals = sgqlc.types.Field(DelegationTotal, graphql_name='delegationTotals')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('StakePermission', graphql_name='permissions')
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
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    block = sgqlc.types.Field(Block, graphql_name='block')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
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

