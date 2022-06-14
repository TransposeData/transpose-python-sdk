![CDN Banner](https://files.readme.io/109da16-TRSP_DocBanner_CDN2.png)
# Welcome to the Transpose CDN

The **Transpose CDN** provides supplementary data for endpoints across the Transpose API suite, including raw block data, NFT images, media, and metadata, collection images, and token symbols.

## Data Models
When querying the Transpose CDN, you will be dealing with the ``CDNResponse`` model.

### CDN Response Model
The **ENS Record Model** contains the full set of information for a single ENS name, including its owner, resolved address, resolver, node, and much more. The **ENS Record Model** follows the following structure: 

#### Attributes

| Name         | Description                            | Type   |
| ------------ | -------------------------------------- | ------ |
| content_type | The content type of the data.          | string |
| content      | The data returned by the CDN in bytes. | bytes  |

#### Methods

| Name     | Description                                       | Usage                            |
| -------- | ------------------------------------------------- | -------------------------------- |
| to_dict  | Returns a dictionary representation of the model. | `CDNResponse.to_dict()`          |
| __dict__ | Returns a dictionary representation of the model. | `CDNResponse.__dict__()`         |
| save     | Saves to model to the disk                        | `CDNResponse.save(path: string)` |



# Endpoint Specifications

## Query Endpoints

### Single Query
This endpoint returns the CDN response for a given query.

#### Usage
```
cdn.query(endpoint)
```

#### Query Parameters
| Parameter | Required | Description            | Type   |
| --------- | -------- | ---------------------- | ------ |
| endpoint  | Yes      | The endpoint to query. | string |

#### Responses
| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [CDN Response](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/cdn.md#CDN-Response-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |


### Bulk Query
This endpoint returns the CDN responses for a given query.

#### Usage
```
cdn.query(endpoints, requests_per_second)
```

#### Query Parameters
| Parameter           | Required | Description                                | Type     |
| ------------------- | -------- | ------------------------------------------ | -------- |
| endpoints           | Yes      | The endpoint to query.                     | string[] |
| requests_per_second | No       | The number of requests to send per second. | int      |

#### Responses
| Code | Title                 | Model                                                                                                          |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| 200  | Success               | [CDN Response](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/cdn.md#CDN-Response-Model) |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes)   |


## Download Endpoints

### Single Save
This endpoint saves a file from the CDN to the local disc.

#### Usage
```
cdn.query(endpoint, path)
```

#### Query Parameters
| Parameter | Required | Description            | Type   |
| --------- | -------- | ---------------------- | ------ |
| endpoint  | Yes      | The endpoint to query. | string |
| path      | No      | The path to save the file to. | string |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | None                                                                                                         |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |


### Bulk Query
This endpoint saves multiple files from the CDN to the local disc.

#### Usage
```
cdn.query(endpoints, requests_per_second, dir)
```

#### Query Parameters
| Parameter           | Required | Description                                | Type     |
| ------------------- | -------- | ------------------------------------------ | -------- |
| endpoints           | Yes      | The endpoint to query.                     | string[] |
| requests_per_second | No       | The number of requests to send per second. | int      |
| dir                 | No       | The directory to save the files to.        | string   |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | None                                                                                                         |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
