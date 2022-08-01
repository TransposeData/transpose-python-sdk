from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_account(account_address='0x56cb1965a68e33F918a9eCE0F3133488258b81b9', occurred_after='2020-01-01 00:00:00',)
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_account(account_address='0x56cb1965a68e33F918a9eCE0F3133488258b81b9', occurred_after='2020-01-01 00:00:00',)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        transactions = api.block.transactions_by_account(account_address='0x56cb1965a68e33F918a9eCE0F3133488258b81b9', occurred_after='2019-01-01 00:00:00', occurred_before='2020-01-01 00:00:00')
        
        assert len(transactions) >= 1
        assert all(transaction.timestamp >= '2019-01-01 00:00:00' and transaction.timestamp <= '2020-01-01 00:00:00' for transaction in transactions)
        
    except Exception:
        assert False