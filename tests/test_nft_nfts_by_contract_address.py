from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        tokens = api.NFT.nfts_by_contract_address(contract_address='0x23581767a106ae21c074b2276d25e5c3e136a68b')
        
        assert len(tokens) >= 10
        assert tokens[0].contract_address != None
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        tokens = api.NFT.nfts_by_contract_address(contract_address='0x23581767a106ae21c074b2276d25e5c3e136a68b')
        
        assert len(tokens) >= 10
        assert tokens[0].contract_address != None
        assert api._next != None
        
        tokens = api.NFT.next()
        
        assert len(tokens) >= 10
        assert tokens[0].contract_address != None
        assert api._next != None
    except Exception:
        assert False