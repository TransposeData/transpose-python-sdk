from ..constants import ENS_API_ENDPOINTS

def _records_by_owner(owner_address: str = None,
                     limit:         int = 10) -> str:
    base_url = '{}?owner_address={}&limit={}'.format(ENS_API_ENDPOINTS['records_by_owner'], owner_address, limit)
    
    return base_url