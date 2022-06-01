![Token API Banner](https://files.readme.io/a8b9223-TRSP_DocBanner_Token_1.png)

# Welcome to the Token API

The **Token API** provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens).

## Endpoint Overview

The **Token API** supports the following groups of endpoints:
1. [Token Info Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Token-Info-Endpoints): Retrieve any token ever created using flexible queries, along with token metadata and symbols.
2. [Owner Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Owner-Endpoints): Retrieve all owners and owner balances for a token (ordered by balance).
3. [Operator Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Operator-Endpoints): Retrieve all operators and operator allowances for a token or owner.
4. [Transfer Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Transfer-Endpoints): Retrieve all transfers, including mints, sends, and burns, for any token or individual account.
5. [Approval Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Approval-Endpoints): Retrieve all token approvals by token and account (supports both ERC-20 allowances and ERC-777 operators).
6. [Native Token Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md#Native-Token-Endpoints): Retrieve all native token transfers and balances for any account.


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

## Token Info Endpoints

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
| standard       | no       | The token standard (one of `ERC-721` or `ERC-20`)                                                   | `string`    |
| order          | no       | The order in which to retrieve the results (either asc or desc).                                    | `order`     |
| limit          | no       | The maximum number of results to retrieve (max 500).                                                | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                              |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get Tokens by Contract Address

This endpoint returns all Ethereum tokens that were created within a given date range (supports pagination).

#### Usage

```
Token.tokens_by_contract_address(contract_address, created_after, created_before, standard, order, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                                          | Type     |
| ---------------- | -------- | -------------------------------------------------------------------------------------------------------------------- | -------- |
| contract_address | yes      | The list of contract addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names). | `string` |

#### Responses

| Code | Title                 | Model                                                                                              |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get Tokens by Name

This endpoint returns all Ethereum tokens that match a given name substring (supports pagination up to 1000 results).

#### Usage

```
Token.tokens_by_name(name, limit)
```

#### Query Parameters

| Parameter | Required | Description                                                                                  | Type      |
| --------- | -------- | -------------------------------------------------------------------------------------------- | --------- |
| name      | yes      | The substring to use in the token name search (case-insensitive, max length 100 characters). | `string`  |
| limit     | no       | The maximum number of results to retrieve (max 50).                                          | `integer` |

#### Responses

| Code | Title                 | Model                                                                                              |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get Tokens by Symbol

This endpoint returns all Ethereum tokens that match a given symbol substring (supports pagination up to 1000 results).

#### Usage

```
Token.tokens_by_symbol(symbol, limit)
```

#### Query Parameters

| Parameter | Required | Description                                                                                    | Type      |
| --------- | -------- | ---------------------------------------------------------------------------------------------- | --------- |
| symbol    | yes      | The substring to use in the token symbol search (case-insensitive, max length 100 characters). | `string`  |
| limit     | no       | The maximum number of results to retrieve (max 50).                                            | `integer` |

#### Responses

| Code | Title                 | Model                                                                                              |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get Tokens by Owner

This endpoint returns all Ethereum tokens that are owned by a given account address, with the included owner balances (supports pagination).

#### Usage

```
Token.tokens_by_owner(owner_address, contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                  | Type      |
| ---------------- | -------- | ---------------------------------------------------------------------------- | --------- |
| owner_address    | yes      | The address of the owner to retrieve tokens for (supports ENS names).        | `string`  |
| contract_address | no       | The contract address of the token to filter results by (supports ENS names). | `string`  |
| limit            | no       | The maximum number of results to retrieve (max 500).                         | `integer` |

#### Responses

| Code | Title                 | Model                                                                                              |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |

## Owner Endpoints

### Get Owners by Contract Address

This endpoint returns all ordered Ethereum accounts that own a given token, identified by contract address and ordered by descending balance (supports pagination).

#### Usage

```
Token.owners_by_contract_address(contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                    | Type      |
| ---------------- | -------- | ------------------------------------------------------------------------------ | --------- |
| contract_address | no       | The contract address of the token to retrieve owners for (supports ENS names). | `string`  |
| limit            | no       | The maximum number of results to retrieve (max 500).                           | `integer` |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token Owner](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Owner-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)             |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)             |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)             |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)             |

## Operator Endpoints

### Get Operators by Contract Address

This endpoint returns all Ethereum accounts that are approved operators within a given token, identified by contract address (supports pagination).

#### Usage

```
Token.operators_by_contract_address(contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                | Type      |
| ---------------- | -------- | ------------------------------------------------------------------------------------------ | --------- |
| contract_address | no       | The contract address of the token to retrieve approved operators for (supports ENS names). | `string`  |
| limit            | no       | The maximum number of results to retrieve (max 500).                                       | `integer` |

#### Responses

| Code | Title                 | Model                                                                                                    |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Operator](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Operator-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |


### Get Operators by Account

This endpoint returns all Ethereum accounts that are approved operators for a given owner account (supports pagination).

#### Usage

```
Token.operators_by_account(owner_address, contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                | Type      |
| ---------------- | -------- | ------------------------------------------------------------------------------------------ | --------- |
| owner_address    | yes      | The address of the owner to retrieve approved operators for (supports ENS names).          | `string`  |
| contract_address | no       | The contract address of the token to retrieve approved operators for (supports ENS names). | `string`  |
| limit            | no       | The maximum number of results to retrieve (max 500).                                       | `integer` |

#### Responses

| Code | Title                 | Model                                                                                                    |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Operator](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Operator-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |

## Transfer Endpoints

### Get Transfers

This endpoint returns all Ethereum token transfers that occurred within the given date range (supports pagination).

#### Usage

```
Token.transfers(transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter by. (one of `mint`, `send`, `burn`, or `all`)              | `string`    |
| order              | no       | The order to sort transfers by. (one of `asc` or `desc`)                                   | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                                                |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |


### Get Transfers by Contract Address

This endpoint returns all Ethereum token transfers that occurred within the given date range for a given token, identified by contract address (supports pagination).

#### Usage

```
Token.transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address   | yes      | The contract address of the token to retrieve transfers for (supports ENS names).          | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter by. (one of `mint`, `send`, `burn`, or `all`)              | `string`    |
| order              | no       | The order to sort transfers by. (one of `asc` or `desc`)                                   | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                                                |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |


### Get Transfers by Account

This endpoint returns all Ethereum token transfers that occurred within the given date range for a given token, identified by contract address (supports pagination).

#### Usage

```
Token.transfers_by_account(account_address, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| account_address    | yes      | The account address to retrieve transfers for (supports ENS names).                        | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter by. (one of `mint`, `send`, `burn`, or `all`)              | `string`    |
| order              | no       | The order to sort transfers by. (one of `asc` or `desc`)                                   | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                                                |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Token Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Token-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                   |

## Approval Endpoints

### Get Operator Approvals

This endpoint returns all Ethereum token operator approvals that occurred within the given date range (supports pagination).

#### Usage
```
Token.operator_approvals(approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter       | Required | Description                                                                                | Type        |
| --------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| approved_after  | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order           | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit           | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                                      |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Operator Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Operator-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |


### Get Operator Approvals by Contract Address

This endpoint returns all Ethereum token operator approvals that occurred within the given date range for a given token, identified by contract address (supports pagination).

#### Usage
```
Token.operator_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                | Type        |
| ---------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address | yes      | The contract address to retrieve operator approvals for (supports ENS names).              | `string`    |
| approved_after   | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before  | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order            | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit            | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                                      |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Operator Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Operator-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |


### Get Operator Approvals by Account Address

This endpoint returns all Ethereum token operator approvals that occurred within the given date range and involved a given account (supports pagination).

#### Usage
```
Token.operator_approvals_by_account_address(account_address, approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter       | Required | Description                                                                                | Type        |
| --------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| account_address | yes      | The account address to retrieve operator approvals for (supports ENS names).               | `string`    |
| approved_after  | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order           | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit           | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                                      |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Operator Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Operator-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |

## Native Token Endpoints

### Get Native Token Transfers

This endpoint returns all Ethereum native token (ETH) transfers that occurred within the given date range (supports pagination).

#### Usage

```
Token.native_token_transfers(transferred_after, transferred_before, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order              | no       | The order to sort transfers by. (one of `asc` or `desc`)                                   | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                                                              |
| ---- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Native Token Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Native-Token-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |


### Get Native Token Transfers by Account

This endpoint returns all Ethereum native token (ETH) transfers that occurred within the given date range (supports pagination).

#### Usage
```
Token.native_token_transfers_by_account(account_address, transferred_after, transferred_before, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| account_address    | yes      | The account address to retrieve native token transfers for (supports ENS names).           | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order              | no       | The order to sort transfers by. (one of `asc` or `desc`)                                   | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                                                              |
| ---- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Native Token Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Native-Token-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                                 |


### Get Native Token Balances by Account

This endpoint returns all Ethereum native token (ETH) balances for a given list of accounts (supports pagination).

#### Usage
```
Token.native_token_balances_by_account(account_addresses)
```

#### Query Parameters

| Parameter         | Required | Description                                                                       | Type     |
| ----------------- | -------- | --------------------------------------------------------------------------------- | -------- |
| account_addresses | yes      | The account addresses to retrieve native token balances for (supports ENS names). | `string` |

#### Responses

| Code | Title                 | Model                                                                                                                            |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Native Token Balance](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/token.md#Native-Token-Balance-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                               |

