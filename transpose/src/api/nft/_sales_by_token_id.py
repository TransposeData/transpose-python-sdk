from ..constants import NFT_API_ENDPOINTS

def _sales_by_token_id(
           contract_address: str,
           token_id: int,
           sold_after: int or str='1970-01-01T00:00:00',
           sold_before: int or str='2050-01-01T00:00:00',
           order: str='asc', 
           limit: int=10) -> str:
        
    base_url = '{}?contract_address={}&token_id={}&sold_after={}&sold_before={}&order={}&limit={}'.format(NFT_API_ENDPOINTS['sales_by_token_id'], contract_address, token_id, sold_after, sold_before, order, limit)
    
    return base_url