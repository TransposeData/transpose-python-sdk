from ._logs_by_date import _logs_by_date
from ._logs_by_block import _logs_by_block
from ._blocks_by_date import _blocks_by_date
from ._blocks_by_number import _blocks_by_number
from ._logs_by_transaction import _logs_by_transaction
from ._accounts_by_address import _accounts_by_address
from ._contracts_by_creator import _contracts_by_creator
from ._transactions_by_hash import _transactions_by_hash
from ._transactions_by_date import _transactions_by_date
from ._transactions_by_block import _transactions_by_block
from ._transactions_by_account import _transactions_by_account
from ._accounts_by_date_created import _accounts_by_date_created

from ...util.models import *
from typing import List

class Block():
    def __init__(self, base_class) -> None:
        self.super  = base_class
    
    # Transpose Pagination
    # https://docs.transpose.io/reference/pagination
    def next(self) -> List[TransposeModel]:
        return self.super.next()
    
    # Get Accounts by Address
    # https://api.transpose.io/v0/block/accounts-by-address
    def accounts_by_address(self,
                            account_addresses: str or list = None,) -> List[Account]:
        return self.super.perform_authorized_request(Account, _accounts_by_address(account_addresses=account_addresses))
    
    # Get Accounts by Date Created
    # https://api.transpose.io/v0/block/accounts-by-date-created
    def accounts_by_date_created(self,
                                 created_after: str or int='1970-01-01T00:00:00Z',
                                 created_before: str or int='2050-01-01T00:00:00Z',
                                 account_type: str = 'wallet',
                                 order: str = 'asc',
                                 limit: int = 10) -> List[Account]:
        return self.super.perform_authorized_request(Account, _accounts_by_date_created(created_after=created_after, created_before=created_before, account_type=account_type, order=order, limit=limit))

    # Get Contracts by Creator
    # https://api.transpose.io/v0/block/contracts-by-creator
    def contracts_by_creator(self,
                            creator_address: str = None,
                            created_before: str or int='2050-01-01T00:00:00Z',
                            created_after:str or int='1970-01-01T00:00:00Z',
                            order: str = 'asc',
                            limit: int = 10,) -> List[Account]:
        return self.super.perform_authorized_request(Account, _contracts_by_creator(creator_address=creator_address, created_before=created_before, created_after=created_after, order=order, limit=limit))

    # Get Blocks by Number
    # https://api.transpose.io/v0/block/blocks-by-number
    def blocks_by_number(self, 
                         block_number_above: int = 0,
                         block_number_below: int = 1000000000,
                         miner: str = None,
                         order: str = 'asc',
                         limit: int = 10) -> List[BlockModel]:
        return self.super.perform_authorized_request(BlockModel, _blocks_by_number(block_number_above=block_number_above, block_number_below=block_number_below, miner=miner, order=order, limit=limit))
    
    # Get Blocks by Date
    # https://api.transpose.io/v0/block/blocks-by-date
    def blocks_by_date(self, 
                       mined_after:str or int='1970-01-01T00:00:00Z',
                       mined_before: str or int='2050-01-01T00:00:00Z',
                       miner: str = None,
                       order: str = 'asc',
                       limit: int = 10) -> List[BlockModel]:
        return self.super.perform_authorized_request(BlockModel, _blocks_by_date(mined_after=mined_after, mined_before=mined_before, miner=miner, order=order, limit=limit))
    
    # Get Transactions by Hash
    # https://api.transpose.io/v0/block/transactions-by-hash
    def transactions_by_hash(self,
                             transaction_hashes: str or list = None,) -> List[Transaction]:
        return self.super.perform_authorized_request(Transaction, _transactions_by_hash(transaction_hashes=transaction_hashes))
    
    # Get Transactions by Block
    # https://api.transpose.io/v0/block/transactions-by-block
    def transactions_by_block(self, 
                              block_number_above: int = 0,
                              block_number_below: int = 1000000000,
                              order: str = 'asc',
                              limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(Transaction, _transactions_by_block(block_number_above=block_number_above, block_number_below=block_number_below, order=order, limit=limit))
    
    # Get Transactions by Date
    # https://api.transpose.io/v0/block/transactions-by-date
    def transactions_by_date(self, 
                             occurred_after: str or int='1970-01-01T00:00:00Z',
                             occurred_before: str or int='2050-01-01T00:00:00Z',
                             order: str = 'asc',
                             limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(Transaction, _transactions_by_date(occurred_after=occurred_after, occurred_before=occurred_before, order=order, limit=limit))

    # Get Transactions by Account
    # https://api.transpose.io/v0/block/transactions-by-account
    def transactions_by_account(self, 
                             account_address: str = None,
                             occurred_after: str or int='1970-01-01T00:00:00Z',
                             occurred_before: str or int='2050-01-01T00:00:00Z',
                             direction: str = 'all',
                             order: str = 'asc',
                             limit: int = 10) -> List[Transaction]:
        return self.super.perform_authorized_request(Transaction, _transactions_by_account(account_address=account_address, occurred_after=occurred_after, occurred_before=occurred_before, direction=direction, order=order, limit=limit))
    
    # Get Logs by Transaction
    # https://api.transpose.io/v0/block/logs-by-transaction
    def logs_by_transaction(self,
                            transaction_hash: str = None,
                            limit: int = 10) -> List[Log]:
        return self.super.perform_authorized_request(Log, _logs_by_transaction(transaction_hash=transaction_hash, limit=limit))
    
    # Get Logs by Block
    # https://api.transpose.io/v0/block/logs-by-block
    def logs_by_block(self, 
                      block_number_above: int = 0,
                      block_number_below: int = 1000000000,
                      contract_address: str = None,
                      event_signature: str = None,
                      order: str = 'asc',
                      limit: int = 10) -> List[Log]:
        return self.super.perform_authorized_request(Log, _logs_by_block(block_number_above=block_number_above, block_number_below=block_number_below,  contract_address=contract_address, event_signature=event_signature, order=order, limit=limit))
    
    # Get Logs by Date
    # https://api.transpose.io/v0/block/logs-by-date
    def logs_by_date(self, 
                     emitted_after: str or int='1970-01-01T00:00:00Z',
                     emitted_before: str or int='2050-01-01T00:00:00Z',
                     contract_address: str = None,
                     event_signature: str = None,
                     order: str = 'asc',
                     limit: int = 10) -> List[Log]:
        return self.super.perform_authorized_request(Log, _logs_by_date(emitted_after=emitted_after, emitted_before=emitted_before, contract_address=contract_address, event_signature=event_signature, order=order, limit=limit))