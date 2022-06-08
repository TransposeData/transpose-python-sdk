from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.nft.owners_by_token_id(contract_address='0x23581767a106ae21c074b2276d25e5c3e136a68b', token_id=1)
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False