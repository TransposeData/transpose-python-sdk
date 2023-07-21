import json

import requests

from ....src.util.errors import raise_custom_error


class SQL:
    def __init__(self, base_class) -> None:
        self.super = base_class

    # Performs the given SQL query
    # https://docs.transpose.io/sql/parameters/
    def query(self, sql_query: str, parameters: dict = {}) -> dict:
        # build headers
        request_headers = {
            "x-api-key": self.super.api_key,
            "x-request-source": "python-sdk",
            "Accept": "application/json",
        }

        # build body
        body = {"sql": sql_query, "parameters": parameters}

        # if in verbose mode, log the endpoint
        print(
            "\n{}\n  {}\n".format(
                "https://api.transpose.io/sql", json.dumps(body, indent=4)
            )
        ) if self.super.verbose else None
        request = requests.post(
            "https://api.transpose.io/sql", headers=request_headers, json=body
        )

        # check for a successful response
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise_custom_error(request.status_code, request.json()["message"])

    # Gets the schema from the Transpose API
    def schema(self) -> dict:
        # build headers
        request_headers = {
            "x-api-key": self.super.api_key,
            "x-request-source": "python-sdk",
            "Accept": "application/json",
        }

        # if in verbose mode, log the endpoint
        request = requests.get(
            "https://api.transpose.io/get-schema",
            headers=request_headers,
        )

        # check for a successful response
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise_custom_error(request.status_code, request.json()["message"])

    # Calls the AI query assistant
    def generate_query(self, text: str, chain: str = "ethereum") -> dict:
        # build headers
        request_headers = {
            "x-api-key": self.super.api_key,
            "x-request-source": "python-sdk",
            "Accept": "application/json",
        }

        # build body
        body = {"text": text, "chain": chain}

        # if in verbose mode, log the endpoint
        print(
            "\n{}\n  {}\n".format(
                "https://api.transpose.io/text-to-sql", json.dumps(body, indent=4)
            )
        ) if self.super.verbose else None

        # make request
        request = requests.post(
            "https://api.transpose.io/text-to-sql",
            headers=request_headers,
            json=body,
        )

        # check for a successful response
        if request.status_code == 200:
            response = request.json()
            return response
        else:
            raise_custom_error(request.status_code, request.json()["message"])
