from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.Token.operator_approvals_by_account(account_address='0xefBaDCad52F6baec237731123e638fd4e34f63C4', approved_after='2015-01-01 00:00:00')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.Token.operator_approvals_by_account(account_address='0xefBaDCad52F6baec237731123e638fd4e34f63C4', approved_after='2015-01-01 00:00:00')
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.Block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        transactions = api.Token.operator_approvals_by_account(account_address='0xefBaDCad52F6baec237731123e638fd4e34f63C4', approved_after='2015-01-01 00:00:00', approved_before='2020-01-01 00:00:00')
        
        assert len(transactions) >= 1
        assert all(transaction.timestamp >= '2015-01-01 00:00:00' and transaction.timestamp <= '2020-01-01 00:00:00' for transaction in transactions)
        
    except Exception:
        assert False