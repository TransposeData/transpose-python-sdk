from ..constants import BLOCK_API_ENDPOINTS

def _blocks_by_date(mined_after:str or int='1970-01-01T00:00:00Z',
                    mined_before: str or int='2050-01-01T00:00:00Z',
                    miner: str = None,
                    order: str = 'asc',
                    limit: int = 10,) -> str:
    base_url = '{}?mined_after={}&mined_before={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['blocks_by_date'], mined_after, mined_before, order, limit)
    
    if miner != None:
        base_url += '&miner={}'.format(miner)
        
    return base_url