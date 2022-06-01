![Token API Banner](https://files.readme.io/a8b9223-TRSP_DocBanner_Token_1.png)

# Welcome to the Token API

The **Token API** provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens).

## Endpoint Overview

The **Token API** supports the following groups of endpoints:
1. *Token Info Endpoints*: Retrieve any token ever created using flexible queries, along with token metadata and symbols.
2. *Owner Endpoints*: Retrieve all owners and owner balances for a token (ordered by balance).
3. *Operator Endpoints*: Retrieve all operators and operator allowances for a token or owner.
4. *Transfer Activity Endpoints*: Retrieve all transfers, including mints, sends, and burns, for any token or individual account.
5. *Approval Activity Endpoints*: Retrieve all token approvals by token and account (supports both ERC-20 allowances and ERC-777 operators).


## Data Models


### Token Model

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

### Token With Owner Model

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

### Token Transfer Model

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

### Token Owner Model

The **Token Owner Model** represents a single token owner. The **Token Owner Model** follows the following structure:

| Name             | Description                                 | Type      |
| ---------------- | ------------------------------------------- | --------- |
| contract_address | The contract address of the ENS collection. | `string`  |
| owner            | The owner's account address.                | `string`  |
| balance          | The owner's balance of the token.           | `integer` |

### Operator Approval Model

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

### Operator Model

The **Operator Model** represents a single authorized operator for an owner's tokens. The **Operator Model** follows the following structure:

| Name             | Description                                                                       | Type      |
| ---------------- | --------------------------------------------------------------------------------- | --------- |
| contract_address | Contract address of the token in which the operator is approved.                  | `string`  |
| owner            | The address of the owner that approved the operator.                              | `string`  |
| operator         | The address of the operator that was approved.                                    | `string`  |
| authorized       | Whether full approval has been granted or not (only supported by ERC-777 tokens). | `boolean` |
| allowance        | The allowance granted to the operator.                                            | `integer` |

### Native Token Transfer Model

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

### Native Token Balance Model

The **Native Token Balance Model** represents an account's native token (Ether) balance. The **Native Token Balance Model** follows the following structure:

| Name            | Description                         | Type      |
| --------------- | ----------------------------------- | --------- |
| account_address | The account address.                | `string`  |
| balance         | The account's native token balance. | `integer` |



# Endpoint Specifications

## Collection Endpoints

### Get Tokens by Date Created

This endpoint returns all Ethereum tokens that were created within a given date range (supports pagination).

#### Usage

```
Token.tokens_by_date_created(created_after, created_before, standard, order, limit)
```

#### Query Parameters

| Parameter      | Required | Description                                                                                         | Type        |
| -------------- | -------- | --------------------------------------------------------------------------------------------------- | ----------- |
| created_after  | no       | The earlier contract creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| created_before | no       | The later contract creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| standard       | no       | The token standard (one of `ERC-721` or `ERC-777`)                                                  | `string`    |
| order          | no       | The order in which to retrieve the results (either asc or desc).                                    | `order`     |
| limit          | no       | The maximum number of results to retrieve (max 500).                                                | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                              |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Error-Model) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Error-Model) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Error-Model) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Error-Model) |
