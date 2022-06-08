from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        blocks = api.Block.blocks_by_hash('0x88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6')
        
        assert len(blocks) == 1
        assert blocks[0].block_number == 1
        
    except Exception:
        assert False