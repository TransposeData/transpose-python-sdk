from transpose import Transpose, api_key

def test_basic_query():
    try:
        api = Transpose(api_key)

        records = api.ens.records_by_name('jbecker.eth')
        
        assert len(records) >= 1
        assert records[0].ens_name == "jbecker.eth"
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api = Transpose(api_key)

        records = api.ens.records_by_name(['jbecker.eth', 'alex101.eth'])
        
        assert len(records) >= 2
        assert records[0].ens_name == "jbecker.eth"
        assert records[1].ens_name == "alex101.eth"
    except Exception:
        assert False