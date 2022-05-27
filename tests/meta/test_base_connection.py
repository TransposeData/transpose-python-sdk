from transpose import Transpose
from transpose.src.util.errors import TransposeInvalidAPIKey

from transpose.src.util.io import read_json_value_at_path

def test_valid_connection():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)
        assert isinstance(api, (Transpose,))
    except Exception:
        assert False

def test_invalid_api_key():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose('some_invalid_api_key')
        assert False
    except TransposeInvalidAPIKey:
        assert True
    except Exception:
        assert False