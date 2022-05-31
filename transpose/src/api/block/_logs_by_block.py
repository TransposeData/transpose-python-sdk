from ..constants import BLOCK_API_ENDPOINTS

def _logs_by_block(block_number_above: int = 0,
                   block_number_below: int = 1000000000,
                   contract_address: str = None,
                   event_signature: str = None,
                   order: str = 'asc',
                   limit: int = 10) -> str:
    base_url = '{}?block_number_above={}&block_number_below={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['logs_by_block'], block_number_above, block_number_below, order, limit)
    
    if contract_address != None:
        base_url += '&contract_address={}'.format(contract_address)
    
    if event_signature != None:
        base_url += '&event_signature={}'.format(event_signature)
    
    return base_url