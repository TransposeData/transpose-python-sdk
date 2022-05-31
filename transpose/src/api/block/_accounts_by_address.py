from ..constants import BLOCK_API_ENDPOINTS

def _accounts_by_address(account_addresses: str = None,) -> str:
    
    # flatten param if it's a array
    if isinstance(account_addresses, (list, tuple,)):
        account_addresses = ','.join(account_addresses)
        
    base_url = '{}?account_addresses={}'.format(BLOCK_API_ENDPOINTS['accounts_by_address'], account_addresses)
    
    return base_url