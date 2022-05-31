from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ENS.transfers_by_token_id(token_id=47645895181634506270738411170683776203852038783850841298346190697157741364209)
        
        assert len(records) >= 1
    except Exception:
        assert False