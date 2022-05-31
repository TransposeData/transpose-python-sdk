from ..constants import NFT_API_ENDPOINTS

def _transfers_by_token_id(contract_address: str = None,
                           token_id: int = None,
                           transferred_after: int or str='1970-01-01T00:00:00',
                           transferred_before: int or str='2050-01-01T00:00:00',
                           transfer_category: str='all',
                           order: str='asc',
                           limit: int=10) -> str:
        
    base_url = '{}?contract_address={}&token_id={}&transferred_after={}&transferred_before={}&transfer_category={}&order={}&limit={}'.format(NFT_API_ENDPOINTS['transfers_by_token_id'], token_id, contract_address, transferred_after, transferred_before, transfer_category, order, limit)
    
    return base_url