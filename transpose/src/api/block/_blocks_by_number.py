from ..constants import BLOCK_API_ENDPOINTS

def _blocks_by_number(block_number_above: int = 0,
                      block_number_below: int = 1000000000,
                      miner: str = None,
                      order: str = 'asc',
                      limit: int = 10,) -> str:
    base_url = '{}?block_number_above={}&block_number_below={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['blocks_by_number'], block_number_above, block_number_below, order, limit)
    
    if miner != None:
        base_url += '&miner={}'.format(miner)
        
    return base_url