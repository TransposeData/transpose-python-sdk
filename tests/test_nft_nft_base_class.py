from transpose import Transpose, api_key

def test_ens_instantiation():
    try:
        api = Transpose(api_key)
        
        assert api.nft
    except Exception:
        assert False