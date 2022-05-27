from transpose import Transpose, api_key

def test_ens_instantiation():
    try:
        api = Transpose(api_key)
        
        print(api.ENS)
    except Exception:
        assert False