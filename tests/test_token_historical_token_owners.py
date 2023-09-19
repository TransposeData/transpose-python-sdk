from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.token.historical_token_owners(
            contract_address='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
        )
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.token.historical_token_owners(
            contract_address='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
        )
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False