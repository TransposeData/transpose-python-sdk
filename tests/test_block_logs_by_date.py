from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_date(emitted_after='2020-01-01 00:00:00',)
        
        assert len(logs) >= 1
        
    except Exception:
        assert False
        
def test_cursor():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_date(emitted_after='2020-01-01 00:00:00',)
        
        assert len(logs) >= 1
        assert api._next != None
        
        logs = api.block.next()
        
        assert len(logs) >= 1
        
    except Exception:
        assert False
        
def test_range():
    try:
        api = Transpose(api_key)

        logs = api.block.logs_by_date(emitted_after='2019-01-01 00:00:00', emitted_before='2020-01-01 00:00:00')
        
        assert len(logs) >= 1
        assert all(log.timestamp >= '2019-01-01 00:00:00' and log.timestamp <= '2020-01-01 00:00:00' for log in logs)
        
    except Exception:
        assert False