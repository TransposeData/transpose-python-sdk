from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.nft.operators_by_account(owner_address='0x00000000005eF87F8cA7014309eCe7260BbcDAEB')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False

def test_cursor():
    try:
        api = Transpose(api_key)

        collections = api.nft.operators_by_account(owner_address='0x00000000005eF87F8cA7014309eCe7260BbcDAEB')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)
        assert api._next != None
        
        collections = api.nft.next()
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False