from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.transfers_by_token_id(token_id=47645895181634506270738411170683776203852038783850841298346190697157741364209)
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 1
        assert records['count'] == len(records['results'])
    except Exception:
        assert False