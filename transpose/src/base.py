import requests

from ..src.util.errors import *
from ..src.api.ens.base import ENS
    
# base class for the Transpose python SDK
class Transpose:
    def __init__(self, api_key: str) -> None:
        
        # verifies that the API key is valid
        if self.perform_authorized_request(None, 'https://api.transpose.io/v0/block/blocks-by-number?block_number_below=1', api_key):
            self.api_key = api_key
            
        # define the subclasses
        self.ENS = ENS(self)
    
    # the base function for performing authorized requests to the Transpose API suite
    def perform_authorized_request(self, caller, endpoint: str, api_key: str=None) -> str:
        
        # build the request
        request_headers = {
            'x-api-key': api_key if api_key else self.api_key,
            'Accept': 'application/json',
        }
        request = requests.get(endpoint, headers=request_headers)
        
        # check for a successful response
        if request.status_code == 200:
            response = request.json()
            
            # If the response contains a paginator, set the paginator on the caller baseclass
            if response['next'] != None:  caller._next = response['next']
            
            return response
        else:
            raise_custom_error(request.status_code, request.json()['message'])