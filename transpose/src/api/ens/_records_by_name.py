from ..constants import ENS_API_ENDPOINTS

def _records_by_name(ens_names: str or list= None) -> str:
    
    # flatten param if it's a array
    if isinstance(ens_names, (list, tuple,)):
        ens_names = ','.join(ens_names)
        
    base_url = '{}?ens_names={}'.format(ENS_API_ENDPOINTS['records_by_ens_name'], ens_names)
    
    return base_url