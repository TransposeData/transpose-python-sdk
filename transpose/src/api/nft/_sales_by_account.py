from ..constants import NFT_API_ENDPOINTS

def _sales_by_account(
           account_address: str,
           sold_after: int or str='1970-01-01T00:00:00',
           sold_before: int or str='2050-01-01T00:00:00',
           role: str='all',
           order: str='asc', 
           limit: int=10) -> str:
        
    base_url = '{}?account_address={}&sold_after={}&sold_before={}&role={}&order={}&limit={}'.format(NFT_API_ENDPOINTS['sales_by_account'], account_address, sold_after, sold_before, role, order, limit)
    
    return base_url