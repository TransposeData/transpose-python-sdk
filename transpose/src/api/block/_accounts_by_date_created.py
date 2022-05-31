from ..constants import BLOCK_API_ENDPOINTS

def _accounts_by_date_created(created_after: str or int='1970-01-01T00:00:00Z',
                              created_before: str or int='2050-01-01T00:00:00Z',
                              account_type: str = 'eoa',
                              order: str = 'asc',
                              limit: int = 10) -> str:
    base_url = '{}?created_after={}&created_before={}&account_type={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['accounts_by_date_created'], created_after, created_before, account_type, order, limit)
    
    return base_url