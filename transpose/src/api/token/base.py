from transpose.src.util.models import Operator, OperatorApproval
from ._swaps import _swaps
from ._transfers import _transfers
from ._swaps_by_pair import _swaps_by_pair
from ._tokens_by_name import _tokens_by_name
from ._tokens_by_owner import _tokens_by_owner
from ._swaps_by_account import _swaps_by_account
from ._tokens_by_symbol import _tokens_by_symbol
from ._transfers_by_account import _transfers_by_account
from ._tokens_by_date_created import _tokens_by_date_created
from ._native_token_transfers import _native_token_transfers
from ._swaps_by_contract_address import _swaps_by_contract_address
from ._tokens_by_contract_address import _tokens_by_contract_address
from ._owners_by_contract_address import _owners_by_contract_address
from ._transfers_by_contract_address import _transfers_by_contract_address
from ._native_token_balances_by_account import _native_token_balances_by_account
from ._native_token_transfers_by_account import _native_token_transfers_by_account

from ...util.models import *
from typing import List

class Token():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()

    # Get Tokens by Date Created
    # https://api.transpose.io/v0/token/tokens-by-date-created
    def tokens_by_date_created(self,
                               created_after: str or int = '1970-01-01 00:00:00',
                               created_before: str or int = '2050-01-01 00:00:00',
                               standard: str or int = 'ERC-20',
                               order: str = 'asc',
                               limit: int = 10) -> List[TokenModel]:
        return self.super.perform_authorized_request(TokenModel, _tokens_by_date_created(created_after, created_before, standard, order, limit))
    
    # Get Tokens by Contract Address
    # https://api.transpose.io/v0/token/tokens-by-contract-address
    def tokens_by_contract_address(self,
                                   contract_addresses: str or list=None) -> List[TokenModel]:
        return self.super.perform_authorized_request(TokenModel, _tokens_by_contract_address(contract_addresses))
    
    # Get Tokens by Name
    # https://api.transpose.io/v0/token/tokens-by-name
    def tokens_by_name(self,
                       name: str=None,
                       limit: int=10,
                       fuzzy: bool=False) -> List[TokenModel]:
        return self.super.perform_authorized_request(TokenModel, _tokens_by_name(name, limit, fuzzy))
    
    # Get Tokens by Symbol
    # https://api.transpose.io/v0/token/tokens-by-symbol
    def tokens_by_symbol(self,
                         symbol: str=None,
                         limit: int=10,
                         fuzzy: bool=False) -> List[TokenModel]:
        return self.super.perform_authorized_request(TokenModel, _tokens_by_symbol(symbol, limit, fuzzy))
    
    # Get Tokens by Owner
    # https://api.transpose.io/v0/token/tokens-by-owner
    def tokens_by_owner(self,
                        owner_address: str=None,
                        contract_address: str=None,
                        limit: int=10) -> List[TokenWithOwner]:
        return self.super.perform_authorized_request(TokenWithOwner, _tokens_by_owner(owner_address, contract_address, limit))
    
    # Get Owners by Contract Address
    def owners_by_contract_address(self,
                                   contract_address: str=None,
                                   limit: int=10) -> List[TokenOwner]:
        return self.super.perform_authorized_request(TokenOwner, _owners_by_contract_address(contract_address, limit))

    # Get Transfers
    # https://api.transpose.io/v0/token/transfers
    def transfers(self,
                  transferred_after: int or str='1970-01-01T00:00:00',
                  transferred_before: int or str='2050-01-01T00:00:00',
                  transfer_category: str='all',
                  order: str='asc',
                  limit: int=10) -> List[TokenTransfer]:
        return self.super.perform_authorized_request(TokenTransfer, _transfers(transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Contract Address
    # https://api.transpose.io/v0/token/transfers-by-contract-address
    def transfers_by_contract_address(self,
                                      contract_address: str = None,
                                      transferred_after: int or str='1970-01-01T00:00:00',
                                      transferred_before: int or str='2050-01-01T00:00:00',
                                      transfer_category: str='all',
                                      order: str='asc',
                                      limit: int=10) -> List[TokenTransfer]:
        return self.super.perform_authorized_request(TokenTransfer, _transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit))

    # Get Transfers by Account
    # https://api.transpose.io/v0/token/transfers-by-account
    def transfers_by_account(self,
                             account_address: str = None,
                             transferred_after: int or str='1970-01-01T00:00:00',
                             transferred_before: int or str='2050-01-01T00:00:00',
                             transfer_category: str='all',
                             order: str='asc',
                             limit: int=10) -> List[TokenTransfer]:
        return self.super.perform_authorized_request(TokenTransfer, _transfers_by_account(account_address, transferred_after, transferred_before, transfer_category, order, limit))

    # Get Native Token Transfers
    # https://api.transpose.io/v0/token/native-token-transfers
    def native_token_transfers (self,
                                transferred_after: int or str='1970-01-01T00:00:00',
                                transferred_before: int or str='2050-01-01T00:00:00',
                                order: str='asc',
                                limit: int=10) -> List[NativeTokenTransfer]:
        return self.super.perform_authorized_request(NativeTokenTransfer, _native_token_transfers(transferred_after, transferred_before, order, limit))
    
    # Get Native Token Transfers by Address
    # https://api.transpose.io/v0/token/native-token-transfers-by-address
    def native_token_transfers_by_account (self,
                                           account_address: str = None,
                                           transferred_after: int or str='1970-01-01T00:00:00',
                                           transferred_before: int or str='2050-01-01T00:00:00',
                                           transfer_direction: str='all',
                                           order: str='asc',
                                           limit: int=10) -> List[NativeTokenTransfer]:
        return self.super.perform_authorized_request(NativeTokenTransfer, _native_token_transfers_by_account(account_address, transferred_after, transferred_before, transfer_direction, order, limit))
    
    # Get Native Token Balances by Account
    # https://api.transpose.io/v0/token/native-token-balances-by-account
    def native_token_balances_by_account (self,
                                          account_addresses: list or str = None) -> List[NativeTokenBalance]:
        return self.super.perform_authorized_request(NativeTokenBalance, _native_token_balances_by_account(account_addresses))
    
    # Get Swaps
    # https://api.transpose.io/v0/token/swaps
    def swaps(self,
              occurred_after: int or str='1970-01-01T00:00:00',
              occurred_before: int or str='2050-01-01T00:00:00',
              order: str='asc',
              limit: int=10) -> List[Swap]:
        return self.super.perform_authorized_request(Swap, _swaps(occurred_after, occurred_before, order, limit))
    
    # Get Swaps by Account
    # https://api.transpose.io/v0/token/swaps-by-account
    def swaps_by_account(self,
                        account_address: str = None,
                        occurred_after: int or str='1970-01-01T00:00:00',
                        occurred_before: int or str='2050-01-01T00:00:00',
                        order: str='asc',
                        limit: int=10) -> List[Swap]:
        return self.super.perform_authorized_request(Swap, _swaps_by_account(account_address, occurred_after, occurred_before, order, limit))
    
    # Get Swaps by Contract Address
    # https://api.transpose.io/v0/token/swaps-by-contract-address
    def swaps_by_contract_address (self,
                                    contract_address: str = None,
                                    direction: str = 'all',
                                    occurred_after: int or str='1970-01-01T00:00:00',
                                    occurred_before: int or str='2050-01-01T00:00:00',
                                    order: str='asc',
                                    limit: int=10) -> List[Swap]:
        return self.super.perform_authorized_request(Swap, _swaps_by_contract_address(contract_address, direction, occurred_after, occurred_before, order, limit))
    
    # Get Swaps by Pair
    # https://api.transpose.io/v0/token/swaps-by-pair
    def swaps_by_pair  (self,
                        token_one: str = None,
                        token_two: str = None,
                        occurred_after: int or str='1970-01-01T00:00:00',
                        occurred_before: int or str='2050-01-01T00:00:00',
                        order: str='asc',
                        limit: int=10) -> List[Swap]:
        return self.super.perform_authorized_request(Swap, _swaps_by_pair(token_one, token_two, occurred_after, occurred_before, order, limit))