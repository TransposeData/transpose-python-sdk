from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        tokens = api.NFT.nfts_by_owner(owner_address='0x7b557aa52d0055d84b1e3f5487d9018f318372c1')
        
        assert len(tokens) >= 1
        assert all(token.contract_address != None for token in tokens)

    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        tokens = api.NFT.nfts_by_owner(owner_address='0x7b557aa52d0055d84b1e3f5487d9018f318372c1')
        
        assert len(tokens) >= 10
        assert all(token.contract_address != None for token in tokens)
        assert api._next != None
        
        tokens = api.NFT.next()
        assert len(tokens) >= 10
        assert all(token.contract_address != None for token in tokens)
        
    except Exception:
        assert False