from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_ens_instantiation():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)
        
        print(api.ENS)
    except Exception:
        assert False