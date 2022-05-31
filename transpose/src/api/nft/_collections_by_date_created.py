from ..constants import NFT_API_ENDPOINTS

def _collections_by_date_created(created_after: str or int = '1970-01-01 00:00:00',
                                created_before: str or int = '2050-01-01 00:00:00',
                                standard: str or int = 'ERC-721',
                                order: str = 'asc',
                                limit: int = 10) -> str:
        
    base_url = '{}?created_after={}&created_before={}&standard={}&order={}&limit={}'.format(NFT_API_ENDPOINTS['collections_by_date_created'], created_after, created_before, standard, order, limit)
    
    return base_url