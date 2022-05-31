from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.NFT.transfers_by_contract_address(contract_address='0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.NFT.transfers_by_contract_address(contract_address='0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb', limit=1)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.Block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False