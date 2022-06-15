![NFT API Banner](https://files.readme.io/73ffe8f-TRSP_DocBanner_NFT.png)

# Welcome to the NFT API

The **NFT API** provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).

## Endpoint Overview

The **NFT API** supports the following groups of endpoints:

1. [Collection Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Collection-Endpoints): Retrieve any NFT collection using flexible queries, along with collection metadata and images.
   1. [Collections by Date Created](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-collections-by-date-created)
   2. [Collections by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-collections-by-contract-address)
   3. [Collections by Name](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-collections-by-name)
   4. [Collections by Symbol](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-collections-by-symbol)
2. [NFT Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#NFT-Endpoints): Retrieve any NFT in existence and rich NFT metadata and media, by date minted, collection, owner, and more.
   1. [NFTs by Date Minted](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-collections-by-symbol)
   2. [NFTs by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nfts-by-contract-address)
   3. [NFTs by Token ID](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nfts-by-token-id)
   4. [NFTs by Name](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nfts-by-name)
   5. [NFTs by Owner](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nfts-by-owner)
   6. [NFTs by Approved Account](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nfts-by-approved-account)
3. [Owner Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Owner-Endpoints): Retrieve all owners for a particular collection or NFT (supports fungible balances for ERC-1155s).
   1. [Owners by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-owners-by-contract-address)
   2. [Owners by Token ID](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-owners-by-token-id)
4. [Operator Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Operator-Endpoints): Retrieve all operators for a specific collection or NFT owner.
   1. [Operators by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-operators-by-contract-address)
   2. [Operators by Account](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-operators-by-account)
5. [Transfer Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Transfer-Endpoints): Retrieve all transfers, including mints, sends, and burns, for any collection, NFT, or individual account.
   1. [Transfers](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-transfers)
   2. [Transfers by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-transfers-by-contract-address)
   3. [Transfers by Token ID](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-transfers-by-token-id)
   4. [Transfers by Account](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-transfers-by-account)
6. [Approval Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Approval-Endpoints): Retrieve all approvals (both NFT and operator approvals), by collection, NFT, account, and more.
   1. [NFT Approvals](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nft-approvals)
   2. [NFT Approvals by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nft-approvals-by-contract-address)
   3. [NFT Approvals by Token ID](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nft-approvals-by-token-id)
   4. [NFT Approvals by Account](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-nft-approvals-by-account)
   5. [Operator Approvals](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-operator-approvals)
   6. [Operator Approvals by Contract Address](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-operator-approvals-by-contract-address)
   7. [Operator Approvals by Account](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#get-operator-approvals-by-account)


## Data Models

### Collection Model

The **Collection Model** represents a single NFT collection. The **Collection Model** follows the following structure:

| Name              | Description                                                                                             | Type        |
| ----------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| contract_address  | Contract address of the collection.                                                                     | `string`    |
| name              | The collection's name.                                                                                  | `string`    |
| symbol            | The collection's symbol                                                                                 | `string`    |
| description       | The collection's description                                                                            | `string`    |
| created_timestamp | The collection's timestamp of creation (in ISO-8601 format).                                            | `date-time` |
| standard          | The collection's NFT standard (ERC-721 or ERC-1155)                                                     | `string`    |
| count             | The number of NFTs in the collection (NFTs minted minus NFTs burned).                                   | `integer`   |
| external_url      | The collection's website URL.                                                                           | `string`    |
| image_url         | The collection's image URL in the Transpose CDN.                                                        | `string`    |
| twitter_username  | The collection's Twitter username.                                                                      | `string`    |
| telegram_url      | The collection's Telegram URL.                                                                          | `string`    |
| discord_url       | The collection's Discord URL.                                                                           | `string`    |
| is_nsfw           | The collection's NSFW status.                                                                           | `boolean`   |
| opensea_slug      | The collection's OpenSea slug.                                                                          | `string`    |
| opensea_url       | The collection's OpenSea URL.                                                                           | `string`    |
| last_refreshed    | The timestamp at which the collection was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |

### NFT Model

The **NFT Model** represents a single NFT with included ownership data (i.e. the owner account and owner's balance). The **NFT Model** follows the following structure:

| Name             | Description                                                      | Type        |
| ---------------- | ---------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the collection.                              | `string`    |
| token_id         | The token ID of the nft.                                         | `integer`   |
| name             | The collection's name.                                           | `string`    |
| description      | The collection's description                                     | `string`    |
| minted_timestamp | The NFT's mint timestamp (in ISO-8601 format).                   | `date-time` |
| supply           | The NFT's supply (zero if NFT has been burned).                  | `integer`   |
| approved_address | The address of the approved account.                             | `string`    |
| image_url        | The NFT's image URL in the Transpose CDN.                        | `string`    |
| media_url        | The NFT's additional media URL in the Transpose CDN.             | `string`    |
| external_url     | The NFT's website URL.                                           | `string`    |
| properties       | The NFT's properties (also referred to as attributes or traits). | `object`    |
| metadata_url     | The NFT's metadata URL in the Transpose CDN.                     | `string`    |

### NFT With Owner Model

The **NFT Model** represents a single NFT with included ownership data (i.e. the owner account and owner's balance). The **NFT Model** follows the following structure:

| Name             | Description                                                      | Type        |
| ---------------- | ---------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the collection.                              | `string`    |
| token_id         | The token ID of the nft.                                         | `integer`   |
| name             | The collection's name.                                           | `string`    |
| description      | The collection's description.                                    | `string`    |
| minted_timestamp | The NFT's mint timestamp (in ISO-8601 format).                   | `date-time` |
| supply           | The NFT's supply (zero if NFT has been burned).                  | `integer`   |
| approved_address | The address of the approved account.                             | `string`    |
| image_url        | The NFT's image URL in the Transpose CDN.                        | `string`    |
| media_url        | The NFT's additional media URL in the Transpose CDN.             | `string`    |
| external_url     | The NFT's website URL.                                           | `string`    |
| properties       | The NFT's properties (also referred to as attributes or traits). | `object`    |
| metadata_url     | The NFT's metadata URL in the Transpose CDN.                     | `string`    |
| owner            | The address of the owner.                                        | `string`    |
| balance          | The owner's balance for the nft.                                 | `integer`   |

### NFT Owner Model

The **NFT Owner Model** represents a single NFT owner. The **NFT Owner Model** follows the following structure:

| Name             | Description                               | Type      |
| ---------------- | ----------------------------------------- | --------- |
| contract_address | Contract address of the NFT's collection. | `string`  |
| token_id         | The token ID of the nft.                  | `integer` |
| owner            | The address of the owner.                 | `string`  |
| balance          | The owner's balance for the nft.          | `integer` |

### NFT Transfer Model

The **NFT Transfer Model** represents a single transfer of an nft. **The NFT Transfer Model** follows the following structure:

| Name             | Description                                                                       | Type        |
| ---------------- | --------------------------------------------------------------------------------- | ----------- |
| contract_address | The contract address of the ENS collection.                                       | `string`    |
| token_id         | The token ID of the ENS name.                                                     | `integer`   |
| block_number     | The block number at which the transfer occurred.                                  | `integer`   |
| log_index        | The log index at which the transfer occurred.                                     | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                              | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                               | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`).            | `string`    |
| operator         | The address of the operator that performed the transfer (only for ERC-1155 NFTs). | `string`    |
| from             | The address of the sender.                                                        | `string`    |
| to               | The address of the receiver.                                                      | `string`    |
| quantity         | The quantity of NFTs transferred.                                                 | `integer`   |

### NFT Approval Model

The **NFT Approval Model** represents a single NFT approval (not to be confused with an operator approval). The **NFT Approval Model** follows the following structure:

| Name             | Description                                                                    | Type        |
| ---------------- | ------------------------------------------------------------------------------ | ----------- |
| contract_address | The contract address of the ENS collection.                                    | `string`    |
| token_id         | The token ID of the ENS name.                                                  | `integer`   |
| block_number     | The block number at which the transfer occurred.                               | `integer`   |
| log_index        | The log index at which the transfer occurred.                                  | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                           | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                            | `date-time` |
| owner            | The address of the NFT owner that approved the account.                        | `string`    |
| approved_account | The address of the account that was approved (only supported by ERC-721 NFTs). | `string`    |

### Operator Model

The **Operator Model** represents a single authorized operator for an owner's NFTs. The **Operator Model** follows the following structure:

| Name             | Description                                                                | Type     |
| ---------------- | -------------------------------------------------------------------------- | -------- |
| contract_address | Contract address of the NFT's collection.                                  | `string` |
| owner            | The address of the owner.                                                  | `string` |
| operator         | The address of the operator (supported by both ERC-721 and ERC-1155 NFTs). | `string` |

### Operator Approval Model

The **Operator Approval Model** represents a single operator approval (not to be confused with an nft approval). The **Operator Approval Model** follows the following structure:

| Name             | Description                                                                            | Type        |
| ---------------- | -------------------------------------------------------------------------------------- | ----------- |
| contract_address | The contract address of the ENS collection.                                            | `string`    |
| token_id         | The token ID of the ENS name.                                                          | `integer`   |
| block_number     | The block number at which the transfer occurred.                                       | `integer`   |
| log_index        | The log index at which the transfer occurred.                                          | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                                   | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                                    | `date-time` |
| owner            | The address of the owner.                                                              | `string`    |
| operator         | The address of the operator (supported by both ERC-721 and ERC-1155 NFTs).             | `string`    |
| authorized       | Whether approval was granted or revoked (supported by both ERC-721 and ERC-1155 NFTs). | `boolean`   |

# Endpoint Specifications

## Collection Endpoints

### Get Collections by Date Created

This endpoint returns all Ethereum NFT collections that were created within a given date range (supports pagination).

#### Usage

```
nft.collections_by_date_created(created_after, created_before, standard, order, limit)
```

#### Query Parameters

| Parameter      | Required | Description                                                                                         | Type        |
| -------------- | -------- | --------------------------------------------------------------------------------------------------- | ----------- |
| created_after  | no       | The earlier contract creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| created_before | no       | The later contract creation date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| standard       | no       | The NFT standard to filter results by (`ERC-721` or `ERC-1155`).                                    | `string`    |
| order          | no       | The order in which to retrieve the results (either asc or desc).                                    | `order`     |
| limit          | no       | The maximum number of results to retrieve (max 500).                                                | `integer`   |

#### Responses

| Code | Title                 | Model                                                                                                      |
| ---- | --------------------- | ---------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Collection](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Collection-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |

### Get Collections by Contract Address

This endpoint returns all Ethereum NFT collections for a given list of contract addresses.

#### Usage

```
nft.collections_by_contract_address(contract_addresses)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                                          | Type     |
| ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------- | -------- |
| contract_addresses | yes      | The list of contract addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names). | `string` |

#### Responses

| Code | Title                 | Model                                                                                                      |
| ---- | --------------------- | ---------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Collection](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Collection-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |

### Get Collections by Name

This endpoint returns all Ethereum NFT collections that match a given name substring (supports pagination up to 1000 results).

#### Usage

```
nft.collections_by_name(name, limit)
```

#### Query Parameters

| Parameter | Required | Description                                                                                       | Type     |
| --------- | -------- | ------------------------------------------------------------------------------------------------- | -------- |
| name      | yes      | The substring to use in the collection name search (case-insensitive, max length 100 characters). | `string` |
| limit     | no       | The maximum number of results to retrieve (max 50).                                               | `string` |

#### Responses

| Code | Title                 | Model                                                                                                      |
| ---- | --------------------- | ---------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Collection](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Collection-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |

### Get Collections by Symbol

This endpoint returns all Ethereum NFT collections that match a given symbol substring (supports pagination up to 1000 results).

#### Usage

```
nft.collections_by_symbol(symbol, limit)
```

#### Query Parameters

| Parameter | Required | Description                                                                                       | Type     |
| --------- | -------- | ------------------------------------------------------------------------------------------------- | -------- |
| symbol    | yes      | The substring to use in the collection name search (case-insensitive, max length 100 characters). | `string` |
| limit     | no       | The maximum number of results to retrieve (max 50).                                               | `string` |

#### Responses

| Code | Title                 | Model                                                                                                      |
| ---- | --------------------- | ---------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [Collection](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Collection-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)           |

## NFT Endpoints

### Get NFTs by Date Minted

This endpoint returns all Ethereum NFTs that were minted within a given date range (supports pagination).

#### Usage

```
nft.nfts_by_date_minted(minted_after, minted_before, contract_address, include_burned_nfts, order, limit)
```

#### Query Parameters

| Parameter           | Required | Description                                                                            | Type        |
| ------------------- | -------- | -------------------------------------------------------------------------------------- | ----------- |
| minted_after        | no       | The earlier mint date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| minted_before       | no       | The later mint date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| contract_address    | no       | The contract address of the collection to filter results by (supports ENS names).      | `string`    |
| include_burned_nfts | no       | Whether or not to include burned NFTs in the results.                                  | `boolean`   |
| order               | no       | The order in which to retrieve the results (either `asc` or `desc`).                   | `string`    |
| limit               | no       | The maximum number of results to retrieve (max 500).                                   | `int`       |

#### Responses

| Code | Title                 | Model                                                                                            |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 200  | Success               | [NFT](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Model)     |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get NFTs by Contract Address

This endpoint returns all Ethereum NFTs within a given collection, identified by contract address (supports pagination).

#### Usage

```
nft.nfts_by_contract_address(contract_addresses, include_burned_nfts, limit)
```

#### Query Parameters

| Parameter           | Required | Description                                                                         | Type       |
| ------------------- | -------- | ----------------------------------------------------------------------------------- | ---------- |
| contract_addresses  | yes      | The contract addresses of the collection to filter results by (supports ENS names). | `string[]` |
| include_burned_nfts | no       | Whether or not to include burned NFTs in the results.                               | `boolean`  |
| limit               | no       | The maximum number of results to retrieve (max 500).                                | `int`      |

#### Responses

| Code | Title                 | Model                                                                                            |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 200  | Success               | [NFT](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Model)     |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get NFTs by Token ID

This endpoint returns all Ethereum NFTs for a given list of collection contract address and token ID pairs, inputted as two arrays of matching length.
#### Usage

```
nft.nfts_by_token_id(contract_addresses, token_ids, include_burned_nfts, limit)
```

#### Query Parameters

| Parameter           | Required | Description                                                                                                                                                 | Type       |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| contract_addresses  | yes      | The contract addresses of the collection to filter results by (supports ENS names).                                                                         | `string[]` |
| token_ids           | yes      | The list of token IDs to retrieve NFTs for, separated by commas (max 100 token IDs per request). Must match the length of the contract_addresses parameter. | `int[]`    |
| include_burned_nfts | no       | Whether or not to include burned NFTs in the results.                                                                                                       | `boolean`  |

#### Responses

| Code | Title                 | Model                                                                                            |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 200  | Success               | [NFT](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Model)     |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |

### Get NFTs by Name

This endpoint returns all Ethereum NFTs that match a given name substring (supports pagination up to 1000 results).#### Usage

```
nft.nfts_by_name(name, include_burned_nfts, limit)
```

#### Query Parameters

| Parameter           | Required | Description                                                                                | Type      |
| ------------------- | -------- | ------------------------------------------------------------------------------------------ | --------- |
| name                | yes      | The substring to use in the NFT name search (case-insensitive, max length 100 characters). | `string`  |
| include_burned_nfts | no       | Whether or not to include burned NFTs in the results.                                      | `boolean` |
| limit               | no       | The maximum number of results to retrieve (max 500).                                       | `int`     |

#### Responses

| Code | Title                 | Model                                                                                            |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 200  | Success               | [NFT](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Model)     |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get NFTs by Owner

This endpoint returns all Ethereum NFTs that are owned by a given account address, with the included owner balances (supports pagination).

```
nft.nfts_by_owner(owner_address, contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                       | Type     |
| ---------------- | -------- | --------------------------------------------------------------------------------- | -------- |
| owner_address    | yes      | The address of the owner to retrieve NFTs for (supports ENS names).               | `string` |
| contract_address | no       | The contract address of the collection to filter results by (supports ENS names). | `string` |
| limit            | no       | The maximum number of results to retrieve (max 500).                              | `int`    |

#### Responses

| Code | Title                 | Model                                                                                            |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 200  | Success               | [NFT](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Model)     |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get NFTs by Approved Account

This endpoint returns all Ethereum NFTs that are approved to be operated a given address (supports pagination).

```
nft.nfts_by_approved_account(approved_address, contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                       | Type     |
| ---------------- | -------- | --------------------------------------------------------------------------------- | -------- |
| approved_address | yes      | The address of the approved account to retrieve NFTs for (supports ENS names).    | `string` |
| contract_address | no       | The contract address of the collection to filter results by (supports ENS names). | `string` |
| limit            | no       | The maximum number of results to retrieve (max 500).                              | `int`    |

#### Responses

| Code | Title                 | Model                                                                                            |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------ |
| 200  | Success               | [NFT](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Model)     |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


## Owner Endpoints

### Get Owners by Contract Address

This endpoint returns all Ethereum accounts that own a given collection, identified by contract address and ordered by descending balance (supports pagination).

```
nft.owners_by_contract_address(contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                         | Type     |
| ---------------- | -------- | ----------------------------------------------------------------------------------- | -------- |
| contract_address | yes      | The contract address of the collection to retrieve owners for (supports ENS names). | `string` |
| limit            | no       | The maximum number of results to retrieve (max 500).                                | `int`    |

#### Responses

| Code | Title                 | Model                                                                                                    |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Owner](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Owner-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |


### Get Owners by Token ID

This endpoint returns all Ethereum accounts that own a given NFT, identified by a collection contract address and token ID pair and ordered by descending balance (supports pagination).

```
nft.owners_by_token_id(contract_address, token_id, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                         | Type     |
| ---------------- | -------- | ----------------------------------------------------------------------------------- | -------- |
| contract_address | yes      | The contract address of the collection to retrieve owners for (supports ENS names). | `string` |
| token_id         | yes      | The token ID of the NFT to retrieve owners for.                                     | `int`    |
| limit            | no       | The maximum number of results to retrieve (max 500).                                | `int`    |

#### Responses

| Code | Title                 | Model                                                                                                    |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Owner](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Owner-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)         |


## Operator Endpoints


### Get Operators by Contract Address

This endpoint returns all Ethereum accounts that are approved operators within a given collection, identified by contract address (supports pagination).

```
nft.operators_by_contract_address(contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                     | Type     |
| ---------------- | -------- | ----------------------------------------------------------------------------------------------- | -------- |
| contract_address | yes      | The contract address of the collection to retrieve approved operators for (supports ENS names). | `string` |
| limit            | no       | The maximum number of results to retrieve (max 500).                                            | `int`    |

#### Responses

| Code | Title                 | Model                                                                                                  |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [Operator](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Operator-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |


### Get Operators by Account

This endpoint returns all Ethereum accounts that are approved operators within a given collection, identified by contract address (supports pagination).

```
nft.operators_by_account(owner_address, contract_address, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                     | Type     |
| ---------------- | -------- | ----------------------------------------------------------------------------------------------- | -------- |
| owner_address    | yes      | The account address of the owner to retrieve approved operators for (supports ENS names).       | `string` |
| contract_address | no       | The contract address of the collection to retrieve approved operators for (supports ENS names). | `string` |
| limit            | no       | The maximum number of results to retrieve (max 500).                                            | `int`    |

#### Responses

| Code | Title                 | Model                                                                                                  |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [Operator](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Operator-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)       |

## Transfer Endpoints

### Get Transfers

This endpoint returns all Ethereum NFT transfers that occurred within the given date range (supports pagination).

```
nft.transfers(transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).      | `string`    |
| order              | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


### Get Transfers by Contract Address

This endpoint returns all Ethereum NFT transfers that occurred within the given date range for a given collection, identified by contract address (supports pagination).

```
nft.transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address   | yes      | The contract address of the collection to retrieve transfers for (supports ENS names).     | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).      | `string`    |
| order              | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


### Get Transfers by Token ID

This endpoint returns all Ethereum NFT transfers that occurred within the given date range for a given collection contract address and token ID pair (supports pagination).

```
nft.transfers_by_token_id(contract_address, token_id, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address   | yes      | The contract address of the collection to retrieve transfers for (supports ENS names).     | `string`    |
| token_id           | yes      | The token ID of the NFT to retrieve transfers for.                                         | `int`       |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).      | `string`    |
| order              | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


### Get Transfers by Account

This endpoint returns all Ethereum NFT transfers that occurred within the given date range and involved a given account (supports pagination).

```
nft.transfers_by_account(account_address, transferred_after, transferred_before, transfer_direction, transfer_category, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                                              | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| account_address    | yes      | The account address of the account to retrieve transfers for.                                                            | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).                               | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).                                 | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).                                    | `string`    |
| transfer_direction | no       | Whether to match transfers that were sent by the account (`sent`), received by the account (`received`), or all (`all`). | `string`    |
| order              | no       | The order in which to return results (one of `asc` or `desc`).                                                           | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                                                     | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


## Approval Endpoints

### Get NFT Approvals

This endpoint returns all Ethereum NFT transfers that occurred within the given date range and involved a given account (supports pagination).

```
nft.nft_approvals(approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter       | Required | Description                                                                                | Type        |
| --------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| approved_after  | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order           | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit           | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


### Get NFT Approvals by Contract Address

This endpoint returns all Ethereum NFT approvals that occurred within the given date range for a given collection, identified by contract address (supports pagination).

```
nft.nft_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                | Type        |
| ---------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address | yes      | The contract address of the collection to retrieve approvals for.                          | `string`    |
| approved_after   | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before  | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order            | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit            | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


### Get NFT Approvals by Token ID

This endpoint returns all Ethereum NFT approvals that occurred within the given date range for a given collection contract address and token ID pair (supports pagination).

```
nft.nft_approvals_by_token_id(contract_address, token_id, approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                | Type        |
| ---------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address | yes      | The contract address of the collection to retrieve approvals for.                          | `string`    |
| token_id         | yes      | The token ID of the NFT to retrieve approvals for.                                         | `int`       |
| approved_after   | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before  | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order            | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit            | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |


### Get NFT Approvals by Account

This endpoint returns all Ethereum NFT approvals that occurred within the given date range and involved a given account (supports pagination).

```
nft.nft_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                                                        | Type        |
| ------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| account_address    | yes      | The account address of the account to retrieve approvals for.                                                                      | `string`    |
| approved_after     | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).                                         | `date-time` |
| approved_before    | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).                                           | `date-time` |
| approval_direction | no       | Whether to match NFT approvals in which the account granted approval (`granted`), received approval (`received`), or both (`all`). | `string`    |
| order              | no       | The order in which to return results (one of `asc` or `desc`).                                                                     | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                                                               | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [NFT Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#NFT-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)               |



### Get Operator Approvals

This endpoint returns all Ethereum NFT operator approvals that occurred within the given date range (supports pagination).

```
nft.operator_approvals(approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter       | Required | Description                                                                                | Type        |
| --------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| approved_after  | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order           | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit           | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                                    |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [Operator Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Operator-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |


### Get Operator Approvals by Contract Address

This endpoint returns all Ethereum NFT operator approvals that occurred within the given date range for a given collection, identified by contract address (supports pagination).

```
nft.operator_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit)
```

#### Query Parameters

| Parameter        | Required | Description                                                                                | Type        |
| ---------------- | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| contract_address | yes      | The contract address of the collection to retrieve approvals for.                          | `string`    |
| approved_after   | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| approved_before  | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| order            | no       | The order in which to return results (one of `asc` or `desc`).                             | `string`    |
| limit            | no       | The maximum number of results to retrieve (max 500).                                       | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                                    |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [Operator Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Operator-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |


### Get Operator Approvals by Account

This endpoint returns all Ethereum NFT operator approvals that occurred within the given date range and involved a given account (supports pagination).

```
nft.operator_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit)
```

#### Query Parameters

| Parameter          | Required | Description                                                                                                                             | Type        |
| ------------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| account_address    | yes      | The account address of the account to retrieve approvals for.                                                                           | `string`    |
| approved_after     | no       | The earlier approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).                                              | `date-time` |
| approved_before    | no       | The later approval date, inclusive (in seconds since the Unix epoch or ISO-8601 format).                                                | `date-time` |
| approval_direction | no       | Whether to match operator approvals in which the account granted approval (`granted`), received approval (`received`), or both (`all`). | `string`    |
| order              | no       | The order in which to return results (one of `asc` or `desc`).                                                                          | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                                                                    | `int`       |

#### Responses

| Code | Title                 | Model                                                                                                                    |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [Operator Approval](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/nft.md#Operator-Approval-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)                         |
