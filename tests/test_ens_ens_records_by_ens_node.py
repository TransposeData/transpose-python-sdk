from transpose import Transpose, api_key

def test_basic_query():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_node('30879C49095CB1D6557B3F69C9CF42086AB084988A430FC123840C745B1E2C71')
        
        assert len(records) >= 1
        assert records.ens_name == "jbecker.eth"
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_node(['30879C49095CB1D6557B3F69C9CF42086AB084988A430FC123840C745B1E2C71', '91B8B3211445F208D05CFCB2CB76AEE336937BCDB6C3013D8E62AC9CA73B028B'])
        
        assert len(records) >= 2
        assert records[0].ens_name == "jbecker.eth"
        assert records[1].ens_name == "alex101.eth"
    except Exception:
        assert False