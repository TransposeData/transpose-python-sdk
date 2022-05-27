class ENS():
    def __init__(self, base_class) -> None:
        self.super = base_class
        self.next  = None
    
    def test(self):
        return self.super.perform_authorized_request('https://api.transpose.io/v0/block/blocks-by-number?block_number_below=1')