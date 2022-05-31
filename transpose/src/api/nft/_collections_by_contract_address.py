from ..constants import NFT_API_ENDPOINTS

def _collections_by_contract_address(contract_addresses: str or list=None) -> str:
    
    # flatten param if it's a array
    if isinstance(contract_addresses, (list, tuple,)):
        contract_addresses = ','.join(contract_addresses)
        
    base_url = '{}?contract_addresses={}'.format(NFT_API_ENDPOINTS['collections_by_contract_address'], contract_addresses)
    
    return base_url