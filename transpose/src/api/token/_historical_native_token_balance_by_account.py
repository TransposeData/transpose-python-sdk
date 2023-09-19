
from ..constants import TOKEN_API_ENDPOINTS

def _historical_native_token_balance_by_account(
    account_address: str = None,
    timestamp: int or str = '2050-01-01T00:00:00',
) -> str:
    base_url = '{}?account_address={}&timestamp={}'.format(TOKEN_API_ENDPOINTS['historical_native_token_balance_by_account'], account_address, timestamp)
    
    return base_url