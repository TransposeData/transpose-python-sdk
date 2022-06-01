from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.Token.tokens_by_date_created(created_after='2019-01-01T00:00:00Z', created_before='2020-01-01T00:00:00Z')
        
        assert len(collections) >= 10
        assert collections[0].contract_address != None
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        collections = api.Token.tokens_by_date_created(created_after='2019-01-01T00:00:00Z', created_before='2020-01-01T00:00:00Z')
        
        assert len(collections) >= 10
        assert collections[0].contract_address != None
        assert api._next != None
        
        collections = api.Token.next()
        
        assert len(collections) >= 10
        assert collections[0].contract_address != None
        assert api._next != None
    except Exception:
        assert False