from ..constants import BLOCK_API_ENDPOINTS

def _internal_transactions_by_date(occurred_after: str or int='1970-01-01T00:00:00Z',
                                   occurred_before: str or int='2050-01-01T00:00:00Z',
                                   order: str = 'asc',
                                   limit: int = 10) -> str:
    base_url = '{}?occurred_after={}&occurred_before={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['internal_transactions_by_date'], occurred_after, occurred_before, order, limit)
    
    return base_url