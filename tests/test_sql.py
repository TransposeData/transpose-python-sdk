from pandas import DataFrame

from transpose import Transpose, api_key
from transpose.src.base import TransposeBadRequest


def test_basic():
    try:
        api = Transpose(api_key)

        response = api.sql.query("SELECT * FROM ethereum.logs LIMIT 1;")
        
        assert response['stats']['count'] == 1
        assert len(response['results']) == 1
        
    except Exception:
        assert False
        
        
def test_batch():
    try:
        api = Transpose(api_key)

        response = api.sql.query("SELECT * FROM ethereum.logs LIMIT 100;")
        
        assert response['stats']['count'] == 100
        assert len(response['results']) == 100
        
    except Exception:
        assert False
        
        
def test_invalid_query():
    try:
        api = Transpose(api_key)

        response = api.sql.query("SELECT * FROM ethereum.lgos LIMIT 1;")
        
        # assert throws
        assert False
        
    except TransposeBadRequest:
        assert True
        
    except Exception:
        assert False


def test_query_df():
    try:
        api = Transpose(api_key)

        response = api.sql.query("SELECT * FROM ethereum.logs LIMIT 100;", return_df=True)

        assert type(response) is DataFrame
        assert len(response) == 100

    except Exception:
        assert False


def test_schema():
    try:
        api = Transpose(api_key)

        response = api.sql.schema()

        assert isinstance(response, dict)
        assert 'ethereum' in response['schema']
        assert 'settlement_layer' in response['schema']['ethereum']

    except Exception:
        assert False
