from ..constants import BLOCK_API_ENDPOINTS

def _transactions_by_hash(transaction_hashes: str = None,) -> str:
    
    # flatten param if it's a array
    if isinstance(transaction_hashes, (list, tuple,)):
        transaction_hashes = ','.join(transaction_hashes)

    base_url = '{}?transaction_hashes={}'.format(BLOCK_API_ENDPOINTS['transactions_by_hash'], transaction_hashes)
    
    return base_url