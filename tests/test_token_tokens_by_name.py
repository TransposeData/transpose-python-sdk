from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.Token.tokens_by_name(name='ape')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        collections = api.Token.tokens_by_name(name='ape')
        
        assert len(collections) >= 10
        assert all(collection.contract_address != None for collection in collections)
        assert api._next != None
        
        collections = api.Token.next()
        assert len(collections) >= 10
        assert all(collection.contract_address != None for collection in collections)
        
    except Exception:
        assert False