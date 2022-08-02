from ..constants import NFT_API_ENDPOINTS

def _nfts_by_date_minted(minted_after: str or int = '1970-01-01 00:00:00',
                         minted_before: str or int = '2050-01-01 00:00:00',
                         contract_address: str = None,
                         order: str = 'asc',
                         limit: int = 10) -> str:
        
    base_url = '{}?minted_after={}&minted_before={}&order={}&limit={}'.format(NFT_API_ENDPOINTS['nfts_by_date_minted'], minted_after, minted_before, order, limit)
    
    if contract_address != None:
        base_url += '&contract_address={}'.format(contract_address)
    
    return base_url