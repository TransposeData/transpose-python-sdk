from ..constants import ENS_API_ENDPOINTS

def _records_by_node(ens_nodes: str or list = None) -> str:
    
    # flatten ens_names if it's a array
    if isinstance(ens_nodes, (list, tuple,)):
        ens_nodes = ','.join(ens_nodes)
        
    base_url = '{}?ens_nodes={}'.format(ENS_API_ENDPOINTS['records_by_ens_node'], ens_nodes)
    
    return base_url