# Welcome to the Transpose Python SDK Documentation

## Product Documentation
You can find specific documentation on a per-product basis below.

|                                                                            Product                                                                            | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628ebc9704701b4d5610ac1a_Blockchain_Logo_Solid.png" width="50" height="50"><br> Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628d465b6551e284a9ae73e4_Wallet_Logo_ENS.png" width="50" height="50"><br> ENS API     | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/6286795ef57a1412d6d767fc_NFT_Logo_Solid.png" width="50" height="50"><br> NFT API      | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
|   <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628fb0f77f6279a920577119_Token_Logo2_Solid.png" width="50" height="50"><br>Token API    | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |

## SDK Documentation
You can learn more about the Transpose SDK and how it works below.

### SDK Classes
The Transpose SDK uses custom classes to represent API responses. 

#### Error Classes
The SDK uses the following error classes to represent API errors:
- ``TransposeBadRequest``
  - Represents a 400 Bad Request error from the Transpose API.
- ``TransposeRateLimit``
  - Represents a 429 Rate Limit error from the Transpose API.
- ``TransposeInvalidAPIKey``
  - Represents a 401 Unauthorized error from the Transpose API.
- ``TransposeInternalServerError``
  - Represents a 500 Internal Server Error error from the Transpose API.
- ``TransposeResourceNotFound``
  - Represents a 404 Not Found error from the Transpose API.

These errors will be raised when the SDK encounters an error from the Transpose API.

#### Response Classes

- ``TransposeAPIResponse``
  - The generic response class for all Transpose API endpoints.
  - Can be interated over to retrieve the response data, represented as a dict, or accessed as a property.
  - If there is only one response, the response data will be contained by the ``TransposeAPIResponse`` class.

  Examples:

  - ``TransposeAPIResponse.ens_name`` works if there is only one response
    - ``TransposeAPIResponse[0].ens_name`` will also work in this case
  - ``TransposeAPIResponse[i].ens_name`` retrieves the ens_name from the i-th response
  - ``TransposeAPIResponse.__dict__()`` returns the response data as an array of dicts which hold the response data
  
- ``TransposeModel``
  - The generic response class for all Transpose API endpoints which wraps each data model as a class.
  - Properties accessed through the classes attributes.
  - Can be represented as a dict.

  Examples:

    - ``TransposeAPIResponse[0]`` returns a ``TransposeModel`` object
    - ``TransposeModel.ens_name`` returns the ens_name from the ``TransposeModel`` object
    - ``TransposeModel.model_name`` returns the model name from the Transpose API response.

### Pagination
Pagination on the Transpose API is straightforward.

Transpose API endpoints will return a maximum of 500 results in a single query. To return the next page, simply call ``api.next()`` or ``api.{product}.next()``. To return the previous page, simply call ``api.previous()`` or ``api.{product}.previous()``.

- If ``api._next`` is ``None``, then there are no next responses to fetch.
- If ``api._previous`` is ``None``, then there are no previous responses to fetch.

You can find a pagination example [here](https://github.com/TransposeData/transpose-python-sdk/tree/main/examples/pagination.py).