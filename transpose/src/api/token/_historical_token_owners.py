from ..constants import TOKEN_API_ENDPOINTS


def _historical_token_owners(
    contract_address: str = None,
    timestamp: int or str = "2050-01-01T00:00:00",
    limit: int = 10,
) -> str:
    base_url = "{}?contract_address={}&timestamp={}&limit={}".format(
        TOKEN_API_ENDPOINTS["historical_token_owners"],
        contract_address,
        timestamp,
        limit,
    )

    return base_url
