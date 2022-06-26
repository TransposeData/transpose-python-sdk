from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_contract_address(contract_address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_contract_address(contract_address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D')
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_filter():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_contract_address(contract_address='0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D')
        
        assert len(transactions) >= 1
        assert all(transaction.contract_address == '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D' for transaction in transactions)
        
    except Exception:
        assert False