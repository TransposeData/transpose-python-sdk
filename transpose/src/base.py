import requests

from ..src.api.ens.base import ENS
    
# base class for the Transpose python SDK
class Transpose:
    def __init__(self, api_key: str) -> None:
        
        # verifies that the API key is valid
        if self.perform_authorized_request('https://api.transpose.io/v0/block/blocks-by-number?block_number_below=1', api_key):
            self.api_key = api_key
            
        # define the subclasses
        self.ENS = ENS(self)
    
    # the base function for performing authorized requests to the Transpose API suite
    def perform_authorized_request(self, endpoint, api_key: str=None) -> str:
        
        # build the request
        request_headers = {
            'x-api-key': api_key if api_key else self.api_key,
            'Accept': 'application/json',
        }
        request = requests.get(endpoint, headers=request_headers)
        
        # check for a successful response
        if request.status_code == 200:
            return request.json()
        elif request.status_code != 403:
            raise BaseException(request.json())
        else:
            raise ValueError('The provided API key, `{}`, is invalid.'.format(api_key))