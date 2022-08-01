import io
import json
import base64

from typing import List
from PIL import Image


# add a .to_dict and .__dict__ method to the list base class
class list(list):
    def to_dict(self):
        return [obj.to_dict() for obj in self]
    
    def __dict__(self):
        return [obj.to_dict() for obj in self]
    

# these are used in static typing so we can return useful tooltips for users
# and allow for proper type checking and syntax highlighting


# parent class for all modelsdi
class TransposeModel:
    def __init__(self, data: object={}) -> None:
        self.__data = data

        # convert the dict object into class attributes
        for key, value in data.items():
            setattr(self, key, value)
    
    # the data object should be returned when the object is converted to a dict
    def __dict__(self) -> dict:
        return self.__data

    # the data object should be returned when the object is converted to a dict
    def to_dict(self) -> dict:
        return self.__data
    
    # allow for subscripting of the data object
    def __getitem__(self, key):
        return self.__data[key]
    
# block API data model wrappers
class Account(TransposeModel):
    def __init__(self, _data: object):
        self.address: str = None
        self.type: str = None
        self.last_active_timestamp: str = None
        self.created_timestamp: str = None
        self.creator: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<AccountObject:  address="{}"  account_type="{}" >'.format(self.address, self.type)
        
class BlockModel(TransposeModel):
    def __init__(self, _data: object):
        self.block_number: int = None
        self.block_hash: str = None
        self.timestamp: str = None
        self.raw_block_data_url: str = None
        self.parent_hash: str = None
        self.mix_hash: str = None
        self.nonce: int = None
        self.sha3_uncles: str = None
        self.difficulty: int = None
        self.total_difficulty: int = None
        self.size: int = None
        self.base_fee_per_gas: int = None
        self.gas_limit: int = None
        self.gas_used: int = None
        self.total_fees_burned: int = None
        self.total_fees_rewarded: int = None
        self.total_fees_saved: int = None
        self.transaction_count: int = None
        self.miner: str = None
        self.mining_reward: int = None
        self.uncle_count: int = None
        self.uncles: List[object] or object = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<BlockObject:  block_number="{}"  block_hash="{}"  miner="{}">'.format(self.block_number, self.block_hash, self.miner)

class Transaction(TransposeModel):
    def __init__(self, _data: object):
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.block_number: int = None
        self.base_fee_per_gas: int = None
        self.max_priority_fee_per_gas: int = None
        self.max_fee_per_gas: int = None
        self.gas_limit: int = None
        self.gas_used: int = None
        self.transaction_fee: int = None
        self.fees_burned: int = None
        self.fees_rewarded: int = None
        self.fees_saved: int = None
        self.nonce: int = None
        self.position: int = None
        self.type: str = None
        self.__setattr__('from', None),
        self.to: str = None
        self.value: int = None
        self.contract_address: str = None
        self.internal_transaction_count: int = None
        self.log_count: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<TransactionObject:  transaction_hash="{}"  from="{}"  to="{}"  value="{}">'.format(self.transaction_hash, self.__getattribute__('from'), self.to, self.value)
        
class InternalTransaction(TransposeModel):
    def __init__(self, _data: object):
        self.block_number: int = None
        self.transaction_position: int = None
        self.trace_address: str = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.category: str = None
        self.gas_limit: int = None
        self.gas_used: int = None
        self.trace_type: str = None
        self.call_type: str = None
        self.__setattr__('from', None),
        self.to: str = None
        self.value: int = None
        self.contract_address: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<InternalTransactionObject:  transaction_hash="{}"  transaction_position="{}"  from="{}"  to="{}"  value="{}">'.format(self.transaction_hash, self.transaction_position, self.__getattribute__('from'), self.to, self.value)
        
class Log(TransposeModel):
    def __init__(self, _data: object):
        self.transaction_hash: str = None
        self.log_index: int = None
        self.transaction_position: int = None
        self.block_number: int = None
        self.timestamp: str = None
        self.address: str = None
        self.topics: List[str] or str = None
        self.data: str = None
        
        super().__init__(_data)
    
    def __repr__(self) -> str:
        return '<LogObject:  transaction_hash="{}"  log_index="{}"  signature="{}">'.format(self.transaction_hash, self.log_index, self.topics[0])
    
      
# ENS API data model wrappers
class ENSRecord(TransposeModel):
    def __init__(self, _data: object):
        self.ens_name: str = None
        self.ens_node: str = None
        self.contract_address: str = None
        self.token_id: int = None
        self.meta_block_number: int = None
        self.owner: str = None
        self.resolver: str = None
        self.resolved_address: str = None
        self.registration_timestamp: str = None
        self.expiration_timestamp: str = None
        self.grace_period_ends: str = None
        self.premium_period_ends: str = None
        self.in_grace_period: bool = None
        self.in_premium_period: bool = None
        self.is_expired: bool = None
        self.last_refreshed: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<ENSRecordObject:  ens_name="{}"  owner="{}"  resolved_address="{}">'.format(self.ens_name, self.owner, self.resolved_address)
        
class ENSTransfer(TransposeModel):
    def __init__(self, _data: object):
        self.ens_name: str = None
        self.ens_node: str = None
        self.contract_address: str = None
        self.token_id: int = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.category: str = None
        self.__setattr__('from', None),
        self.to: str = None
        
        super().__init__(_data)
    
    def __repr__(self) -> str:
        return '<ENSTransferObject:  transaction_hash="{}"  from="{}"  to="{}"  ens_name="{}">'.format(self.transaction_hash, self.__getattribute__('from'), self.to, self.ens_name)


# NFT API data model wrappers
class Collection(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.name: str = None
        self.symbol: str = None
        self.description: str = None
        self.created_timestamp: str = None
        self.standard: str = None
        self.count: int = None
        self.external_url: str = None
        self.image_url: str = None
        self.twitter_username: str = None
        self.telegram_url: str = None
        self.discord_url: str = None
        self.is_nsfw: bool = None
        self.opensea_url: str = None
        self.last_refreshed: str = None
        
        super().__init__(_data)
    
    def __repr__(self) -> str:
        return '<CollectionObject:  contract_address="{}"  name="{}"  standard="{}">'.format(self.contract_address, self.name, self.standard)
    
class NFTModel(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.name: str = None
        self.description: str = None
        self.minted_timestamp: str = None
        self.supply: int = None
        self.image_url: str = None
        self.media_url: str = None
        self.external_url: str = None
        self.properties: List[object] or object = None
        self.metadata_url: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NFTObject:  name="{}"  token_id="{}">'.format(self.name, self.token_id)

class NFTWithOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.name: str = None
        self.description: str = None
        self.minted_timestamp: str = None
        self.supply: int = None
        self.image_url: str = None
        self.media_url: str = None
        self.external_url: str = None
        self.properties: List[object] or object = None
        self.metadata_url: str = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
    
    def __repr__(self) -> str:
        return '<NFTObject:  contract_address="{}"  token_id="{}"  owner="{}">'.format(self.contract_address, self.token_id, self.owner)
    
class NFTOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NFTOwnerObject:  owner="{}"  contract_address="{}"  token_id="{}">'.format(self.contract_address, self.token_id, self.owner)
        
class NFTTransfer(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.category: str = None
        self.__setattr__('from', None),
        self.to: str = None
        self.quantity: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NFTTransferObject:  transaction_hash="{}"  from="{}"  to="{}"  contract_address="{}"  token_id="{}">'.format(self.transaction_hash, self.__getattribute__('from'), self.to, self.contract_address, self.token_id)
        
class NFTApproval(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.owner: str = None
        self.approved_account: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NFTApprovalObject:  transaction_hash="{}" owner="{}" approved_account="{}"  contract_address="{}"  token_id="{}">'.format(self.transaction_hash, self.owner, self.approved_account, self.contract_address, self.token_id)
        
class Operator(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.owner: str = None
        self.operator: str = None
        self.authorized: bool = None
        self.allowance: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<OperatorObject:  contract_address="{}"  owner="{}"  operator="{}"  authorized="{}"  allowance="{}">'.format(self.contract_address, self.owner, self.operator, self.authorized, self.allowance)
        
class OperatorApproval(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.owner: str = None
        self.operator: str = None
        self.authorized: bool = None
        self.allowance: int = None

        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<OperatorApprovalObject:  transaction_hash="{}"  owner="{}"  operator="{}"  authorized="{}"  allowance="{}>'.format(self.transaction_hash, self.owner, self.operator, self.authorized, self.allowance)

# token data model wrappers
class TokenModel(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.name: str = None
        self.symobl: str = None
        self.decimals: int = None
        self.created_timestamp: str = None
        self.standard: str = None
        self.supply: int = None
        self.external_url: str = None
        self.image_url: str = None
        self.twitter_username: str = None
        self.telegeram_url: str = None
        self.discord_url: str = None
        self.whitepaper_url: str = None
        self.last_refreshed: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<TokenObject:  contract_address="{}"  name="{}"  standard="{}">'.format(self.contract_address, self.name, self.standard)
        
class TokenWithOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.name: str = None
        self.symobl: str = None
        self.decimals: int = None
        self.created_timestamp: str = None
        self.standard: str = None
        self.supply: int = None
        self.external_url: str = None
        self.image_url: str = None
        self.twitter_username: str = None
        self.telegeram_url: str = None
        self.discord_url: str = None
        self.whitepaper_url: str = None
        self.last_refreshed: str = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<TokenWithOwnerObject:  contract_address="{}"  owner="{}"  balance="{}">'.format(self.contract_address, self.owner, self.balance)
        
class TokenTransfer(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.category: str = None
        self.operator: str = None
        self.__setattr__('from', None),
        self.to: str = None
        self.quantity: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<TokenTransferObject:  transaction_hash="{}"  from="{}"  to="{}"  contract_address="{}"  quantity="{}">'.format(self.transaction_hash, self.__getattribute__('from'), self.to, self.contract_address, self.quantity)

class TokenOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<TokenOwnerObject:  contract_address="{}"  owner="{}"  balance="{}">'.format(self.contract_address, self.owner, self.balance)
        
class NativeTokenTransfer(TransposeModel):
    def __init__(self, _data: object):
        self.block_number: int = None
        self.activity_id: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.category: str = None
        self.operator: str = None
        self.__setattr__('from', None),
        self.to: str = None
        self.quantity: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NativeTokenTransferObject:  transaction_hash="{}"  from="{}"  to="{}"  quantity="{}">'.format(self.transaction_hash, self.__getattribute__('from'), self.to, self.quantity)
        
class NativeTokenBalance(TransposeModel):
    def __init__(self, _data: object):
        self.account_address: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NativeTokenBalanceObject:  account_address="{}"  balance="{}">'.format(self.account_address, self.balance)

class Swap(TransposeModel):
    def __init__(self, _data: object):
        self.pair_contract_address: str = None
        self.from_token: str = None
        self.to_token: str = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.exchange_name: str = None
        self.contract_version: str = None
        self.quantity_in: int = None
        self.quantity_out: int = None
        self.effective_price: float = None
        self.sender: str = None
        self.origin: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<Swap:  from_token="{}"  to_token="{}"  quantity_in="{}"  quantity_out="{}">'.format(self.from_token, self.to_token, self.quantity_in, self.quantity_out)

class NFTSale(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.exchange_name: str = None
        self.contract_version: str = None
        self.is_multi_token_sale: bool = None
        self.multi_token_sale_index: int = None
        self.quantity: int = None
        self.payment_token: str = None
        self.price: int = None
        self.eth_price: int = None
        self.usd_price: int = None
        self.buyer: str = None
        self.seller: str = None
        
        super().__init__(_data)
        
    def __repr__(self) -> str:
        return '<NFTSale:  buyer="{}"  seller="{}"  contract_address="{}"  token_id="{}">'.format(self.buyer, self.seller, self.contract_address, self.token_id)
     