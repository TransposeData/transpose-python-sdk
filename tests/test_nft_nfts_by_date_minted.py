from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        tokens = api.nft.nfts_by_date_minted(minted_after='2019-01-01T00:00:00Z', minted_before='2020-01-01T00:00:00Z')
        
        assert len(tokens) >= 10
        assert tokens[0].contract_address != None
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        tokens = api.nft.nfts_by_date_minted(minted_after='2019-01-01T00:00:00Z', minted_before='2020-01-01T00:00:00Z')
        
        assert len(tokens) >= 10
        assert tokens[0].contract_address != None
        assert api._next != None
        
        tokens = api.nft.next()
        
        assert len(tokens) >= 10
        assert tokens[0].contract_address != None
        assert api._next != None
    except Exception:
        assert False