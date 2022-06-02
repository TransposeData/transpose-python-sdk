from ._transfers import _transfers
from ._nfts_by_name import _nfts_by_name
from ._nft_approvals import _nft_approvals
from ._nfts_by_owner import _nfts_by_owner
from ._nfts_by_token_id import _nfts_by_token_id
from ._operator_approvals import _operator_approvals
from ._owners_by_token_id import _owners_by_token_id
from ._collections_by_name import _collections_by_name
from ._nfts_by_date_minted import _nfts_by_date_minted
from ._operators_by_account import _operators_by_account
from ._transfers_by_account import _transfers_by_account
from ._transfers_by_token_id import _transfers_by_token_id
from ._collections_by_symbol import _collections_by_symbol
from ._nft_approvals_by_account import _nft_approvals_by_account
from ._nfts_by_approved_account import _nfts_by_approved_account
from ._nfts_by_contract_address import _nfts_by_contract_address
from ._nft_approvals_by_token_id import _nft_approvals_by_token_id
from ._owners_by_contract_address import _owners_by_contract_address
from ._collections_by_date_created import _collections_by_date_created
from ._operator_approvals_by_account import _operator_approvals_by_account
from ._operators_by_contract_address import _operators_by_contract_address
from ._transfers_by_contract_address import _transfers_by_contract_address
from ._collections_by_contract_address import _collections_by_contract_address
from ._nft_approvals_by_contract_address import _nft_approvals_by_contract_address
from ._operator_approvals_by_contract_address import _operator_approvals_by_contract_address

from transpose.extras import Collection, NFT, NFTWithOwner, NFTOwner, NFTTransfer, Operator, OperatorApproval, NFTApproval, TransposeModel
from typing import List

class NFT():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()
    
    def previous(self) -> List[TransposeModel]:
        return self.super.previous()
    
    # Get Collections by Date Created
    # https://api.transpose.io/v0/nft/collections-by-date-created
    def collections_by_date_created(self,
                                    created_after: str or int = '1970-01-01 00:00:00',
                                    created_before: str or int = '2050-01-01 00:00:00',
                                    standard: str or int = 'ERC-721',
                                    order: str = 'asc',
                                    limit: int = 10) -> List[Collection]:
        return self.super.perform_authorized_request(_collections_by_date_created(created_after, created_before, standard, order, limit))
    
    # Get Collections by Contract Address
    # https://api.transpose.io/v0/nft/collections-by-contract-address
    def collections_by_contract_address(self, contract_addresses: str or list=None) -> List[Collection]:
        return self.super.perform_authorized_request(_collections_by_contract_address(contract_addresses))
    
    # Get Collections by Name
    # https://api.transpose.io/v0/nft/collections-by-name
    def collections_by_name(self, 
                            name: str=None,
                            limit: int=10) -> List[Collection]:
        return self.super.perform_authorized_request(_collections_by_name(name, limit))
    
    # Get Collections by Synbol
    # https://api.transpose.io/v0/nft/collections-by-symbol
    def collections_by_symbol(self,
                              symbol: str=None,
                              limit: int=10) -> List[Collection]:
        return self.super.perform_authorized_request(_collections_by_symbol(symbol, limit))
    
    # Get NFTs by Date Minted
    # https://api.transpose.io/v0/nft/nfts-by-date-minted
    def nfts_by_date_minted(self,
                            minted_after: str or int = '1970-01-01 00:00:00',
                            minted_before: str or int = '2050-01-01 00:00:00',
                            contract_address: str = None,
                            include_burned_nfts: bool = False,
                            order: str = 'asc',
                            limit: int = 10) -> List[NFT]:
        return self.super.perform_authorized_request(_nfts_by_date_minted(minted_after, minted_before, contract_address, include_burned_nfts, order, limit))
    
    # Get NFTs by Contract Address
    # https://api.transpose.io/v0/nft/nfts-by-contract-address
    def nfts_by_contract_address(self,
                                 contract_address: str = None,
                                 include_burned_nfts: bool = False,
                                 limit: int = 10) -> List[NFT]:
        return self.super.perform_authorized_request(_nfts_by_contract_address(contract_address, include_burned_nfts, limit))
    
    # Get NFTs by Token ID
    # https://api.transpose.io/v0/nft/nfts-by-token-id
    def nfts_by_token_id(self,
                         contract_addresses: str = None,
                         token_ids: str or int = None,
                         include_burned_nfts: bool = False) -> List[NFT]:
        return self.super.perform_authorized_request(_nfts_by_token_id(contract_addresses, token_ids, include_burned_nfts))
    
    # Get NFTs by Name
    # https://api.transpose.io/v0/nft/nfts-by-name
    def nfts_by_name(self,
                     name: str = None, 
                     include_burned_nfts: bool = False,
                     limit: int = 10) -> List[NFT]:
        return self.super.perform_authorized_request(_nfts_by_name(name, include_burned_nfts, limit))
    
    # Get NFTs by Owner
    # https://api.transpose.io/v0/nft/nfts-by-owner
    def nfts_by_owner(self,
                      owner_address: str = None,
                      contract_address: str = None,
                      limit: int = 10) -> List[NFTWithOwner]:
        return self.super.perform_authorized_request(_nfts_by_owner(owner_address, contract_address, limit))
    
    # Get NFTs by Approved Account
    # https://api.transpose.io/v0/nft/nfts-by-approved-account
    def nfts_by_approved_account(self,
                                 approved_account: str = None,
                                 contract_address: str = None,
                                 limit: int = 10) -> List[NFT]:
        return self.super.perform_authorized_request(_nfts_by_approved_account(approved_account, contract_address, limit))
    
    # Get Owners by Contract Address
    # https://api.transpose.io/v0/nft/owners-by-contract-address
    def owners_by_contract_address(self,
                                   contract_address: str = None,
                                   limit: int = 10) -> List[NFTOwner]:
        return self.super.perform_authorized_request(_owners_by_contract_address(contract_address, limit))
    
    # Get Owners by Token ID
    # https://api.transpose.io/v0/nft/owners-by-token-id
    def owners_by_token_id(self,
                           contract_address: str = None,
                           token_id: str or int = None,
                           limit: int = 10) -> List[NFTOwner]:
        return self.super.perform_authorized_request(_owners_by_token_id(contract_address, token_id, limit))
    
    # Get Transfers
    # https://api.transpose.io/v0/nft/transfers
    def transfers(self,
                  transferred_after: int or str='1970-01-01T00:00:00',
                  transferred_before: int or str='2050-01-01T00:00:00',
                  transfer_category: str='all',
                  order: str='asc',
                  limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(_transfers(transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Contract Address
    # https://api.transpose.io/v0/nft/transfers-by-contract-address
    def transfers_by_contract_address(self,
                                      contract_address: str = None,
                                      transferred_after: int or str='1970-01-01T00:00:00',
                                      transferred_before: int or str='2050-01-01T00:00:00',
                                      transfer_category: str='all',
                                      order: str='asc',
                                      limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(_transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit))
    
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
        return self.super.perform_authorized_request(_transfers_by_token_id(token_id, contract_address, transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Account
    # https://api.transpose.io/v0/nft/transfers-by-account
    def transfers_by_account(self,
                             account_address: str = None,
                             transferred_after: int or str='1970-01-01T00:00:00',
                             transferred_before: int or str='2050-01-01T00:00:00',
                             transfer_category: str='all',
                             order: str='asc',
                             limit: int=10) -> List[NFTTransfer]:
        return self.super.perform_authorized_request(_transfers_by_account(account_address, transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Operators by Contract Address
    # https://api.transpose.io/v0/nft/operators-by-contract-address
    def operators_by_contract_address(self,
                                      contract_address: str = None,
                                      limit: int = 10) -> List[Operator]:
        return self.super.perform_authorized_request(_operators_by_contract_address(contract_address, limit))
    
    # Get Operators by Account
    # https://api.transpose.io/v0/nft/operators-by-account
    def operators_by_account(self,
                             owner_address: str = None,
                             contract_address: str = None,
                             limit: int = 10) -> List[Operator]:
        return self.super.perform_authorized_request(_operators_by_account(owner_address, contract_address, limit))
    
    # Get NFT Approvals
    # https://api.transpose.io/v0/nft/nft-approvals
    def nft_approvals(self,
                      approved_after: str or int = '1970-01-01T00:00:00',
                      approved_before: str or int = '2050-01-01T00:00:00',
                      order: str = 'asc',
                      limit: int = 10) -> List[NFTApproval]:
        return self.super.perform_authorized_request(_nft_approvals(approved_after, approved_before, order, limit))
    
    # Get NFT Approvals by Contract Address
    # https://api.transpose.io/v0/nft/approvals-by-contract-address
    def nft_approvals_by_contract_address(self,
                                          contract_address: str = None,
                                          approved_after: str or int = '1970-01-01T00:00:00',
                                          approved_before: str or int = '2050-01-01T00:00:00',
                                          order: str = 'asc',
                                          limit: int = 10) -> List[NFTApproval]:
        return self.super.perform_authorized_request(_nft_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit))
    
    # Get NFT Approvals by Token ID
    # https://api.transpose.io/v0/nft/nft-approvals-by-token-id
    def nft_approvals_by_token_id(self,
                                  contract_address: str = None,
                                  token_id: int = None,
                                  approved_after: str or int = '1970-01-01T00:00:00',
                                  approved_before: str or int = '2050-01-01T00:00:00',
                                  order: str = 'asc',
                                  limit: int = 10) -> List[NFTApproval]:
        return self.super.perform_authorized_request(_nft_approvals_by_token_id(contract_address, token_id, approved_after, approved_before, order, limit))
    
    # Get NFT Approvals by Account
    # https://api.transpose.io/v0/nft/nft-approvals-by-account
    def nft_approvals_by_account(self,
                                 account_address: str = None,
                                 approved_after: str or int = '1970-01-01T00:00:00',
                                 approved_before: str or int = '2050-01-01T00:00:00',
                                 approval_direction: str = 'all',
                                 order: str = 'asc',
                                 limit: int = 10) -> List[NFTApproval]:
        return self.super.perform_authorized_request(_nft_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit))
    
    # Get Operator Approvals
    # https://api.transpose.io/v0/nft/operator-approvals
    def operator_approvals(self,
                      approved_after: str or int = '1970-01-01T00:00:00',
                      approved_before: str or int = '2050-01-01T00:00:00',
                      order: str = 'asc',
                      limit: int = 10) -> List[OperatorApproval]:
        return self.super.perform_authorized_request(_operator_approvals(approved_after, approved_before, order, limit))
    
    # Get Operator by Contract Address
    # https://api.transpose.io/v0/nft/operator-approvals-by-contract-address
    def operator_approvals_by_contract_address(self,
                                          contract_address: str = None,
                                          approved_after: str or int = '1970-01-01T00:00:00',
                                          approved_before: str or int = '2050-01-01T00:00:00',
                                          order: str = 'asc',
                                          limit: int = 10) -> List[OperatorApproval]:
        return self.super.perform_authorized_request(_operator_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit))
    
    # Get Operator Approvals by Account
    # https://api.transpose.io/v0/nft/operator-approvals-by-account
    def operator_approvals_by_account(self,
                                 account_address: str = None,
                                 approved_after: str or int = '1970-01-01T00:00:00',
                                 approved_before: str or int = '2050-01-01T00:00:00',
                                 approval_direction: str = 'all',
                                 order: str = 'asc',
                                 limit: int = 10) -> List[OperatorApproval]:
        return self.super.perform_authorized_request(_operator_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit))