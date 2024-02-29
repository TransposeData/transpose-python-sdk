from ...util.models import QueryResult
from ....src.util.client import get_api_request, post_api_request


class SQL():
    def __init__(self, base_class) -> None:
        self.super = base_class

    # Performs the given SQL query
    # https://docs.transpose.io/sql/parameters/
    def query(
        self,
        sql_query: str,
        parameters: dict = {},
    ) -> QueryResult:

        url = "https://api.transpose.io/sql"
        body = {
            'sql': sql_query,
            'parameters': parameters
        }

        result = post_api_request(
            url=url,
            api_key=self.super.api_key,
            body=body,
            verbose=self.super.verbose
        )

        return QueryResult(result)

    # Gets the schema from the Transpose API
    def schema(self) -> dict:

        url = "https://api.transpose.io/get-schema"
        return get_api_request(
            url=url,
            api_key=self.super.api_key,
            verbose=self.super.verbose
        )
