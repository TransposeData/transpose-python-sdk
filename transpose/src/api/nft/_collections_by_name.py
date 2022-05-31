from ..constants import NFT_API_ENDPOINTS

def _collections_by_name(name: str=None,
                         limit: int=10) -> str:
    
    base_url = '{}?substring={}&limit={}'.format(NFT_API_ENDPOINTS['collections_by_name'], name, limit)
    
    return base_url