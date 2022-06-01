from transpose import Transpose, api_key

def test_basic_query():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_token_id(47645895181634506270738411170683776203852038783850841298346190697157741364209)
        
        assert len(records) >= 1
        assert records.ens_name == "jbecker.eth"
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_token_id([47645895181634506270738411170683776203852038783850841298346190697157741364209, 13225908152018412121024807084765641568966466069787946801937436973220509838633])
        
        assert len(records) >= 2
        assert records[0].ens_name == "alex101.eth"
        assert records[1].ens_name == "jbecker.eth"
    except Exception:
        assert False