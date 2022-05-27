from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_resolver('0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 10
        assert records['count'] == len(records['results'])
    except Exception:
        assert False
        
def test_cursor():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_resolver('0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41')
        
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