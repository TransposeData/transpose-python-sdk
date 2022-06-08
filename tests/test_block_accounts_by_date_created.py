from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        account = api.block.accounts_by_date_created(created_after='2019-01-01T00:00:00Z', created_before='2020-01-01T00:00:00Z')
        
        assert len(account) >= 10
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        account = api.block.accounts_by_date_created(created_after='2019-01-01T00:00:00Z', created_before='2020-01-01T00:00:00Z')
        
        assert len(account) >= 10
        assert api._next != None
        
        account = api.block.next()
        
        assert len(account) >= 10
        
    except Exception:
        assert False