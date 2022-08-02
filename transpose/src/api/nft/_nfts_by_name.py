from ..constants import NFT_API_ENDPOINTS

def _nfts_by_name(name: str=None,
                  limit: int=10,
                  fuzzy: bool=False) -> str:
    
    base_url = '{}?substring={}&limit={}&fuzzy={}'.format(NFT_API_ENDPOINTS['nfts_by_name'], name, limit, fuzzy)
    
    return base_url