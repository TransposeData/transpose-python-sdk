from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.nft.nft_approvals_by_token_id(contract_address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id=20, approved_after='2019-01-01 00:00:00')
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        transactions = api.nft.nft_approvals_by_token_id(contract_address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id=20, approved_after='2019-01-01 00:00:00', limit=1)
        
        assert len(transactions) >= 1
        assert api._next != None
        
        transactions = api.block.next()
        
        assert len(transactions) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        transactions = api.nft.nft_approvals_by_token_id(contract_address='0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d', token_id=20, approved_after='2019-01-01 00:00:00', approved_before='2022-01-01 00:00:00')
        
        assert len(transactions) >= 1
        assert all(transaction.timestamp >= '2019-01-01 00:00:00' and transaction.timestamp <= '2023-01-01 00:00:00' for transaction in transactions)
        
    except Exception:
        assert False