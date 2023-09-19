from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.token.historical_native_token_balance_by_account(
            account_address='vitalik.eth'
        )
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.token.historical_native_token_balance_by_account(
            account_address='vitalik.eth'
        )
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False