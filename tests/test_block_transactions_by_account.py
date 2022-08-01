from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_account(account_address='0x0000000009cb38fb8a1bbb8ada23c8261118f019')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_account(account_address='0x0000000009cb38fb8a1bbb8ada23c8261118f019')
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False