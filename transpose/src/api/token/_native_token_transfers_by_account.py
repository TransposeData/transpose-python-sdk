from ..constants import TOKEN_API_ENDPOINTS

def _native_token_transfers_by_account (account_address: str = None,
                                        transferred_after: int or str='1970-01-01T00:00:00',
                                        transferred_before: int or str='2050-01-01T00:00:00',
                                        transfer_direction: str = 'all',
                                        order: str='asc',
                                        limit: int=10) -> str:
        
    base_url = '{}?account_address={}&transferred_after={}&transferred_before={}&transfer_direction={}&order={}&limit={}'.format(TOKEN_API_ENDPOINTS['native_token_transfers_by_account'], account_address, transferred_after, transferred_before, transfer_direction, order, limit)
    
    return base_url