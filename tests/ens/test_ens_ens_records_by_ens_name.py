from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic_query():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_ens_name('jbecker.eth')
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_ens_name(['jbecker.eth', 'alex101.eth'])
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False