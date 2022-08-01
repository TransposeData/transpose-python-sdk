from ..constants import TOKEN_API_ENDPOINTS

def _swaps_by_contract_address  (contract_address: str,
                      direction: str='all',
                      occurred_after: int or str='1970-01-01T00:00:00',
                      occurred_before: int or str='2050-01-01T00:00:00',
                      order: str='asc',
                      limit: int=10) -> str:
        
    base_url = '{}?contract_address={}&direction={}&occurred_after={}&occurred_before={}&order={}&limit={}'.format(TOKEN_API_ENDPOINTS['swaps_by_contract_address'], contract_address, direction, occurred_after, occurred_before, order, limit)
    
    return base_url