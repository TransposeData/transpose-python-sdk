from ..constants import NFT_API_ENDPOINTS

def _owners_by_token_id(contract_address: str = None,
                                token_id: int = None,
                                limit: int = 10) -> str:
        
    base_url = '{}?contract_address={}&token_id={}&limit={}'.format(NFT_API_ENDPOINTS['owners_by_token_id'], contract_address, token_id, limit)
    
    return base_url