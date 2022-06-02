from transpose.src.util.models import Operator, OperatorApproval
from ._transfers import _transfers
from ._tokens_by_name import _tokens_by_name
from ._tokens_by_owner import _tokens_by_owner
from ._tokens_by_symbol import _tokens_by_symbol
from ._operator_approvals import _operator_approvals
from ._transfers_by_account import _transfers_by_account
from ._operators_by_account import _operators_by_account
from ._tokens_by_date_created import _tokens_by_date_created
from ._native_token_transfers import _native_token_transfers
from ._tokens_by_contract_address import _tokens_by_contract_address
from ._owners_by_contract_address import _owners_by_contract_address
from ._operator_approvals_by_account import _operator_approvals_by_account
from ._transfers_by_contract_address import _transfers_by_contract_address
from ._operators_by_contract_address import _operators_by_contract_address
from ._native_token_balances_by_account import _native_token_balances_by_account
from ._native_token_transfers_by_account import _native_token_transfers_by_account
from ._operator_approvals_by_contract_address import _operator_approvals_by_contract_address

from transpose.extras import Token, TokenOwner, TokenWithOwner, TokenTransfer, NativeTokenBalance, NativeTokenTransfer, TransposeModel
from typing import List

class Token():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()
    
    def previous(self) -> List[TransposeModel]:
        return self.super.previous()

    # Get Tokens by Date Created
    # https://api.transpose.io/v0/token/tokens-by-date-created
    def tokens_by_date_created(self,
                               created_after: str or int = '1970-01-01 00:00:00',
                               created_before: str or int = '2050-01-01 00:00:00',
                               standard: str or int = 'ERC-20',
                               order: str = 'asc',
                               limit: int = 10) -> List[Token]:
        return self.super.perform_authorized_request(_tokens_by_date_created(created_after, created_before, standard, order, limit))
    
    # Get Tokens by Contract Address
    # https://api.transpose.io/v0/token/tokens-by-contract-address
    def tokens_by_contract_address(self, contract_addresses: str or list=None) -> List[Token]:
        return self.super.perform_authorized_request(_tokens_by_contract_address(contract_addresses))
    
    # Get Tokens by Name
    # https://api.transpose.io/v0/token/tokens-by-name
    def tokens_by_name(self,
                       name: str=None,
                       limit: int=10) -> List[Token]:
        return self.super.perform_authorized_request(_tokens_by_name(name, limit))
    
    # Get Tokens by Symbol
    # https://api.transpose.io/v0/token/tokens-by-symbol
    def tokens_by_symbol(self,
                         symbol: str=None,
                         limit: int=10) -> List[Token]:
        return self.super.perform_authorized_request(_tokens_by_symbol(symbol, limit))
    
    # Get Tokens by Owner
    # https://api.transpose.io/v0/token/tokens-by-owner
    def tokens_by_owner(self,
                        owner_address: str=None,
                        contract_address: str=None,
                        limit: int=10) -> List[TokenWithOwner]:
        return self.super.perform_authorized_request(_tokens_by_owner(owner_address, contract_address, limit))
    
    # Get Owners by Contract Address
    def owners_by_contract_address(self,
                                   contract_address: str=None,
                                   limit: int=10) -> List[TokenOwner]:
        return self.super.perform_authorized_request(_owners_by_contract_address(contract_address, limit))
    
    # Get Operators by Contract Address
    # https://api.transpose.io/v0/token/operators-by-contract-address
    def operators_by_contract_address(self,
                                      contract_address: str = None,
                                      limit: int = 10) -> List[Operator]:
        return self.super.perform_authorized_request(_operators_by_contract_address(contract_address, limit))
    
    # Get Operators by Account
    # https://api.transpose.io/v0/token/operators-by-account
    def operators_by_account(self,
                             owner_address: str = None,
                             contract_address: str = None,
                             limit: int = 10) -> List[Operator]:
        return self.super.perform_authorized_request(_operators_by_account(owner_address, contract_address, limit))
    
    # Get Transfers
    # https://api.transpose.io/v0/token/transfers
    def transfers(self,
                  transferred_after: int or str='1970-01-01T00:00:00',
                  transferred_before: int or str='2050-01-01T00:00:00',
                  transfer_category: str='all',
                  order: str='asc',
                  limit: int=10) -> List[TokenTransfer]:
        return self.super.perform_authorized_request(_transfers(transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Transfers by Contract Address
    # https://api.transpose.io/v0/token/transfers-by-contract-address
    def transfers_by_contract_address(self,
                                      contract_address: str = None,
                                      transferred_after: int or str='1970-01-01T00:00:00',
                                      transferred_before: int or str='2050-01-01T00:00:00',
                                      transfer_category: str='all',
                                      order: str='asc',
                                      limit: int=10) -> List[TokenTransfer]:
        return self.super.perform_authorized_request(_transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit))

    # Get Transfers by Account
    # https://api.transpose.io/v0/token/transfers-by-account
    def transfers_by_account(self,
                             account_address: str = None,
                             transferred_after: int or str='1970-01-01T00:00:00',
                             transferred_before: int or str='2050-01-01T00:00:00',
                             transfer_category: str='all',
                             order: str='asc',
                             limit: int=10) -> List[TokenTransfer]:
        return self.super.perform_authorized_request(_transfers_by_account(account_address, transferred_after, transferred_before, transfer_category, order, limit))
    
    # Get Operator by Contract Address
    # https://api.transpose.io/v0/token/operator-approvals-by-contract-address
    def operator_approvals_by_contract_address(self,
                                          contract_address: str = None,
                                          approved_after: str or int = '1970-01-01T00:00:00',
                                          approved_before: str or int = '2050-01-01T00:00:00',
                                          order: str = 'asc',
                                          limit: int = 10) -> List[OperatorApproval]:
        return self.super.perform_authorized_request(_operator_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit))
    
    # Get Operator Approvals by Account
    # https://api.transpose.io/v0/token/operator-approvals-by-account
    def operator_approvals_by_account(self,
                                 account_address: str = None,
                                 approved_after: str or int = '1970-01-01T00:00:00',
                                 approved_before: str or int = '2050-01-01T00:00:00',
                                 approval_direction: str = 'all',
                                 order: str = 'asc',
                                 limit: int = 10) -> List[OperatorApproval]:
        return self.super.perform_authorized_request(_operator_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit))
    
    # Get Operator Approvals
    # https://api.transpose.io/v0/token/operator-approvals
    def operator_approvals(self,
                      approved_after: str or int = '1970-01-01T00:00:00',
                      approved_before: str or int = '2050-01-01T00:00:00',
                      order: str = 'asc',
                      limit: int = 10) -> List[OperatorApproval]:
        return self.super.perform_authorized_request(_operator_approvals(approved_after, approved_before, order, limit))
    
    # Get Native Token Transfers
    # https://api.transpose.io/v0/token/native-token-transfers
    def native_token_transfers (self,
                                transferred_after: int or str='1970-01-01T00:00:00',
                                transferred_before: int or str='2050-01-01T00:00:00',
                                order: str='asc',
                                limit: int=10) -> List[NativeTokenTransfer]:
        return self.super.perform_authorized_request(_native_token_transfers(transferred_after, transferred_before, order, limit))
    
    # Get Native Token Transfers by Address
    # https://api.transpose.io/v0/token/native-token-transfers-by-address
    def native_token_transfers_by_account (self,
                                           account_address: str = None,
                                           transferred_after: int or str='1970-01-01T00:00:00',
                                           transferred_before: int or str='2050-01-01T00:00:00',
                                           transfer_direction: str='all',
                                           order: str='asc',
                                           limit: int=10) -> List[NativeTokenTransfer]:
        return self.super.perform_authorized_request(_native_token_transfers_by_account(account_address, transferred_after, transferred_before, transfer_direction, order, limit))
    
    # Get Native Token Balances by Account
    # https://api.transpose.io/v0/token/native-token-balances-by-account
    def native_token_balances_by_account (self,
                                          account_addresses: list or str=None) -> List[NativeTokenBalance]:
        return self.super.perform_authorized_request(_native_token_balances_by_account(account_addresses))