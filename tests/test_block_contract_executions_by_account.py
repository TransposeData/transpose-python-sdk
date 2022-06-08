from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.block.contract_executions_by_account(account_address="0x6666666b0b46056247e7d6cbdb78287f4d12574d")
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.block.contract_executions_by_account(account_address="0x6666666b0b46056247e7d6cbdb78287f4d12574d", limit=1)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        transactions = api.block.contract_executions_by_account(account_address="0x6666666b0b46056247e7d6cbdb78287f4d12574d", occurred_after='2019-01-01 00:00:00', occurred_before='2023-01-01 00:00:00')
        
        assert len(transactions) >= 1
        assert all(transaction.timestamp >= '2019-01-01 00:00:00' and transaction.timestamp <= '2023-01-01 00:00:00' for transaction in transactions)
        
    except Exception:
        assert False