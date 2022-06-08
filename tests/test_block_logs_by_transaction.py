from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_transaction(transaction_hash='0xc3274de6377eb49e09c608d68c6a74ee0dc87130a9bcf9760b3f7025c8cf898c')
        
        assert len(logs) >= 1
        
    except Exception:
        assert False
        
def test_basic():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_transaction(transaction_hash='0xc3274de6377eb49e09c608d68c6a74ee0dc87130a9bcf9760b3f7025c8cf898c', limit=1)
        
        assert len(logs) >= 1
        assert api._next != None
        
        logs = api.block.next()
        
        assert len(logs) >= 1
        
    except Exception:
        assert False