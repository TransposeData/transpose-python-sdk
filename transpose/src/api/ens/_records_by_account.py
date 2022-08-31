from ..constants import ENS_API_ENDPOINTS

def _records_by_account(resolved_address: str) -> str:
    base_url = '{}?resolved_address={}'.format(ENS_API_ENDPOINTS['records_by_account'], resolved_address)
    
    return base_url