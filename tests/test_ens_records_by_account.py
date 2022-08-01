from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        primary_record = api.ens.records_by_account('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
        assert len(primary_record) >= 1
        assert primary_record[0].ens_name == "jbecker.eth"
        
    except Exception:
        assert False
        
def test_batch():
    try:
        api = Transpose(api_key)

        primary_record = api.ens.records_by_account(['0x6666666b0b46056247e7d6cbdb78287f4d12574d', '0x6b912F9Dd1A35794f6CAb59Fdd1adCA0794A64D0'])
        
        assert len(primary_record) >= 1
        assert primary_record[0].ens_name == "jbecker.eth"
        assert primary_record[1].ens_name == "alexhimself.eth"
        
    except Exception:
        assert False