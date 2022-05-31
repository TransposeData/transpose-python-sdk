from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.Block.transactions_by_hash(transaction_hashes='0x78b4eed73e03569052caba1e6555aa3f1eae5d206d84f923ca9039de220bec48')
        
        assert len(transactions) == 1
        assert transactions.transaction_hash == '0x78b4eed73e03569052caba1e6555aa3f1eae5d206d84f923ca9039de220bec48'
        
    except Exception:
        assert False