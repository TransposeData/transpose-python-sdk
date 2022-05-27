
def records_by_owner(owner_address: str = None,
                     limit:         int = 10) -> str:
    base_url = 'https://api.transpose.io/v0/ens/ens-records-by-owner?owner_address={}&limit={}'.format(owner_address, limit)
    
    return base_url