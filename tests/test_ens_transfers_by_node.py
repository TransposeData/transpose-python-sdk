from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ENS.transfers_by_node(node='30879C49095CB1D6557B3F69C9CF42086AB084988A430FC123840C745B1E2C71')
        
        assert len(records) >= 1
    except Exception:
        assert False