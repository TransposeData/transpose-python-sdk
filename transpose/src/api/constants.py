
ENS_API_ENDPOINTS = {

    # ENS Record Endpoints
    'records_by_owner':               'https://api.transpose.io/v0/ens/ens-records-by-owner',
    'primary_ens_records_by_account': 'https://api.transpose.io/v0/ens/primary-ens-records-by-account',
    'records_by_ens_name':            'https://api.transpose.io/v0/ens/ens-records-by-name',
    'records_by_ens_node':            'https://api.transpose.io/v0/ens/ens-records-by-node',
    'records_by_ens_token_id':        'https://api.transpose.io/v0/ens/ens-records-by-token-id',
    'records_by_resolver':            'https://api.transpose.io/v0/ens/ens-records-by-resolver',
    'records_by_date':                'https://api.transpose.io/v0/ens/ens-records-by-date',

    # ENS Transfer Endpoints
    'transfers_by_ens_name':          'https://api.transpose.io/v0/ens/ens-transfers-by-name',
    'transfers_by_ens_node':          'https://api.transpose.io/v0/ens/ens-transfers-by-node',
    'transfers_by_ens_token_id':      'https://api.transpose.io/v0/ens/ens-transfers-by-token-id',
}

BLOCK_API_ENDPOINTS = {

    # Account Endpoints
    'accounts_by_address':                    'https://api.transpose.io/v0/block/accounts-by-address',
    'accounts_by_date_created':               'https://api.transpose.io/v0/block/accounts-by-date-created',
    
    # Block Endpoints
    'blocks_by_hash':                         'https://api.transpose.io/v0/block/blocks-by-hash',
    'blocks_by_number':                       'https://api.transpose.io/v0/block/blocks-by-number',
    'blocks_by_date':                         'https://api.transpose.io/v0/block/blocks-by-date',
    
    # Transaction Endpoints
    'transactions_by_hash':                   'https://api.transpose.io/v0/block/transactions-by-hash',
    'transactions_by_block':                  'https://api.transpose.io/v0/block/transactions-by-block',
    'transactions_by_date':                   'https://api.transpose.io/v0/block/transactions-by-date',
    'contract_executions_by_account':         'https://api.transpose.io/v0/block/contract-executions-by-account',
    'contract_executions_by_contract':        'https://api.transpose.io/v0/block/contract-executions-by-contract',
    'contract_executions_by_method':          'https://api.transpose.io/v0/block/contract-executions-by-contract-method',
    'internal_transactions_by_transaction':   'https://api.transpose.io/v0/block/internal-transactions-by-transaction',
    'internal_transactions_by_block':         'https://api.transpose.io/v0/block/internal-transactions-by-block',
    'internal_transactions_by_date':          'https://api.transpose.io/v0/block/internal-transactions-by-date',
    
    # Log Endpoints
    'logs_by_transaction':                    'https://api.transpose.io/v0/block/logs-by-transaction',
    'logs_by_block':                          'https://api.transpose.io/v0/block/logs-by-block',
    'logs_by_date':                           'https://api.transpose.io/v0/block/logs-by-date',
}