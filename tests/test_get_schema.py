import json
from transpose import Transpose, api_key
from transpose.src.base import TransposeBadRequest

def test_basic():
    try:
        api = Transpose(api_key)

        response = api.sql.schema()
        
        # ensure resp is dict
        assert type(response) is dict
        
        # ensure resp exists
        assert 'schema' in response
        assert len(response['schema']) > 0
        
        # ensure all chains are present
        assert 'ethereum' in response['schema']
        assert 'polygon' in response['schema']
        assert 'goerli' in response['schema']
        assert 'arbitrum' in response['schema']
        assert 'canto' in response['schema']
        assert 'scroll' in response['schema']
        
    except Exception:
        assert False