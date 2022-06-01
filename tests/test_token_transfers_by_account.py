from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.Token.transfers_by_account(account_address='0x7b557aa52d0055d84b1e3f5487d9018f318372c1')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.Token.transfers_by_account(account_address='0x7b557aa52d0055d84b1e3f5487d9018f318372c1', limit=1)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.Block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False