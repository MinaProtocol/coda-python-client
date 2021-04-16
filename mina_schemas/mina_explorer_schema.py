import sgqlc.types
import sgqlc.types.datetime


mina_explorer_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class BlockSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('DATETIME_DESC', 'STATEHASH_ASC', 'RECEIVEDTIME_DESC', 'CREATOR_ASC', 'CREATOR_DESC', 'STATEHASHFIELD_ASC', 'DATETIME_ASC', 'STATEHASH_DESC', 'RECEIVEDTIME_ASC', 'BLOCKHEIGHT_ASC', 'BLOCKHEIGHT_DESC', 'STATEHASHFIELD_DESC')


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
    __choices__ = ('PROVER_ASC', 'PROVER_DESC', 'BLOCKHEIGHT_ASC', 'BLOCKSTATEHASH_DESC', 'DATETIME_ASC', 'DATETIME_DESC', 'FEE_DESC', 'BLOCKHEIGHT_DESC', 'BLOCKSTATEHASH_ASC', 'FEE_ASC')


class StakeSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('NONCE_ASC', 'PK_ASC', 'PK_DESC', 'RECEIPT_CHAIN_HASH_ASC', 'RECEIPT_CHAIN_HASH_DESC', 'EPOCH_ASC', 'EPOCH_DESC', 'PUBLIC_KEY_ASC', 'BALANCE_ASC', 'BALANCE_DESC', 'TOKEN_ASC', 'CHAINID_ASC', 'CHAINID_DESC', 'PUBLIC_KEY_DESC', 'NONCE_DESC', 'LEDGERHASH_ASC', 'VOTING_FOR_ASC', 'VOTING_FOR_DESC', 'DELEGATE_DESC', 'TOKEN_DESC', 'LEDGERHASH_DESC', 'DELEGATE_ASC')


String = sgqlc.types.String

class TransactionSortByInput(sgqlc.types.Enum):
    __schema__ = mina_explorer_schema
    __choices__ = ('BLOCKSTATEHASH_ASC', 'NONCE_ASC', 'TO_DESC', 'BLOCKHEIGHT_DESC', 'DATETIME_ASC', 'FEE_DESC', 'FEETOKEN_ASC', 'KIND_DESC', 'AMOUNT_ASC', 'HASH_ASC', 'DATETIME_DESC', 'FROM_DESC', 'ID_DESC', 'MEMO_ASC', 'BLOCKSTATEHASH_DESC', 'FAILUREREASON_DESC', 'FEETOKEN_DESC', 'FEE_ASC', 'HASH_DESC', 'TOKEN_ASC', 'TOKEN_DESC', 'FAILUREREASON_ASC', 'TO_ASC', 'BLOCKHEIGHT_ASC', 'NONCE_DESC', 'ID_ASC', 'FROM_ASC', 'MEMO_DESC', 'KIND_ASC', 'AMOUNT_DESC')



########################################################################
# Input Objects
########################################################################
class BlockCreatorAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockCreatorAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_gt', 'public_key_lte', 'public_key_exists', 'public_key_nin', 'and_', 'public_key_in', 'or_', 'public_key_ne', 'public_key_lt', 'public_key_gte')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockCreatorAccountQueryInput')), graphql_name='AND')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockCreatorAccountQueryInput')), graphql_name='OR')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')


class BlockCreatorAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'public_key_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')


class BlockInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('received_time', 'state_hash', 'block_height', 'state_hash_field', 'snark_jobs', 'creator', 'date_time', 'canonical', 'creator_account', 'transactions', 'winner_account', 'protocol_state')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobInsertInput'), graphql_name='snarkJobs')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    creator_account = sgqlc.types.Field(BlockCreatorAccountInsertInput, graphql_name='creatorAccount')
    transactions = sgqlc.types.Field('BlockTransactionInsertInput', graphql_name='transactions')
    winner_account = sgqlc.types.Field('BlockWinnerAccountInsertInput', graphql_name='winnerAccount')
    protocol_state = sgqlc.types.Field('BlockProtocolStateInsertInput', graphql_name='protocolState')


class BlockProtocolStateBlockchainStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date', 'snarked_ledger_hash', 'staged_ledger_hash', 'utc_date')
    date = sgqlc.types.Field(Long, graphql_name='date')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')


class BlockProtocolStateBlockchainStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('staged_ledger_hash_lte', 'snarked_ledger_hash_nin', 'staged_ledger_hash_exists', 'date_exists', 'utc_date_in', 'and_', 'date_in', 'staged_ledger_hash_ne', 'date', 'staged_ledger_hash_in', 'staged_ledger_hash_gte', 'snarked_ledger_hash_lt', 'date_lte', 'snarked_ledger_hash_exists', 'date_lt', 'utc_date_lte', 'snarked_ledger_hash_gte', 'date_nin', 'utc_date', 'utc_date_gte', 'snarked_ledger_hash_lte', 'staged_ledger_hash_lt', 'or_', 'date_gt', 'snarked_ledger_hash_in', 'date_ne', 'staged_ledger_hash_nin', 'snarked_ledger_hash_ne', 'staged_ledger_hash', 'snarked_ledger_hash_gt', 'utc_date_ne', 'snarked_ledger_hash', 'utc_date_lt', 'utc_date_exists', 'date_gte', 'staged_ledger_hash_gt', 'utc_date_nin', 'utc_date_gt')
    staged_ledger_hash_lte = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_lte')
    snarked_ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snarkedLedgerHash_nin')
    staged_ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stagedLedgerHash_exists')
    date_exists = sgqlc.types.Field(Boolean, graphql_name='date_exists')
    utc_date_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='utcDate_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateBlockchainStateQueryInput')), graphql_name='AND')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='date_in')
    staged_ledger_hash_ne = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_ne')
    date = sgqlc.types.Field(Long, graphql_name='date')
    staged_ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagedLedgerHash_in')
    staged_ledger_hash_gte = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_gte')
    snarked_ledger_hash_lt = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_lt')
    date_lte = sgqlc.types.Field(Long, graphql_name='date_lte')
    snarked_ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='snarkedLedgerHash_exists')
    date_lt = sgqlc.types.Field(Long, graphql_name='date_lt')
    utc_date_lte = sgqlc.types.Field(Long, graphql_name='utcDate_lte')
    snarked_ledger_hash_gte = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_gte')
    date_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='date_nin')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')
    utc_date_gte = sgqlc.types.Field(Long, graphql_name='utcDate_gte')
    snarked_ledger_hash_lte = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_lte')
    staged_ledger_hash_lt = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateBlockchainStateQueryInput')), graphql_name='OR')
    date_gt = sgqlc.types.Field(Long, graphql_name='date_gt')
    snarked_ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='snarkedLedgerHash_in')
    date_ne = sgqlc.types.Field(Long, graphql_name='date_ne')
    staged_ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stagedLedgerHash_nin')
    snarked_ledger_hash_ne = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_ne')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    snarked_ledger_hash_gt = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash_gt')
    utc_date_ne = sgqlc.types.Field(Long, graphql_name='utcDate_ne')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    utc_date_lt = sgqlc.types.Field(Long, graphql_name='utcDate_lt')
    utc_date_exists = sgqlc.types.Field(Boolean, graphql_name='utcDate_exists')
    date_gte = sgqlc.types.Field(Long, graphql_name='date_gte')
    staged_ledger_hash_gt = sgqlc.types.Field(String, graphql_name='stagedLedgerHash_gt')
    utc_date_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='utcDate_nin')
    utc_date_gt = sgqlc.types.Field(Long, graphql_name='utcDate_gt')


class BlockProtocolStateBlockchainStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('utc_date', 'utc_date_unset', 'date', 'date_unset', 'snarked_ledger_hash', 'snarked_ledger_hash_unset', 'staged_ledger_hash', 'staged_ledger_hash_unset')
    utc_date = sgqlc.types.Field(Long, graphql_name='utcDate')
    utc_date_unset = sgqlc.types.Field(Boolean, graphql_name='utcDate_unset')
    date = sgqlc.types.Field(Long, graphql_name='date')
    date_unset = sgqlc.types.Field(Boolean, graphql_name='date_unset')
    snarked_ledger_hash = sgqlc.types.Field(String, graphql_name='snarkedLedgerHash')
    snarked_ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='snarkedLedgerHash_unset')
    staged_ledger_hash = sgqlc.types.Field(String, graphql_name='stagedLedgerHash')
    staged_ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stagedLedgerHash_unset')


class BlockProtocolStateConsensusStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('last_vrf_output', 'slot_since_genesis', 'total_currency', 'next_epoch_data', 'min_window_density', 'epoch_count', 'slot', 'has_ancestor_in_same_checkpoint_window', 'staking_epoch_data', 'block_height', 'blockchain_length', 'epoch')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    next_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumInsertInput', graphql_name='nextEpochData')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumInsertInput', graphql_name='stakingEpochData')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')


class BlockProtocolStateConsensusStateNextEpochDatumInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('lock_checkpoint', 'seed', 'start_checkpoint', 'epoch_length', 'ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    ledger = sgqlc.types.Field('BlockProtocolStateConsensusStateNextEpochDatumLedgerInsertInput', graphql_name='ledger')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash', 'total_currency')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash_ne', 'total_currency_in', 'hash_lte', 'hash_gte', 'total_currency_gt', 'hash_nin', 'hash_lt', 'total_currency_exists', 'total_currency_nin', 'total_currency_lte', 'total_currency', 'hash_exists', 'hash_gt', 'hash_in', 'total_currency_ne', 'or_', 'hash', 'total_currency_gte', 'total_currency_lt', 'and_')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='totalCurrency_in')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    total_currency_gt = sgqlc.types.Field(Long, graphql_name='totalCurrency_gt')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='totalCurrency_nin')
    total_currency_lte = sgqlc.types.Field(Long, graphql_name='totalCurrency_lte')
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    total_currency_ne = sgqlc.types.Field(Long, graphql_name='totalCurrency_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput')), graphql_name='OR')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    total_currency_gte = sgqlc.types.Field(Long, graphql_name='totalCurrency_gte')
    total_currency_lt = sgqlc.types.Field(Long, graphql_name='totalCurrency_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput')), graphql_name='AND')


class BlockProtocolStateConsensusStateNextEpochDatumLedgerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash_unset', 'total_currency', 'total_currency_unset', 'hash')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    total_currency = sgqlc.types.Field(Long, graphql_name='totalCurrency')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')


class BlockProtocolStateConsensusStateNextEpochDatumQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('and_', 'epoch_length_gte', 'start_checkpoint', 'epoch_length_lte', 'lock_checkpoint_lte', 'start_checkpoint_gt', 'start_checkpoint_nin', 'seed_lt', 'epoch_length_nin', 'seed_nin', 'seed_exists', 'seed_ne', 'epoch_length_ne', 'ledger', 'seed_gte', 'lock_checkpoint_lt', 'epoch_length_gt', 'lock_checkpoint_ne', 'seed_gt', 'lock_checkpoint_gt', 'lock_checkpoint', 'start_checkpoint_exists', 'start_checkpoint_ne', 'seed_lte', 'start_checkpoint_in', 'epoch_length_lt', 'epoch_length_in', 'seed', 'start_checkpoint_lte', 'lock_checkpoint_in', 'ledger_exists', 'lock_checkpoint_nin', 'lock_checkpoint_exists', 'seed_in', 'or_', 'start_checkpoint_lt', 'epoch_length', 'epoch_length_exists', 'lock_checkpoint_gte', 'start_checkpoint_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumQueryInput')), graphql_name='AND')
    epoch_length_gte = sgqlc.types.Field(Int, graphql_name='epochLength_gte')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    epoch_length_lte = sgqlc.types.Field(Int, graphql_name='epochLength_lte')
    lock_checkpoint_lte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lte')
    start_checkpoint_gt = sgqlc.types.Field(String, graphql_name='startCheckpoint_gt')
    start_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_nin')
    seed_lt = sgqlc.types.Field(String, graphql_name='seed_lt')
    epoch_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_nin')
    seed_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_nin')
    seed_exists = sgqlc.types.Field(Boolean, graphql_name='seed_exists')
    seed_ne = sgqlc.types.Field(String, graphql_name='seed_ne')
    epoch_length_ne = sgqlc.types.Field(Int, graphql_name='epochLength_ne')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumLedgerQueryInput, graphql_name='ledger')
    seed_gte = sgqlc.types.Field(String, graphql_name='seed_gte')
    lock_checkpoint_lt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lt')
    epoch_length_gt = sgqlc.types.Field(Int, graphql_name='epochLength_gt')
    lock_checkpoint_ne = sgqlc.types.Field(String, graphql_name='lockCheckpoint_ne')
    seed_gt = sgqlc.types.Field(String, graphql_name='seed_gt')
    lock_checkpoint_gt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gt')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    start_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_exists')
    start_checkpoint_ne = sgqlc.types.Field(String, graphql_name='startCheckpoint_ne')
    seed_lte = sgqlc.types.Field(String, graphql_name='seed_lte')
    start_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_in')
    epoch_length_lt = sgqlc.types.Field(Int, graphql_name='epochLength_lt')
    epoch_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_in')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint_lte = sgqlc.types.Field(String, graphql_name='startCheckpoint_lte')
    lock_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_in')
    ledger_exists = sgqlc.types.Field(Boolean, graphql_name='ledger_exists')
    lock_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_nin')
    lock_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_exists')
    seed_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateNextEpochDatumQueryInput')), graphql_name='OR')
    start_checkpoint_lt = sgqlc.types.Field(String, graphql_name='startCheckpoint_lt')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    epoch_length_exists = sgqlc.types.Field(Boolean, graphql_name='epochLength_exists')
    lock_checkpoint_gte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gte')
    start_checkpoint_gte = sgqlc.types.Field(String, graphql_name='startCheckpoint_gte')


class BlockProtocolStateConsensusStateNextEpochDatumUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('ledger', 'lock_checkpoint', 'lock_checkpoint_unset', 'epoch_length_inc', 'epoch_length_unset', 'seed_unset', 'seed', 'epoch_length', 'start_checkpoint_unset', 'ledger_unset', 'start_checkpoint')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumLedgerUpdateInput, graphql_name='ledger')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    lock_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_unset')
    epoch_length_inc = sgqlc.types.Field(Int, graphql_name='epochLength_inc')
    epoch_length_unset = sgqlc.types.Field(Boolean, graphql_name='epochLength_unset')
    seed_unset = sgqlc.types.Field(Boolean, graphql_name='seed_unset')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    start_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_unset')
    ledger_unset = sgqlc.types.Field(Boolean, graphql_name='ledger_unset')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')


class BlockProtocolStateConsensusStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height_lte', 'total_currency_nin', 'slot_since_genesis_lte', 'slot_in', 'slot_ne', 'blockchain_length_exists', 'slot', 'slot_since_genesis_nin', 'slot_since_genesis_lt', 'blockchain_length_in', 'has_ancestor_in_same_checkpoint_window_ne', 'epoch_count_gte', 'or_', 'total_currency_in', 'last_vrf_output_lte', 'slot_exists', 'slot_nin', 'epoch_count_ne', 'last_vrf_output_gte', 'block_height_in', 'block_height_lt', 'last_vrf_output_exists', 'last_vrf_output_in', 'staking_epoch_data_exists', 'total_currency', 'slot_lte', 'total_currency_ne', 'epoch_count_nin', 'block_height_nin', 'last_vrf_output_ne', 'min_window_density_lt', 'epoch_lt', 'blockchain_length_lte', 'epoch_in', 'epoch_count_in', 'slot_since_genesis_exists', 'slot_gte', 'blockchain_length', 'epoch_ne', 'min_window_density', 'blockchain_length_nin', 'epoch_nin', 'block_height_exists', 'blockchain_length_ne', 'epoch_count_exists', 'epoch_count', 'slot_since_genesis_ne', 'staking_epoch_data', 'last_vrf_output_lt', 'slot_gt', 'min_window_density_in', 'min_window_density_exists', 'slot_since_genesis', 'slot_since_genesis_in', 'epoch_lte', 'min_window_density_gt', 'epoch_exists', 'block_height', 'block_height_gte', 'epoch_gte', 'epoch_gt', 'next_epoch_data_exists', 'block_height_gt', 'min_window_density_gte', 'has_ancestor_in_same_checkpoint_window_exists', 'slot_lt', 'last_vrf_output_nin', 'next_epoch_data', 'epoch', 'last_vrf_output_gt', 'epoch_count_lte', 'has_ancestor_in_same_checkpoint_window', 'total_currency_gte', 'slot_since_genesis_gte', 'epoch_count_lt', 'total_currency_exists', 'total_currency_lt', 'and_', 'slot_since_genesis_gt', 'blockchain_length_lt', 'block_height_ne', 'blockchain_length_gte', 'min_window_density_ne', 'min_window_density_nin', 'total_currency_lte', 'last_vrf_output', 'epoch_count_gt', 'blockchain_length_gt', 'min_window_density_lte', 'total_currency_gt')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    slot_since_genesis_lte = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_lte')
    slot_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slot_in')
    slot_ne = sgqlc.types.Field(Int, graphql_name='slot_ne')
    blockchain_length_exists = sgqlc.types.Field(Boolean, graphql_name='blockchainLength_exists')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    slot_since_genesis_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slotSinceGenesis_nin')
    slot_since_genesis_lt = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_lt')
    blockchain_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockchainLength_in')
    has_ancestor_in_same_checkpoint_window_ne = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_ne')
    epoch_count_gte = sgqlc.types.Field(Int, graphql_name='epochCount_gte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateQueryInput')), graphql_name='OR')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    last_vrf_output_lte = sgqlc.types.Field(String, graphql_name='lastVrfOutput_lte')
    slot_exists = sgqlc.types.Field(Boolean, graphql_name='slot_exists')
    slot_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slot_nin')
    epoch_count_ne = sgqlc.types.Field(Int, graphql_name='epochCount_ne')
    last_vrf_output_gte = sgqlc.types.Field(String, graphql_name='lastVrfOutput_gte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    last_vrf_output_exists = sgqlc.types.Field(Boolean, graphql_name='lastVrfOutput_exists')
    last_vrf_output_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastVrfOutput_in')
    staking_epoch_data_exists = sgqlc.types.Field(Boolean, graphql_name='stakingEpochData_exists')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    slot_lte = sgqlc.types.Field(Int, graphql_name='slot_lte')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    epoch_count_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochCount_nin')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    last_vrf_output_ne = sgqlc.types.Field(String, graphql_name='lastVrfOutput_ne')
    min_window_density_lt = sgqlc.types.Field(Int, graphql_name='minWindowDensity_lt')
    epoch_lt = sgqlc.types.Field(Int, graphql_name='epoch_lt')
    blockchain_length_lte = sgqlc.types.Field(Int, graphql_name='blockchainLength_lte')
    epoch_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_in')
    epoch_count_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochCount_in')
    slot_since_genesis_exists = sgqlc.types.Field(Boolean, graphql_name='slotSinceGenesis_exists')
    slot_gte = sgqlc.types.Field(Int, graphql_name='slot_gte')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    epoch_ne = sgqlc.types.Field(Int, graphql_name='epoch_ne')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    blockchain_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockchainLength_nin')
    epoch_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_nin')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    blockchain_length_ne = sgqlc.types.Field(Int, graphql_name='blockchainLength_ne')
    epoch_count_exists = sgqlc.types.Field(Boolean, graphql_name='epochCount_exists')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    slot_since_genesis_ne = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_ne')
    staking_epoch_data = sgqlc.types.Field('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput', graphql_name='stakingEpochData')
    last_vrf_output_lt = sgqlc.types.Field(String, graphql_name='lastVrfOutput_lt')
    slot_gt = sgqlc.types.Field(Int, graphql_name='slot_gt')
    min_window_density_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minWindowDensity_in')
    min_window_density_exists = sgqlc.types.Field(Boolean, graphql_name='minWindowDensity_exists')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    slot_since_genesis_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='slotSinceGenesis_in')
    epoch_lte = sgqlc.types.Field(Int, graphql_name='epoch_lte')
    min_window_density_gt = sgqlc.types.Field(Int, graphql_name='minWindowDensity_gt')
    epoch_exists = sgqlc.types.Field(Boolean, graphql_name='epoch_exists')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    epoch_gte = sgqlc.types.Field(Int, graphql_name='epoch_gte')
    epoch_gt = sgqlc.types.Field(Int, graphql_name='epoch_gt')
    next_epoch_data_exists = sgqlc.types.Field(Boolean, graphql_name='nextEpochData_exists')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    min_window_density_gte = sgqlc.types.Field(Int, graphql_name='minWindowDensity_gte')
    has_ancestor_in_same_checkpoint_window_exists = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_exists')
    slot_lt = sgqlc.types.Field(Int, graphql_name='slot_lt')
    last_vrf_output_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lastVrfOutput_nin')
    next_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumQueryInput, graphql_name='nextEpochData')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    last_vrf_output_gt = sgqlc.types.Field(String, graphql_name='lastVrfOutput_gt')
    epoch_count_lte = sgqlc.types.Field(Int, graphql_name='epochCount_lte')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    slot_since_genesis_gte = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_gte')
    epoch_count_lt = sgqlc.types.Field(Int, graphql_name='epochCount_lt')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateQueryInput')), graphql_name='AND')
    slot_since_genesis_gt = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_gt')
    blockchain_length_lt = sgqlc.types.Field(Int, graphql_name='blockchainLength_lt')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    blockchain_length_gte = sgqlc.types.Field(Int, graphql_name='blockchainLength_gte')
    min_window_density_ne = sgqlc.types.Field(Int, graphql_name='minWindowDensity_ne')
    min_window_density_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='minWindowDensity_nin')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    epoch_count_gt = sgqlc.types.Field(Int, graphql_name='epochCount_gt')
    blockchain_length_gt = sgqlc.types.Field(Int, graphql_name='blockchainLength_gt')
    min_window_density_lte = sgqlc.types.Field(Int, graphql_name='minWindowDensity_lte')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')


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
    __field_names__ = ('total_currency', 'hash')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    hash = sgqlc.types.Field(String, graphql_name='hash')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('hash_exists', 'total_currency_gt', 'total_currency_nin', 'total_currency_in', 'total_currency_ne', 'and_', 'total_currency_gte', 'hash_lt', 'hash_nin', 'hash_gt', 'hash_ne', 'total_currency_exists', 'total_currency_lte', 'hash_gte', 'total_currency', 'total_currency_lt', 'hash', 'hash_lte', 'or_', 'hash_in')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    total_currency_gt = sgqlc.types.Field(Float, graphql_name='totalCurrency_gt')
    total_currency_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_nin')
    total_currency_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='totalCurrency_in')
    total_currency_ne = sgqlc.types.Field(Float, graphql_name='totalCurrency_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput')), graphql_name='AND')
    total_currency_gte = sgqlc.types.Field(Float, graphql_name='totalCurrency_gte')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    total_currency_exists = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_exists')
    total_currency_lte = sgqlc.types.Field(Float, graphql_name='totalCurrency_lte')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_lt = sgqlc.types.Field(Float, graphql_name='totalCurrency_lt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput')), graphql_name='OR')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')


class BlockProtocolStateConsensusStateStakingEpochDatumLedgerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('total_currency_unset', 'hash', 'hash_unset', 'total_currency', 'total_currency_inc')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')


class BlockProtocolStateConsensusStateStakingEpochDatumQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length_lt', 'epoch_length', 'seed_in', 'start_checkpoint_gte', 'start_checkpoint_exists', 'ledger', 'lock_checkpoint_lte', 'epoch_length_in', 'start_checkpoint_lt', 'or_', 'seed_gte', 'seed_lt', 'lock_checkpoint_gt', 'seed_ne', 'seed', 'lock_checkpoint_nin', 'seed_exists', 'ledger_exists', 'start_checkpoint_in', 'lock_checkpoint_in', 'lock_checkpoint_gte', 'seed_nin', 'lock_checkpoint_lt', 'lock_checkpoint_exists', 'start_checkpoint_ne', 'seed_gt', 'start_checkpoint_gt', 'seed_lte', 'start_checkpoint_lte', 'start_checkpoint_nin', 'start_checkpoint', 'lock_checkpoint', 'epoch_length_gte', 'lock_checkpoint_ne', 'epoch_length_lte', 'epoch_length_nin', 'epoch_length_ne', 'epoch_length_gt', 'epoch_length_exists', 'and_')
    epoch_length_lt = sgqlc.types.Field(Int, graphql_name='epochLength_lt')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    seed_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_in')
    start_checkpoint_gte = sgqlc.types.Field(String, graphql_name='startCheckpoint_gte')
    start_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_exists')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumLedgerQueryInput, graphql_name='ledger')
    lock_checkpoint_lte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lte')
    epoch_length_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_in')
    start_checkpoint_lt = sgqlc.types.Field(String, graphql_name='startCheckpoint_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput')), graphql_name='OR')
    seed_gte = sgqlc.types.Field(String, graphql_name='seed_gte')
    seed_lt = sgqlc.types.Field(String, graphql_name='seed_lt')
    lock_checkpoint_gt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gt')
    seed_ne = sgqlc.types.Field(String, graphql_name='seed_ne')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    lock_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_nin')
    seed_exists = sgqlc.types.Field(Boolean, graphql_name='seed_exists')
    ledger_exists = sgqlc.types.Field(Boolean, graphql_name='ledger_exists')
    start_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_in')
    lock_checkpoint_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lockCheckpoint_in')
    lock_checkpoint_gte = sgqlc.types.Field(String, graphql_name='lockCheckpoint_gte')
    seed_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='seed_nin')
    lock_checkpoint_lt = sgqlc.types.Field(String, graphql_name='lockCheckpoint_lt')
    lock_checkpoint_exists = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_exists')
    start_checkpoint_ne = sgqlc.types.Field(String, graphql_name='startCheckpoint_ne')
    seed_gt = sgqlc.types.Field(String, graphql_name='seed_gt')
    start_checkpoint_gt = sgqlc.types.Field(String, graphql_name='startCheckpoint_gt')
    seed_lte = sgqlc.types.Field(String, graphql_name='seed_lte')
    start_checkpoint_lte = sgqlc.types.Field(String, graphql_name='startCheckpoint_lte')
    start_checkpoint_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='startCheckpoint_nin')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    epoch_length_gte = sgqlc.types.Field(Int, graphql_name='epochLength_gte')
    lock_checkpoint_ne = sgqlc.types.Field(String, graphql_name='lockCheckpoint_ne')
    epoch_length_lte = sgqlc.types.Field(Int, graphql_name='epochLength_lte')
    epoch_length_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epochLength_nin')
    epoch_length_ne = sgqlc.types.Field(Int, graphql_name='epochLength_ne')
    epoch_length_gt = sgqlc.types.Field(Int, graphql_name='epochLength_gt')
    epoch_length_exists = sgqlc.types.Field(Boolean, graphql_name='epochLength_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateConsensusStateStakingEpochDatumQueryInput')), graphql_name='AND')


class BlockProtocolStateConsensusStateStakingEpochDatumUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('epoch_length', 'seed', 'start_checkpoint', 'lock_checkpoint_unset', 'epoch_length_inc', 'start_checkpoint_unset', 'ledger_unset', 'seed_unset', 'epoch_length_unset', 'lock_checkpoint', 'ledger')
    epoch_length = sgqlc.types.Field(Int, graphql_name='epochLength')
    seed = sgqlc.types.Field(String, graphql_name='seed')
    start_checkpoint = sgqlc.types.Field(String, graphql_name='startCheckpoint')
    lock_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='lockCheckpoint_unset')
    epoch_length_inc = sgqlc.types.Field(Int, graphql_name='epochLength_inc')
    start_checkpoint_unset = sgqlc.types.Field(Boolean, graphql_name='startCheckpoint_unset')
    ledger_unset = sgqlc.types.Field(Boolean, graphql_name='ledger_unset')
    seed_unset = sgqlc.types.Field(Boolean, graphql_name='seed_unset')
    epoch_length_unset = sgqlc.types.Field(Boolean, graphql_name='epochLength_unset')
    lock_checkpoint = sgqlc.types.Field(String, graphql_name='lockCheckpoint')
    ledger = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumLedgerUpdateInput, graphql_name='ledger')


class BlockProtocolStateConsensusStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('blockchain_length_unset', 'epoch_count', 'staking_epoch_data', 'min_window_density_inc', 'min_window_density_unset', 'staking_epoch_data_unset', 'epoch_inc', 'slot_inc', 'next_epoch_data', 'block_height', 'epoch', 'total_currency_inc', 'block_height_unset', 'slot_unset', 'slot_since_genesis', 'blockchain_length', 'epoch_unset', 'slot', 'total_currency', 'total_currency_unset', 'has_ancestor_in_same_checkpoint_window', 'last_vrf_output_unset', 'slot_since_genesis_unset', 'min_window_density', 'slot_since_genesis_inc', 'has_ancestor_in_same_checkpoint_window_unset', 'next_epoch_data_unset', 'block_height_inc', 'epoch_count_inc', 'blockchain_length_inc', 'last_vrf_output', 'epoch_count_unset')
    blockchain_length_unset = sgqlc.types.Field(Boolean, graphql_name='blockchainLength_unset')
    epoch_count = sgqlc.types.Field(Int, graphql_name='epochCount')
    staking_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateStakingEpochDatumUpdateInput, graphql_name='stakingEpochData')
    min_window_density_inc = sgqlc.types.Field(Int, graphql_name='minWindowDensity_inc')
    min_window_density_unset = sgqlc.types.Field(Boolean, graphql_name='minWindowDensity_unset')
    staking_epoch_data_unset = sgqlc.types.Field(Boolean, graphql_name='stakingEpochData_unset')
    epoch_inc = sgqlc.types.Field(Int, graphql_name='epoch_inc')
    slot_inc = sgqlc.types.Field(Int, graphql_name='slot_inc')
    next_epoch_data = sgqlc.types.Field(BlockProtocolStateConsensusStateNextEpochDatumUpdateInput, graphql_name='nextEpochData')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    total_currency_inc = sgqlc.types.Field(Float, graphql_name='totalCurrency_inc')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    slot_unset = sgqlc.types.Field(Boolean, graphql_name='slot_unset')
    slot_since_genesis = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis')
    blockchain_length = sgqlc.types.Field(Int, graphql_name='blockchainLength')
    epoch_unset = sgqlc.types.Field(Boolean, graphql_name='epoch_unset')
    slot = sgqlc.types.Field(Int, graphql_name='slot')
    total_currency = sgqlc.types.Field(Float, graphql_name='totalCurrency')
    total_currency_unset = sgqlc.types.Field(Boolean, graphql_name='totalCurrency_unset')
    has_ancestor_in_same_checkpoint_window = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow')
    last_vrf_output_unset = sgqlc.types.Field(Boolean, graphql_name='lastVrfOutput_unset')
    slot_since_genesis_unset = sgqlc.types.Field(Boolean, graphql_name='slotSinceGenesis_unset')
    min_window_density = sgqlc.types.Field(Int, graphql_name='minWindowDensity')
    slot_since_genesis_inc = sgqlc.types.Field(Int, graphql_name='slotSinceGenesis_inc')
    has_ancestor_in_same_checkpoint_window_unset = sgqlc.types.Field(Boolean, graphql_name='hasAncestorInSameCheckpointWindow_unset')
    next_epoch_data_unset = sgqlc.types.Field(Boolean, graphql_name='nextEpochData_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    epoch_count_inc = sgqlc.types.Field(Int, graphql_name='epochCount_inc')
    blockchain_length_inc = sgqlc.types.Field(Int, graphql_name='blockchainLength_inc')
    last_vrf_output = sgqlc.types.Field(String, graphql_name='lastVrfOutput')
    epoch_count_unset = sgqlc.types.Field(Boolean, graphql_name='epochCount_unset')


class BlockProtocolStateInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('previous_state_hash', 'blockchain_state', 'consensus_state')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateInsertInput, graphql_name='blockchainState')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateInsertInput, graphql_name='consensusState')


class BlockProtocolStateQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('previous_state_hash_lt', 'previous_state_hash_gt', 'previous_state_hash_nin', 'previous_state_hash_exists', 'blockchain_state_exists', 'consensus_state_exists', 'previous_state_hash_lte', 'previous_state_hash_in', 'and_', 'previous_state_hash_gte', 'consensus_state', 'blockchain_state', 'or_', 'previous_state_hash', 'previous_state_hash_ne')
    previous_state_hash_lt = sgqlc.types.Field(String, graphql_name='previousStateHash_lt')
    previous_state_hash_gt = sgqlc.types.Field(String, graphql_name='previousStateHash_gt')
    previous_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='previousStateHash_nin')
    previous_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='previousStateHash_exists')
    blockchain_state_exists = sgqlc.types.Field(Boolean, graphql_name='blockchainState_exists')
    consensus_state_exists = sgqlc.types.Field(Boolean, graphql_name='consensusState_exists')
    previous_state_hash_lte = sgqlc.types.Field(String, graphql_name='previousStateHash_lte')
    previous_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='previousStateHash_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateQueryInput')), graphql_name='AND')
    previous_state_hash_gte = sgqlc.types.Field(String, graphql_name='previousStateHash_gte')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateQueryInput, graphql_name='consensusState')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateQueryInput, graphql_name='blockchainState')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockProtocolStateQueryInput')), graphql_name='OR')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')
    previous_state_hash_ne = sgqlc.types.Field(String, graphql_name='previousStateHash_ne')


class BlockProtocolStateUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('consensus_state_unset', 'previous_state_hash', 'previous_state_hash_unset', 'blockchain_state', 'blockchain_state_unset', 'consensus_state')
    consensus_state_unset = sgqlc.types.Field(Boolean, graphql_name='consensusState_unset')
    previous_state_hash = sgqlc.types.Field(String, graphql_name='previousStateHash')
    previous_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='previousStateHash_unset')
    blockchain_state = sgqlc.types.Field(BlockProtocolStateBlockchainStateUpdateInput, graphql_name='blockchainState')
    blockchain_state_unset = sgqlc.types.Field(Boolean, graphql_name='blockchainState_unset')
    consensus_state = sgqlc.types.Field(BlockProtocolStateConsensusStateUpdateInput, graphql_name='consensusState')


class BlockQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('state_hash_nin', 'snark_jobs_exists', 'state_hash_in', 'creator_exists', 'date_time_lt', 'block_height_lte', 'state_hash_gte', 'creator_account', 'snark_jobs_in', 'state_hash', 'state_hash_field_ne', 'creator_lt', 'creator_ne', 'creator', 'creator_nin', 'received_time_gte', 'and_', 'canonical', 'block_height_gt', 'snark_jobs', 'state_hash_field_in', 'date_time_nin', 'date_time_exists', 'state_hash_field_nin', 'state_hash_ne', 'canonical_exists', 'received_time_ne', 'winner_account', 'creator_in', 'state_hash_field_gt', 'canonical_ne', 'state_hash_field', 'block_height_exists', 'block_height_gte', 'creator_gt', 'received_time_in', 'block_height_lt', 'or_', 'date_time_lte', 'transactions_exists', 'state_hash_lte', 'date_time', 'received_time_gt', 'snark_jobs_nin', 'date_time_in', 'date_time_ne', 'block_height_in', 'state_hash_field_lt', 'received_time_lt', 'protocol_state_exists', 'state_hash_lt', 'date_time_gte', 'creator_lte', 'state_hash_field_lte', 'winner_account_exists', 'received_time_lte', 'block_height_ne', 'transactions', 'received_time_exists', 'block_height', 'protocol_state', 'date_time_gt', 'state_hash_field_gte', 'received_time', 'state_hash_gt', 'received_time_nin', 'state_hash_field_exists', 'state_hash_exists', 'creator_gte', 'creator_account_exists', 'block_height_nin')
    state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_nin')
    snark_jobs_exists = sgqlc.types.Field(Boolean, graphql_name='snarkJobs_exists')
    state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_in')
    creator_exists = sgqlc.types.Field(Boolean, graphql_name='creator_exists')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    state_hash_gte = sgqlc.types.Field(String, graphql_name='stateHash_gte')
    creator_account = sgqlc.types.Field(BlockCreatorAccountQueryInput, graphql_name='creatorAccount')
    snark_jobs_in = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs_in')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    state_hash_field_ne = sgqlc.types.Field(String, graphql_name='stateHashField_ne')
    creator_lt = sgqlc.types.Field(String, graphql_name='creator_lt')
    creator_ne = sgqlc.types.Field(String, graphql_name='creator_ne')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    creator_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='creator_nin')
    received_time_gte = sgqlc.types.Field(DateTime, graphql_name='receivedTime_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockQueryInput')), graphql_name='AND')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs')
    state_hash_field_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHashField_in')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    state_hash_field_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHashField_nin')
    state_hash_ne = sgqlc.types.Field(String, graphql_name='stateHash_ne')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    received_time_ne = sgqlc.types.Field(DateTime, graphql_name='receivedTime_ne')
    winner_account = sgqlc.types.Field('BlockWinnerAccountQueryInput', graphql_name='winnerAccount')
    creator_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='creator_in')
    state_hash_field_gt = sgqlc.types.Field(String, graphql_name='stateHashField_gt')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    creator_gt = sgqlc.types.Field(String, graphql_name='creator_gt')
    received_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='receivedTime_in')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockQueryInput')), graphql_name='OR')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    transactions_exists = sgqlc.types.Field(Boolean, graphql_name='transactions_exists')
    state_hash_lte = sgqlc.types.Field(String, graphql_name='stateHash_lte')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    received_time_gt = sgqlc.types.Field(DateTime, graphql_name='receivedTime_gt')
    snark_jobs_nin = sgqlc.types.Field(sgqlc.types.list_of('BlockSnarkJobQueryInput'), graphql_name='snarkJobs_nin')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    state_hash_field_lt = sgqlc.types.Field(String, graphql_name='stateHashField_lt')
    received_time_lt = sgqlc.types.Field(DateTime, graphql_name='receivedTime_lt')
    protocol_state_exists = sgqlc.types.Field(Boolean, graphql_name='protocolState_exists')
    state_hash_lt = sgqlc.types.Field(String, graphql_name='stateHash_lt')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    creator_lte = sgqlc.types.Field(String, graphql_name='creator_lte')
    state_hash_field_lte = sgqlc.types.Field(String, graphql_name='stateHashField_lte')
    winner_account_exists = sgqlc.types.Field(Boolean, graphql_name='winnerAccount_exists')
    received_time_lte = sgqlc.types.Field(DateTime, graphql_name='receivedTime_lte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    transactions = sgqlc.types.Field('BlockTransactionQueryInput', graphql_name='transactions')
    received_time_exists = sgqlc.types.Field(Boolean, graphql_name='receivedTime_exists')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    protocol_state = sgqlc.types.Field(BlockProtocolStateQueryInput, graphql_name='protocolState')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    state_hash_field_gte = sgqlc.types.Field(String, graphql_name='stateHashField_gte')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')
    state_hash_gt = sgqlc.types.Field(String, graphql_name='stateHash_gt')
    received_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='receivedTime_nin')
    state_hash_field_exists = sgqlc.types.Field(Boolean, graphql_name='stateHashField_exists')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    creator_gte = sgqlc.types.Field(String, graphql_name='creator_gte')
    creator_account_exists = sgqlc.types.Field(Boolean, graphql_name='creatorAccount_exists')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')


class BlockSnarkJobInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('work_ids', 'block_height', 'block_state_hash', 'date_time', 'fee', 'prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')


class BlockSnarkJobQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee_lte', 'prover_in', 'fee_exists', 'block_state_hash_lt', 'block_state_hash_ne', 'date_time_in', 'prover_gte', 'block_height_lt', 'fee_ne', 'work_ids_in', 'block_state_hash', 'date_time_ne', 'fee_lt', 'block_height_gte', 'block_height_in', 'fee_gte', 'block_height', 'work_ids_nin', 'block_height_lte', 'block_height_ne', 'prover_lte', 'block_height_nin', 'block_state_hash_in', 'date_time_gt', 'block_state_hash_lte', 'prover', 'fee_in', 'date_time_lt', 'prover_gt', 'date_time', 'fee_gt', 'date_time_exists', 'block_height_exists', 'prover_nin', 'or_', 'block_state_hash_gt', 'prover_exists', 'block_state_hash_exists', 'fee', 'work_ids', 'work_ids_exists', 'block_state_hash_gte', 'fee_nin', 'block_height_gt', 'date_time_lte', 'prover_lt', 'date_time_gte', 'and_', 'date_time_nin', 'block_state_hash_nin', 'prover_ne')
    fee_lte = sgqlc.types.Field(Int, graphql_name='fee_lte')
    prover_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_in')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    block_state_hash_lt = sgqlc.types.Field(String, graphql_name='blockStateHash_lt')
    block_state_hash_ne = sgqlc.types.Field(String, graphql_name='blockStateHash_ne')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    prover_gte = sgqlc.types.Field(String, graphql_name='prover_gte')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    fee_ne = sgqlc.types.Field(Int, graphql_name='fee_ne')
    work_ids_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_in')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    fee_lt = sgqlc.types.Field(Int, graphql_name='fee_lt')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    fee_gte = sgqlc.types.Field(Int, graphql_name='fee_gte')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    work_ids_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_nin')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    prover_lte = sgqlc.types.Field(String, graphql_name='prover_lte')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    block_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_in')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    block_state_hash_lte = sgqlc.types.Field(String, graphql_name='blockStateHash_lte')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_in')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    prover_gt = sgqlc.types.Field(String, graphql_name='prover_gt')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee_gt = sgqlc.types.Field(Int, graphql_name='fee_gt')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    prover_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockSnarkJobQueryInput')), graphql_name='OR')
    block_state_hash_gt = sgqlc.types.Field(String, graphql_name='blockStateHash_gt')
    prover_exists = sgqlc.types.Field(Boolean, graphql_name='prover_exists')
    block_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_exists')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    work_ids_exists = sgqlc.types.Field(Boolean, graphql_name='workIds_exists')
    block_state_hash_gte = sgqlc.types.Field(String, graphql_name='blockStateHash_gte')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_nin')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    prover_lt = sgqlc.types.Field(String, graphql_name='prover_lt')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockSnarkJobQueryInput')), graphql_name='AND')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    block_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_nin')
    prover_ne = sgqlc.types.Field(String, graphql_name='prover_ne')


class BlockSnarkJobUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_state_hash_unset', 'fee_unset', 'fee', 'block_height', 'block_state_hash', 'block_height_inc', 'block_height_unset', 'work_ids', 'date_time_unset', 'work_ids_unset', 'date_time', 'prover', 'prover_unset', 'fee_inc')
    block_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_unset')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    work_ids_unset = sgqlc.types.Field(Boolean, graphql_name='workIds_unset')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    prover_unset = sgqlc.types.Field(Boolean, graphql_name='prover_unset')
    fee_inc = sgqlc.types.Field(Int, graphql_name='fee_inc')


class BlockTransactionCoinbaseReceiverAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionCoinbaseReceiverAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_ne', 'public_key_gt', 'and_', 'public_key_gte', 'public_key_in', 'or_', 'public_key', 'public_key_lt', 'public_key_nin', 'public_key_exists', 'public_key_lte')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionCoinbaseReceiverAccountQueryInput')), graphql_name='AND')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionCoinbaseReceiverAccountQueryInput')), graphql_name='OR')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')


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
    __field_names__ = ('type_in', 'fee_nin', 'type_exists', 'type_gte', 'fee_exists', 'type_lt', 'type_lte', 'fee_lt', 'type', 'recipient_in', 'fee_ne', 'and_', 'type_gt', 'fee_gt', 'type_nin', 'recipient_nin', 'type_ne', 'fee_in', 'recipient_gte', 'recipient_lt', 'fee_gte', 'recipient_exists', 'fee', 'recipient', 'recipient_lte', 'recipient_ne', 'recipient_gt', 'fee_lte', 'or_')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='type_in')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_nin')
    type_exists = sgqlc.types.Field(Boolean, graphql_name='type_exists')
    type_gte = sgqlc.types.Field(String, graphql_name='type_gte')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    type_lt = sgqlc.types.Field(String, graphql_name='type_lt')
    type_lte = sgqlc.types.Field(String, graphql_name='type_lte')
    fee_lt = sgqlc.types.Field(Long, graphql_name='fee_lt')
    type = sgqlc.types.Field(String, graphql_name='type')
    recipient_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipient_in')
    fee_ne = sgqlc.types.Field(Long, graphql_name='fee_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionFeeTransferQueryInput')), graphql_name='AND')
    type_gt = sgqlc.types.Field(String, graphql_name='type_gt')
    fee_gt = sgqlc.types.Field(Long, graphql_name='fee_gt')
    type_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='type_nin')
    recipient_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='recipient_nin')
    type_ne = sgqlc.types.Field(String, graphql_name='type_ne')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_in')
    recipient_gte = sgqlc.types.Field(String, graphql_name='recipient_gte')
    recipient_lt = sgqlc.types.Field(String, graphql_name='recipient_lt')
    fee_gte = sgqlc.types.Field(Long, graphql_name='fee_gte')
    recipient_exists = sgqlc.types.Field(Boolean, graphql_name='recipient_exists')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    recipient = sgqlc.types.Field(String, graphql_name='recipient')
    recipient_lte = sgqlc.types.Field(String, graphql_name='recipient_lte')
    recipient_ne = sgqlc.types.Field(String, graphql_name='recipient_ne')
    recipient_gt = sgqlc.types.Field(String, graphql_name='recipient_gt')
    fee_lte = sgqlc.types.Field(Long, graphql_name='fee_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionFeeTransferQueryInput')), graphql_name='OR')


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
    __field_names__ = ('user_commands', 'coinbase', 'coinbase_receiver_account', 'fee_transfer')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandInsertInput'), graphql_name='userCommands')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountInsertInput, graphql_name='coinbaseReceiverAccount')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferInsertInput), graphql_name='feeTransfer')


class BlockTransactionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('or_', 'coinbase_receiver_account', 'fee_transfer_in', 'coinbase_gt', 'and_', 'coinbase_ne', 'coinbase_exists', 'user_commands', 'coinbase', 'coinbase_lt', 'coinbase_nin', 'fee_transfer', 'coinbase_in', 'coinbase_lte', 'fee_transfer_nin', 'coinbase_receiver_account_exists', 'user_commands_in', 'coinbase_gte', 'user_commands_nin', 'fee_transfer_exists', 'user_commands_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionQueryInput')), graphql_name='OR')
    coinbase_receiver_account = sgqlc.types.Field(BlockTransactionCoinbaseReceiverAccountQueryInput, graphql_name='coinbaseReceiverAccount')
    fee_transfer_in = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer_in')
    coinbase_gt = sgqlc.types.Field(Long, graphql_name='coinbase_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionQueryInput')), graphql_name='AND')
    coinbase_ne = sgqlc.types.Field(Long, graphql_name='coinbase_ne')
    coinbase_exists = sgqlc.types.Field(Boolean, graphql_name='coinbase_exists')
    user_commands = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands')
    coinbase = sgqlc.types.Field(Long, graphql_name='coinbase')
    coinbase_lt = sgqlc.types.Field(Long, graphql_name='coinbase_lt')
    coinbase_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='coinbase_nin')
    fee_transfer = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer')
    coinbase_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='coinbase_in')
    coinbase_lte = sgqlc.types.Field(Long, graphql_name='coinbase_lte')
    fee_transfer_nin = sgqlc.types.Field(sgqlc.types.list_of(BlockTransactionFeeTransferQueryInput), graphql_name='feeTransfer_nin')
    coinbase_receiver_account_exists = sgqlc.types.Field(Boolean, graphql_name='coinbaseReceiverAccount_exists')
    user_commands_in = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands_in')
    coinbase_gte = sgqlc.types.Field(Long, graphql_name='coinbase_gte')
    user_commands_nin = sgqlc.types.Field(sgqlc.types.list_of('BlockTransactionUserCommandQueryInput'), graphql_name='userCommands_nin')
    fee_transfer_exists = sgqlc.types.Field(Boolean, graphql_name='feeTransfer_exists')
    user_commands_exists = sgqlc.types.Field(Boolean, graphql_name='userCommands_exists')


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
    __field_names__ = ('token_gte', 'token_lt', 'token_lte', 'token_ne', 'token_gt', 'token_in', 'token_nin', 'token_exists', 'and_', 'token', 'or_')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFeePayerQueryInput')), graphql_name='AND')
    token = sgqlc.types.Field(Int, graphql_name='token')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFeePayerQueryInput')), graphql_name='OR')


class BlockTransactionUserCommandFeePayerUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'token', 'token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')


class BlockTransactionUserCommandFromAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandFromAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_gte', 'token_lt', 'or_', 'token_lte', 'token_in', 'and_', 'token', 'token_nin', 'token_ne', 'token_exists', 'token_gt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFromAccountQueryInput')), graphql_name='OR')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandFromAccountQueryInput')), graphql_name='AND')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')


class BlockTransactionUserCommandFromAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'token', 'token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')


class BlockTransactionUserCommandInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('id', 'source', 'to_account', 'kind', 'from_', 'token', 'date_time', 'hash', 'is_delegation', 'fee', 'amount', 'fee_payer', 'from_account', 'block_height', 'receiver', 'failure_reason', 'block_state_hash', 'nonce', 'memo', 'fee_token', 'to')
    id = sgqlc.types.Field(String, graphql_name='id')
    source = sgqlc.types.Field('BlockTransactionUserCommandSourceInsertInput', graphql_name='source')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccountInsertInput', graphql_name='toAccount')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    token = sgqlc.types.Field(Int, graphql_name='token')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerInsertInput, graphql_name='feePayer')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountInsertInput, graphql_name='fromAccount')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiverInsertInput', graphql_name='receiver')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    to = sgqlc.types.Field(String, graphql_name='to')


class BlockTransactionUserCommandQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receiver_exists', 'hash_gte', 'failure_reason', 'hash_exists', 'nonce', 'block_state_hash_exists', 'id', 'from_gte', 'fee_gt', 'failure_reason_in', 'nonce_lte', 'block_state_hash', 'source_exists', 'kind_nin', 'token_gt', 'fee_token_gte', 'from_in', 'fee_token_lte', 'from_lte', 'from_account_exists', 'to_account_exists', 'to_ne', 'is_delegation', 'kind_ne', 'fee_exists', 'fee_lt', 'nonce_in', 'block_state_hash_gt', 'id_exists', 'memo', 'from_account', 'id_gt', 'block_state_hash_in', 'block_height_exists', 'id_gte', 'id_lte', 'memo_lt', 'date_time_exists', 'kind_in', 'hash_nin', 'block_state_hash_gte', 'to_gte', 'block_height_gte', 'to_nin', 'amount_gte', 'id_lt', 'fee_lte', 'amount_gt', 'fee_token', 'nonce_gte', 'is_delegation_exists', 'token_exists', 'fee_token_gt', 'and_', 'token_lt', 'date_time', 'fee_payer_exists', 'block_state_hash_ne', 'token_lte', 'kind_gte', 'nonce_nin', 'fee_token_nin', 'date_time_ne', 'amount_lt', 'id_ne', 'id_nin', 'source', 'from_nin', 'block_state_hash_lte', 'amount_exists', 'failure_reason_lte', 'amount_in', 'fee_token_ne', 'failure_reason_exists', 'nonce_lt', 'block_height', 'memo_gte', 'failure_reason_ne', 'amount_lte', 'block_height_ne', 'token_in', 'block_state_hash_lt', 'fee_token_exists', 'fee_token_lt', 'fee_in', 'or_', 'hash_ne', 'nonce_ne', 'from_gt', 'amount_ne', 'hash_gt', 'to_account', 'to_exists', 'block_height_lt', 'id_in', 'nonce_gt', 'hash', 'from_ne', 'kind_lte', 'nonce_exists', 'block_height_nin', 'hash_lte', 'date_time_lt', 'token_gte', 'fee_gte', 'failure_reason_lt', 'date_time_gte', 'to_gt', 'memo_in', 'to_lte', 'memo_nin', 'memo_exists', 'from_', 'date_time_gt', 'hash_in', 'to', 'fee_payer', 'amount', 'block_state_hash_nin', 'kind_exists', 'is_delegation_ne', 'failure_reason_gte', 'kind', 'from_lt', 'to_lt', 'memo_ne', 'block_height_gt', 'date_time_nin', 'date_time_lte', 'from_exists', 'fee_ne', 'amount_nin', 'hash_lt', 'fee_token_in', 'block_height_in', 'block_height_lte', 'date_time_in', 'kind_gt', 'kind_lt', 'fee_nin', 'fee', 'memo_gt', 'token_nin', 'token_ne', 'to_in', 'failure_reason_gt', 'failure_reason_nin', 'token', 'memo_lte', 'receiver')
    receiver_exists = sgqlc.types.Field(Boolean, graphql_name='receiver_exists')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    block_state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_exists')
    id = sgqlc.types.Field(String, graphql_name='id')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    fee_gt = sgqlc.types.Field(Int, graphql_name='fee_gt')
    failure_reason_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_in')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    source_exists = sgqlc.types.Field(Boolean, graphql_name='source_exists')
    kind_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_nin')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    fee_token_gte = sgqlc.types.Field(Int, graphql_name='feeToken_gte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_in')
    fee_token_lte = sgqlc.types.Field(Int, graphql_name='feeToken_lte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_account_exists = sgqlc.types.Field(Boolean, graphql_name='fromAccount_exists')
    to_account_exists = sgqlc.types.Field(Boolean, graphql_name='toAccount_exists')
    to_ne = sgqlc.types.Field(String, graphql_name='to_ne')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    kind_ne = sgqlc.types.Field(String, graphql_name='kind_ne')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    fee_lt = sgqlc.types.Field(Int, graphql_name='fee_lt')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    block_state_hash_gt = sgqlc.types.Field(String, graphql_name='blockStateHash_gt')
    id_exists = sgqlc.types.Field(Boolean, graphql_name='id_exists')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountQueryInput, graphql_name='fromAccount')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    block_state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_in')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    memo_lt = sgqlc.types.Field(String, graphql_name='memo_lt')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    kind_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_in')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    block_state_hash_gte = sgqlc.types.Field(String, graphql_name='blockStateHash_gte')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    to_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_nin')
    amount_gte = sgqlc.types.Field(Int, graphql_name='amount_gte')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    fee_lte = sgqlc.types.Field(Int, graphql_name='fee_lte')
    amount_gt = sgqlc.types.Field(Int, graphql_name='amount_gt')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    is_delegation_exists = sgqlc.types.Field(Boolean, graphql_name='isDelegation_exists')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    fee_token_gt = sgqlc.types.Field(Int, graphql_name='feeToken_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandQueryInput')), graphql_name='AND')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee_payer_exists = sgqlc.types.Field(Boolean, graphql_name='feePayer_exists')
    block_state_hash_ne = sgqlc.types.Field(String, graphql_name='blockStateHash_ne')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    kind_gte = sgqlc.types.Field(String, graphql_name='kind_gte')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    fee_token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_nin')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    amount_lt = sgqlc.types.Field(Int, graphql_name='amount_lt')
    id_ne = sgqlc.types.Field(String, graphql_name='id_ne')
    id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_nin')
    source = sgqlc.types.Field('BlockTransactionUserCommandSourceQueryInput', graphql_name='source')
    from_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_nin')
    block_state_hash_lte = sgqlc.types.Field(String, graphql_name='blockStateHash_lte')
    amount_exists = sgqlc.types.Field(Boolean, graphql_name='amount_exists')
    failure_reason_lte = sgqlc.types.Field(String, graphql_name='failureReason_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='amount_in')
    fee_token_ne = sgqlc.types.Field(Int, graphql_name='feeToken_ne')
    failure_reason_exists = sgqlc.types.Field(Boolean, graphql_name='failureReason_exists')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    memo_gte = sgqlc.types.Field(String, graphql_name='memo_gte')
    failure_reason_ne = sgqlc.types.Field(String, graphql_name='failureReason_ne')
    amount_lte = sgqlc.types.Field(Int, graphql_name='amount_lte')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    block_state_hash_lt = sgqlc.types.Field(String, graphql_name='blockStateHash_lt')
    fee_token_exists = sgqlc.types.Field(Boolean, graphql_name='feeToken_exists')
    fee_token_lt = sgqlc.types.Field(Int, graphql_name='feeToken_lt')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandQueryInput')), graphql_name='OR')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    amount_ne = sgqlc.types.Field(Int, graphql_name='amount_ne')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    to_account = sgqlc.types.Field('BlockTransactionUserCommandToAccountQueryInput', graphql_name='toAccount')
    to_exists = sgqlc.types.Field(Boolean, graphql_name='to_exists')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_in')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    from_ne = sgqlc.types.Field(String, graphql_name='from_ne')
    kind_lte = sgqlc.types.Field(String, graphql_name='kind_lte')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    fee_gte = sgqlc.types.Field(Int, graphql_name='fee_gte')
    failure_reason_lt = sgqlc.types.Field(String, graphql_name='failureReason_lt')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    memo_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_in')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    memo_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_nin')
    memo_exists = sgqlc.types.Field(Boolean, graphql_name='memo_exists')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    to = sgqlc.types.Field(String, graphql_name='to')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerQueryInput, graphql_name='feePayer')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    block_state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='blockStateHash_nin')
    kind_exists = sgqlc.types.Field(Boolean, graphql_name='kind_exists')
    is_delegation_ne = sgqlc.types.Field(Boolean, graphql_name='isDelegation_ne')
    failure_reason_gte = sgqlc.types.Field(String, graphql_name='failureReason_gte')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    memo_ne = sgqlc.types.Field(String, graphql_name='memo_ne')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    from_exists = sgqlc.types.Field(Boolean, graphql_name='from_exists')
    fee_ne = sgqlc.types.Field(Int, graphql_name='fee_ne')
    amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='amount_nin')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    fee_token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_in')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    kind_gt = sgqlc.types.Field(String, graphql_name='kind_gt')
    kind_lt = sgqlc.types.Field(String, graphql_name='kind_lt')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='fee_nin')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    memo_gt = sgqlc.types.Field(String, graphql_name='memo_gt')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_in')
    failure_reason_gt = sgqlc.types.Field(String, graphql_name='failureReason_gt')
    failure_reason_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_nin')
    token = sgqlc.types.Field(Int, graphql_name='token')
    memo_lte = sgqlc.types.Field(String, graphql_name='memo_lte')
    receiver = sgqlc.types.Field('BlockTransactionUserCommandReceiverQueryInput', graphql_name='receiver')


class BlockTransactionUserCommandReceiverInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandReceiverQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_exists', 'public_key', 'public_key_lte', 'public_key_nin', 'or_', 'public_key_gt', 'public_key_lt', 'public_key_ne', 'public_key_gte', 'public_key_in', 'and_')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandReceiverQueryInput')), graphql_name='OR')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandReceiverQueryInput')), graphql_name='AND')


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
    __field_names__ = ('and_', 'public_key_gt', 'public_key', 'public_key_in', 'public_key_exists', 'or_', 'public_key_nin', 'public_key_lt', 'public_key_ne', 'public_key_gte', 'public_key_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandSourceQueryInput')), graphql_name='AND')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandSourceQueryInput')), graphql_name='OR')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')


class BlockTransactionUserCommandSourceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_unset', 'public_key')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='publicKey_unset')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class BlockTransactionUserCommandToAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(Int, graphql_name='token')


class BlockTransactionUserCommandToAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_lt', 'or_', 'token_exists', 'token_nin', 'and_', 'token_lte', 'token_gt', 'token_ne', 'token_gte', 'token', 'token_in')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandToAccountQueryInput')), graphql_name='OR')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockTransactionUserCommandToAccountQueryInput')), graphql_name='AND')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')


class BlockTransactionUserCommandToAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token_unset', 'token', 'token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')


class BlockTransactionUserCommandUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receiver', 'hash_unset', 'fee_token_unset', 'nonce', 'id', 'date_time_unset', 'fee_unset', 'failure_reason_unset', 'token', 'to_account_unset', 'from_unset', 'kind', 'fee_payer', 'to_account', 'source_unset', 'fee', 'memo', 'is_delegation_unset', 'hash', 'token_unset', 'from_account', 'failure_reason', 'block_state_hash_unset', 'block_state_hash', 'from_', 'source', 'from_account_unset', 'block_height_unset', 'memo_unset', 'fee_payer_unset', 'amount_inc', 'fee_inc', 'amount', 'receiver_unset', 'kind_unset', 'nonce_inc', 'amount_unset', 'token_inc', 'block_height', 'fee_token_inc', 'fee_token', 'id_unset', 'to', 'nonce_unset', 'block_height_inc', 'to_unset', 'is_delegation', 'date_time')
    receiver = sgqlc.types.Field(BlockTransactionUserCommandReceiverUpdateInput, graphql_name='receiver')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    fee_token_unset = sgqlc.types.Field(Boolean, graphql_name='feeToken_unset')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    id = sgqlc.types.Field(String, graphql_name='id')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    failure_reason_unset = sgqlc.types.Field(Boolean, graphql_name='failureReason_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    to_account_unset = sgqlc.types.Field(Boolean, graphql_name='toAccount_unset')
    from_unset = sgqlc.types.Field(Boolean, graphql_name='from_unset')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    fee_payer = sgqlc.types.Field(BlockTransactionUserCommandFeePayerUpdateInput, graphql_name='feePayer')
    to_account = sgqlc.types.Field(BlockTransactionUserCommandToAccountUpdateInput, graphql_name='toAccount')
    source_unset = sgqlc.types.Field(Boolean, graphql_name='source_unset')
    fee = sgqlc.types.Field(Int, graphql_name='fee')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    is_delegation_unset = sgqlc.types.Field(Boolean, graphql_name='isDelegation_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    from_account = sgqlc.types.Field(BlockTransactionUserCommandFromAccountUpdateInput, graphql_name='fromAccount')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    block_state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='blockStateHash_unset')
    block_state_hash = sgqlc.types.Field(String, graphql_name='blockStateHash')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    source = sgqlc.types.Field(BlockTransactionUserCommandSourceUpdateInput, graphql_name='source')
    from_account_unset = sgqlc.types.Field(Boolean, graphql_name='fromAccount_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    memo_unset = sgqlc.types.Field(Boolean, graphql_name='memo_unset')
    fee_payer_unset = sgqlc.types.Field(Boolean, graphql_name='feePayer_unset')
    amount_inc = sgqlc.types.Field(Int, graphql_name='amount_inc')
    fee_inc = sgqlc.types.Field(Int, graphql_name='fee_inc')
    amount = sgqlc.types.Field(Int, graphql_name='amount')
    receiver_unset = sgqlc.types.Field(Boolean, graphql_name='receiver_unset')
    kind_unset = sgqlc.types.Field(Boolean, graphql_name='kind_unset')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    amount_unset = sgqlc.types.Field(Boolean, graphql_name='amount_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    fee_token_inc = sgqlc.types.Field(Int, graphql_name='feeToken_inc')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    id_unset = sgqlc.types.Field(Boolean, graphql_name='id_unset')
    to = sgqlc.types.Field(String, graphql_name='to')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    to_unset = sgqlc.types.Field(Boolean, graphql_name='to_unset')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')


class BlockUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('date_time', 'creator_account_unset', 'snark_jobs', 'block_height_unset', 'canonical_unset', 'snark_jobs_unset', 'transactions_unset', 'protocol_state', 'protocol_state_unset', 'creator_account', 'state_hash_field', 'canonical', 'block_height', 'state_hash_unset', 'received_time_unset', 'creator', 'transactions', 'winner_account', 'winner_account_unset', 'date_time_unset', 'block_height_inc', 'creator_unset', 'state_hash_field_unset', 'state_hash', 'received_time')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    creator_account_unset = sgqlc.types.Field(Boolean, graphql_name='creatorAccount_unset')
    snark_jobs = sgqlc.types.Field(sgqlc.types.list_of(BlockSnarkJobUpdateInput), graphql_name='snarkJobs')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    snark_jobs_unset = sgqlc.types.Field(Boolean, graphql_name='snarkJobs_unset')
    transactions_unset = sgqlc.types.Field(Boolean, graphql_name='transactions_unset')
    protocol_state = sgqlc.types.Field(BlockProtocolStateUpdateInput, graphql_name='protocolState')
    protocol_state_unset = sgqlc.types.Field(Boolean, graphql_name='protocolState_unset')
    creator_account = sgqlc.types.Field(BlockCreatorAccountUpdateInput, graphql_name='creatorAccount')
    state_hash_field = sgqlc.types.Field(String, graphql_name='stateHashField')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    received_time_unset = sgqlc.types.Field(Boolean, graphql_name='receivedTime_unset')
    creator = sgqlc.types.Field(String, graphql_name='creator')
    transactions = sgqlc.types.Field(BlockTransactionUpdateInput, graphql_name='transactions')
    winner_account = sgqlc.types.Field('BlockWinnerAccountUpdateInput', graphql_name='winnerAccount')
    winner_account_unset = sgqlc.types.Field(Boolean, graphql_name='winnerAccount_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    creator_unset = sgqlc.types.Field(Boolean, graphql_name='creator_unset')
    state_hash_field_unset = sgqlc.types.Field(Boolean, graphql_name='stateHashField_unset')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    received_time = sgqlc.types.Field(DateTime, graphql_name='receivedTime')


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
    __field_names__ = ('total_in', 'locked_lte', 'liquid_lt', 'state_hash_lte', 'unknown_ne', 'unknown_gte', 'state_hash_ne', 'block_height_nin', 'locked_gte', 'block_height_exists', 'or_', 'block_height_lt', 'state_hash_lt', 'unknown_nin', 'total_exists', 'state_hash_nin', 'state_hash_gt', 'liquid_ne', 'state_hash', 'unknown_in', 'total_lte', 'unknown_lt', 'block_height', 'liquid_gte', 'state_hash_gte', 'locked_exists', 'total_ne', 'and_', 'block_height_lte', 'liquid_nin', 'total', 'block_height_gte', 'liquid_in', 'unknown_gt', 'unknown_lte', 'locked_gt', 'block_height_gt', 'block_height_ne', 'locked_lt', 'locked_ne', 'locked', 'state_hash_exists', 'total_gte', 'state_hash_in', 'liquid', 'unknown_exists', 'locked_nin', 'locked_in', 'total_nin', 'total_gt', 'total_lt', 'liquid_lte', 'block_height_in', 'liquid_exists', 'unknown', 'liquid_gt')
    total_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='total_in')
    locked_lte = sgqlc.types.Field(Long, graphql_name='locked_lte')
    liquid_lt = sgqlc.types.Field(Int, graphql_name='liquid_lt')
    state_hash_lte = sgqlc.types.Field(String, graphql_name='stateHash_lte')
    unknown_ne = sgqlc.types.Field(Long, graphql_name='unknown_ne')
    unknown_gte = sgqlc.types.Field(Long, graphql_name='unknown_gte')
    state_hash_ne = sgqlc.types.Field(String, graphql_name='stateHash_ne')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    locked_gte = sgqlc.types.Field(Long, graphql_name='locked_gte')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountBalanceQueryInput')), graphql_name='OR')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    state_hash_lt = sgqlc.types.Field(String, graphql_name='stateHash_lt')
    unknown_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='unknown_nin')
    total_exists = sgqlc.types.Field(Boolean, graphql_name='total_exists')
    state_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_nin')
    state_hash_gt = sgqlc.types.Field(String, graphql_name='stateHash_gt')
    liquid_ne = sgqlc.types.Field(Int, graphql_name='liquid_ne')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    unknown_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='unknown_in')
    total_lte = sgqlc.types.Field(Long, graphql_name='total_lte')
    unknown_lt = sgqlc.types.Field(Long, graphql_name='unknown_lt')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    liquid_gte = sgqlc.types.Field(Int, graphql_name='liquid_gte')
    state_hash_gte = sgqlc.types.Field(String, graphql_name='stateHash_gte')
    locked_exists = sgqlc.types.Field(Boolean, graphql_name='locked_exists')
    total_ne = sgqlc.types.Field(Long, graphql_name='total_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountBalanceQueryInput')), graphql_name='AND')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    liquid_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='liquid_nin')
    total = sgqlc.types.Field(Long, graphql_name='total')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    liquid_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='liquid_in')
    unknown_gt = sgqlc.types.Field(Long, graphql_name='unknown_gt')
    unknown_lte = sgqlc.types.Field(Long, graphql_name='unknown_lte')
    locked_gt = sgqlc.types.Field(Long, graphql_name='locked_gt')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    locked_lt = sgqlc.types.Field(Long, graphql_name='locked_lt')
    locked_ne = sgqlc.types.Field(Long, graphql_name='locked_ne')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    state_hash_exists = sgqlc.types.Field(Boolean, graphql_name='stateHash_exists')
    total_gte = sgqlc.types.Field(Long, graphql_name='total_gte')
    state_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='stateHash_in')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    unknown_exists = sgqlc.types.Field(Boolean, graphql_name='unknown_exists')
    locked_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='locked_nin')
    locked_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='locked_in')
    total_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='total_nin')
    total_gt = sgqlc.types.Field(Long, graphql_name='total_gt')
    total_lt = sgqlc.types.Field(Long, graphql_name='total_lt')
    liquid_lte = sgqlc.types.Field(Int, graphql_name='liquid_lte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    liquid_exists = sgqlc.types.Field(Boolean, graphql_name='liquid_exists')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    liquid_gt = sgqlc.types.Field(Int, graphql_name='liquid_gt')


class BlockWinnerAccountBalanceUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('block_height_inc', 'total_unset', 'block_height_unset', 'liquid_unset', 'state_hash', 'liquid_inc', 'locked_unset', 'state_hash_unset', 'total', 'block_height', 'liquid', 'locked', 'unknown', 'unknown_unset')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    total_unset = sgqlc.types.Field(Boolean, graphql_name='total_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    liquid_unset = sgqlc.types.Field(Boolean, graphql_name='liquid_unset')
    state_hash = sgqlc.types.Field(String, graphql_name='stateHash')
    liquid_inc = sgqlc.types.Field(Int, graphql_name='liquid_inc')
    locked_unset = sgqlc.types.Field(Boolean, graphql_name='locked_unset')
    state_hash_unset = sgqlc.types.Field(Boolean, graphql_name='stateHash_unset')
    total = sgqlc.types.Field(Long, graphql_name='total')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    liquid = sgqlc.types.Field(Int, graphql_name='liquid')
    locked = sgqlc.types.Field(Long, graphql_name='locked')
    unknown = sgqlc.types.Field(Long, graphql_name='unknown')
    unknown_unset = sgqlc.types.Field(Boolean, graphql_name='unknown_unset')


class BlockWinnerAccountInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key', 'balance')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceInsertInput, graphql_name='balance')


class BlockWinnerAccountQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('balance_exists', 'public_key_gt', 'public_key', 'public_key_exists', 'public_key_ne', 'public_key_gte', 'and_', 'balance', 'public_key_in', 'or_', 'public_key_lt', 'public_key_nin', 'public_key_lte')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountQueryInput')), graphql_name='AND')
    balance = sgqlc.types.Field(BlockWinnerAccountBalanceQueryInput, graphql_name='balance')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BlockWinnerAccountQueryInput')), graphql_name='OR')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')


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
    __field_names__ = ('work_ids', 'block_height', 'block', 'canonical', 'date_time', 'fee', 'prover')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    block = sgqlc.types.Field(SnarkBlockStateHashRelationInput, graphql_name='block')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    prover = sgqlc.types.Field(String, graphql_name='prover')


class SnarkQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('prover_gt', 'date_time_exists', 'canonical_ne', 'fee_ne', 'date_time_nin', 'prover_lt', 'fee', 'block_height', 'date_time_in', 'and_', 'prover_lte', 'block_height_in', 'prover', 'block_exists', 'canonical_exists', 'fee_lte', 'fee_gt', 'block_height_lte', 'date_time_lte', 'block_height_lt', 'block_height_exists', 'work_ids', 'block_height_nin', 'fee_exists', 'prover_in', 'block_height_gte', 'fee_lt', 'date_time_gte', 'block_height_gt', 'fee_in', 'prover_nin', 'block_height_ne', 'date_time_ne', 'date_time_lt', 'prover_gte', 'prover_exists', 'or_', 'prover_ne', 'work_ids_in', 'date_time_gt', 'block', 'fee_nin', 'date_time', 'work_ids_exists', 'work_ids_nin', 'canonical', 'fee_gte')
    prover_gt = sgqlc.types.Field(String, graphql_name='prover_gt')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    fee_ne = sgqlc.types.Field(Float, graphql_name='fee_ne')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    prover_lt = sgqlc.types.Field(String, graphql_name='prover_lt')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SnarkQueryInput')), graphql_name='AND')
    prover_lte = sgqlc.types.Field(String, graphql_name='prover_lte')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    block_exists = sgqlc.types.Field(Boolean, graphql_name='block_exists')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    fee_lte = sgqlc.types.Field(Float, graphql_name='fee_lte')
    fee_gt = sgqlc.types.Field(Float, graphql_name='fee_gt')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    prover_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_in')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    fee_lt = sgqlc.types.Field(Float, graphql_name='fee_lt')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_in')
    prover_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='prover_nin')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    prover_gte = sgqlc.types.Field(String, graphql_name='prover_gte')
    prover_exists = sgqlc.types.Field(Boolean, graphql_name='prover_exists')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('SnarkQueryInput')), graphql_name='OR')
    prover_ne = sgqlc.types.Field(String, graphql_name='prover_ne')
    work_ids_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_in')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    block = sgqlc.types.Field(BlockQueryInput, graphql_name='block')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='fee_nin')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    work_ids_exists = sgqlc.types.Field(Boolean, graphql_name='workIds_exists')
    work_ids_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds_nin')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    fee_gte = sgqlc.types.Field(Float, graphql_name='fee_gte')


class SnarkUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('fee_unset', 'block', 'prover', 'block_height_inc', 'block_unset', 'work_ids', 'canonical', 'block_height_unset', 'block_height', 'fee_inc', 'canonical_unset', 'prover_unset', 'date_time_unset', 'work_ids_unset', 'date_time', 'fee')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    block = sgqlc.types.Field(SnarkBlockStateHashRelationInput, graphql_name='block')
    prover = sgqlc.types.Field(String, graphql_name='prover')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    block_unset = sgqlc.types.Field(Boolean, graphql_name='block_unset')
    work_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='workIds')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    fee_inc = sgqlc.types.Field(Float, graphql_name='fee_inc')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    prover_unset = sgqlc.types.Field(Boolean, graphql_name='prover_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    work_ids_unset = sgqlc.types.Field(Boolean, graphql_name='workIds_unset')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class StakeInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receipt_chain_hash', 'ledger_hash', 'timing', 'delegate', 'token', 'pk', 'voting_for', 'chain_id', 'balance', 'nonce', 'permissions', 'epoch', 'public_key')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    timing = sgqlc.types.Field('StakeTimingInsertInput', graphql_name='timing')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    token = sgqlc.types.Field(Int, graphql_name='token')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field('StakePermissionInsertInput', graphql_name='permissions')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')


class StakePermissionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('set_verification_key', 'stake', 'edit_state', 'send', 'set_delegate', 'set_permissions')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')


class StakePermissionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('edit_state_lt', 'send_lt', 'and_', 'send_gte', 'set_delegate_in', 'edit_state_exists', 'stake_exists', 'send_in', 'set_verification_key_gte', 'send_ne', 'or_', 'set_verification_key_nin', 'set_delegate_nin', 'set_permissions_exists', 'set_permissions', 'set_permissions_lt', 'send_gt', 'set_permissions_in', 'set_verification_key_gt', 'edit_state_nin', 'set_verification_key', 'set_delegate_gt', 'set_permissions_gte', 'set_verification_key_exists', 'edit_state_gt', 'set_delegate', 'stake_ne', 'edit_state_ne', 'set_delegate_exists', 'send_nin', 'set_verification_key_lte', 'send_lte', 'set_permissions_ne', 'edit_state_gte', 'send', 'stake', 'set_permissions_lte', 'set_verification_key_in', 'edit_state', 'set_delegate_gte', 'set_permissions_gt', 'edit_state_lte', 'edit_state_in', 'set_delegate_lte', 'set_verification_key_ne', 'set_delegate_lt', 'set_verification_key_lt', 'set_delegate_ne', 'set_permissions_nin', 'send_exists')
    edit_state_lt = sgqlc.types.Field(String, graphql_name='edit_state_lt')
    send_lt = sgqlc.types.Field(String, graphql_name='send_lt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakePermissionQueryInput')), graphql_name='AND')
    send_gte = sgqlc.types.Field(String, graphql_name='send_gte')
    set_delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_in')
    edit_state_exists = sgqlc.types.Field(Boolean, graphql_name='edit_state_exists')
    stake_exists = sgqlc.types.Field(Boolean, graphql_name='stake_exists')
    send_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_in')
    set_verification_key_gte = sgqlc.types.Field(String, graphql_name='set_verification_key_gte')
    send_ne = sgqlc.types.Field(String, graphql_name='send_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakePermissionQueryInput')), graphql_name='OR')
    set_verification_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_nin')
    set_delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_delegate_nin')
    set_permissions_exists = sgqlc.types.Field(Boolean, graphql_name='set_permissions_exists')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_permissions_lt = sgqlc.types.Field(String, graphql_name='set_permissions_lt')
    send_gt = sgqlc.types.Field(String, graphql_name='send_gt')
    set_permissions_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_in')
    set_verification_key_gt = sgqlc.types.Field(String, graphql_name='set_verification_key_gt')
    edit_state_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_nin')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    set_delegate_gt = sgqlc.types.Field(String, graphql_name='set_delegate_gt')
    set_permissions_gte = sgqlc.types.Field(String, graphql_name='set_permissions_gte')
    set_verification_key_exists = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_exists')
    edit_state_gt = sgqlc.types.Field(String, graphql_name='edit_state_gt')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    stake_ne = sgqlc.types.Field(Boolean, graphql_name='stake_ne')
    edit_state_ne = sgqlc.types.Field(String, graphql_name='edit_state_ne')
    set_delegate_exists = sgqlc.types.Field(Boolean, graphql_name='set_delegate_exists')
    send_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='send_nin')
    set_verification_key_lte = sgqlc.types.Field(String, graphql_name='set_verification_key_lte')
    send_lte = sgqlc.types.Field(String, graphql_name='send_lte')
    set_permissions_ne = sgqlc.types.Field(String, graphql_name='set_permissions_ne')
    edit_state_gte = sgqlc.types.Field(String, graphql_name='edit_state_gte')
    send = sgqlc.types.Field(String, graphql_name='send')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')
    set_permissions_lte = sgqlc.types.Field(String, graphql_name='set_permissions_lte')
    set_verification_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_verification_key_in')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    set_delegate_gte = sgqlc.types.Field(String, graphql_name='set_delegate_gte')
    set_permissions_gt = sgqlc.types.Field(String, graphql_name='set_permissions_gt')
    edit_state_lte = sgqlc.types.Field(String, graphql_name='edit_state_lte')
    edit_state_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='edit_state_in')
    set_delegate_lte = sgqlc.types.Field(String, graphql_name='set_delegate_lte')
    set_verification_key_ne = sgqlc.types.Field(String, graphql_name='set_verification_key_ne')
    set_delegate_lt = sgqlc.types.Field(String, graphql_name='set_delegate_lt')
    set_verification_key_lt = sgqlc.types.Field(String, graphql_name='set_verification_key_lt')
    set_delegate_ne = sgqlc.types.Field(String, graphql_name='set_delegate_ne')
    set_permissions_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='set_permissions_nin')
    send_exists = sgqlc.types.Field(Boolean, graphql_name='send_exists')


class StakePermissionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('send', 'set_verification_key_unset', 'edit_state_unset', 'send_unset', 'edit_state', 'set_delegate', 'set_delegate_unset', 'stake_unset', 'set_permissions', 'set_permissions_unset', 'set_verification_key', 'stake')
    send = sgqlc.types.Field(String, graphql_name='send')
    set_verification_key_unset = sgqlc.types.Field(Boolean, graphql_name='set_verification_key_unset')
    edit_state_unset = sgqlc.types.Field(Boolean, graphql_name='edit_state_unset')
    send_unset = sgqlc.types.Field(Boolean, graphql_name='send_unset')
    edit_state = sgqlc.types.Field(String, graphql_name='edit_state')
    set_delegate = sgqlc.types.Field(String, graphql_name='set_delegate')
    set_delegate_unset = sgqlc.types.Field(Boolean, graphql_name='set_delegate_unset')
    stake_unset = sgqlc.types.Field(Boolean, graphql_name='stake_unset')
    set_permissions = sgqlc.types.Field(String, graphql_name='set_permissions')
    set_permissions_unset = sgqlc.types.Field(Boolean, graphql_name='set_permissions_unset')
    set_verification_key = sgqlc.types.Field(String, graphql_name='set_verification_key')
    stake = sgqlc.types.Field(Boolean, graphql_name='stake')


class StakeQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_nin', 'ledger_hash_exists', 'chain_id_nin', 'receipt_chain_hash_exists', 'voting_for_lte', 'nonce_gte', 'timing_exists', 'token_exists', 'voting_for_gt', 'epoch_in', 'epoch', 'ledger_hash_in', 'nonce_lte', 'receipt_chain_hash_gt', 'pk_gte', 'delegate_nin', 'receipt_chain_hash_ne', 'nonce_in', 'balance_nin', 'public_key_gte', 'delegate_exists', 'chain_id_in', 'ledger_hash_lte', 'pk_lte', 'epoch_gte', 'balance_exists', 'receipt_chain_hash_in', 'public_key_gt', 'balance_gt', 'epoch_exists', 'token_gte', 'epoch_lt', 'chain_id', 'pk_in', 'pk_lt', 'balance', 'token_lte', 'delegate_lte', 'delegate_in', 'voting_for_lt', 'permissions_exists', 'balance_ne', 'ledger_hash_gte', 'delegate', 'nonce_nin', 'chain_id_exists', 'delegate_gt', 'chain_id_lt', 'chain_id_lte', 'pk', 'receipt_chain_hash_lte', 'receipt_chain_hash_nin', 'ledger_hash_gt', 'chain_id_ne', 'public_key_exists', 'epoch_nin', 'voting_for', 'pk_ne', 'nonce_gt', 'voting_for_in', 'ledger_hash', 'or_', 'chain_id_gte', 'token', 'epoch_lte', 'balance_lt', 'timing', 'voting_for_ne', 'token_gt', 'public_key_ne', 'receipt_chain_hash_gte', 'delegate_ne', 'receipt_chain_hash', 'token_in', 'epoch_gt', 'public_key_lte', 'public_key', 'voting_for_gte', 'token_lt', 'balance_in', 'voting_for_nin', 'public_key_in', 'receipt_chain_hash_lt', 'token_nin', 'epoch_ne', 'balance_lte', 'pk_gt', 'balance_gte', 'voting_for_exists', 'permissions', 'delegate_gte', 'pk_nin', 'ledger_hash_ne', 'nonce_exists', 'chain_id_gt', 'token_ne', 'public_key_lt', 'delegate_lt', 'nonce_lt', 'ledger_hash_nin', 'and_', 'nonce_ne', 'nonce', 'ledger_hash_lt', 'pk_exists')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_nin')
    ledger_hash_exists = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_exists')
    chain_id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chainId_nin')
    receipt_chain_hash_exists = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_exists')
    voting_for_lte = sgqlc.types.Field(String, graphql_name='voting_for_lte')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    timing_exists = sgqlc.types.Field(Boolean, graphql_name='timing_exists')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    voting_for_gt = sgqlc.types.Field(String, graphql_name='voting_for_gt')
    epoch_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_in')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    ledger_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_in')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    receipt_chain_hash_gt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gt')
    pk_gte = sgqlc.types.Field(String, graphql_name='pk_gte')
    delegate_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_nin')
    receipt_chain_hash_ne = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_ne')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_nin')
    public_key_gte = sgqlc.types.Field(String, graphql_name='public_key_gte')
    delegate_exists = sgqlc.types.Field(Boolean, graphql_name='delegate_exists')
    chain_id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='chainId_in')
    ledger_hash_lte = sgqlc.types.Field(String, graphql_name='ledgerHash_lte')
    pk_lte = sgqlc.types.Field(String, graphql_name='pk_lte')
    epoch_gte = sgqlc.types.Field(Int, graphql_name='epoch_gte')
    balance_exists = sgqlc.types.Field(Boolean, graphql_name='balance_exists')
    receipt_chain_hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_in')
    public_key_gt = sgqlc.types.Field(String, graphql_name='public_key_gt')
    balance_gt = sgqlc.types.Field(Float, graphql_name='balance_gt')
    epoch_exists = sgqlc.types.Field(Boolean, graphql_name='epoch_exists')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    epoch_lt = sgqlc.types.Field(Int, graphql_name='epoch_lt')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    pk_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pk_in')
    pk_lt = sgqlc.types.Field(String, graphql_name='pk_lt')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    delegate_lte = sgqlc.types.Field(String, graphql_name='delegate_lte')
    delegate_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='delegate_in')
    voting_for_lt = sgqlc.types.Field(String, graphql_name='voting_for_lt')
    permissions_exists = sgqlc.types.Field(Boolean, graphql_name='permissions_exists')
    balance_ne = sgqlc.types.Field(Float, graphql_name='balance_ne')
    ledger_hash_gte = sgqlc.types.Field(String, graphql_name='ledgerHash_gte')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    chain_id_exists = sgqlc.types.Field(Boolean, graphql_name='chainId_exists')
    delegate_gt = sgqlc.types.Field(String, graphql_name='delegate_gt')
    chain_id_lt = sgqlc.types.Field(String, graphql_name='chainId_lt')
    chain_id_lte = sgqlc.types.Field(String, graphql_name='chainId_lte')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    receipt_chain_hash_lte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lte')
    receipt_chain_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='receipt_chain_hash_nin')
    ledger_hash_gt = sgqlc.types.Field(String, graphql_name='ledgerHash_gt')
    chain_id_ne = sgqlc.types.Field(String, graphql_name='chainId_ne')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='public_key_exists')
    epoch_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='epoch_nin')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    pk_ne = sgqlc.types.Field(String, graphql_name='pk_ne')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    voting_for_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_in')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeQueryInput')), graphql_name='OR')
    chain_id_gte = sgqlc.types.Field(String, graphql_name='chainId_gte')
    token = sgqlc.types.Field(Int, graphql_name='token')
    epoch_lte = sgqlc.types.Field(Int, graphql_name='epoch_lte')
    balance_lt = sgqlc.types.Field(Float, graphql_name='balance_lt')
    timing = sgqlc.types.Field('StakeTimingQueryInput', graphql_name='timing')
    voting_for_ne = sgqlc.types.Field(String, graphql_name='voting_for_ne')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    public_key_ne = sgqlc.types.Field(String, graphql_name='public_key_ne')
    receipt_chain_hash_gte = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_gte')
    delegate_ne = sgqlc.types.Field(String, graphql_name='delegate_ne')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    epoch_gt = sgqlc.types.Field(Int, graphql_name='epoch_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='public_key_lte')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    voting_for_gte = sgqlc.types.Field(String, graphql_name='voting_for_gte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='balance_in')
    voting_for_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='voting_for_nin')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='public_key_in')
    receipt_chain_hash_lt = sgqlc.types.Field(String, graphql_name='receipt_chain_hash_lt')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    epoch_ne = sgqlc.types.Field(Int, graphql_name='epoch_ne')
    balance_lte = sgqlc.types.Field(Float, graphql_name='balance_lte')
    pk_gt = sgqlc.types.Field(String, graphql_name='pk_gt')
    balance_gte = sgqlc.types.Field(Float, graphql_name='balance_gte')
    voting_for_exists = sgqlc.types.Field(Boolean, graphql_name='voting_for_exists')
    permissions = sgqlc.types.Field(StakePermissionQueryInput, graphql_name='permissions')
    delegate_gte = sgqlc.types.Field(String, graphql_name='delegate_gte')
    pk_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pk_nin')
    ledger_hash_ne = sgqlc.types.Field(String, graphql_name='ledgerHash_ne')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    chain_id_gt = sgqlc.types.Field(String, graphql_name='chainId_gt')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    public_key_lt = sgqlc.types.Field(String, graphql_name='public_key_lt')
    delegate_lt = sgqlc.types.Field(String, graphql_name='delegate_lt')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    ledger_hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='ledgerHash_nin')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeQueryInput')), graphql_name='AND')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    ledger_hash_lt = sgqlc.types.Field(String, graphql_name='ledgerHash_lt')
    pk_exists = sgqlc.types.Field(Boolean, graphql_name='pk_exists')


class StakeTimingInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('timed_epoch_end', 'vesting_period', 'initial_minimum_balance', 'vesting_increment', 'untimed_slot', 'cliff_amount', 'timed_in_epoch', 'cliff_time', 'timed_weighting')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')


class StakeTimingQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('initial_minimum_balance', 'initial_minimum_balance_lt', 'untimed_slot_in', 'vesting_increment_lte', 'or_', 'initial_minimum_balance_gte', 'timed_weighting', 'untimed_slot_gt', 'vesting_increment_exists', 'untimed_slot_gte', 'timed_weighting_gt', 'vesting_increment_nin', 'cliff_amount_ne', 'cliff_amount_nin', 'cliff_time_lt', 'vesting_period_lt', 'timed_weighting_ne', 'vesting_period', 'vesting_period_nin', 'vesting_increment', 'vesting_increment_gt', 'cliff_time', 'timed_epoch_end', 'untimed_slot', 'initial_minimum_balance_exists', 'cliff_amount_gte', 'timed_in_epoch_exists', 'cliff_amount_lte', 'initial_minimum_balance_nin', 'cliff_time_nin', 'initial_minimum_balance_in', 'and_', 'vesting_period_gte', 'vesting_increment_lt', 'vesting_increment_gte', 'cliff_amount_lt', 'vesting_period_lte', 'cliff_time_lte', 'timed_in_epoch_ne', 'timed_epoch_end_exists', 'timed_weighting_nin', 'timed_epoch_end_ne', 'cliff_time_exists', 'cliff_time_gt', 'timed_weighting_lte', 'timed_weighting_in', 'cliff_time_gte', 'vesting_period_exists', 'untimed_slot_exists', 'cliff_time_ne', 'timed_weighting_exists', 'cliff_amount_exists', 'cliff_amount_in', 'vesting_period_gt', 'untimed_slot_lte', 'timed_weighting_lt', 'cliff_amount', 'untimed_slot_lt', 'untimed_slot_ne', 'initial_minimum_balance_gt', 'vesting_increment_ne', 'vesting_increment_in', 'vesting_period_ne', 'untimed_slot_nin', 'timed_in_epoch', 'initial_minimum_balance_ne', 'initial_minimum_balance_lte', 'timed_weighting_gte', 'vesting_period_in', 'cliff_amount_gt', 'cliff_time_in')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    initial_minimum_balance_lt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lt')
    untimed_slot_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='untimed_slot_in')
    vesting_increment_lte = sgqlc.types.Field(Float, graphql_name='vesting_increment_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeTimingQueryInput')), graphql_name='OR')
    initial_minimum_balance_gte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gte')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    untimed_slot_gt = sgqlc.types.Field(Int, graphql_name='untimed_slot_gt')
    vesting_increment_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_exists')
    untimed_slot_gte = sgqlc.types.Field(Int, graphql_name='untimed_slot_gte')
    timed_weighting_gt = sgqlc.types.Field(Float, graphql_name='timed_weighting_gt')
    vesting_increment_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_nin')
    cliff_amount_ne = sgqlc.types.Field(Float, graphql_name='cliff_amount_ne')
    cliff_amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_nin')
    cliff_time_lt = sgqlc.types.Field(Int, graphql_name='cliff_time_lt')
    vesting_period_lt = sgqlc.types.Field(Int, graphql_name='vesting_period_lt')
    timed_weighting_ne = sgqlc.types.Field(Float, graphql_name='timed_weighting_ne')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    vesting_period_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_nin')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    vesting_increment_gt = sgqlc.types.Field(Float, graphql_name='vesting_increment_gt')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    initial_minimum_balance_exists = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_exists')
    cliff_amount_gte = sgqlc.types.Field(Float, graphql_name='cliff_amount_gte')
    timed_in_epoch_exists = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_exists')
    cliff_amount_lte = sgqlc.types.Field(Float, graphql_name='cliff_amount_lte')
    initial_minimum_balance_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_nin')
    cliff_time_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_nin')
    initial_minimum_balance_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='initial_minimum_balance_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StakeTimingQueryInput')), graphql_name='AND')
    vesting_period_gte = sgqlc.types.Field(Int, graphql_name='vesting_period_gte')
    vesting_increment_lt = sgqlc.types.Field(Float, graphql_name='vesting_increment_lt')
    vesting_increment_gte = sgqlc.types.Field(Float, graphql_name='vesting_increment_gte')
    cliff_amount_lt = sgqlc.types.Field(Float, graphql_name='cliff_amount_lt')
    vesting_period_lte = sgqlc.types.Field(Int, graphql_name='vesting_period_lte')
    cliff_time_lte = sgqlc.types.Field(Int, graphql_name='cliff_time_lte')
    timed_in_epoch_ne = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_ne')
    timed_epoch_end_exists = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_exists')
    timed_weighting_nin = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='timed_weighting_nin')
    timed_epoch_end_ne = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_ne')
    cliff_time_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_time_exists')
    cliff_time_gt = sgqlc.types.Field(Int, graphql_name='cliff_time_gt')
    timed_weighting_lte = sgqlc.types.Field(Float, graphql_name='timed_weighting_lte')
    timed_weighting_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='timed_weighting_in')
    cliff_time_gte = sgqlc.types.Field(Int, graphql_name='cliff_time_gte')
    vesting_period_exists = sgqlc.types.Field(Boolean, graphql_name='vesting_period_exists')
    untimed_slot_exists = sgqlc.types.Field(Boolean, graphql_name='untimed_slot_exists')
    cliff_time_ne = sgqlc.types.Field(Int, graphql_name='cliff_time_ne')
    timed_weighting_exists = sgqlc.types.Field(Boolean, graphql_name='timed_weighting_exists')
    cliff_amount_exists = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_exists')
    cliff_amount_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cliff_amount_in')
    vesting_period_gt = sgqlc.types.Field(Int, graphql_name='vesting_period_gt')
    untimed_slot_lte = sgqlc.types.Field(Int, graphql_name='untimed_slot_lte')
    timed_weighting_lt = sgqlc.types.Field(Float, graphql_name='timed_weighting_lt')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    untimed_slot_lt = sgqlc.types.Field(Int, graphql_name='untimed_slot_lt')
    untimed_slot_ne = sgqlc.types.Field(Int, graphql_name='untimed_slot_ne')
    initial_minimum_balance_gt = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_gt')
    vesting_increment_ne = sgqlc.types.Field(Float, graphql_name='vesting_increment_ne')
    vesting_increment_in = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='vesting_increment_in')
    vesting_period_ne = sgqlc.types.Field(Int, graphql_name='vesting_period_ne')
    untimed_slot_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='untimed_slot_nin')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    initial_minimum_balance_ne = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_ne')
    initial_minimum_balance_lte = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_lte')
    timed_weighting_gte = sgqlc.types.Field(Float, graphql_name='timed_weighting_gte')
    vesting_period_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='vesting_period_in')
    cliff_amount_gt = sgqlc.types.Field(Float, graphql_name='cliff_amount_gt')
    cliff_time_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='cliff_time_in')


class StakeTimingUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('timed_in_epoch', 'timed_weighting_inc', 'cliff_amount_unset', 'initial_minimum_balance_unset', 'timed_epoch_end', 'cliff_time', 'initial_minimum_balance_inc', 'untimed_slot_unset', 'cliff_amount', 'timed_in_epoch_unset', 'untimed_slot', 'cliff_time_inc', 'untimed_slot_inc', 'vesting_increment_inc', 'timed_weighting_unset', 'vesting_increment', 'initial_minimum_balance', 'vesting_period', 'vesting_period_inc', 'vesting_increment_unset', 'vesting_period_unset', 'cliff_time_unset', 'timed_weighting', 'timed_epoch_end_unset', 'cliff_amount_inc')
    timed_in_epoch = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch')
    timed_weighting_inc = sgqlc.types.Field(Float, graphql_name='timed_weighting_inc')
    cliff_amount_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_amount_unset')
    initial_minimum_balance_unset = sgqlc.types.Field(Boolean, graphql_name='initial_minimum_balance_unset')
    timed_epoch_end = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end')
    cliff_time = sgqlc.types.Field(Int, graphql_name='cliff_time')
    initial_minimum_balance_inc = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance_inc')
    untimed_slot_unset = sgqlc.types.Field(Boolean, graphql_name='untimed_slot_unset')
    cliff_amount = sgqlc.types.Field(Float, graphql_name='cliff_amount')
    timed_in_epoch_unset = sgqlc.types.Field(Boolean, graphql_name='timed_in_epoch_unset')
    untimed_slot = sgqlc.types.Field(Int, graphql_name='untimed_slot')
    cliff_time_inc = sgqlc.types.Field(Int, graphql_name='cliff_time_inc')
    untimed_slot_inc = sgqlc.types.Field(Int, graphql_name='untimed_slot_inc')
    vesting_increment_inc = sgqlc.types.Field(Float, graphql_name='vesting_increment_inc')
    timed_weighting_unset = sgqlc.types.Field(Boolean, graphql_name='timed_weighting_unset')
    vesting_increment = sgqlc.types.Field(Float, graphql_name='vesting_increment')
    initial_minimum_balance = sgqlc.types.Field(Float, graphql_name='initial_minimum_balance')
    vesting_period = sgqlc.types.Field(Int, graphql_name='vesting_period')
    vesting_period_inc = sgqlc.types.Field(Int, graphql_name='vesting_period_inc')
    vesting_increment_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_increment_unset')
    vesting_period_unset = sgqlc.types.Field(Boolean, graphql_name='vesting_period_unset')
    cliff_time_unset = sgqlc.types.Field(Boolean, graphql_name='cliff_time_unset')
    timed_weighting = sgqlc.types.Field(Float, graphql_name='timed_weighting')
    timed_epoch_end_unset = sgqlc.types.Field(Boolean, graphql_name='timed_epoch_end_unset')
    cliff_amount_inc = sgqlc.types.Field(Float, graphql_name='cliff_amount_inc')


class StakeUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('delegate', 'token_unset', 'chain_id', 'balance_inc', 'receipt_chain_hash', 'epoch', 'timing_unset', 'public_key', 'ledger_hash', 'ledger_hash_unset', 'pk_unset', 'voting_for', 'delegate_unset', 'nonce_inc', 'token_inc', 'token', 'epoch_unset', 'timing', 'receipt_chain_hash_unset', 'nonce_unset', 'chain_id_unset', 'epoch_inc', 'permissions_unset', 'nonce', 'permissions', 'voting_for_unset', 'balance', 'pk', 'public_key_unset', 'balance_unset')
    delegate = sgqlc.types.Field(String, graphql_name='delegate')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    chain_id = sgqlc.types.Field(String, graphql_name='chainId')
    balance_inc = sgqlc.types.Field(Float, graphql_name='balance_inc')
    receipt_chain_hash = sgqlc.types.Field(String, graphql_name='receipt_chain_hash')
    epoch = sgqlc.types.Field(Int, graphql_name='epoch')
    timing_unset = sgqlc.types.Field(Boolean, graphql_name='timing_unset')
    public_key = sgqlc.types.Field(String, graphql_name='public_key')
    ledger_hash = sgqlc.types.Field(String, graphql_name='ledgerHash')
    ledger_hash_unset = sgqlc.types.Field(Boolean, graphql_name='ledgerHash_unset')
    pk_unset = sgqlc.types.Field(Boolean, graphql_name='pk_unset')
    voting_for = sgqlc.types.Field(String, graphql_name='voting_for')
    delegate_unset = sgqlc.types.Field(Boolean, graphql_name='delegate_unset')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token = sgqlc.types.Field(Int, graphql_name='token')
    epoch_unset = sgqlc.types.Field(Boolean, graphql_name='epoch_unset')
    timing = sgqlc.types.Field(StakeTimingUpdateInput, graphql_name='timing')
    receipt_chain_hash_unset = sgqlc.types.Field(Boolean, graphql_name='receipt_chain_hash_unset')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    chain_id_unset = sgqlc.types.Field(Boolean, graphql_name='chainId_unset')
    epoch_inc = sgqlc.types.Field(Int, graphql_name='epoch_inc')
    permissions_unset = sgqlc.types.Field(Boolean, graphql_name='permissions_unset')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    permissions = sgqlc.types.Field(StakePermissionUpdateInput, graphql_name='permissions')
    voting_for_unset = sgqlc.types.Field(Boolean, graphql_name='voting_for_unset')
    balance = sgqlc.types.Field(Float, graphql_name='balance')
    pk = sgqlc.types.Field(String, graphql_name='pk')
    public_key_unset = sgqlc.types.Field(Boolean, graphql_name='public_key_unset')
    balance_unset = sgqlc.types.Field(Boolean, graphql_name='balance_unset')


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
    __field_names__ = ('token', 'token_gt', 'token_gte', 'token_in', 'or_', 'token_lt', 'token_lte', 'and_', 'token_exists', 'token_ne', 'token_nin')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFeePayerQueryInput')), graphql_name='OR')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFeePayerQueryInput')), graphql_name='AND')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')


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
    __field_names__ = ('token_lte', 'token_ne', 'and_', 'or_', 'token_exists', 'token_in', 'token_lt', 'token_gte', 'token_nin', 'token', 'token_gt')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFromAccountQueryInput')), graphql_name='AND')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionFromAccountQueryInput')), graphql_name='OR')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')


class TransactionFromAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class TransactionInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('to', 'is_delegation', 'nonce', 'source', 'to_account', 'token', 'fee_payer', 'from_account', 'fee', 'amount', 'failure_reason', 'date_time', 'kind', 'hash', 'block_height', 'memo', 'receiver', 'id', 'fee_token', 'canonical', 'block', 'from_')
    to = sgqlc.types.Field(String, graphql_name='to')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    source = sgqlc.types.Field('TransactionSourceInsertInput', graphql_name='source')
    to_account = sgqlc.types.Field('TransactionToAccountInsertInput', graphql_name='toAccount')
    token = sgqlc.types.Field(Int, graphql_name='token')
    fee_payer = sgqlc.types.Field(TransactionFeePayerInsertInput, graphql_name='feePayer')
    from_account = sgqlc.types.Field(TransactionFromAccountInsertInput, graphql_name='fromAccount')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    receiver = sgqlc.types.Field('TransactionReceiverInsertInput', graphql_name='receiver')
    id = sgqlc.types.Field(String, graphql_name='id')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    block = sgqlc.types.Field(TransactionBlockStateHashRelationInput, graphql_name='block')
    from_ = sgqlc.types.Field(String, graphql_name='from')


class TransactionQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('amount_gte', 'kind', 'fee_token_lt', 'token_ne', 'fee_token_ne', 'hash_lte', 'amount_in', 'fee_gt', 'kind_ne', 'to_account', 'memo_exists', 'fee_payer_exists', 'token_lt', 'hash_ne', 'amount_exists', 'fee_token_exists', 'to_lt', 'kind_lt', 'hash_nin', 'block_height_lt', 'token_exists', 'date_time_in', 'canonical', 'nonce', 'from_exists', 'canonical_exists', 'from_', 'from_ne', 'to_nin', 'nonce_lte', 'fee_token_gte', 'id_nin', 'amount', 'kind_lte', 'memo_lte', 'failure_reason_lt', 'kind_gt', 'id_gt', 'from_lt', 'receiver_exists', 'id_in', 'failure_reason_gte', 'kind_nin', 'from_gte', 'canonical_ne', 'token', 'nonce_exists', 'date_time_gte', 'kind_gte', 'fee_token', 'from_lte', 'is_delegation', 'block_height_lte', 'is_delegation_exists', 'to_in', 'date_time_lt', 'hash_in', 'fee_payer', 'from_gt', 'memo_gt', 'hash_exists', 'fee_lt', 'id_ne', 'amount_ne', 'block_exists', 'block_height_gt', 'hash_lt', 'failure_reason_nin', 'nonce_gt', 'is_delegation_ne', 'block_height_nin', 'to_ne', 'fee_lte', 'source_exists', 'date_time_lte', 'date_time', 'nonce_gte', 'from_account_exists', 'id_exists', 'fee_ne', 'failure_reason_ne', 'amount_gt', 'fee_token_gt', 'fee_exists', 'block_height', 'kind_in', 'fee_in', 'block_height_in', 'to_exists', 'date_time_gt', 'memo', 'block_height_ne', 'id_gte', 'amount_lte', 'id_lte', 'memo_in', 'to_gte', 'receiver', 'or_', 'date_time_exists', 'token_gte', 'kind_exists', 'token_nin', 'block', 'source', 'id', 'fee', 'fee_gte', 'hash_gte', 'amount_nin', 'amount_lt', 'id_lt', 'failure_reason_exists', 'and_', 'token_in', 'token_gt', 'hash', 'date_time_nin', 'nonce_ne', 'fee_token_lte', 'to_lte', 'token_lte', 'memo_gte', 'fee_nin', 'to', 'from_account', 'to_account_exists', 'failure_reason_in', 'memo_ne', 'nonce_in', 'block_height_exists', 'fee_token_in', 'failure_reason_lte', 'failure_reason', 'hash_gt', 'memo_nin', 'fee_token_nin', 'from_nin', 'from_in', 'nonce_lt', 'failure_reason_gt', 'memo_lt', 'to_gt', 'nonce_nin', 'block_height_gte', 'date_time_ne')
    amount_gte = sgqlc.types.Field(Long, graphql_name='amount_gte')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    fee_token_lt = sgqlc.types.Field(Int, graphql_name='feeToken_lt')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    fee_token_ne = sgqlc.types.Field(Int, graphql_name='feeToken_ne')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='amount_in')
    fee_gt = sgqlc.types.Field(Long, graphql_name='fee_gt')
    kind_ne = sgqlc.types.Field(String, graphql_name='kind_ne')
    to_account = sgqlc.types.Field('TransactionToAccountQueryInput', graphql_name='toAccount')
    memo_exists = sgqlc.types.Field(Boolean, graphql_name='memo_exists')
    fee_payer_exists = sgqlc.types.Field(Boolean, graphql_name='feePayer_exists')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    hash_ne = sgqlc.types.Field(String, graphql_name='hash_ne')
    amount_exists = sgqlc.types.Field(Boolean, graphql_name='amount_exists')
    fee_token_exists = sgqlc.types.Field(Boolean, graphql_name='feeToken_exists')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    kind_lt = sgqlc.types.Field(String, graphql_name='kind_lt')
    hash_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_nin')
    block_height_lt = sgqlc.types.Field(Int, graphql_name='blockHeight_lt')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    date_time_in = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_in')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    from_exists = sgqlc.types.Field(Boolean, graphql_name='from_exists')
    canonical_exists = sgqlc.types.Field(Boolean, graphql_name='canonical_exists')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_ne = sgqlc.types.Field(String, graphql_name='from_ne')
    to_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_nin')
    nonce_lte = sgqlc.types.Field(Int, graphql_name='nonce_lte')
    fee_token_gte = sgqlc.types.Field(Int, graphql_name='feeToken_gte')
    id_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_nin')
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    kind_lte = sgqlc.types.Field(String, graphql_name='kind_lte')
    memo_lte = sgqlc.types.Field(String, graphql_name='memo_lte')
    failure_reason_lt = sgqlc.types.Field(String, graphql_name='failureReason_lt')
    kind_gt = sgqlc.types.Field(String, graphql_name='kind_gt')
    id_gt = sgqlc.types.Field(String, graphql_name='id_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    receiver_exists = sgqlc.types.Field(Boolean, graphql_name='receiver_exists')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='id_in')
    failure_reason_gte = sgqlc.types.Field(String, graphql_name='failureReason_gte')
    kind_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_nin')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    canonical_ne = sgqlc.types.Field(Boolean, graphql_name='canonical_ne')
    token = sgqlc.types.Field(Int, graphql_name='token')
    nonce_exists = sgqlc.types.Field(Boolean, graphql_name='nonce_exists')
    date_time_gte = sgqlc.types.Field(DateTime, graphql_name='dateTime_gte')
    kind_gte = sgqlc.types.Field(String, graphql_name='kind_gte')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    block_height_lte = sgqlc.types.Field(Int, graphql_name='blockHeight_lte')
    is_delegation_exists = sgqlc.types.Field(Boolean, graphql_name='isDelegation_exists')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='to_in')
    date_time_lt = sgqlc.types.Field(DateTime, graphql_name='dateTime_lt')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='hash_in')
    fee_payer = sgqlc.types.Field(TransactionFeePayerQueryInput, graphql_name='feePayer')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    memo_gt = sgqlc.types.Field(String, graphql_name='memo_gt')
    hash_exists = sgqlc.types.Field(Boolean, graphql_name='hash_exists')
    fee_lt = sgqlc.types.Field(Long, graphql_name='fee_lt')
    id_ne = sgqlc.types.Field(String, graphql_name='id_ne')
    amount_ne = sgqlc.types.Field(Long, graphql_name='amount_ne')
    block_exists = sgqlc.types.Field(Boolean, graphql_name='block_exists')
    block_height_gt = sgqlc.types.Field(Int, graphql_name='blockHeight_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    failure_reason_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_nin')
    nonce_gt = sgqlc.types.Field(Int, graphql_name='nonce_gt')
    is_delegation_ne = sgqlc.types.Field(Boolean, graphql_name='isDelegation_ne')
    block_height_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_nin')
    to_ne = sgqlc.types.Field(String, graphql_name='to_ne')
    fee_lte = sgqlc.types.Field(Long, graphql_name='fee_lte')
    source_exists = sgqlc.types.Field(Boolean, graphql_name='source_exists')
    date_time_lte = sgqlc.types.Field(DateTime, graphql_name='dateTime_lte')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')
    nonce_gte = sgqlc.types.Field(Int, graphql_name='nonce_gte')
    from_account_exists = sgqlc.types.Field(Boolean, graphql_name='fromAccount_exists')
    id_exists = sgqlc.types.Field(Boolean, graphql_name='id_exists')
    fee_ne = sgqlc.types.Field(Long, graphql_name='fee_ne')
    failure_reason_ne = sgqlc.types.Field(String, graphql_name='failureReason_ne')
    amount_gt = sgqlc.types.Field(Long, graphql_name='amount_gt')
    fee_token_gt = sgqlc.types.Field(Int, graphql_name='feeToken_gt')
    fee_exists = sgqlc.types.Field(Boolean, graphql_name='fee_exists')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    kind_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='kind_in')
    fee_in = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_in')
    block_height_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='blockHeight_in')
    to_exists = sgqlc.types.Field(Boolean, graphql_name='to_exists')
    date_time_gt = sgqlc.types.Field(DateTime, graphql_name='dateTime_gt')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    block_height_ne = sgqlc.types.Field(Int, graphql_name='blockHeight_ne')
    id_gte = sgqlc.types.Field(String, graphql_name='id_gte')
    amount_lte = sgqlc.types.Field(Long, graphql_name='amount_lte')
    id_lte = sgqlc.types.Field(String, graphql_name='id_lte')
    memo_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_in')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    receiver = sgqlc.types.Field('TransactionReceiverQueryInput', graphql_name='receiver')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionQueryInput')), graphql_name='OR')
    date_time_exists = sgqlc.types.Field(Boolean, graphql_name='dateTime_exists')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    kind_exists = sgqlc.types.Field(Boolean, graphql_name='kind_exists')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    block = sgqlc.types.Field(BlockQueryInput, graphql_name='block')
    source = sgqlc.types.Field('TransactionSourceQueryInput', graphql_name='source')
    id = sgqlc.types.Field(String, graphql_name='id')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    fee_gte = sgqlc.types.Field(Long, graphql_name='fee_gte')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    amount_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='amount_nin')
    amount_lt = sgqlc.types.Field(Long, graphql_name='amount_lt')
    id_lt = sgqlc.types.Field(String, graphql_name='id_lt')
    failure_reason_exists = sgqlc.types.Field(Boolean, graphql_name='failureReason_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionQueryInput')), graphql_name='AND')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    date_time_nin = sgqlc.types.Field(sgqlc.types.list_of(DateTime), graphql_name='dateTime_nin')
    nonce_ne = sgqlc.types.Field(Int, graphql_name='nonce_ne')
    fee_token_lte = sgqlc.types.Field(Int, graphql_name='feeToken_lte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')
    memo_gte = sgqlc.types.Field(String, graphql_name='memo_gte')
    fee_nin = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='fee_nin')
    to = sgqlc.types.Field(String, graphql_name='to')
    from_account = sgqlc.types.Field(TransactionFromAccountQueryInput, graphql_name='fromAccount')
    to_account_exists = sgqlc.types.Field(Boolean, graphql_name='toAccount_exists')
    failure_reason_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='failureReason_in')
    memo_ne = sgqlc.types.Field(String, graphql_name='memo_ne')
    nonce_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_in')
    block_height_exists = sgqlc.types.Field(Boolean, graphql_name='blockHeight_exists')
    fee_token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_in')
    failure_reason_lte = sgqlc.types.Field(String, graphql_name='failureReason_lte')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    memo_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='memo_nin')
    fee_token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='feeToken_nin')
    from_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_nin')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='from_in')
    nonce_lt = sgqlc.types.Field(Int, graphql_name='nonce_lt')
    failure_reason_gt = sgqlc.types.Field(String, graphql_name='failureReason_gt')
    memo_lt = sgqlc.types.Field(String, graphql_name='memo_lt')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    nonce_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nonce_nin')
    block_height_gte = sgqlc.types.Field(Int, graphql_name='blockHeight_gte')
    date_time_ne = sgqlc.types.Field(DateTime, graphql_name='dateTime_ne')


class TransactionReceiverInsertInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key',)
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')


class TransactionReceiverQueryInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('public_key_exists', 'public_key', 'public_key_gte', 'public_key_lt', 'public_key_gt', 'public_key_lte', 'public_key_nin', 'or_', 'public_key_in', 'and_', 'public_key_ne')
    public_key_exists = sgqlc.types.Field(Boolean, graphql_name='publicKey_exists')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionReceiverQueryInput')), graphql_name='OR')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionReceiverQueryInput')), graphql_name='AND')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')


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
    __field_names__ = ('and_', 'public_key_gt', 'public_key_lte', 'public_key_ne', 'or_', 'public_key_nin', 'public_key_lt', 'public_key_in', 'public_key_gte', 'public_key', 'public_key_exists')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionSourceQueryInput')), graphql_name='AND')
    public_key_gt = sgqlc.types.Field(String, graphql_name='publicKey_gt')
    public_key_lte = sgqlc.types.Field(String, graphql_name='publicKey_lte')
    public_key_ne = sgqlc.types.Field(String, graphql_name='publicKey_ne')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionSourceQueryInput')), graphql_name='OR')
    public_key_nin = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_nin')
    public_key_lt = sgqlc.types.Field(String, graphql_name='publicKey_lt')
    public_key_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='publicKey_in')
    public_key_gte = sgqlc.types.Field(String, graphql_name='publicKey_gte')
    public_key = sgqlc.types.Field(String, graphql_name='publicKey')
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
    __field_names__ = ('or_', 'token_ne', 'token', 'token_exists', 'token_gte', 'token_lt', 'token_in', 'token_nin', 'token_gt', 'and_', 'token_lte')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionToAccountQueryInput')), graphql_name='OR')
    token_ne = sgqlc.types.Field(Int, graphql_name='token_ne')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_exists = sgqlc.types.Field(Boolean, graphql_name='token_exists')
    token_gte = sgqlc.types.Field(Int, graphql_name='token_gte')
    token_lt = sgqlc.types.Field(Int, graphql_name='token_lt')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_in')
    token_nin = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='token_nin')
    token_gt = sgqlc.types.Field(Int, graphql_name='token_gt')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TransactionToAccountQueryInput')), graphql_name='AND')
    token_lte = sgqlc.types.Field(Int, graphql_name='token_lte')


class TransactionToAccountUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('token', 'token_inc', 'token_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')


class TransactionUpdateInput(sgqlc.types.Input):
    __schema__ = mina_explorer_schema
    __field_names__ = ('receiver', 'fee_token', 'kind_unset', 'nonce_inc', 'block', 'fee_token_inc', 'block_height_inc', 'memo', 'memo_unset', 'canonical', 'from_', 'source', 'nonce', 'to_account_unset', 'fee_payer_unset', 'hash', 'kind', 'block_height', 'from_unset', 'is_delegation_unset', 'to_account', 'canonical_unset', 'date_time_unset', 'fee_token_unset', 'token', 'fee_payer', 'from_account', 'fee_unset', 'amount_unset', 'nonce_unset', 'to', 'to_unset', 'source_unset', 'block_height_unset', 'is_delegation', 'id', 'hash_unset', 'amount', 'token_unset', 'fee', 'failure_reason_unset', 'id_unset', 'token_inc', 'from_account_unset', 'receiver_unset', 'block_unset', 'failure_reason', 'date_time')
    receiver = sgqlc.types.Field(TransactionReceiverUpdateInput, graphql_name='receiver')
    fee_token = sgqlc.types.Field(Int, graphql_name='feeToken')
    kind_unset = sgqlc.types.Field(Boolean, graphql_name='kind_unset')
    nonce_inc = sgqlc.types.Field(Int, graphql_name='nonce_inc')
    block = sgqlc.types.Field(TransactionBlockStateHashRelationInput, graphql_name='block')
    fee_token_inc = sgqlc.types.Field(Int, graphql_name='feeToken_inc')
    block_height_inc = sgqlc.types.Field(Int, graphql_name='blockHeight_inc')
    memo = sgqlc.types.Field(String, graphql_name='memo')
    memo_unset = sgqlc.types.Field(Boolean, graphql_name='memo_unset')
    canonical = sgqlc.types.Field(Boolean, graphql_name='canonical')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    source = sgqlc.types.Field(TransactionSourceUpdateInput, graphql_name='source')
    nonce = sgqlc.types.Field(Int, graphql_name='nonce')
    to_account_unset = sgqlc.types.Field(Boolean, graphql_name='toAccount_unset')
    fee_payer_unset = sgqlc.types.Field(Boolean, graphql_name='feePayer_unset')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    kind = sgqlc.types.Field(String, graphql_name='kind')
    block_height = sgqlc.types.Field(Int, graphql_name='blockHeight')
    from_unset = sgqlc.types.Field(Boolean, graphql_name='from_unset')
    is_delegation_unset = sgqlc.types.Field(Boolean, graphql_name='isDelegation_unset')
    to_account = sgqlc.types.Field(TransactionToAccountUpdateInput, graphql_name='toAccount')
    canonical_unset = sgqlc.types.Field(Boolean, graphql_name='canonical_unset')
    date_time_unset = sgqlc.types.Field(Boolean, graphql_name='dateTime_unset')
    fee_token_unset = sgqlc.types.Field(Boolean, graphql_name='feeToken_unset')
    token = sgqlc.types.Field(Int, graphql_name='token')
    fee_payer = sgqlc.types.Field(TransactionFeePayerUpdateInput, graphql_name='feePayer')
    from_account = sgqlc.types.Field(TransactionFromAccountUpdateInput, graphql_name='fromAccount')
    fee_unset = sgqlc.types.Field(Boolean, graphql_name='fee_unset')
    amount_unset = sgqlc.types.Field(Boolean, graphql_name='amount_unset')
    nonce_unset = sgqlc.types.Field(Boolean, graphql_name='nonce_unset')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_unset = sgqlc.types.Field(Boolean, graphql_name='to_unset')
    source_unset = sgqlc.types.Field(Boolean, graphql_name='source_unset')
    block_height_unset = sgqlc.types.Field(Boolean, graphql_name='blockHeight_unset')
    is_delegation = sgqlc.types.Field(Boolean, graphql_name='isDelegation')
    id = sgqlc.types.Field(String, graphql_name='id')
    hash_unset = sgqlc.types.Field(Boolean, graphql_name='hash_unset')
    amount = sgqlc.types.Field(Long, graphql_name='amount')
    token_unset = sgqlc.types.Field(Boolean, graphql_name='token_unset')
    fee = sgqlc.types.Field(Long, graphql_name='fee')
    failure_reason_unset = sgqlc.types.Field(Boolean, graphql_name='failureReason_unset')
    id_unset = sgqlc.types.Field(Boolean, graphql_name='id_unset')
    token_inc = sgqlc.types.Field(Int, graphql_name='token_inc')
    from_account_unset = sgqlc.types.Field(Boolean, graphql_name='fromAccount_unset')
    receiver_unset = sgqlc.types.Field(Boolean, graphql_name='receiver_unset')
    block_unset = sgqlc.types.Field(Boolean, graphql_name='block_unset')
    failure_reason = sgqlc.types.Field(String, graphql_name='failureReason')
    date_time = sgqlc.types.Field(DateTime, graphql_name='dateTime')



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
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(TransactionInsertInput), graphql_name='data', default=None)),
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
))
    )
    update_many_blocks = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManyBlocks', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(BlockQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(BlockUpdateInput), graphql_name='set', default=None)),
))
    )
    update_many_snarks = sgqlc.types.Field('UpdateManyPayload', graphql_name='updateManySnarks', args=sgqlc.types.ArgDict((
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(SnarkUpdateInput), graphql_name='set', default=None)),
        ('query', sgqlc.types.Arg(SnarkQueryInput, graphql_name='query', default=None)),
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
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
        ('set', sgqlc.types.Arg(sgqlc.types.non_null(TransactionUpdateInput), graphql_name='set', default=None)),
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
        ('data', sgqlc.types.Arg(sgqlc.types.non_null(TransactionInsertInput), graphql_name='data', default=None)),
        ('query', sgqlc.types.Arg(TransactionQueryInput, graphql_name='query', default=None)),
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

