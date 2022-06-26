from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_token_id(contract_address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D', token_id=999)
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_token_id(contract_address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D', token_id=999, limit=1)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_filter():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_token_id(contract_address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D', token_id=999)
        
        assert len(transactions) >= 1
        assert all(transaction.contract_address == '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D' and transaction.token_id == 999 for transaction in transactions)
        
    except Exception:
        assert False