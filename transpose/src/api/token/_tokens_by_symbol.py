from ..constants import TOKEN_API_ENDPOINTS

def _tokens_by_symbol(symbol: str=None,
                      limit: int=10) -> str:
    
    base_url = '{}?substring={}&limit={}'.format(TOKEN_API_ENDPOINTS['tokens_by_symbol'], symbol, limit)
    
    return base_url