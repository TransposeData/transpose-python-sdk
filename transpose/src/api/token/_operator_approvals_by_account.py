from ..constants import TOKEN_API_ENDPOINTS

def _operator_approvals_by_account(account_address: str = None,
                              approved_after: int or str='1970-01-01T00:00:00',
                              approved_before: int or str='2050-01-01T00:00:00',
                              approval_direction: str = 'all',
                              order: str='asc',
                              limit: int=10) -> str:
        
    base_url = '{}?account_address={}&approved_after={}&approved_before={}&approval_direction={}&order={}&limit={}'.format(TOKEN_API_ENDPOINTS['operator_approvals_by_account'], account_address, approved_after, approved_before, approval_direction, order, limit)
    
    return base_url