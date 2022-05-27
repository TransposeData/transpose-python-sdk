from ..constants import ENS_API_ENDPOINTS

def _records_by_date(timestamp_after: str or int='1970-01-01T00:00:00Z',
                     timestamp_before: str or int='2050-01-01T00:00:00Z',
                     type:  str= 'registration',
                     order: str= 'asc',
                     limit: int= 10) -> str:
    base_url = '{}?timestamp_after={}&timestamp_before={}&type={}&order={}&limit={}'.format(ENS_API_ENDPOINTS['records_by_date'], timestamp_after, timestamp_before, type, order, limit)
    
    return base_url