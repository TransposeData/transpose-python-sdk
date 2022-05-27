from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic_query():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_token_id(47645895181634506270738411170683776203852038783850841298346190697157741364209)
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        records = api.ENS.records_by_token_id([47645895181634506270738411170683776203852038783850841298346190697157741364209, 13225908152018412121024807084765641568966466069787946801937436973220509838633])
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False