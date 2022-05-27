from transpose import Transpose, api_key

def test_basic_query():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_name('jbecker.eth')
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False
        
def test_batch_query():
    try:
        api = Transpose(api_key)

        records = api.ENS.records_by_name(['jbecker.eth', 'alex101.eth'])
        
        assert records['status'] == 'success'
        assert records['count'] == len(records['results'])
        assert len(records['results']) >= 1
    except Exception:
        assert False