from ..constants import NFT_API_ENDPOINTS

def _nfts_by_contract_address(contract_address: str = None,
                              include_burned_nfts: bool = False,
                              limit: int = 10) -> str:
        
    base_url = '{}?contract_address={}&include_burned_nfts={}&limit={}'.format(NFT_API_ENDPOINTS['nfts_by_contract_address'], contract_address, include_burned_nfts, limit)
    
    return base_url