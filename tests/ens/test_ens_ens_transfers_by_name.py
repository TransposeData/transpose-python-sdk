from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ENS.transfers_by_name(ens_name='jbecker.eth')
        
        assert records['status'] == 'success'
        assert len(records['results']) >= 1
        assert records['count'] == len(records['results'])
    except Exception:
        assert False