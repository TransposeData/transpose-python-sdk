from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        account = api.block.contracts_by_creator('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f')
        
        assert len(account) >= 1
        
    except Exception:
        assert False