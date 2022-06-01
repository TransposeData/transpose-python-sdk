import requests

from transpose.src.util.generic_model import TransposeAPIResponse

from ..src.util.errors import *
from ..src.api.ens.base import ENS
from ..src.api.nft.base import NFT
from ..src.api.block.base import Block
from ..src.api.token.base import Token

    
# base class for the Transpose python SDK
class Transpose:
    def __init__(self, api_key: str, verbose: bool=False) -> None:
        self._next = None
        self._previous = None
        self.verbose = verbose
        
        # verifies that the API key is valid
        if self.perform_authorized_request('https://api.transpose.io/v0/block/blocks-by-number?block_number_below=1', api_key):
            self.api_key = api_key
            
        # define the subclasses
        self.ENS   = ENS(self)
        self.NFT   = NFT(self)
        self.Block = Block(self)
        self.Token = Token(self)
    
    def next(self) -> str:
        return self.perform_authorized_request(self._next)
    
    def previous(self) -> str:
        return self.perform_authorized_request(self._previous)
    
    # the base function for performing authorized requests to the Transpose API suite
    def perform_authorized_request(self, endpoint: str, api_key: str=None) -> str:
        
        # if in verbose mode, log the endpoint
        print(endpoint) if self.verbose else None
        
        # build the request
        request_headers = {
            'x-api-key': api_key if api_key else self.api_key,
            'Accept': 'application/json',
        }
        request = requests.get(endpoint, headers=request_headers)
        
        # check for a successful response
        if request.status_code == 200:
            response = request.json()
            
            # If the response contains a paginator, set the paginator's next endpoint
            if response['next'] != None:
                self._previous = endpoint
                self._next = response['next']
            
            return TransposeAPIResponse('TransposeDataModel', response['results'])
        else:
            raise_custom_error(request.status_code, request.json()['message'])

    # TODO: save previous response in a class variable _previous and add support for backwards pagination
