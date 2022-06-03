from ..constants import TOKEN_API_ENDPOINTS

def _tokens_by_owner(owner_address: str=None,
                     contract_address: str=None,
                     limit: int=10) -> str:
    
    base_url = '{}?owner_address={}&limit={}'.format(TOKEN_API_ENDPOINTS['tokens_by_owner'], owner_address, limit)
    
    if contract_address != None:
        base_url += '&contract_address={}'.format(contract_address)
    
    return base_url