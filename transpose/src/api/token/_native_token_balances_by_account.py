from ..constants import TOKEN_API_ENDPOINTS

def _native_token_balances_by_account(account_addresses: str or list) -> str:
    
    # flatten list of account addresses
    if isinstance(account_addresses, (list, tuple)):
        account_addresses = ",".join(account_addresses)
        
    base_url = '{}?account_addresses={}'.format(TOKEN_API_ENDPOINTS['native_token_balances_by_account'], account_addresses)
    
    return base_url