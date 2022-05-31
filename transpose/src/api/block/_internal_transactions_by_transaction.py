from ..constants import BLOCK_API_ENDPOINTS

def _internal_transactions_by_transaction(transaction_hash: str = None, limit: int = 10) -> str:
    base_url = '{}?transaction_hash={}&limit={}'.format(BLOCK_API_ENDPOINTS['internal_transactions_by_transaction'], transaction_hash, limit)
    
    return base_url