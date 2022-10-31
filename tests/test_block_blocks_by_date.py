from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        blocks = api.block.blocks_by_date(added_after='2020-01-01 00:00:00',)
        
        assert len(blocks) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        blocks = api.block.blocks_by_date(added_after='2020-01-01 00:00:00',)
        
        assert len(blocks) >= 1
        assert api._next != None
        
        blocks = api.block.next()
        
        assert len(blocks) >= 1
        
    except Exception:
        assert False