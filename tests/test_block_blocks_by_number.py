from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        blocks = api.Block.blocks_by_number(block_number_above=0)
        
        assert len(blocks) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        blocks = api.Block.blocks_by_number(block_number_above=0)
        
        assert len(blocks) >= 1
        assert api._next != None
        
        blocks = api.Block.next()
        
        assert len(blocks) >= 1
        
    except Exception:
        assert False
        
def test_miner():
    try:
        api = Transpose(api_key)

        blocks = api.Block.blocks_by_number(block_number_above=0, miner='0x00192Fb10dF37c9FB26829eb2CC623cd1BF599E8')
        
        assert len(blocks) >= 1
        assert not any(block.miner != '0x00192Fb10dF37c9FB26829eb2CC623cd1BF599E8' for block in blocks)
        
    except Exception:
        assert False