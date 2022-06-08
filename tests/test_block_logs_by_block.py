from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_block(block_number_above=0)
        
        assert len(logs) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_block(block_number_above=0)
        
        assert len(logs) >= 1
        assert api._next != None
        
        logs = api.block.next()
        
        assert len(logs) >= 1
        
    except Exception:
        assert False
        
def test_blockrange():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_block(block_number_above=0, block_number_below=100000)
        
        assert len(logs) >= 1
        assert all(log.block_number <= 100000 for log in logs)
        
    except Exception:
        assert False