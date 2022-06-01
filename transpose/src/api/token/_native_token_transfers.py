from ..constants import TOKEN_API_ENDPOINTS

def _native_token_transfers(transferred_after: int or str='1970-01-01T00:00:00',
                            transferred_before: int or str='2050-01-01T00:00:00',
                            order: str='asc',
                            limit: int=10) -> str:
        
    base_url = '{}?transferred_after={}&transferred_before={}&order={}&limit={}'.format(TOKEN_API_ENDPOINTS['native_token_transfers'], transferred_after, transferred_before, order, limit)
    
    return base_url