from ._records_by_date import _records_by_date
from ._records_by_name import _records_by_name
from ._records_by_owner import _records_by_owner
from ._records_by_account import _records_by_account
from ._transfers_by_name import _transfers_by_name
from ._records_by_token_id import _records_by_token_id
from ._transfers_by_token_id import _transfers_by_token_id

from ...util.models import *
from typing import List

class ENS():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()
        
    # Get ENS Records by Owner
    # https://docs.transpose.io/reference/get_ens-records-by-owner
    def records_by_owner(self, 
                         owner_address: str = None,
                         limit: int = 10) -> List[ENSRecord]:
        return self.super.perform_authorized_request(ENSRecord, _records_by_owner(owner_address=owner_address, limit=limit))
    
    # Get ENS Records by Account
    # https://docs.transpose.io/reference/ens-records-by-account
    def records_by_account(self,
                           account_addresses: str or list = None,) -> List[ENSRecord]:
        return self.super.perform_authorized_request(ENSRecord, _records_by_account(account_addresses=account_addresses))
    
    # Get ENS Records by ENS Name
    # https://docs.transpose.io/reference/get_ens-records-by-name
    def records_by_name(self,
                        ens_names: str or list = None,) -> List[ENSRecord]:
        return self.super.perform_authorized_request(ENSRecord, _records_by_name(ens_names=ens_names))

    # Get ENS Records by ENS Token ID
    # https://docs.transpose.io/reference/get_ens-records-by-token-id
    def records_by_token_id(self,
                            token_ids: int or list = None,) -> List[ENSRecord]:
        return self.super.perform_authorized_request(ENSRecord, _records_by_token_id(token_ids=token_ids))

    # Get ENS Records by Date
    # https://docs.transpose.io/reference/get_ens-records-by-date
    def records_by_date(self,
                        timestamp_after: str or int='1970-01-01T00:00:00Z',
                        timestamp_before: str or int='2050-01-01T00:00:00Z',
                        type:  str= 'registration',
                        order: str= 'asc',
                        limit: int= 10) -> List[ENSRecord]:
        return self.super.perform_authorized_request(ENSRecord, _records_by_date(timestamp_after=timestamp_after, timestamp_before=timestamp_before, type=type, order=order, limit=limit))
    
    # Get ENS Transfers by ENS Name
    # https://docs.transpose.io/reference/get_ens-transfers-by-name
    def transfers_by_name(self,
                          ens_name: str= None,
                          transferred_after: int or str='1970-01-01T00:00:00',
                          transferred_before: int or str='2050-01-01T00:00:00',
                          transfer_category: str='all',
                          order: str='asc',
                          limit: int=10) -> List[ENSTransfer]:
        return self.super.perform_authorized_request(ENSTransfer, _transfers_by_name(ens_name=ens_name, transferred_after=transferred_after, transferred_before=transferred_before, transfer_category=transfer_category, order=order, limit=limit))

    # Get ENS Transfers by ENS Token ID
    # https://docs.transpose.io/reference/get_ens-transfers-by-name
    def transfers_by_token_id(self,
                              token_id: str= None,
                              transferred_after: int or str='1970-01-01 00:00:00',
                              transferred_before: int or str='2050-01-01 00:00:00',
                              transfer_category: str='all',
                              order: str='asc',
                              limit: int=10) -> List[ENSTransfer]:
        return self.super.perform_authorized_request(ENSTransfer, _transfers_by_token_id(token_id=token_id, transferred_after=transferred_after, transferred_before=transferred_before, transfer_category=transfer_category, order=order, limit=limit))
