import base64
import json
from typing import List

# these are used in static typing so we can return useful tooltips for users
# and allow for proper type checking and syntax highlighting

# parent class for all models
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
    
# block API data model wrappers
class Account(TransposeModel):
    def __init__(self, _data: object):
        self.account_address: str = None
        self.created_timestamp: str = None
        self.account_type: bool = None
        self.eth_balance: int = None
        
        super().__init__(_data)
        
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

class Transaction(TransposeModel):
    def __init__(self, _data: object):
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.block_number: int = None
        self.category: str = None
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
        self.method_id: str = None
        self.method_args: List[str] or str = None
        self.contract_address: str = None
        self.internal_transaction_count: int = None
        self.log_count: int = None
        
        super().__init__(_data)
        
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
        
# ENS API data model wrappers
class ENSRecord(TransposeModel):
    def __init__(self, _data: object):
        self.ens_name: str = None
        self.ens_node: str = None
        self.contract_address: str = None
        self.token_id: int = None
        self.seq_id: int = None
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
        
class NFTModel(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.name: str = None
        self.description: str = None
        self.minted_timestamp: str = None
        self.supply: int = None
        self.approved_address: str = None
        self.image_url: str = None
        self.media_url: str = None
        self.external_url: str = None
        self.properties: List[object] or object = None
        self.metadata_url: str = None
        
        super().__init__(_data)

class NFTWithOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.name: str = None
        self.description: str = None
        self.minted_timestamp: str = None
        self.supply: int = None
        self.approved_address: str = None
        self.image_url: str = None
        self.media_url: str = None
        self.external_url: str = None
        self.properties: List[object] or object = None
        self.metadata_url: str = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
class NFTOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.token_id: int = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
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
        
class Operator(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.owner: str = None
        self.operator: str = None
        self.authorized: bool = None
        self.allowance: int = None
        
        super().__init__(_data)
        
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

class TokenOwner(TransposeModel):
    def __init__(self, _data: object):
        self.contract_address: str = None
        self.owner: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
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
        
class NativeTokenBalance(TransposeModel):
    def __init__(self, _data: object):
        self.account_address: str = None
        self.balance: int = None
        
        super().__init__(_data)
        
class CDNResponse():
    def __init__(self, content_type, content):
        self.content_type: str = content_type
        self.content: str = content
        
    # the data object should be returned when the object is converted to a dict
    def __dict__(self) -> dict:
        return {
            'content_type': self.content_type,
            'content': self.content
        }

    # the data object should be returned when the object is converted to a dict
    def to_dict(self) -> dict:
        return {
            'content_type': self.content_type,
            'content': self.content
        }
        
    def save(self, path: str) -> None:
        
        # attempt to base64 decode the data
        decoded_data = self.content
        try:
            decoded_data = base64.decodebytes(decoded_data)
        except:
            pass
        
        # write the data to the file
        with open(path, 'wb') as f:
            f.write(decoded_data)
            
    def json(self) -> object:
        # attempt to base64 decode the data
        decoded_data = self.content
        try:
            decoded_data = base64.decodebytes(decoded_data)
            return json.loads(decoded_data)
        except:
            return None
        
        