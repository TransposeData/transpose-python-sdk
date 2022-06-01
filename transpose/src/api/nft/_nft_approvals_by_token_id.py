from ..constants import NFT_API_ENDPOINTS

def _nft_approvals_by_token_id (contract_address: str = None,
                                token_id: int = None,
                                approved_after: int or str='1970-01-01T00:00:00',
                                approved_before: int or str='2050-01-01T00:00:00',
                                order: str='asc',
                                limit: int=10) -> str:
        
    base_url = '{}?contract_address={}&token_id={}&approved_after={}&approved_before={}&order={}&limit={}'.format(NFT_API_ENDPOINTS['nft_approvals_by_token_id'], contract_address, token_id, approved_after, approved_before, order, limit)
    
    return base_url