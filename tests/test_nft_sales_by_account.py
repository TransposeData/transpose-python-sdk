from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_account(account_address='0xF9d3d8376Ad581e0804AD451800a2Df8210b8a20')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_account(account_address='0xF9d3d8376Ad581e0804AD451800a2Df8210b8a20', limit=1)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_filter():
    try:
        api = Transpose(api_key)

        transactions = api.nft.sales_by_account(account_address='0xF9d3d8376Ad581e0804AD451800a2Df8210b8a20')
        
        assert len(transactions) >= 1
        assert all(transaction.buyer or transaction.seller == '0xF9d3d8376Ad581e0804AD451800a2Df8210b8a20' for transaction in transactions)
        
    except Exception:
        assert False