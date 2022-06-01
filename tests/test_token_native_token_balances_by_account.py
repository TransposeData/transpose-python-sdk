from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        transactions = api.Token.native_token_balances_by_account(account_addresses="jbecker.eth")
        
        assert len(transactions) == 1
        
    except Exception:
        assert False

def test_batch():
    try:
        api = Transpose(api_key)

        transactions = api.Token.native_token_balances_by_account(account_addresses=["jbecker.eth","alex101.eth"])
        
        assert len(transactions) == 2
        
    except Exception:
        assert False