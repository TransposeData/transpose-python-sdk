![ENS API Banner](https://files.readme.io/c59e02a-TRSP_DocBanner_ENS.png)
# Welcome to the ENS API

The **ENS API** provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.

## Endpoint Overview
The **ENS API** supports the following groups of endpoints:
 
1. [Record Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md#Record-Endpoints): Retrieve any ENS record ever created by account, owner, name, node, registration date, expiration date and more.
2. [Transfer Activity Endpoints](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md#Transfer-Activity-Endpoints): Retrieve all historical and live ENS name transfers and registrations.

## Data Models

### ENS Record Model
The **ENS Record Model** contains the full set of information for a single ENS name, including its owner, resolved address, resolver, node, and much more. The **ENS Record Model** follows the following structure: 

| Name                   | Description                                                                                             | Type        |
| ---------------------- | ------------------------------------------------------------------------------------------------------- | ----------- |
| ens_name               | The ENS name.                                                                                           | `string`    |
| ens_node               | The unique ENS nodehash which points to the ENS name.                                                   | `string`    |
| contract_address       | The contract address of the ENS collection.                                                             | `string`    |
| token_id               | The token ID of the ENS name.                                                                           | `integer`   |
| seq_id                 | Unique sequential ID of the ENS name used by the Transpose backend.                                     | `integer`   |
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

### ENS Transfer Model
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

# Endpoint Specifications

## Record Endpoints

### Get ENS Records by Owner
This endpoint returns ENS records for names that are owned by a given account (supports pagination).

#### Usage
```
ENS.records_by_owner(owner_address, limit)
```

#### Query Parameters
| Parameter     | Required | Description                                                                        | Type      |
| ------------- | -------- | ---------------------------------------------------------------------------------- | --------- |
| owner_address | yes      | The account address of the owner to retrieve ENS records for (supports ENS names). | `string`  |
| limit         | no       | The maximum number of results to retrieve (max 500).                               | `integer` |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |



### Get ENS Records by Date
This endpoint returns ENS records with events occurring in a given date range (supports pagination).

#### Usage
```
ENS.records_by_date(timestamp_after, timestamp_before, type, order, limit)
```

#### Query Parameters
| Parameter        | Required | Description                                                              | Type        |
| ---------------- | -------- | ------------------------------------------------------------------------ | ----------- |
| timestamp_after  | no       | The earliest timestamp to retrieve ENS records for (in ISO-8601 format). | `date-time` |
| timestamp_before | no       | The latest timestamp to retrieve ENS records for (in ISO-8601 format).   | `date-time` |
| type             | no       | The type of date to filter by. (one of `registration` or `expiration`).  | `string`    |
| order            | no       | The order in which to return the results. (one of `asc` or `desc`).      | `string`    |
| limit            | no       | The maximum number of results to retrieve (max 500).                     | `integer`   |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get Primary ENS Records by Account
This endpoint returns primary ENS records for names that resolve to a given list of account addresses.

#### Usage
```
ENS.primary_ens_records_by_account(account_address)
```

#### Query Parameters
| Parameter       | Required | Description                                                                                                   | Type       |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------- | ---------- |
| account_address | yes      | The list of account addresses to retrieve ENS names for, separated by commas (max 100 addresses per request). | `string[]` |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get ENS Records by ENS Name
This endpoint returns ENS records that correspond to a given list of ENS names.

#### Usage
```
ENS.records_by_name(ens_names)
```

#### Query Parameters
| Parameter | Required | Description                                        | Type       |
| --------- | -------- | -------------------------------------------------- | ---------- |
| ens_names | yes      | The list of ENS names to retrieve ENS records for. | `string[]` |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get ENS Records by ENS Node
This endpoint returns ENS records that correspond to a given list of ENS node.

#### Usage
```
ENS.records_by_node(ens_nodes)
```

#### Query Parameters
| Parameter | Required | Description                                     | Type       |
| --------- | -------- | ----------------------------------------------- | ---------- |
| ens_nodes | yes      | The list of ENS nodes to query ENS records for. | `string[]` |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get ENS Records by ENS Token ID
This endpoint returns ENS records for a given list of ENS token IDs.

#### Usage
```
ENS.records_by_token_id(token_ids)
```

#### Query Parameters
| Parameter | Required | Description                                         | Type        |
| --------- | -------- | --------------------------------------------------- | ----------- |
| token_ids | yes      | The list of ENS token IDs to query ENS records for. | `integer[]` |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Get ENS Records by ENS Resolver
This endpoint returns ENS records for a given ENS resolver (supports pagination).
#### Usage
```
ENS.records_by_resolver(token_ids)
```

#### Query Parameters
| Parameter | Required | Description                                                  | Type      |
| --------- | -------- | ------------------------------------------------------------ | --------- |
| token_ids | yes      | The address of the ENS resolver to retrieve ENS records for. | `string`  |
| limit     | no       | The maximum number of results to retrieve (max 500).         | `integer` |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model)   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


## Transfer Activity Endpoints

### Get ENS Transfers by ENS Name
This endpoint returns ENS transfers for a given ENS name (supports pagination).
#### Usage
```
ENS.transfers_by_name(ens_name, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters
| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| ens_name           | yes      | The ENS name to retrieve transfers for (max 256 characters).                               | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).      | `string`    |
| order              | no       | The order in which to retrieve the results (either `asc` or `desc`).                       | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |


#### Responses
| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [ENS Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |


### Get ENS Transfers by ENS Node
This endpoint returns ENS transfers for a given ENS node (supports pagination).
#### Usage
```
ENS.transfers_by_node(node, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters
| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| node               | yes      | The ENS nodehash to retrieve transfers for.                                                | `string`    |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).      | `string`    |
| order              | no       | The order in which to retrieve the results (either `asc` or `desc`).                       | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |


#### Responses
| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [ENS Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |


### Get ENS Transfers by ENS Token ID
This endpoint returns ENS transfers for a given ENS token ID (supports pagination).
#### Usage
```
ENS.transfers_by_token_id(token_id, transferred_after, transferred_before, transfer_category, order, limit)
```

#### Query Parameters
| Parameter          | Required | Description                                                                                | Type        |
| ------------------ | -------- | ------------------------------------------------------------------------------------------ | ----------- |
| token_id           | yes      | The ENS token ID to retrieve transfers for.                                                | `integer`   |
| transferred_after  | no       | The earlier transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format). | `date-time` |
| transferred_before | no       | The later transfer date, inclusive (in seconds since the Unix epoch or ISO-8601 format).   | `date-time` |
| transfer_category  | no       | The transfer category to filter results by (one of `mint`, `send`, `burn`, or `all`).      | `string`    |
| order              | no       | The order in which to retrieve the results (either `asc` or `desc`).                       | `string`    |
| limit              | no       | The maximum number of results to retrieve (max 500).                                       | `integer`   |


#### Responses
| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [ENS Transfer](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Transfer-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
