from transpose import Transpose, api_key
from transpose.src.util.errors import TransposeInvalidAPIKey

def test_polygon_connection_chain_name():
    try:
        api = Transpose(api_key, chain="polygon")
        assert isinstance(api, (Transpose,))
    except Exception:
        assert False

def test_polygon_connection_chain_id():
    try:
        api = Transpose(api_key, chain_id=137)
        assert isinstance(api, (Transpose,))
    except Exception:
        assert False