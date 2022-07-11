from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps_by_pair(token_one='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', token_two='0xdAC17F958D2ee523a2206206994597C13D831ec7',)
        
        assert len(swaps) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps_by_pair(token_one='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', token_two='0xdAC17F958D2ee523a2206206994597C13D831ec7', occurred_after='2019-01-01 00:00:00')
        
        assert len(swaps) >= 1
        assert api._next != None
        
        swaps = api.block.next()
        
        assert len(swaps) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        swaps = api.token.swaps_by_pair(token_one='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', token_two='0xdAC17F958D2ee523a2206206994597C13D831ec7', occurred_after='2019-01-01 00:00:00', occurred_before='2023-01-01 00:00:00')
        
        assert len(swaps) >= 1
        assert all(swap.from_token == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2' or swap.to_token == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2' for swap in swaps)
        assert all(swap.from_token == '0xdAC17F958D2ee523a2206206994597C13D831ec7' or swap.to_token == '0xdAC17F958D2ee523a2206206994597C13D831ec7' for swap in swaps)
        assert all(swap.timestamp >= '2019-01-01 00:00:00' and swap.timestamp <= '2023-01-01 00:00:00' for swap in swaps)
        
    except Exception:
        assert False