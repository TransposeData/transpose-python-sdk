import json
from typing import Union

import requests
try:
    import pandas as pd
    from pandas import DataFrame
except:
    pd = None
    DataFrame = None

from transpose.src.util.errors import raise_custom_error


def build_headers(api_key: str) -> dict:
    return {
        'x-api-key': api_key,
        'x-request-source': 'python-sdk',
        'Accept': 'application/json',
    }


def handle_response(request: requests.Response, return_df: bool = False) -> Union[dict, DataFrame]:
    if request.status_code == 200:

        # return the response as a DataFrame
        if return_df:

            # check if pandas is installed
            if not pd:
                raise ImportError("Pandas is not installed. Please install pandas to use this feature.")

            return pd.DataFrame(request.json()['results'])

        # return the response as a dictionary
        return request.json()

    else:
        raise_custom_error(request.status_code, request.json()['message'])


def get_api_request(
    url: str,
    api_key: str,
    body: dict = None,
    params=None,
    return_df: bool = False,
    verbose: bool = False
) -> Union[dict, DataFrame]:

    # set body/parameters to an empty dictionary if not provided
    body = {} if body is None else body
    params = {} if params is None else params

    # build headers
    request_headers = build_headers(api_key)

    # if in verbose mode, log the endpoint
    print("\n{}\n  {}\n".format(url, json.dumps(body, indent=4))) if verbose else None
    request = requests.get(
        url,
        headers=request_headers,
        json=body,
        params=params
    )

    return handle_response(request, return_df)


def post_api_request(
    url: str,
    api_key: str,
    body: dict,
    params=None,
    return_df: bool = False,
    verbose: bool = False
) -> Union[dict, DataFrame]:

    # set body/parameters to an empty dictionary if not provided
    body = {} if body is None else body
    params = {} if params is None else params

    # build headers
    request_headers = build_headers(api_key)

    # if in verbose mode, log the endpoint
    print("\n{}\n  {}\n".format(url, json.dumps(body, indent=4))) if verbose else None
    request = requests.post(
        url,
        headers=request_headers,
        json=body,
        params=params
    )

    return handle_response(request, return_df)
