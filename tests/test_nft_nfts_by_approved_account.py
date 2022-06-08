from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        tokens = api.nft.nfts_by_approved_account(approved_account='0x09fE5f0236F0Ea5D930197DCE254d77B04128075', limit=1)
        
        assert len(tokens) >= 1
        assert all(token.contract_address != None for token in tokens)

    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        tokens = api.nft.nfts_by_approved_account(approved_account='0x09fE5f0236F0Ea5D930197DCE254d77B04128075', limit=1)
        
        assert len(tokens) >= 1
        assert all(token.contract_address != None for token in tokens)
        assert api._next != None
        
        tokens = api.nft.next()
        assert len(tokens) >= 1
        assert all(token.contract_address != None for token in tokens)
        
    except Exception:
        assert False