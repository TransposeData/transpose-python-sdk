from ._sales import _sales
from ._transfers import _transfers
from ._nfts_by_name import _nfts_by_name
from ._nfts_by_owner import _nfts_by_owner
from ._sales_by_account import _sales_by_account
from ._nfts_by_token_id import _nfts_by_token_id
from ._sales_by_token_id import _sales_by_token_id
from ._owners_by_token_id import _owners_by_token_id
from ._collections_by_name import _collections_by_name
from ._nfts_by_date_minted import _nfts_by_date_minted
from ._transfers_by_account import _transfers_by_account
from ._transfers_by_token_id import _transfers_by_token_id
from ._collections_by_symbol import _collections_by_symbol
from ._nfts_by_contract_address import _nfts_by_contract_address
from ._sales_by_contract_address import _sales_by_contract_address
from ._owners_by_contract_address import _owners_by_contract_address
from ._collections_by_date_created import _collections_by_date_created
from ._transfers_by_contract_address import _transfers_by_contract_address
from ._collections_by_contract_address import _collections_by_contract_address

from ...util.models import *
from typing import List

class NFT():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()
        
    # Get Collections by Date Created
    # https://api.transpose.io/v0/nft/collections-by-date-created
    def collections_by_date_created(self,
                                    created_after: str or int = '1970-01-01 00:00:00',
                                    created_before: str or int = '2050-01-01 00:00:00',
                                    standard: str or int = 'ERC-721',
                                    order: str = 'asc',
                                    limit: int = 10) -> List[Collection]:
        return self.super.perform_authorized_request(Collection, _collections_by_date_created(created_after, created_before, standard, order, limit))
    
    # Get Collections by Contract Address
    # https://api.transpose.io/v0/nft/collections-by-contract-address
    def collections_by_contract_address(self,
                                        contract_addresses: str or list=None) -> List[Collection]:
        return self.super.perform_authorized_request(Collection, _collections_by_contract_address(contract_addresses))
    
    # Get Collections by Name
    # https://api.transpose.io/v0/nft/collections-by-name
    def collections_by_name(self, 
                            name: str=None,
                            limit: int=10,
                            fuzzy: bool=False) -> List[Collection]:
        return self.super.perform_authorized_request(Collection, _collections_by_name(name, limit, fuzzy))
    
    # Get Collections by Synbol
    # https://api.transpose.io/v0/nft/collections-by-symbol
    def collections_by_symbol(self,
                              symbol: str=None,
                              limit: int=10,
                              fuzzy: bool=False) -> List[Collection]:
        return self.super.perform_authorized_request(Collection, _collections_by_symbol(symbol, limit, fuzzy))
    
    # Get NFTs by Date Minted
    # https://api.transpose.io/v0/nft/nfts-by-date-minted
    def nfts_by_date_minted(self,
                            minted_after: str or int = '1970-01-01 00:00:00',
                            minted_before: str or int = '2050-01-01 00:00:00',
                            contract_address: str = None,
                            order: str = 'asc',
                            limit: int = 10) -> List[NFTModel]:
        return self.super.perform_authorized_request(NFTModel, _nfts_by_date_minted(minted_after, minted_before, contract_address, order, limit))
    
    # Get NFTs by Contract Address
    # https://api.transpose.io/v0/nft/nfts-by-contract-address
    def nfts_by_contract_address(self,
                                 contract_address: str = None,
                                 limit: int = 10) -> List[NFTModel]:
        return self.super.perform_authorized_request(NFTModel, _nfts_by_contract_address(contract_address, limit))
    
    # Get NFTs by Token ID
    # https://api.transpose.io/v0/nft/nfts-by-token-id
    def nfts_by_token_id(self,
                         contract_addresses: str or list = None,
                         token_ids: str or int = None) -> List[NFTModel]:
        return self.super.perform_authorized_request(NFTModel, _nfts_by_token_id(contract_addresses, token_ids))
    
    # Get NFTs by Name
    # https://api.transpose.io/v0/nft/nfts-by-name
    def nfts_by_name(self,
                     name: str = None, 
                     limit: int = 10,
                     fuzzy: bool=False) -> List[NFTModel]:
        return self.super.perform_authorized_request(NFTModel, _nfts_by_name(name, limit, fuzzy))
    
    # Get NFTs by Owner
    # https://api.transpose.io/v0/nft/nfts-by-owner
    def nfts_by_owner(self,
                      owner_address: str = None,
                      contract_address: str = None,
                      limit: int = 10) -> List[NFTWithOwner]:
        return self.super.perform_authorized_request(NFTWithOwner, _nfts_by_owner(owner_address, contract_address, limit))

    # Get Owners by Contract Address
    # https://api.transpose.io/v0/nft/owners-by-contract-address
    def owners_by_contract_address(self,
                                   contract_address: str = None,
                                   limit: int = 10) -> List[NFTOwner]:
        return self.super.perform_authorized_request(NFTOwner, _owners_by_contract_address(contract_address, limit))
    
    # Get Owners by Token ID
    # https://api.transpose.io/v0/nft/owners-by-token-id
    def owners_by_token_id(self,
                           contract_address: str = None,
                           token_id: str or int = None,
                           limit: int = 10) -> List[NFTOwner]:
        return self.super.perform_authorized_request(NFTOwner, _owners_by_token_id(contract_address, token_id, limit))
    
    # Get Transfers
    # https://api.transpose.io/v0/nft/transfers
    def transfers(self,
                  transferred_after: int or str='1970-01-01T00:00:00',
                  transferred_before: int or str='2050-01-01T00:00:00',
                  transfer_category: str='all',
                  order: str='asc',
                  limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(NFTTransfer, _transfers(transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Contract Address
    # https://api.transpose.io/v0/nft/transfers-by-contract-address
    def transfers_by_contract_address(self,
                                      contract_address: str = None,
                                      transferred_after: int or str='1970-01-01T00:00:00',
                                      transferred_before: int or str='2050-01-01T00:00:00',
                                      transfer_category: str='all',
                                      order: str='asc',
                                      limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(NFTTransfer, _transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Token ID
    # https://api.transpose.io/v0/nft/transfers-by-token-id
    def transfers_by_token_id(self,
                              token_id: int = None,
                              contract_address: str = None,
                              transferred_after: int or str='1970-01-01T00:00:00',
                              transferred_before: int or str='2050-01-01T00:00:00',
                              transfer_category: str='all',
                              order: str='asc',
                              limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(NFTTransfer, _transfers_by_token_id(token_id, contract_address, transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Account
    # https://api.transpose.io/v0/nft/transfers-by-account
    def transfers_by_account(self,
                             account_address: str = None,
                             transferred_after: int or str='1970-01-01T00:00:00',
                             transferred_before: int or str='2050-01-01T00:00:00',
                             transfer_category: str='all',
                             order: str='asc',
                             limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(NFTTransfer, _transfers_by_account(account_address, transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Sales
    # https://api.transpose.io/v0/nft/sales
    def sales(self,
              sold_after: str or int = '1970-01-01T00:00:00',
              sold_before: str or int = '2050-01-01T00:00:00',
              order: str = 'asc',
              limit: int = 10) -> List[NFTSale]:
        return self.super.perform_authorized_request(NFTSale, _sales(sold_after, sold_before, order, limit))
    
    # Get Sales by Contract Address
    # https://api.transpose.io/v0/nft/sales_by_contract_address
    def sales_by_contract_address(self,
              contract_address: str = None,
              sold_after: str or int = '1970-01-01T00:00:00',
              sold_before: str or int = '2050-01-01T00:00:00',
              order: str = 'asc',
              limit: int = 10) -> List[NFTSale]:
        return self.super.perform_authorized_request(NFTSale, _sales_by_contract_address(contract_address, sold_after, sold_before, order, limit))
    
    # Get Sales by Token ID
    # https://api.transpose.io/v0/nft/sales_by_token_id
    def sales_by_token_id(self,
              contract_address: str = None,
              token_id: int = None,
              sold_after: str or int = '1970-01-01T00:00:00',
              sold_before: str or int = '2050-01-01T00:00:00',
              order: str = 'asc',
              limit: int = 10) -> List[NFTSale]:
        return self.super.perform_authorized_request(NFTSale, _sales_by_token_id(contract_address, token_id, sold_after, sold_before, order, limit))
    
    # Get Sales by Account Address
    # https://api.transpose.io/v0/nft/sales_by_account
    def sales_by_account(self,
              account_address: str = None,
              sold_after: str or int = '1970-01-01T00:00:00',
              sold_before: str or int = '2050-01-01T00:00:00',
              role: str = 'all',
              order: str = 'asc',
              limit: int = 10) -> List[NFTSale]:
        return self.super.perform_authorized_request(NFTSale, _sales_by_account(account_address, sold_after, sold_before, role, order, limit))
    