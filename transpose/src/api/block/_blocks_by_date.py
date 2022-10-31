from ..constants import BLOCK_API_ENDPOINTS

def _blocks_by_date(added_after:str or int='1970-01-01T00:00:00Z',
                    added_before: str or int='2050-01-01T00:00:00Z',
                    order: str = 'asc',
                    limit: int = 10,) -> str:
    base_url = '{}?added_after={}&added_before={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['blocks_by_date'], added_after, added_before, order, limit)
        
    return base_url