from ..constants import BLOCK_API_ENDPOINTS

def _blocks_by_hash(block_hashes: str = None,) -> str:
    base_url = '{}?block_hashes={}'.format(BLOCK_API_ENDPOINTS['blocks_by_hash'], block_hashes)
    
    return base_url