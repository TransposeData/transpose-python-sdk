from ..constants import BLOCK_API_ENDPOINTS

def _accounts_by_address(account_addresses: str = None,) -> str:
    base_url = '{}?account_addresses={}'.format(BLOCK_API_ENDPOINTS['accounts_by_address'], account_addresses)
    
    return base_url