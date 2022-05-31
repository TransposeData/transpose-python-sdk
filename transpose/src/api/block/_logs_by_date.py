from ..constants import BLOCK_API_ENDPOINTS

def _logs_by_date(emitted_after: str or int='1970-01-01T00:00:00Z',
                  emitted_before: str or int='2050-01-01T00:00:00Z',
                  contract_address: str = None,
                  event_signature: str = None,
                  order: str = 'asc',
                  limit: int = 10) -> str:
    base_url = '{}?emitted_after={}&emitted_before={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['logs_by_date'], emitted_after, emitted_before, order, limit)
    
    if contract_address != None:
        base_url += '&contract_address={}'.format(contract_address)
    
    if event_signature != None:
        base_url += '&event_signature={}'.format(event_signature)
    
    return base_url