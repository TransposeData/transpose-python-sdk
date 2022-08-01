from ..constants import BLOCK_API_ENDPOINTS

def _contracts_by_creator(creator_address: str = None,
                          created_before: str or int='2050-01-01T00:00:00Z',
                          created_after:str or int='1970-01-01T00:00:00Z',
                          order: str = 'asc',
                          limit: int = 10,) -> str:
        
    base_url = '{}?creator_address={}&created_before={}&created_after={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['contracts_by_creator'], creator_address, created_before, created_after, order, limit)
    
    return base_url