from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        records = api.ens.records_by_owner('0x6666666b0b46056247e7d6cbdb78287f4d12574d')
        
        assert len(records) >= 1
        assert any(record.ens_name == "jbecker.eth" for record in records)
    except Exception:
        assert False