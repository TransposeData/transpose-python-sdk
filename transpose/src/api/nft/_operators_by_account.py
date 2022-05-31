from ..constants import NFT_API_ENDPOINTS

def _operators_by_account(owner_address: str = None,
                          contract_address: str = None,
                          limit: int = 10) -> str:
        
    base_url = '{}?owner_address={}&limit={}'.format(NFT_API_ENDPOINTS['operators_by_account'], owner_address, limit)
    
    if contract_address != None:
        base_url += '&contract_address={}'.format(contract_address)
    
    return base_url