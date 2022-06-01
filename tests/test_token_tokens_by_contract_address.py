from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        collections = api.Token.tokens_by_contract_address(contract_addresses='0xa478c2975ab1ea89e8196811f51a7b7ade33eb11')
        
        assert len(collections) >= 1
        assert all(collection.contract_address != None for collection in collections)

    except Exception:
        assert False
        
def test_batch():
    try:
        api = Transpose(api_key)

        collections = api.Token.tokens_by_contract_address(contract_addresses=['0xa478c2975ab1ea89e8196811f51a7b7ade33eb11', '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'])
        
        assert len(collections) >= 2
        assert all(collection.contract_address != None for collection in collections)
        
    except Exception:
        assert False