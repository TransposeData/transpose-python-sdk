from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.transfers_by_ens_node(node='30879C49095CB1D6557B3F69C9CF42086AB084988A430FC123840C745B1E2C71')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 1
        assert records['count'] == len(records['results'])
    except Exception:
        assert False