from transpose import Transpose, api_key

def test_basic():
    try:
        api = Transpose(api_key)

        tokens = api.NFT.nfts_by_token_id(contract_addresses='0x23581767a106ae21c074b2276d25e5c3e136a68b', token_ids=1)
        
        assert len(tokens) >= 1
        assert all(token.contract_address != None for token in tokens)

    except Exception:
        assert False
        
def test_batch():
    try:
        api = Transpose(api_key)

        tokens = api.NFT.nfts_by_token_id(contract_addresses=['0x23581767a106ae21c074b2276d25e5c3e136a68b', '0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d'], token_ids=[1, 1])
        
        assert len(tokens) >= 2
        assert all(token.contract_address != None for token in tokens)
        
    except Exception:
        assert False