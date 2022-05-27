import json

class NFT():
    def __init__(self, base_class) -> None:
        self.super = base_class
        self._next  = None
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> str:
        return self.super.perform_authorized_request(self, self._next)
    
    