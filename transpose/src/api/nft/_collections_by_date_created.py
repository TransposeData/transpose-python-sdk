from ..constants import NFT_API_ENDPOINTS

def _collections_by_date_created(created_after: str or int = '1970-01-01 00:00:00',
                                created_before: str or int = '2050-01-01 00:00:00',
                                standard: str or int = None,
                                order: str = 'asc',
                                limit: int = 10) -> str:

    standard_query = ""
    if standard is not None:
        standard_query = "&standard={}".format(standard)
        
    base_url = '{}?created_after={}&created_before={}{}&order={}&limit={}'.format(NFT_API_ENDPOINTS['collections_by_date_created'], created_after, created_before, standard_query, order, limit)
    
    return base_url