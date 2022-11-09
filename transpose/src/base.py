import time
import requests

from ..src.util.models import *

from ..src.util.errors import *
from ..src.api.ens.base import ENS
from ..src.api.nft.base import NFT
from ..src.api.block.base import Block
from ..src.api.token.base import Token


# base class for the Transpose python SDK
class Transpose:
    def __init__(
        self,
        api_key: str,
        debug: bool=False,
        host: str=None,
        chain_id: int=0,
        chain: str="ethereum",
        json: bool=False,
    ) -> None:

        self._next = None
        self._next_class_name = None
        self.host = host if host else 'https://api.transpose.io'
        self.verbose = debug
        self.json = json
        
        if chain.lower() == "ethereum": 
            self.chain_id = 1
            
        if chain.lower() == "polygon":  
            self.chain_id = 137
        
        if chain_id != 0:
            self.chain_id = chain_id

        # verifies that the API key is valid
        if self.perform_authorized_request(Block, 'https://api.transpose.io/v0/block/blocks-by-number?block_number_below=1', api_key):
            self.api_key = api_key
                        
        # define the subclasses
        self.ens   = ENS(self)
        self.nft   = NFT(self)
        self.block = Block(self)
        self.token = Token(self)
        
        # deprecated in favor of the new API
        self.ENS = self.ens
        self.NFT = self.nft
        self.Block = self.block
        self.Token = self.token
    
    def next(self) -> str:
        return self.perform_authorized_request(self._next_class_name, self._next)
    
    def set_chain(self, chain_id: int=0, chain: str="ethereum") -> None:
        if chain.lower() == "ethereum": 
            self.chain_id = 1
            
        if chain.lower() == "polygon":  
            self.chain_id = 137
        
        if chain_id != 0:
            self.chain_id = chain_id
    
    # this can be renamed later. Pagination helper function to get many 
    def bulk_request(self, endpoint_response: List, requests_per_second: int=None, results_to_fetch: int=999999999999) -> List:
        api_response_data = endpoint_response
    
        while len(api_response_data) < results_to_fetch and self._next is not None:
            
            api_response_data += self.next()
            
            # if the user specified a requests per second, sleep for the appropriate amount of time
            # has a 1% buffer.
            if requests_per_second is not None:
                time.sleep(1.01 / requests_per_second)
        
        return api_response_data[0:results_to_fetch]
    
    # the base function for performing authorized requests to the Transpose API suite
    def perform_authorized_request(self, model: type, endpoint: str, api_key: str=None):
        if endpoint is None: 
            return None
        
        # build the request
        request_headers = {
            'x-api-key': api_key if api_key else self.api_key,
            'Accept': 'application/json',
        }
        
        # add chain_id to the request
        endpoint += f'&chain_id={self.chain_id}'
        
        # if in verbose mode, log the endpoint
        print("\n{}\n  {}\n".format(endpoint.replace("https://api.transpose.io", self.host).split("?")[0], "\n  ".join(endpoint.split("?")[1].split("&")))) if self.verbose else None
        request = requests.get(endpoint.replace("https://api.transpose.io", self.host), headers=request_headers)
        
        # check for a successful response
        if request.status_code == 200:
            
            response = request.json()
            
            # If the response contains a paginator, set the paginator's next endpoint
            if response['next'] is None:
                self._next = None
                self._next_class_name = None
            else: 
                self._next = response['next']
                self._next_class_name = model
            
            # if we are in json mode, return the raw json
            if self.json:
                return response

            return list(model(dict(each)) for each in response['results'])
        else:
            raise_custom_error(request.status_code, request.json()['message'])