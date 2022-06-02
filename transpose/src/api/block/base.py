from ._logs_by_date import _logs_by_date
from ._logs_by_block import _logs_by_block
from ._blocks_by_date import _blocks_by_date
from ._blocks_by_hash import _blocks_by_hash
from ._blocks_by_number import _blocks_by_number
from ._logs_by_transaction import _logs_by_transaction
from ._accounts_by_address import _accounts_by_address
from ._transactions_by_hash import _transactions_by_hash
from ._transactions_by_date import _transactions_by_date
from ._transactions_by_block import _transactions_by_block
from ._accounts_by_date_created import _accounts_by_date_created
from ._internal_transactions_by_date import _internal_transactions_by_date
from ._contract_executions_by_account import _contract_executions_by_account
from ._internal_transactions_by_block import _internal_transactions_by_block
from ._contract_executions_by_contract import _contract_executions_by_contract
from ._contract_executions_by_contract_method import _contract_executions_by_method
from ._internal_transactions_by_transaction import _internal_transactions_by_transaction

from transpose.extras import Account, Block, Transaction, InternalTransaction, Log, TransposeModel
from typing import List

class Block():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()
    
    def previous(self) -> List[TransposeModel]:
        return self.super.previous()
    
    # Get Accounts by Address
    # https://api.transpose.io/v0/block/accounts-by-address
    def accounts_by_address(self, account_addresses: str = None,) -> List[Account]:
        return self.super.perform_authorized_request(_accounts_by_address(account_addresses=account_addresses))
    
    # Get Accounts by Date Created
    # https://api.transpose.io/v0/block/accounts-by-date-created
    def accounts_by_date_created(self,
                                 created_after: str or int='1970-01-01T00:00:00Z',
                                 created_before: str or int='2050-01-01T00:00:00Z',
                                 account_type: str = 'eoa',
                                 order: str = 'asc',
                                 limit: int = 10) -> List[Account]:
        return self.super.perform_authorized_request(_accounts_by_date_created(created_after=created_after, created_before=created_before, account_type=account_type, order=order, limit=limit))
    
    # Get Blocks by Hash
    # https://api.transpose.io/v0/block/blocks-by-hash
    def blocks_by_hash(self, block_hashes: str = None,) -> List[Block]:
        return self.super.perform_authorized_request(_blocks_by_hash(block_hashes=block_hashes))
    
    # Get Blocks by Number
    # https://api.transpose.io/v0/block/blocks-by-number
    def blocks_by_number(self, 
                         block_number_above: int = 0,
                         block_number_below: int = 1000000000,
                         miner: str = None,
                         order: str = 'asc',
                         limit: int = 10) -> List[Block]:
        return self.super.perform_authorized_request(_blocks_by_number(block_number_above=block_number_above, block_number_below=block_number_below, miner=miner, order=order, limit=limit))
    
    # Get Blocks by Date
    # https://api.transpose.io/v0/block/blocks-by-date
    def blocks_by_date(self, 
                       mined_after:str or int='1970-01-01T00:00:00Z',
                       mined_before: str or int='2050-01-01T00:00:00Z',
                       miner: str = None,
                       order: str = 'asc',
                       limit: int = 10) -> List[Block]:
        return self.super.perform_authorized_request(_blocks_by_date(mined_after=mined_after, mined_before=mined_before, miner=miner, order=order, limit=limit))
    
    # Get Transactions by Hash
    # https://api.transpose.io/v0/block/transactions-by-hash
    def transactions_by_hash(self, transaction_hashes: str = None,) -> List[Transaction]:
        return self.super.perform_authorized_request(_transactions_by_hash(transaction_hashes=transaction_hashes))
    
    # Get Transactions by Block
    # https://api.transpose.io/v0/block/transactions-by-block
    def transactions_by_block(self, 
                              block_number_above: int = 0,
                              block_number_below: int = 1000000000,
                              order: str = 'asc',
                              limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(_transactions_by_block(block_number_above=block_number_above, block_number_below=block_number_below, order=order, limit=limit))
    
    # Get Transactions by Date
    # https://api.transpose.io/v0/block/transactions-by-date
    def transactions_by_date(self, 
                             occurred_after: str or int='1970-01-01T00:00:00Z',
                             occurred_before: str or int='2050-01-01T00:00:00Z',
                             order: str = 'asc',
                             limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(_transactions_by_date(occurred_after=occurred_after, occurred_before=occurred_before, order=order, limit=limit))
    
    # Get Contract Executions by Account
    # https://api.transpose.io/v0/block/contract-executions-by-account
    def contract_executions_by_account(self, 
                                       account_address: str = None,
                                       occurred_after: str or int='1970-01-01T00:00:00Z',
                                       occurred_before: str or int='2050-01-01T00:00:00Z',
                                       order: str = 'asc',
                                       limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(_contract_executions_by_account(account_address=account_address, occurred_after=occurred_after, occurred_before=occurred_before, order=order, limit=limit))
    
    # Get Contract Executions by Contract
    # https://api.transpose.io/v0/block/contract-executions-by-contract
    def contract_executions_by_contract(self, 
                                        contract_address: str = None,
                                        occurred_after: str or int='1970-01-01T00:00:00Z',
                                        occurred_before: str or int='2050-01-01T00:00:00Z',
                                        order: str = 'asc',
                                        limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(_contract_executions_by_contract(contract_address=contract_address, occurred_after=occurred_after, occurred_before=occurred_before, order=order, limit=limit))
    
    # Get Contract Executions by Contract Method
    def contract_executions_by_method(self,
                                      contract_address: str = None,
                                      method_id: str = None,
                                      occurred_after: str or int='1970-01-01T00:00:00Z',
                                      occurred_before: str or int='2050-01-01T00:00:00Z',
                                      order: str = 'asc',
                                      limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(_contract_executions_by_method(contract_address=contract_address, method_id=method_id, occurred_after=occurred_after, occurred_before=occurred_before, order=order, limit=limit))
    
    # Get Internal Transactions by Transaction
    # https://api.transpose.io/v0/block/internal-transactions-by-hash
    def internal_transactions_by_transaction(self, transaction_hash: str = None, limit: int = 10) -> List[InternalTransaction]:
        return self.super.perform_authorized_request(_internal_transactions_by_transaction(transaction_hash=transaction_hash, limit=limit))
    
    # Get Internal Transactions by Block
    # https://api.transpose.io/v0/block/internal-transactions-by-block
    def internal_transactions_by_block(self, 
                              block_number_above: int = 0,
                              block_number_below: int = 1000000000,
                              order: str = 'asc',
                              limit: int = 10) -> List[InternalTransaction]:
        return self.super.perform_authorized_request(_internal_transactions_by_block(block_number_above=block_number_above, block_number_below=block_number_below, order=order, limit=limit))
    
    # Get Internal Transactions by Date
    # https://api.transpose.io/v0/block/internal-transactions-by-date
    def internal_transactions_by_date(self, 
                             occurred_after: str or int='1970-01-01T00:00:00Z',
                             occurred_before: str or int='2050-01-01T00:00:00Z',
                             order: str = 'asc',
                             limit: int = 10) -> List[InternalTransaction]:
        return self.super.perform_authorized_request(_internal_transactions_by_date(occurred_after=occurred_after, occurred_before=occurred_before, order=order, limit=limit))
    
    # Get Logs by Transaction
    # https://api.transpose.io/v0/block/logs-by-transaction
    def logs_by_transaction(self, transaction_hash: str = None, limit: int = 10) -> List[Log]:
        return self.super.perform_authorized_request(_logs_by_transaction(transaction_hash=transaction_hash, limit=limit))
    
    # Get Logs by Block
    # https://api.transpose.io/v0/block/logs-by-block
    def logs_by_block(self, 
                      block_number_above: int = 0,
                      block_number_below: int = 1000000000,
                      contract_address: str = None,
                      event_signature: str = None,
                      order: str = 'asc',
                      limit: int = 10) -> List[Log]:
        return self.super.perform_authorized_request(_logs_by_block(block_number_above=block_number_above, block_number_below=block_number_below,  contract_address=contract_address, event_signature=event_signature, order=order, limit=limit))
    
    # Get Logs by Date
    # https://api.transpose.io/v0/block/logs-by-date
    def logs_by_date(self, 
                     emitted_after: str or int='1970-01-01T00:00:00Z',
                     emitted_before: str or int='2050-01-01T00:00:00Z',
                     contract_address: str = None,
                     event_signature: str = None,
                     order: str = 'asc',
                     limit: int = 10) -> List[Log]:
        return self.super.perform_authorized_request(_logs_by_date(emitted_after=emitted_after, emitted_before=emitted_before, contract_address=contract_address, event_signature=event_signature, order=order, limit=limit))