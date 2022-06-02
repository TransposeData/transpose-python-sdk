from ..constants import TOKEN_API_ENDPOINTS

def _owners_by_contract_address (contract_address: str = None,
                                 limit: int = 10) -> str:
        
    base_url = '{}?contract_address={}&limit={}'.format(TOKEN_API_ENDPOINTS['owners_by_contract_address'], contract_address, limit)
    
    return base_url