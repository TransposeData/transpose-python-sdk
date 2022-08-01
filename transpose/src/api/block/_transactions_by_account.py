from ..constants import BLOCK_API_ENDPOINTS

def _transactions_by_account(
                          account_address: str = None,
                          occurred_after: str or int='1970-01-01T00:00:00Z',
                          occurred_before: str or int='2050-01-01T00:00:00Z',
                          direction: str = 'all',
                          order: str = 'asc',
                          limit: int = 10) -> str:
    base_url = '{}?account_address={}&occurred_after={}&occurred_before={}&transaction_direction={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['transactions_by_account'], account_address, occurred_after, occurred_before, direction, order, limit)
    
    return base_url