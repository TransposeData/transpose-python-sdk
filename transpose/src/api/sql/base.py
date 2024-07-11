from typing import Union

import pandas as pd

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
        parameters: dict = None,
        return_df: bool = False
    ) -> Union[QueryResult, pd.DataFrame]:

        if parameters is None:
            parameters = {}

        url = "https://api.transpose.io/sql"
        body = {
            'sql': sql_query,
            'parameters': parameters
        }

        result = post_api_request(
            url=url,
            api_key=self.super.api_key,
            body=body,
            return_df=return_df,
            verbose=self.super.verbose
        )

        return result if return_df else QueryResult(result)

    # Gets the schema from the Transpose API
    def schema(self) -> dict:

        url = "https://api.transpose.io/get-schema"
        return get_api_request(
            url=url,
            api_key=self.super.api_key,
            verbose=self.super.verbose
        )
