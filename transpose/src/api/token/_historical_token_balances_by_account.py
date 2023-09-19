from ..constants import TOKEN_API_ENDPOINTS


def _historical_token_balances_by_account(
    account_address: str = None,
    contract_address: str = None,
    timestamp: int or str = "2050-01-01T00:00:00",
    limit: int = 10,
) -> str:
    base_url = "{}?account_address={}&timestamp={}&limit={}{}".format(
        TOKEN_API_ENDPOINTS["historical_token_balances_by_account"],
        account_address,
        timestamp,
        limit,
        "&contract_address={}".format(contract_address)
        if contract_address is not None
        else "",
    )

    return base_url
