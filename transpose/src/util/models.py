from typing import List

# these are used in static typing so we can return useful tooltips for users
# and allow for proper type checking and syntax highlighting


# block API data model wrappers
class Account:
    def __init__(self):
        self.account_address: str = None
        self.created_timestamp: str = None
        self.account_type: bool = None
        self.eth_balance: int = None
        
class Block:
    def __init__(self):
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

class Transaction:
    def __init__(self):
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
        
class InternalTransaction:
    def __init__(self):
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
        
class Log:
    def __init__(self):
        self.transaction_hash: str = None
        self.log_index: int = None
        self.transaction_position: int = None
        self.block_number: int = None
        self.timestamp: str = None
        self.address: str = None
        self.topics: List[str] or str = None
        self.data: str = None
        
        
# ENS API data model wrappers
class ENSRecord:
    def __init__(self):
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
        
class ENSTransfer:
    def __init__(self):
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
        

# NFT API data model wrappers
class Collection:
    def __init__(self):
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
        
class NFT:
    def __init__(self):
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

class NFTWithOwner:
    def __init__(self):
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
        
class NFTOwner:
    def __init__(self):
        self.contract_address: str = None
        self.token_id: int = None
        self.owner: str = None
        self.balance: int = None
        
class NFTTransfer:
    def __init__(self):
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
        
class NFTApproval:
    def __init__(self):
        self.contract_address: str = None
        self.token_id: int = None
        self.block_number: int = None
        self.log_index: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.owner: str = None
        self.approved_account: str = None
        
class Operator:
    def __init__(self):
        self.contract_address: str = None
        self.owner: str = None
        self.operator: str = None
        self.authorized: bool = None
        self.allowance: int = None
        
class OperatorApproval:
    def __init__(self):
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


# token data model wrappers
class Token:
    def __init__(self):
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
        
class TokenWithOwner:
    def __init__(self):
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
        
class TokenTransfer:
    def __init__(self):
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

class TokenOwner:
    def __init__(self):
        self.contract_address: str = None
        self.owner: str = None
        self.balance: int = None
        
class NativeTokenTransfer:
    def __init__(self):
        self.block_number: int = None
        self.activity_id: int = None
        self.transaction_hash: str = None
        self.timestamp: str = None
        self.category: str = None
        self.operator: str = None
        self.__setattr__('from', None),
        self.to: str = None
        self.quantity: int = None
        
class NativeTokenBalance:
    def __init__(self):
        self.account_address: str = None
        self.balance: int = None