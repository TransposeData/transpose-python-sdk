import json
import requests

from ....src.util.errors import raise_custom_error


class SQL():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Performs the given SQL query
    # https://docs.transpose.io/sql/parameters/
    def query(self,
              sql_query: str,
              parameters: dict={}) -> dict:
        
        # build headers
        request_headers = {
            'x-api-key': self.super.api_key,
            'Accept': 'application/json',
        }
        
        # buold body
        body = {
            'sql': sql_query,
            'parameters': parameters
        }

        # if in verbose mode, log the endpoint
        print("\n{}\n  {}\n".format("https://api.transpose.io/sql", json.dumps(body, indent=4))) if self.super.verbose else None
        request = requests.post(
            "https://api.transpose.io/sql",
            headers=request_headers,
            json=body
        )
        
        # check for a successful response
        if request.status_code == 200:
            
            response = request.json()
            return response
        else:
            raise_custom_error(request.status_code, request.json()['message'])