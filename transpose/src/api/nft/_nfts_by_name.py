from ..constants import NFT_API_ENDPOINTS

def _nfts_by_name(name: str=None,
                  include_burned_nfts: bool=False,
                  limit: int=10) -> str:
    
    base_url = '{}?substring={}&include_burned_nfts={}&limit={}'.format(NFT_API_ENDPOINTS['nfts_by_name'], name, include_burned_nfts, limit)
    
    return base_url