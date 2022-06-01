from ..constants import TOKEN_API_ENDPOINTS

def _tokens_by_contract_address(contract_addresses: str or list=None) -> str:
    
    # flatten param if it's a array
    if isinstance(contract_addresses, (list, tuple,)):
        contract_addresses = ','.join(contract_addresses)
        
    base_url = '{}?contract_addresses={}'.format(TOKEN_API_ENDPOINTS['tokens_by_contract_address'], contract_addresses)
    
    return base_url