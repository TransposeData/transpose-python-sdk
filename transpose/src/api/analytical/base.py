import json
from typing import Union

import requests
try:
    import pandas as pd
    from pandas import DataFrame
except:
    pd = None
    DataFrame = None

from ....src.util.errors import raise_custom_error


class Analytical():
    def __init__(self, base_class) -> None:
        self.super  = base_class

    # https://docs.transpose.io/sql/analytical/
    def query(self,
              sql_query: str,
              parameters: dict={},
              return_df: bool = True if pd else False) -> Union[dict, DataFrame]:

        # build headers
        request_headers = {
            'x-api-key': self.super.api_key,
            'x-request-source': 'python-sdk',
            'Accept': 'application/json',
        }

        # build body
        body = {
            'sql': sql_query,
            'parameters': parameters
        }

        # if in verbose mode, log the endpoint
        print("\n{}\n  {}\n".format("https://api.transpose.io/sql/analytical", json.dumps(body, indent=4))) if self.super.verbose else None
        request = requests.post(
            "https://api.transpose.io/sql/analytical",
            headers=request_headers,
            json=body
        )

        # check for a successful response
        if request.status_code == 200:

            response = request.json()
            if return_df:
                return pd.DataFrame(response['results'])

            return response
        else:
            raise_custom_error(request.status_code, request.json()['message'])
