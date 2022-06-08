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
The Transpose SDK uses custom classes to represent API responses:

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
The SDK will always return a list of response objects from the Transpose API. For example, calling the ``ENS.records_by_date`` endpoint will return a list of ``Record`` objects.

These response objects can be accessed in the following ways:
  - ``Record[0].ens_name`` will return the first record's ens_name.
  - ``Record[i].ens_name`` retrieves the ens_name from the i-th response
  
All response objects can also be accessed as a dictionary by calling ``.to_dict()`` on them:
  - ``Record[0].to_dict()`` will return the first record as a dictionary.
  - ``Record[i].to_dict()`` retrieves the i-th record as a dictionary.

### Pagination

Pagination on the Transpose API is straightforward.

Transpose API endpoints will return a maximum of 500 results in a single query. To return the next page, simply call ``api.next()``. If ``api.next()`` returns ``None``, then there are no more pages.

Here is a standard pagination implementation:

```python
while True:
    data = api.next()

    # sleep to avoid rate limits
    time.sleep(1)

    # if there are no more pages, exit loop
    if data is None: break

    # otherwise, print length of data
    else: print(len(data))
```
