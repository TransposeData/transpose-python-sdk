from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        primary_record = api.ENS.primary_ens_records_by_account('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
    except Exception:
        assert False
        
def test_batch():
    try:
        api = Transpose(api_key)

        primary_record = api.ENS.primary_ens_records_by_account(['0x6666666b0b46056247e7d6cbdb78287f4d12574d', '0x6b912F9Dd1A35794f6CAb59Fdd1adCA0794A64D0'])
        
    except Exception:
        assert False