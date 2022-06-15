![Block API Banner](https://files.readme.io/888a1d9-TRSP_DocBanner_Block.png)
# Welcome to the Block API

The **Block API** provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.

## Endpoint Overview
The **Block API** supports the following groups of endpoints:
 

1. [Account Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md#Account-Endpoints): Retrieve any account, including both externally-owned accounts and smart contracts, along with essential account metadata.
2. [Block Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md#Block-Endpoints): Retrieve every block in existence with smart fee calculations and flexible query parameters.
3. [Transaction Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md#Transaction-Endpoints): Retrieve every transaction ever created with powerful query parameters that let you filter by block number, transaction hash, involved addresses, transfer value, target contract, target contract method, and more.
4. [Internal Transaction Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md#Internal-Transaction-Endpoints): Retrieve every single internal transaction, including zero-value traces, in a cleaned format by block, date or transaction.
5. [Log Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md#Log-Endpoints): Retrieve and filter all historical logs by account, topic, contract, and much more.


# Endpoint Specifications

## Account Endpoints
| SDK Method                                                                                  | Endpoint URL                       | Returns         |
| ------------------------------------------------------------------------------------------- | ---------------------------------- | --------------- |
| `block.accounts_by_address(account_addresses)`                                              | `GET /v0/block/accounts-by-address`      | `List[Account]` |
| `block.accounts_by_date_created(created_after, created_before, account_type, order, limit)` | `GET /v0/block/accounts-by-date-created` | `List[Account]` |

### Account Model
<details>
<summary>View Model Specification</summary>

The **Account Model** represents a single account. This includes both externally-owned accounts and smart contracts. The **Account Model** follows the following structure: 

| Name              | Description                                                                                 | Type        |
| ----------------- | ------------------------------------------------------------------------------------------- | ----------- |
| account_address   | The address of the account (as a checksum address)                                          | `string`    |
| created_timestamp | The date at which the account was first created (following the pattern 2022-05-10T17:32:22) | `date-time` |
| account_type      | The type of the account. (One of `eoa` or `contract`)                                       | `string`    |
| eth_balance       | The ETH balance of the account (in Wei)                                                     | `integer`   |

</details>


## Block Endpoints
| SDK Method                                                                            | Endpoint URL               | Returns       |
| ------------------------------------------------------------------------------------- | -------------------------- | ------------- |
| `block.block_by_hash(block_hashes)`                                                   | `GET /v0/block/blocks-by-hash`   | `List[Block]` |
| `block.blocks_by_number(block_number_above, block_number_below, miner, order, limit)` | `GET /v0/block/blocks-by-number` | `List[Block]` |
| `block.blocks_by_date(mined_after, mined_before, miner, order, limit)`                | `GET /v0/block/blocks-by-date`   | `List[Block]` |

### Block Model
<details>
<summary>View Model Specification</summary>

The **Block Model** represents a single block. The **Block Model** follows the following structure:

| Name                | Description                                                                 | Type        |
| ------------------- | --------------------------------------------------------------------------- | ----------- |
| block_number        | The block's number.                                                         | `integer`   |
| block_hash          | The hash of all the block's contents.                                       | `string`    |
| timestamp           | The block's timestamp (in ISO-8601 format).                                 | `date-time` |
| raw_block_data_url  | The URL of the block's raw JSON data in the Transpose CDN.                  | `url`       |
| parent_hash         | The block hash of the block's parent.                                       | `string`    |
| mix_hash            | The block's mix hash, used in the proof of work algorithm.                  | `string`    |
| nonce               | The block's nonce, used in the proof of work algorithm.                     | `string`    |
| sha3_uncles         | The hash of the block's uncle blocks.                                       | `string`    |
| difficulty          | The block's mining difficulty.                                              | `integer`   |
| total_difficulty    | Total difficulty of all blocks up until the block.                          | `integer`   |
| size                | The block's size (in bytes).                                                | `integer`   |
| base_fee_per_gas    | The base fee to include a transaction in the block (in Wei per gas unit).   | `integer`   |
| gas_limit           | The maximum amount of gas that can be used in the block (in gas units).     | `integer`   |
| gas_used            | The amount of gas used in the block (in gas units).                         | `integer`   |
| total_fees_burned   | The amount of transaction fees burned in the block (see EIP-1559) (in Wei). | `integer`   |
| total_fees_rewarded | The amount of transaction fees rewarded to the miner of the block (in Wei). | `integer`   |
| total_fees_saved    | The amount of transaction fees saved by transactions in the block (in Wei). | `integer`   |
| transaction_count   | The number of transactions in the block.                                    | `integer`   |
| miner               | The address of the miner who mined the block.                               | `string`    |
| mining_reward       | The amount rewarded to the miner of the block (in Wei).                     | `integer`   |
| uncle_count         | The number of uncle blocks included in the block.                           | `integer`   |
| uncles              | The uncle blocks included in the block (maximum 2 uncles per block).        | `array`     |

</details>

## Transaction Endpoints
| SDK Method                                                                                                                 | Endpoint URL                                     | Returns             |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------- |
| `block.transactions_by_hash(transaction_hashes)`                                                                           | `GET /v0/block/transactions-by-hash`                   | `List[Transaction]` |
| `block.transactions_by_block(block_number_above, block_number_below, order, limit)`                                        | `GET /v0/block/transactions-by-block`                  | `List[Transaction]` |
| `block.transactions_by_date(occurred_after, occurred_before, miner, order, limit)`                                         | `GET /v0/block/transactions-by-date`                   | `List[Transaction]` |
| `block.contract_executions_by_account(account_address, occurred_after, occurred_before, miner, order, limit)`              | `GET /v0/block/contract-executions-by-account`         | `List[Transaction]` |
| `block.contract_executions_by_contract(contract_address, occurred_after, occurred_before, miner, order, limit)`            | `GET /v0/block/contract-executions-by-contract`        | `List[Transaction]` |
| `block.contract_executions_by_contract(contract_address, method_id, occurred_after, occurred_before, miner, order, limit)` | `GET /v0/block/contract-executions-by-contract-method` | `List[Transaction]` |

### Transaction Model
<details>
<summary>View Model Specification</summary>

The **Transaction Model** represents a single transaction. The **Transaction Model** follows the following structure:

| Name                       | Description                                                                                                            | Type        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| transaction_hash           | The transaction hash at which the transfer occurred.                                                                   | `string`    |
| timestamp                  | The timestamp of the transfer (in ISO-8601 format).                                                                    | `date-time` |
| block_number               | The block number the transaction was included in.                                                                      | `integer`   |
| category                   | The category of the ENS name transfer (one of `mint`, `send`, `burn`).                                                 | `string`    |
| base_fee_per_gas           | The base fee to include a transaction in the block (in Wei per gas unit).                                              | `integer`   |
| max_priority_fee_per_gas   | The maximum priority fee used by the transaction (in Wei per gas unit).                                                | `integer`   |
| max_fee_per_gas            | The maximum fee used by the transaction (in Wei per gas unit).                                                         | `integer`   |
| gas_limit                  | The maximum amount of gas that can be used in the block (in gas units).                                                | `integer`   |
| gas_used                   | The amount of gas used in the block (in gas units).                                                                    | `integer`   |
| gas_price                  | The actual price of gas used in the transaction (in Wei per gas unit).                                                 | `integer`   |
| transaction_fee            | The gas fee paid by the transaction (in Wei).                                                                          | `integer`   |
| fees_burned                | The amount of transaction fees burned by the transaction (see EIP-1559) (in Wei).                                      | `integer`   |
| fees_rewarded              | The amount of transaction fees rewarded to the miner of the transaction (in Wei).                                      | `integer`   |
| fees_saved                 | The amount of transaction fees saved by the transaction (in Wei).                                                      | `integer`   |
| nonce                      | The transaction sender's nonce.                                                                                        | `integer`   |
| position                   | The position of the transaction in the block.                                                                          | `integer`   |
| type                       | The type of the transaction (see EIP-1559, EIP-2718).                                                                  | `integer`   |
| from                       | The address of the sender.                                                                                             | `string`    |
| to                         | The address of the receiver.                                                                                           | `string`    |
| value                      | The amount sent by the transaction (in Wei).                                                                           | `integer`   |
| method_id                  | The 10-character method ID of the target contract method that was called by the transaction, if any (e.g. 0x23b872dd). | `string`    |
| method_args                | A list of 64-character arguments used to call the target contract method, if any.                                      | `array`     |
| contract_address           | The address of the contract created by the transaction, if any.                                                        | `string`    |
| internal_transaction_count | The number of internal transactions produced in the transaction                                                        | `integer`   |
| log_count                  | The number of logs produced in the transaction.                                                                        | `integer`   |

</details>


## Internal Transaction Endpoints
| SDK Method                                                                                   | Endpoint URL                             | Returns                     |
| -------------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------- |
| `block.internal_transactions_by_hash(transaction_hash, limit)`                               | `GET /v0/block/internal-transactions-by-hash`  | `List[InternalTransaction]` |
| `block.internal_transactions_by_block(block_number_above, block_number_below, order, limit)` | `GET /v0/block/internal-transactions-by-block` | `List[InternalTransaction]` |
| `block.internal_transactions_by_date(occurred_after, occurred_before, miner, order, limit)`  | `GET /v0/block/internal-transactions-by-date`  | `List[InternalTransaction]` |

### Internal Transaction Model
<details>
<summary>View Model Specification</summary>

The **Internal Transaction Model** represents a single internal transaction (also known as an EVM trace). The **Internal Transaction Model** follows the following structure:

| Name                 | Description                                                             | Type        |
| -------------------- | ----------------------------------------------------------------------- | ----------- |
| block_number         | The block number the transaction was included in.                       | `integer`   |
| transaction_position | The position of the parent transaction in the block.                    | `integer`   |
| trace_address        | The full array address of the internal transaction trace.               | `array`     |
| transaction_hash     | The transaction hash at which the transfer occurred.                    | `string`    |
| timestamp            | The timestamp of the transfer (in ISO-8601 format).                     | `date-time` |
| category             | The category of the ENS name transfer (one of `mint`, `send`, `burn`).  | `string`    |
| gas_limit            | The maximum amount of gas that can be used in the block (in gas units). | `integer`   |
| gas_used             | The amount of gas used in the block (in gas units).                     | `integer`   |
| trace_type           | The type of EVM trace that created the internal transaction.            | `integer`   |
| call_type            | The call type of the internal transaction trace.                        | `integer`   |
| from                 | The address of the sender.                                              | `string`    |
| to                   | The address of the receiver.                                            | `string`    |
| value                | The amount sent by the transaction (in Wei).                            | `integer`   |
| contract_address     | The address of the contract created by the transaction, if any.         | `string`    |

</details>


## Log Endpoints
| SDK Method                                                                                                     | Endpoint URL                  | Returns     |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----------- |
| `block.logs_by_transaction(transaction_hash, limit)`                                                           | `GET /v0/block/logs-by-transaction` | `List[Log]` |
| `block.logs_by_block(block_number_above, block_number_below, contract_address, event_signature, order, limit)` | `GET /v0/block/logs-by-block`       | `List[Log]` |
| `block.logs_by_date(block_number_above, block_number_below, contract_address, event_signature, order, limit)`  | `GET /v0/block/logs-by-date`        | `List[Log]` |

### Log Model
<details>
<summary>View Model Specification</summary>

The **Log Model** represents a single transaction log. The **Log Model** follows the following structure:

| Name                 | Description                                             | Type        |
| -------------------- | ------------------------------------------------------- | ----------- |
| block_number         | The block number the transaction was included in.       | `integer`   |
| log_index            | The index of the log in the block.                      | `integer`   |
| transaction_position | The position of the parent transaction in the block.    | `integer`   |
| transaction_hash     | The transaction hash at which the transfer occurred.    | `string`    |
| timestamp            | The timestamp of the transfer (in ISO-8601 format).     | `date-time` |
| address              | The address of the smart contract that emitted the log. | `string`    |
| topics               | The topics of the log (maximum 4 topics per log).       | `array`     |
| data                 | The data of the log (bytes data as a hex string).       | `string`    |

</details>