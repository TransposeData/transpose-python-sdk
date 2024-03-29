from ...util.models import QueryResult
from ....src.util.client import post_api_request


class Analytical():
    def __init__(self, base_class) -> None:
        self.super = base_class

    # Performs the given SQL query
    # https://docs.transpose.io/sql/parameters/
    def query(
        self,
        sql_query: str,
        parameters: dict = None,
    ) -> QueryResult:

        parameters = {} if parameters is None else parameters

        url = "https://api.transpose.io/sql/analytical"
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
