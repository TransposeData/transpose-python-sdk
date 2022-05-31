from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.NFT.owners_by_contract_address(contract_address='0x23581767a106ae21c074b2276d25e5c3e136a68b')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        collections = api.NFT.owners_by_contract_address(contract_address='0x23581767a106ae21c074b2276d25e5c3e136a68b')
        
        assert len(collections) >= 10
        assert all(collection.contract_address != None for collection in collections)
        assert api._next != None
        
        collections = api.NFT.next()
        
        assert len(collections) >= 10
        assert all(collection.contract_address != None for collection in collections)
    except Exception:
        assert False