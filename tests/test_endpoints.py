from datetime import datetime
from transpose import Transpose, api_key
from transpose.src.base import TransposeInvalidAPIKey

def test_basic():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('ohlc', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False
        
def test_normalize_1():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('https://api.transpose.io/endpoint/ohlc', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False
        
def test_normalize_2():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('https://api.transpose.io/ohlc', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False

def test_normalize_3():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('https://api.transpose.io/ohlc/', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False
        
def test_normalize_4():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('https://api.transpose.io/endpoint/ohlc/', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False
        
def test_normalize_5():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('https://api.transpose.io/endpoint/ohlc/1', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False
        
def test_normalize_6():
    try:
        api = Transpose(api_key)
        
        parameters = {
            'start_date': datetime.now().isoformat().split("T")[0],
            'time_interval': '1 day',
            'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
        }

        response = api.endpoint.query('https://api.transpose.io/endpoint/ohlc/1/', parameters)
        
        assert response['stats']['count'] >= 1
        assert len(response['results']) >= 1
        
    except Exception:
        assert False
        
def test_invalid():
    try:
        api = Transpose(api_key)
        response = api.endpoint.query('https://api.transpose.io/endpoint/invalid-nafsndklfasnfkln', {})
        
        # assert throws
        assert False
        
    except TransposeInvalidAPIKey:
        assert True
        
    except Exception:
        assert False