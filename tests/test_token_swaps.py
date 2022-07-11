from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps(occurred_after='2019-01-01 00:00:00')
        
        assert len(swaps) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps(occurred_after='2019-01-01 00:00:00')
        
        assert len(swaps) >= 1
        assert api._next != None
        
        swaps = api.block.next()
        
        assert len(swaps) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps(occurred_after='2019-01-01 00:00:00', occurred_before='2023-01-01 00:00:00')
        
        assert len(swaps) >= 1
        assert all(swap.timestamp >= '2019-01-01 00:00:00' and swap.timestamp <= '2023-01-01 00:00:00' for swap in swaps)
        
    except Exception:
        assert False