from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        response = api.sql.generate_query("Give me the most recently updated ENS name that is 3 characters long. Since all ens names end in \".eth\", you'll need to add 4 to the search length. Optimize this query as much as possible.", "ethereum")
        
        # ensure resp is dict
        assert type(response) is dict
        assert 'options' in response
        assert type(response['options']) is list
        
        for option in response['options']:
            assert 'SELECT' in option
                
    except Exception:
        assert False