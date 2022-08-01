from ..constants import ENS_API_ENDPOINTS

def _records_by_account(account_addresses: str or list = None) -> str:
    
    # flatten account_address if it's a array
    if isinstance(account_addresses, (list, tuple,)):
        account_addresses = ','.join(account_addresses)
        
    base_url = '{}?account_addresses={}'.format(ENS_API_ENDPOINTS['records_by_account'], account_addresses)
    
    return base_url