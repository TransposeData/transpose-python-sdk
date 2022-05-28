import requests

from transpose.src.util.generic_model import TransposeAPIResponse

from ..src.util.errors import *
from ..src.api.ens.base import ENS
from ..src.api.nft.base import NFT
from ..src.api.block.base import Block
from ..src.api.token.base import Token

    
# base class for the Transpose python SDK
class Transpose:
    def __init__(self, api_key: str) -> None:
        
        # verifies that the API key is valid
        if self.perform_authorized_request(None, 'https://api.transpose.io/v0/block/blocks-by-number?block_number_below=1', api_key):
            self.api_key = api_key
            
        # define the subclasses
        self.ENS   = ENS(self)
        self.Block = Block(self)
        self.NFT   = NFT(self)
        self.Token = Token(self)
    
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
            
            return response['results']  #TransposeAPIResponse('GenericModel', response['results'])
        else:
            raise_custom_error(request.status_code, request.json()['message'])

    # TODO: move _next to this base class
    # TODO: save previous response in a class variable _previous and add support for backwards pagination
    # TODO: generic class for responses instead of json