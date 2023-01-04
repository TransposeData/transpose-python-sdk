from ..constants import BLOCK_API_ENDPOINTS

def _transactions_by_account(
                          account_address: str = None,
                          direction: str = 'all',
                          order: str = 'asc',
                          limit: int = 10) -> str:
    base_url = '{}?account_address={}&transaction_direction={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['transactions_by_account'], account_address, direction, order, limit)
    
    return base_url