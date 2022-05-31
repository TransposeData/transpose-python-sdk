![Block API Banner](https://files.readme.io/73ffe8f-TRSP_DocBanner_NFT.png)
# Welcome to the NFT API

The **NFT API** provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).

## Endpoint Overview
The **NFT API** supports the following groups of endpoints:
 
1. *Collection Info Endpoints*: Retrieve any NFT collection using flexible queries, along with collection metadata and images.
2. *NFT Info Endpoints*: Retrieve any NFT in existence and rich NFT metadata and media, by date minted, collection, owner, and more.
3. *Owner Endpoints*: Retrieve all owners for a particular collection or NFT (supports fungible balances for ERC-1155s).
4. *Operator Endpoints*: Retrieve all operators for a specific collection or NFT owner.
5. *Transfer Activity Endpoints*: Retrieve all transfers, including mints, sends, and burns, for any collection, NFT, or individual account.
6. *Approval Activity Endpoints*: Retrieve all approvals (both NFT and operator approvals), by collection, NFT, account, and more.


## Data Models

### Error Model
The **Error Model** contains the full set of information for errors on the Transpose API suite.
| Name    | Description                     | Type     |
| ------- | ------------------------------- | -------- |
| status  | The status of the request.      | `string` |
| message | A message describing the error. | `string` |


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
| opensea_slug      | The colelction's OpenSea slug.                                                                          | `string`    |
| opensea_url       | The collection's OpenSea URL.                                                                           | `string`    |
| last_refreshed    | The timestamp at which the collection was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |

### NFT Model
The** NFT Model** represents a single NFT with included ownership data (i.e. the owner account and owner's balance). The **NFT Model** follows the following structure:

| Name             | Description                                                      | Type        |
| ---------------- | ---------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the collection.                              | `string`    |
| token_id         | The token ID of the NFT.                                         | `integer`   |
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
The** NFT Model** represents a single NFT with included ownership data (i.e. the owner account and owner's balance). The **NFT Model** follows the following structure:

| Name             | Description                                                      | Type        |
| ---------------- | ---------------------------------------------------------------- | ----------- |
| contract_address | Contract address of the collection.                              | `string`    |
| token_id         | The token ID of the NFT.                                         | `integer`   |
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
| balance          | The owner's balance for the NFT.                                 | `integer`   |

### NFT Owner Model
The **NFT Owner Model** represents a single NFT owner. The **NFT Owner Model** follows the following structure:

| Name             | Description                               | Type      |
| ---------------- | ----------------------------------------- | --------- |
| contract_address | Contract address of the NFT's collection. | `string`  |
| token_id         | The token ID of the NFT.                  | `integer` |
| owner            | The address of the owner.                 | `string`  |
| balance          | The owner's balance for the NFT.          | `integer` |

### NFT Transfer Model
The **NFT Transfer Model** represents a single transfer of an NFT. **The NFT Transfer Model** follows the following structure:

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
Block.accounts_by_address(account_addresses)
```

#### Query Parameters
| Parameter         | Required | Description                                                                                                         | Type       |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------- | ---------- |
| account_addresses | yes      | The list of account addresses to retrieve, separated by commas (max 100 addresses per request, supports ENS names). | `string[]` |

#### Responses
| Code | Title                 | Model                                                                                                  |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [Account](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/block.md#Account-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/block.md#Error-Model)     |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/block.md#Error-Model)     |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/block.md#Error-Model)     |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/block.md#Error-Model)     |