![Token API Banner](https://files.readme.io/a8b9223-TRSP_DocBanner_Token_1.png)

# Welcome to the Token API

The **Token API** provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens).

## Endpoint Overview

The **Token API** supports the following groups of endpoints:
1. [Token Info Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Token-Info-Endpoints): Retrieve any token ever created using flexible queries, along with token metadata and symbols.
2. [Owner Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Owner-Endpoints): Retrieve all owners and owner balances for a token (ordered by balance).
3. [Operator Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Operator-Endpoints): Retrieve all operators and operator allowances for a token or owner.
4. [Transfer Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Transfer-Endpoints): Retrieve all transfers, including mints, sends, and burns, for any token or individual account.
5. [Swap Activity Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Swap-Activity-Endpoints): Retrieve all swaps for any token, account, or date range across all decentralized exchanges.
6. [Approval Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Approval-Endpoints): Retrieve all token approvals by token and account (supports both ERC-20 allowances and ERC-777 operators).
7. [Native Token Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Native-Token-Endpoints): Retrieve all native token transfers and balances for any account.

# Endpoint Specifications

## Token Info Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.tokens_by_date_created(created_after, created_before, standard, order, limit)` | `GET /v0/token/tokens-by-date-created` | `List[Token]` |
| `token.tokens_by_contract_address(contract_address, created_after, created_before, standard, order, limit)` | `GET /v0/token/tokens-by-contract-address` | `List[Token]` |
| `token.tokens_by_name(name, limit)` | `GET /v0/token/tokens-by-name` | `List[Token]` |
| `token.tokens_by_symbol(symbol, limit)` | `GET /v0/token/tokens-by-symbol` | `List[Token]` |
| `token.tokens_by_owner(owner_address, contract_address, limit)` | `GET /v0/token/tokens-by-owner` | `List[TokenWithOwner]` |

### Token Model
<details>
<summary>View Model Specification</summary>

The **Token Model** represents a single NFT token. The **Token Model** follows the following structure:

| Name              | Description                                                                                        | Type        |
| ----------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| contract_address  | Contract address of the token                                                                      | `string`    |
| name              | Name of the token                                                                                  | `string`    |
| symbol            | Symbol of the token                                                                                | `string`    |
| decimals          | The number of decimals used by the token in user representations.                                  | `integer`   |
| created_timestamp | The token's timestamp of creation (in ISO-8601 format).                                            | `date-time` |
| standard          | The standard of the token (ERC-20 or ERC-777).                                                     | `string`    |
| supply            | The token's total supply (tokens minted minus tokens burned).                                      | `integer`   |
| external_url      | The token's website URL.                                                                           | `string`    |
| image_url         | The token's image URL in the Transpose CDN.                                                        | `string`    |
| twitter_username  | The token's Twitter username.                                                                      | `string`    |
| telegram_url      | The token's Telegram URL.                                                                          | `string`    |
| discord_url       | The token's Discord URL.                                                                           | `string`    |
| whitepaper_url    | The token's whitepaper URL.                                                                        | `string`    |
| last_refreshed    | The timestamp at which the token was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |

</details>

### Token With Owner Model
<details>
<summary>View Model Specification</summary>

The **Token With Owner Model** represents a single token with included ownership data (i.e. the owner account and owner's balance). The **Token With Owner Model** follows the following structure:

| Name              | Description                                                                                        | Type        |
| ----------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| contract_address  | Contract address of the token                                                                      | `string`    |
| name              | Name of the token                                                                                  | `string`    |
| symbol            | Symbol of the token                                                                                | `string`    |
| decimals          | The number of decimals used by the token in user representations.                                  | `integer`   |
| created_timestamp | The token's timestamp of creation (in ISO-8601 format).                                            | `date-time` |
| standard          | The standard of the token (ERC-20 or ERC-777).                                                     | `string`    |
| supply            | The token's total supply (tokens minted minus tokens burned).                                      | `integer`   |
| external_url      | The token's website URL.                                                                           | `string`    |
| image_url         | The token's image URL in the Transpose CDN.                                                        | `string`    |
| twitter_username  | The token's Twitter username.                                                                      | `string`    |
| telegram_url      | The token's Telegram URL.                                                                          | `string`    |
| discord_url       | The token's Discord URL.                                                                           | `string`    |
| whitepaper_url    | The token's whitepaper URL.                                                                        | `string`    |
| last_refreshed    | The timestamp at which the token was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |
| owner             | The owner's account address.                                                                       | `string`    |
| balance           | The owner's balance of the token.                                                                  | `integer`   |

</details>


## Owner Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.owners_by_contract_address(contract_address, limit)` | `GET /v0/token/owners-by-contract-address` | `List[TokenOwner]` |

### Token Owner Model
<details>
<summary>View Model Specification</summary>

The **Token Owner Model** represents a single token owner. The **Token Owner Model** follows the following structure:

| Name             | Description                                 | Type      |
| ---------------- | ------------------------------------------- | --------- |
| contract_address | The contract address of the ENS collection. | `string`  |
| owner            | The owner's account address.                | `string`  |
| balance          | The owner's balance of the token.           | `integer` |

</details>


## Operator Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.operators_by_contract_address(contract_address, limit)` | `GET /v0/token/operators-by-contract-address` | `List[Operator]` |
| `token.operators_by_account(owner_address, contract_address, limit)` | `GET /v0/token/operators-by-account` | `List[Operator]` |

### Operator Model
<details>
<summary>View Model Specification</summary>

The **Operator Model** represents a single authorized operator for an owner's tokens. The **Operator Model** follows the following structure:

| Name             | Description                                                                       | Type      |
| ---------------- | --------------------------------------------------------------------------------- | --------- |
| contract_address | Contract address of the token in which the operator is approved.                  | `string`  |
| owner            | The address of the owner that approved the operator.                              | `string`  |
| operator         | The address of the operator that was approved.                                    | `string`  |
| authorized       | Whether full approval has been granted or not (only supported by ERC-777 tokens). | `boolean` |
| allowance        | The allowance granted to the operator.                                            | `integer` |

</details>


## Transfer Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.transfers(transferred_after, transferred_before, transfer_category, order, limit)` | `GET /v0/token/transfers` | `List[TokenTransfer]` |
| `token.transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit)` | `GET /v0/token/transfers-by-contract-address` | `List[TokenTransfer]` |
| `token.transfers_by_account(account_address, transferred_after, transferred_before, transfer_category, order, limit)` | `GET /v0/token/transfers-by-account` | `List[TokenTransfer]` |

### Token Transfer Model
<details>
<summary>View Model Specification</summary>

The **Token Transfer Model** represents a single token transfer. The **Token Transfer Model** follows the following structure:

| Name             | Description                                                            | Type        |
| ---------------- | ---------------------------------------------------------------------- | ----------- |
| contract_address | The contract address of the ENS collection.                            | `string`    |
| block_number     | The block number at which the transfer occurred.                       | `integer`   |
| log_index        | The log index at which the transfer occurred.                          | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                   | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                    | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`). | `string`    |
| operator         | The address of the operator that performed the transfer.               | `string`    |
| from             | The address of the sender.                                             | `string`    |
| to               | The address of the receiver.                                           | `string`    |
| quantity         | The quantity of tokens transferred.                                    | `integer`   |

</details>


## Approval Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.operator_approvals(approved_after, approved_before, order, limit)` | `GET /v0/token/operator-approvals` | `List[OperatorApproval]` |
| `token.operator_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit)` | `GET /v0/token/operator-approvals-by-contract-address` | `List[OperatorApproval]` |
| `token.operator_approvals_by_account_address(account_address, approved_after, approved_before, order, limit)` | `GET /v0/token/operator-approvals-by-account-address` | `List[OperatorApproval]` |

### Operator Approval Model
<details>
<summary>View Model Specification</summary>

The **Operator Approval Model** represents a single operator approval. The **Operator Approval Model** follows the following structure:

| Name             | Description                                                                       | Type        |
| ---------------- | --------------------------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the token in which the operator is approved.                  | `string`    |
| block_number     | The block number at which the transfer occurred.                                  | `integer`   |
| log_index        | The log index at which the transfer occurred.                                     | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                              | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                               | `date-time` |
| owner            | The address of the owner.                                                         | `string`    |
| operator         | The address of the operator that was approved.                                    | `string`    |
| authorized       | Whether full approval has been granted or not (only supported by ERC-777 tokens). | `boolean`   |
| allowance        | The allowance granted to the operator.                                            | `integer`   |

</details>


## Swap Activity Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.swaps(occurred_after, occurred_before, order, limit)` | `GET /v0/token/swaps` | `List[Swap]` |
| `token.swaps_by_account(account_address, occurred_after, occurred_before, order, limit)` | `GET /v0/token/swaps-by-account` | `List[Swap]` |
| `token.swaps_by_token(token_address, direction, occurred_after, occurred_before, order, limit)` | `GET /v0/token/swaps-by-token` | `List[Swap]` |
| `token.swaps_by_pair(token_one, token_two occurred_after, occurred_before, order, limit)` | `GET /v0/token/swaps-by-pair` | `List[Swap]` |


### Token Swap Model
<details>
<summary>View Model Specification</summary>

The **Token Swap Model** represents a single token swap. The **Token Swap Model** follows the following structure:

| Name             | Description                                                                 | Type        |
| ---------------- | --------------------------------------------------------------------------- | ----------- |
| pair_contract_address | Contract address of the token pair, if applicable. | `string` |
| from_token | Contract address of the token swapped from. | `string` |
| to_token | Contract address of the token swapped to. | `string` |
| block_number | The block number at which the swap occurred. | `integer` |
| log_index | The log index at which the swap occurred. | `integer` |
| transaction_hash | The transaction hash at which the swap occurred. | `string` |
| timestamp | The timestamp of the swap (in ISO-8601 format). | `date-time` |
| confirmed | Whether the swap is confirmed (i.e 10 blocks have been mined since the swap occurred). | `boolean` |
| exchange_name | The name of the exchange that hosted the token swap. | `string` |
| contract_version | The version of the exchange contract that hosted the token swap. | `string` |
| amount_in | The amount of tokens the swapper put into the swap. | `integer` |
| amount_out | The amount of tokens that the swapper received from the swap | `integer` |
| effective_price | The effective price of `to_token` denominated in `from_token` (`amount_out` / `amount_in`). | `number` |
| sender | The address of the sender (may be a router contract address). | `string` |
| origin |The address of the originator of the swap transaction. | `string` |
</details>

## Native Token Endpoints
| SDK Method | Endpoint URL | Returns |
| ---------- | ------------ | ------- |
| `token.native_token_transfers(transferred_after, transferred_before, order, limit)` | `GET /v0/token/native-token-transfers` | `List[NativeTokenTransfer]` |
| `token.native_token_transfers_by_account(account_address, transferred_after, transferred_before, order, limit)` | `GET /v0/token/native-token-transfers-by-account` | `List[NativeTokenTransfer]` |
| `token.native_token_balances_by_account(account_addresses)` | `GET /v0/token/native-token-balances-by-account` | `List[NativeTokenBalance]` |


### Native Token Transfer Model
<details>
<summary>View Model Specification</summary>

The **Native Token Transfer Model** represents a single native token transfer. The **Native Token Transfer Model** follows the following structure:

| Name             | Description                                                                 | Type        |
| ---------------- | --------------------------------------------------------------------------- | ----------- |
| block_number     | The block number at which the transfer occurred.                            | `integer`   |
| activity_id      | A sequential ID to identify the correct ordering of native token transfers. | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                        | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                         | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`).      | `string`    |
| operator         | The address of the operator that performed the transfer.                    | `string`    |
| from             | The address of the sender.                                                  | `string`    |
| to               | The address of the receiver.                                                | `string`    |
| quantity         | The quantity of tokens transferred.                                         | `integer`   |

</details>

### Native Token Balance Model
<details>
<summary>View Model Specification</summary>

The **Native Token Balance Model** represents an account's native token (Ether) balance. The **Native Token Balance Model** follows the following structure:

| Name            | Description                         | Type      |
| --------------- | ----------------------------------- | --------- |
| account_address | The account address.                | `string`  |
| balance         | The account's native token balance. | `integer` |

</details>
