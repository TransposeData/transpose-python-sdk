from transpose import Transpose

from transpose.src.util.io import read_json_value_at_path

def test_basic():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        primary_record = api.ENS.primary_ens_records_by_account('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
    except Exception:
        assert False
        
def test_batch():
    try:
        api_key = read_json_value_at_path('./keys/api.json', 'api_key')
        api = Transpose(api_key)

        primary_record = api.ENS.primary_ens_records_by_account(['0x6666666b0b46056247e7d6cbdb78287f4d12574d', '0x6b912F9Dd1A35794f6CAb59Fdd1adCA0794A64D0'])
        
    except Exception:
        assert False