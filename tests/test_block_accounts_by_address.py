from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        account = api.block.accounts_by_address('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
        assert len(account) >= 1
        assert account[0].address.lower() == "0x6666666b0b46056247e7d6cbdb78287f4d12574d"
        
    except Exception:
        assert False