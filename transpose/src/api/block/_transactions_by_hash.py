from ..constants import BLOCK_API_ENDPOINTS

def _transactions_by_hash(transaction_hashes: str = None,) -> str:
    base_url = '{}?transaction_hashes={}'.format(BLOCK_API_ENDPOINTS['transactions_by_hash'], transaction_hashes)
    
    return base_url