from ..constants import ENS_API_ENDPOINTS

def _transfers_by_name(ens_name: str= None,
                           transferred_after: int or str='1970-01-01T00:00:00',
                           transferred_before: int or str='2050-01-01T00:00:00',
                           order: str='asc',
                           limit: int=10) -> str:
        
    base_url = '{}?ens_name={}&transferred_after={}&transferred_before={}&order={}&limit={}'.format(ENS_API_ENDPOINTS['transfers_by_ens_name'], ens_name, transferred_after, transferred_before, order, limit)
    
    return base_url