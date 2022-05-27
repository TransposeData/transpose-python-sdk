from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_date(timestamp_after='2019-01-01T00:00:00Z', timestamp_before='2020-01-01T00:00:00Z')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 10
        assert records['count'] == len(records['results'])
    except Exception:
        assert False
        
def test_cursor():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_date(timestamp_after='2019-01-01T00:00:00Z', timestamp_before='2020-01-01T00:00:00Z')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 10
        assert records['count'] == len(records['results'])
        
        assert api.ENS._next != None
        
        records = api.ENS.next()
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 10
        assert records['count'] == len(records['results'])
    except Exception:
        assert False