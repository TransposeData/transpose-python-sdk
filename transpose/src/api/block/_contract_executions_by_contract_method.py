from ..constants import BLOCK_API_ENDPOINTS

def _contract_executions_by_method (contract_address: str = None,
                                    method_id: str = None,
                                    occurred_after: int or str= '1970-01-01 00:00:00',
                                    occurred_before: int or str = '2050-01-01 00:00:00',
                                    order: str = 'asc',
                                    limit: int = 10,) -> str:
    base_url = '{}?contract_address={}&method_id={}&occurred_after={}&occurred_before={}&order={}&limit={}'.format(BLOCK_API_ENDPOINTS['contract_executions_by_method'], contract_address, method_id, occurred_after, occurred_before, order, limit)
        
    return base_url