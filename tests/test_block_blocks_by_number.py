from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        blocks = api.block.blocks_by_number(block_number_above=1)
        
        assert len(blocks) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        blocks = api.block.blocks_by_number(block_number_above=1)
        
        assert len(blocks) >= 1
        assert api._next != None
        
        blocks = api.block.next()
        
        assert len(blocks) >= 1
        
    except Exception:
        assert False