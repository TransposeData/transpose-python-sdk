from transpose import Transpose, api_key
from transpose.src.util.errors import TransposeInvalidAPIKey

def test_valid_connection():
    try:
        api = Transpose(api_key)
        assert isinstance(api, (Transpose,))
    except Exception:
        assert False

def test_invalid_api_key():
    try:
        api = Transpose('some_invalid_api_key')
        assert False
    except TransposeInvalidAPIKey:
        assert True
    except Exception:
        assert False