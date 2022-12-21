![ENS API Banner](https://files.readme.io/5fcfe11-ENS_Docs_Banners.png)
# Welcome to the ENS API

The **ENS API** provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.

## Endpoint Overview
The **ENS API** supports the following groups of endpoints:
 
1. [Record Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md#Record-Endpoints): Retrieve any ENS record ever created by account, owner, name, node, registration date, expiration date and more.
2. [Transfer Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md#Transfer-Endpoints): Retrieve all historical and live ENS name transfers and registrations.


# Endpoint Specifications

## Record Endpoints
| SDK Method                                                                   | Endpoint URL                                 | Returns           |
| ---------------------------------------------------------------------------- | -------------------------------------------- | ----------------- |
| `ens.records_by_owner(owner_address, limit)`                                 | `GET /v0/ens/ens-records-by-owner`           | `List[ENSRecord]` |
| `ens.records_by_date(timestamp_after, timestamp_before, type, order, limit)` | `GET /v0/ens/ens-records-by-date`            | `List[ENSRecord]` |
| `ens.records_by_account(resolved_address)`                                   | `GET /v0/ens/ens-records-by-account`         | `List[ENSRecord]` |
| `ens.records_by_name(ens_names)`                                             | `GET /v0/ens/ens-records-by-name`            | `List[ENSRecord]` |
| `ens.records_by_token_id(token_ids)`                                         | `GET /v0/ens/ens-records-by-token-id`        | `List[ENSRecord]` |

### ENS Record Model
<details>
<summary>View Model Specification</summary>

The **ENS Record Model** contains the full set of information for a single ENS name, including its owner, resolved address, resolver, node, and much more. The **ENS Record Model** follows the following structure: 

| Name                   | Description                                                                                             | Type        |
| ---------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| ens_name               | The ENS name.                                                                                           | `string`    |
| ens_node               | The unique ENS nodehash which points to the ENS name.                                                   | `string`    |
| contract_address       | The contract address of the ENS collection.                                                             | `string`    |
| token_id               | The token ID of the ENS name.                                                                           | `integer`   |
| meta_block_number                 | Unique sequential ID of the ENS name used by the Transpose backend.                                     | `integer`   |
| owner                  | The owner of the ENS name.                                                                              | `string`    |
| resolver               | The resolver contract address of the ENS name.                                                          | `string`    |
| resolved_address       | The address which has this ENS name set to be their primary name.                                       | `string`    |
| registration_timestamp | The timestamp on which this ENS name was registerred (in ISO-8601 format).                              | `date-time` |
| expiration_timestamp   | The timestamp on which this ENS registration will expire (in ISO-8601 format).                          | `date-time` |
| grace_period_ends      | The timestamp on which the ENS grace period will end (in ISO-8601 format).                              | `date-time` |
| premium_period_ends    | The timestamp on which the ENS premium period will end (in ISO-8601 format).                            | `date-time` |
| in_grace_period        | Whether the ENS name is currently in the 90 day grace period.                                           | `boolean`   |
| in_premium_period      | Whether the ENS name is currently in the 21 day premium period.                                         | `boolean`   |
| is_expired             | Whether the ENS name is currently expired.                                                              | `boolean`   |
| last_refreshed         | The timestamp at which the ENS record was last refreshed by the Transpose backend (in ISO-8601 format). | `date-time` |

</details>


## Transfer Endpoints
| SDK Method                                                                                                    | Endpoint URL                            | Returns             |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------- |
| `ens.transfers_by_name(ens_name, transferred_after, transferred_before, order, limit)`     | `GET /v0/ens/ens-transfers-by-name`     | `List[ENSTransfer]` |
| `ens.transfers_by_token_id(token_id, transferred_after, transferred_before, order, limit)` | `GET /v0/ens/ens-transfers-by-token-id` | `List[ENSTransfer]` |

### ENS Transfer Model
<details>
<summary>View Model Specification</summary>

The **ENS Transfer Model** represents a single transfer of an ENS name. The **ENS Transfer Model** follows the following structure:

| Name             | Description                                                            | Type        |
| ---------------- | ---------------------------------------------------------------------- | ----------- |
| ens_name         | The ENS name.                                                          | `string`    |
| ens_node         | The unique ENS nodehash which points to the ENS name.                  | `string`    |
| contract_address | The contract address of the ENS collection.                            | `string`    |
| token_id         | The token ID of the ENS name.                                          | `integer`   |
| block_number     | The block number at which the transfer occurred.                       | `integer`   |
| log_index        | The log index at which the transfer occurred.                          | `integer`   |
| transaction_hash | The transaction hash at which the transfer occurred.                   | `string`    |
| timestamp        | The timestamp of the transfer (in ISO-8601 format).                    | `date-time` |
| category         | The category of the ENS name transfer (one of `mint`, `send`, `burn`). | `string`    |
| from             | The address of the sender.                                             | `string`    |
| to               | The address of the receiver.                                           | `string`    |

</details>