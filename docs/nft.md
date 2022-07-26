![NFT API Banner](https://files.readme.io/dc52b4f-TRSP_Docs_Banners.png)

# Welcome to the NFT API

The **NFT API** provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).

## Endpoint Overview

The **NFT API** supports the following groups of endpoints:

1. [Collection Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Collection-Endpoints): Retrieve any NFT collection using flexible queries, along with collection metadata and images.
2. [NFT Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#NFT-Endpoints): Retrieve any NFT in existence and rich NFT metadata and media, by date minted, collection, owner, and more.
3. [Sale Activity Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Sale-Endpoints): Retrieve any NFT sale given an account, collection, or date range across many decentralized exchanges.
4. [Owner Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Owner-Endpoints): Retrieve all owners for a particular collection or NFT (supports fungible balances for ERC-1155s).
5. [Operator Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Operator-Endpoints): Retrieve all operators for a specific collection or NFT owner.
6. [Transfer Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Transfer-Endpoints): Retrieve all transfers, including mints, sends, and burns, for any collection, NFT, or individual account.
7. [Approval Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md#Approval-Endpoints): Retrieve all approvals (both NFT and operator approvals), by collection, NFT, account, and more.


# Endpoint Specifications

## Collection Endpoints
| SDK Method                                                                               | Endpoint URL                                  | Returns            |
| ---------------------------------------------------------------------------------------- | --------------------------------------------- | ------------------ |
| `nft.collections_by_date_created(created_after, created_before, standard, order, limit)` | `GET /v0/nft/collections-by-date-created`     | `List[Collection]` |
| `nft.collections_by_contract_address(contract_addresses)`                                | `GET /v0/nft/collections-by-contract-address` | `List[Collection]` |
| `nft.collections_by_name(name, limit, fuzzy)`                                                   | `GET /v0/nft/collections-by-name`             | `List[Collection]` |
| `nft.collections_by_symbol(symbol, limit, fuzzy)`                                               | `GET /v0/nft/collections-by-symbol`           | `List[Collection]` |

### Collection Model
<details>
<summary>View Model Specification</summary>

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

</details>


## NFT Endpoints
| SDK Method                                                                                                  | Endpoint URL                           | Returns              |
| ----------------------------------------------------------------------------------------------------------- | -------------------------------------- | -------------------- |
| `nft.nfts_by_date_minted(minted_after, minted_before, contract_address, include_burned_nfts, order, limit)` | `GET /v0/nft/nfts-by-date-minted`      | `List[NFT]`          |
| `nft.nfts_by_contract_address(contract_addresses, include_burned_nfts, limit)`                              | `GET /v0/nft/nfts-by-contract-address` | `List[NFT]`          |
| `nft.nfts_by_token_id(contract_addresses, token_ids, include_burned_nfts, limit)`                           | `GET /v0/nft/nfts-by-token-id`         | `List[NFT]`          |
| `nft.nfts_by_name(name, include_burned_nfts, limit, fuzzy)`                                                        | `GET /v0/nft/nfts-by-name`             | `List[NFT]`          |
| `nft.nfts_by_owner(owner_address, contract_address, limit)`                                                 | `GET /v0/nft/nfts-by-owner`            | `List[NFTWithOwner]` |
| `nft.nfts_by_approved_account(approved_address, contract_address, limit)`                                   | `GET /v0/nft/nfts-by-approved-account` | `List[NFT]`          |


### NFT Model
<details>
<summary>View Model Specification</summary>

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

</details>

### NFT With Owner Model
<details>
<summary>View Model Specification</summary>

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

</details>


## Owner Endpoints
| SDK Method                                                  | Endpoint URL                             | Returns          |
| ----------------------------------------------------------- | ---------------------------------------- | ---------------- |
| `nft.owners_by_contract_address(contract_address, limit)`   | `GET /v0/nft/owners-by-contract-address` | `List[NFTOwner]` |
| `nft.owners_by_token_id(contract_address, token_id, limit)` | `GET /v0/nft/owners-by-token-id`         | `List[NFTOwner]` |

### NFT Owner Model
<details>
<summary>View Model Specification</summary>

The **NFT Owner Model** represents a single NFT owner. The **NFT Owner Model** follows the following structure:

| Name             | Description                               | Type      |
| ---------------- | ----------------------------------------- | --------- |
| contract_address | Contract address of the NFT's collection. | `string`  |
| token_id         | The token ID of the nft.                  | `integer` |
| owner            | The address of the owner.                 | `string`  |
| balance          | The owner's balance for the nft.          | `integer` |

</details>


## Operator Endpoints
| SDK Method                                                         | Endpoint URL                                | Returns          |
| ------------------------------------------------------------------ | ------------------------------------------- | ---------------- |
| `nft.operators_by_contract_address(contract_address, limit)`       | `GET /v0/nft/operators-by-contract-address` | `List[Operator]` |
| `nft.operators_by_account(owner_address, contract_address, limit)` | `GET /v0/nft/operators-by-account`          | `List[Operator]` |

### Operator Model
<details>
<summary>View Model Specification</summary>

The **Operator Model** represents a single authorized operator for an owner's NFTs. The **Operator Model** follows the following structure:

| Name             | Description                                                                | Type     |
| ---------------- | -------------------------------------------------------------------------- | -------- |
| contract_address | Contract address of the NFT's collection.                                  | `string` |
| owner            | The address of the owner.                                                  | `string` |
| operator         | The address of the operator (supported by both ERC-721 and ERC-1155 NFTs). | `string` |

</details>


## Transfer Endpoints
| SDK Method                                                                                                                              | Endpoint URL                                | Returns             |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------- |
| `nft.transfers(transferred_after, transferred_before, transfer_category, order, limit)`                                                 | `GET /v0/nft/transfers`                     | `List[NFTTransfer]` |
| `nft.transfers_by_contract_address(contract_address, transferred_after, transferred_before, transfer_category, order, limit)`           | `GET /v0/nft/transfers-by-contract-address` | `List[NFTTransfer]` |
| `nft.transfers_by_token_id(contract_address, token_id, transferred_after, transferred_before, transfer_category, order, limit)`         | `GET /v0/nft/transfers-by-token-id`         | `List[NFTTransfer]` |
| `nft.transfers_by_account(account_address, transferred_after, transferred_before, transfer_direction, transfer_category, order, limit)` | `GET /v0/nft/transfers-by-account`          | `List[NFTTransfer]` |

### NFT Transfer Model
<details>
<summary>View Model Specification</summary>

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

</details>


## Approval Endpoints
| SDK Method                                                                                                              | Endpoint URL                                         | Returns                  |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------ |
| `nft.nft_approvals(approved_after, approved_before, order, limit)`                                                      | `GET /v0/nft/nft-approvals`                          | `List[NFTApproval]`      |
| `nft.nft_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit)`                | `GET /v0/nft/nft-approvals-by-contract-address`      | `List[NFTApproval]`      |
| `nft.nft_approvals_by_token_id(contract_address, token_id, approved_after, approved_before, order, limit)`              | `GET /v0/nft/nft-approvals-by-token-id`              | `List[NFTApproval]`      |
| `nft.nft_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit)`      | `GET /v0/nft/nft-approvals-by-account`               | `List[NFTApproval]`      |
| `nft.operator_approvals(approved_after, approved_before, order, limit)`                                                 | `GET /v0/nft/operator-approvals`                     | `List[OperatorApproval]` |
| `nft.operator_approvals_by_contract_address(contract_address, approved_after, approved_before, order, limit)`           | `GET /v0/nft/operator-approvals-by-contract-address` | `List[OperatorApproval]` |
| `nft.operator_approvals_by_account(account_address, approved_after, approved_before, approval_direction, order, limit)` | `GET /v0/nft/operator-approvals-by-account`          | `List[OperatorApproval]` |

### Operator Approval Model
<details>
<summary>View Model Specification</summary>

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

</details>

### NFT Approval Model
<details>
<summary>View Model Specification</summary>

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

</details>


## Sale Endpoints
| SDK Method                                                                                            | Endpoint URL                            | Returns         |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------- | --------------- |
| `nft.sales(sold_after, sold_before, confirmed, order, limit)`                                         | `GET /v0/nft/sales`                     | `List[NFTSale]` |
| `nft.sales_by_contract_address(contract_address, sold_after, sold_before, confirmed, order, limit)`   | `GET /v0/nft/sales-by-contract-address` | `List[NFTSale]` |
| `nft.sales_by_token_id(contract_address, token_id, sold_after, sold_before, confirmed, order, limit)` | `GET /v0/nft/sales-by-contract-address` | `List[NFTSale]` |
| `nft.sales_by_account(account_address, sold_after, sold_before, role, confirmed, order, limit)`       | `GET /v0/nft/sales-by-account`          | `List[NFTSale]` |

### NFT Sale Model
<details>
<summary>View Model Specification</summary>

The **NFT Sale Model** represents a single NFT Sale on an exchange. The **NFT Sale Model** follows the following structure:

| Name                   | Description                                                                                   | Type        |
| ---------------------- | --------------------------------------------------------------------------------------------- | ----------- |
| contract_address       | Contract address of the NFT.                                                                  | `string`    |
| token_id               | Token ID of the NFT.                                                                          | `integer`   |
| block_number           | Block number at which the sale occurred.                                                      | `integer`   |
| log_index              | Log index at which the sale occurred.                                                         | `integer`   |
| transaction_hash       | Transaction hash at which the sale occurred.                                                  | `string`    |
| timestamp              | Timestamp of the sale (in ISO-8601 format).                                                   | `date-time` |
| confirmed              | Whether the sale has been confirmed.                                                          | `boolean`   |
| exchange_name          | Name of the exchange where the sale occurred.                                                 | `string`    |
| contract_version       | The version of the exchange contract that hosted the NFT sale.                                | `string`    |
| is_multi_token_sale    | Whether the sale is a multi-token sale.                                                       | `boolean`   |
| multi_token_sale_index | Whether the sale is a multi-token sale, including more than one unique NFT.                   | `integer`   |
| quantity               | The quantity of the NFT sold.                                                                 | `integer`   |
| payment_token          | The payment token used for the sale.                                                          | `string`    |
| price                  | The total value of this sale in the payment token (formatted with the smallest denomination). | `integer`   |
| eth_price              | The total value of this sale in ETH.                                                          | `integer`   |
| usd_price              | The total value of this sale in USD.                                                          | `integer`   |
| buyer                  | The address of the buyer.                                                                     | `string`    |
| seller                 | The address of the seller.                                                                    | `string`    |


</details>
