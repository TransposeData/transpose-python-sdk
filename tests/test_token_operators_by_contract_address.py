from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.Token.operators_by_contract_address(contract_address='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        collections = api.Token.operators_by_contract_address(contract_address='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2')
        
        assert len(collections) >= 10
        assert all(collection.contract_address != None for collection in collections)
        assert api._next != None
        
        collections = api.Token.next()
        
        assert len(collections) >= 10
        assert all(collection.contract_address != None for collection in collections)
    except Exception:
        assert False