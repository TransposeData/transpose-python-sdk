![CDN Banner](https://files.readme.io/109da16-TRSP_DocBanner_CDN2.png)
# Welcome to the Transpose CDN

The **Transpose CDN** provides supplementary data for endpoints across the Transpose API suite, including raw block data, NFT images, media, and metadata, collection images, and token symbols.

# Endpoint Specifications

## Query Endpoints

| SDK Method             | Endpoint URL | Returns       |
| ---------------------- | ------------ | ------------- |
| `cdn.query(endpoint)` | `*`          | `CDNResponse` |
| `cdn.bulk_query(endpoints, requests_per_second)` | `*`          | `List[CDNResponse]` |


### CDN Response Model
<details>
<summary>View Model Specification</summary>

The **CDN Response Model** contains the content type, content, and helper methods which can assist you in working with CDN data. The **CDN Record Model** follows the following structure: 

#### Attributes

| Name         | Description                   | Type   |
| ------------ | ----------------------------- | ------ |
| content_type | The content type of the data. | string |
| content      | The data returned by the CDN. | string |

#### Methods

| Name         | Description                                        | Usage                            |
| ------------ | -------------------------------------------------- | -------------------------------- |
| to_dict      | Returns a dictionary representation of the model.  | `CDNResponse.to_dict()`          |
| \_\_dict\_\_ | Returns a dictionary representation of the model.  | `CDNResponse.__dict__()`         |
| save         | Saves to model to the disk                         | `CDNResponse.save(path: string)` |
| json         | Attempt to get the CDNResponse.contents as a dict. | `CDNResponse.json()`             |
| image        | Attempt to parse the CDNResponse as a PIL image.   | `CDNResponse.image()`            |

</details>


## Download Endpoints

| SDK Method             | Endpoint URL | Returns       |
| ---------------------- | ------------ | ------------- |
| `cdn.save(endpoint)` | `*`          | `None` |
| `cdn.bulk_save(endpoints, requests_per_second, dir)` | `*`          | `None` |

### CDN Response Model
<details>
<summary>View Model Specification</summary>

The **CDN Response Model** contains the content type, content, and helper methods which can assist you in working with CDN data. The **CDN Record Model** follows the following structure: 

#### Attributes

| Name         | Description                   | Type   |
| ------------ | ----------------------------- | ------ |
| content_type | The content type of the data. | string |
| content      | The data returned by the CDN. | string |

#### Methods

| Name         | Description                                        | Usage                            |
| ------------ | -------------------------------------------------- | -------------------------------- |
| to_dict      | Returns a dictionary representation of the model.  | `CDNResponse.to_dict()`          |
| \_\_dict\_\_ | Returns a dictionary representation of the model.  | `CDNResponse.__dict__()`         |
| save         | Saves to model to the disk                         | `CDNResponse.save(path: string)` |
| json         | Attempt to get the CDNResponse.contents as a dict. | `CDNResponse.json()`             |
| image        | Attempt to parse the CDNResponse as a PIL image.   | `CDNResponse.image()`            |

</details>