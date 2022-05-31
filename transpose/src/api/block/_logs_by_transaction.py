from ..constants import BLOCK_API_ENDPOINTS

def _logs_by_transaction(transaction_hash: str = None, limit: int = 10) -> str:
    
    # flatten param if it's a array
    if isinstance(transaction_hash, (list, tuple,)):
        transaction_hash = ','.join(transaction_hash)
        
    base_url = '{}?transaction_hash={}&limit={}'.format(BLOCK_API_ENDPOINTS['logs_by_transaction'], transaction_hash, limit)
    
    return base_url