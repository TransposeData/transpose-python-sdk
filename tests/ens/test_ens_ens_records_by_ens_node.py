from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic_query():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_ens_node('30879C49095CB1D6557B3F69C9CF42086AB084988A430FC123840C745B1E2C71')
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_ens_node(['30879C49095CB1D6557B3F69C9CF42086AB084988A430FC123840C745B1E2C71', '91B8B3211445F208D05CFCB2CB76AEE336937BCDB6C3013D8E62AC9CA73B028B'])
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False