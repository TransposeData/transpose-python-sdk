from ..constants import TOKEN_API_ENDPOINTS

def _swaps_by_account(account_address: str,
                      occurred_after: int or str='1970-01-01T00:00:00',
                      occurred_before: int or str='2050-01-01T00:00:00',
                      confirmed: bool=True,
                      order: str='asc',
                      limit: int=10) -> str:
        
    base_url = '{}?account_address={}&occurred_after={}&occurred_before={}&confirmed={}&order={}&limit={}'.format(TOKEN_API_ENDPOINTS['swaps_by_account'], account_address, occurred_after, occurred_before, confirmed, order, limit)
    
    return base_url