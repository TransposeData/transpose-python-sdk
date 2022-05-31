from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ENS.transfers_by_name(ens_name='jbecker.eth')
        
        assert len(records) >= 1
    except Exception:
        assert False