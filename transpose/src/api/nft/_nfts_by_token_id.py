from ..constants import NFT_API_ENDPOINTS

def _nfts_by_token_id(contract_addresses: str or list = None,
                      token_ids: int or list = None) -> str:
    
    # flatten param if it's a array
    if isinstance(contract_addresses, (list, tuple,)):
        contract_addresses = ','.join(contract_addresses)
        
    # flatten param if it's a array
    if isinstance(token_ids, (list, tuple,)):
        token_ids = ','.join([str(id) for id in token_ids])
    
    base_url = '{}?contract_addresses={}&token_ids={}'.format(NFT_API_ENDPOINTS['nfts_by_token_id'], contract_addresses, token_ids)
    
    return base_url