from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps_by_account(account_address='0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D')
        
        assert len(swaps) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps_by_account(account_address='0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D', occurred_after='2019-01-01 00:00:00')
        
        assert len(swaps) >= 1
        assert api._next != None
        
        swaps = api.block.next()
        
        assert len(swaps) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps_by_account(account_address='0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D', occurred_after='2019-01-01 00:00:00', occurred_before='2023-01-01 00:00:00')
        
        assert len(swaps) >= 1
        assert all(swap.origin == '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D' or swap.sender == '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D' for swap in swaps)
        assert all(swap.timestamp >= '2019-01-01 00:00:00' and swap.timestamp <= '2023-01-01 00:00:00' for swap in swaps)
        
    except Exception:
        assert False