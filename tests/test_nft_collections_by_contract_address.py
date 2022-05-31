from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.NFT.collections_by_contract_address(contract_addresses='0x23581767a106ae21c074b2276d25e5c3e136a68b')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False
        
def test_batch():
    try:
        api = Transpose(api_key)

        collections = api.NFT.collections_by_contract_address(contract_addresses=['0x23581767a106ae21c074b2276d25e5c3e136a68b', '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'])
        
        assert len(collections) >= 2
        assert all(collection.contract_address != None for collection in collections)
        
    except Exception:
        assert False