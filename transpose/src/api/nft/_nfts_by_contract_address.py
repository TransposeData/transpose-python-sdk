from ..constants import NFT_API_ENDPOINTS

def _nfts_by_contract_address(contract_address: str = None,
                              limit: int = 10) -> str:
        
    base_url = '{}?contract_address={}&limit={}'.format(NFT_API_ENDPOINTS['nfts_by_contract_address'], contract_address, limit)
    
    return base_url