from ..constants import ENS_API_ENDPOINTS

def _records_by_token_id(token_ids: int or list = None) -> str:
    
    # flatten ens_names if it's a array
    if isinstance(token_ids, (list, tuple,)):
        token_ids = ','.join([str(id) for id in token_ids])
        
    base_url = '{}?token_ids={}'.format(ENS_API_ENDPOINTS['records_by_ens_token_id'], token_ids)
    
    return base_url