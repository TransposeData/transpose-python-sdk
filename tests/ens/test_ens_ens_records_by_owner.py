from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_owner('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 1
        assert records['count'] == len(records['results'])
    except Exception:
        assert False