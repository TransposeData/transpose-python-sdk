# Welcome to the Transpose Python SDK Documentation

## Product Documentation
You can find specific documentation on a per-product basis below.

|                                                                            Product                                                                            | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628ebc9704701b4d5610ac1a_Blockchain_Logo_Solid.png" width="50" height="50"><br> Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628d465b6551e284a9ae73e4_Wallet_Logo_ENS.png" width="50" height="50"><br> ENS API     | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
|     <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/6286795ef57a1412d6d767fc_NFT_Logo_Solid.png" width="50" height="50"><br> NFT API      | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
|   <img src="https://assets.website-files.com/624cc12cbb8535a77bafc47d/628fb0f77f6279a920577119_Token_Logo2_Solid.png" width="50" height="50"><br>Token API    | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
|      <img src="https://assets.website-files.com/624c8536aa7f872fe6829dbd/628feeeb8eb1204a1c701cd1_CDN_Logo_Red-p-500.png" width="50" height="50"><br>CDN      | The Transpose CDN provides supplementary data for endpoints across the Transpose API suite, including raw block data, NFT images, media, and metadata, collection images, and token symbols.                                 | [CDN Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/cdn.md)         |

## SDK Documentation
You can learn more about the Transpose SDK and how it works below.

### SDK Classes
The Transpose SDK uses custom classes to represent API responses:

#### Error Classes
<details>
<summary>SDK Error Class Specifications</summary>
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
</details>

#### Response Classes
<details>
<summary>Response Class Specifications</summary>

The SDK will always return a list of response objects from the Transpose API. For example, calling the ``ens.records_by_date`` endpoint will return a list of ``ENSRecord`` objects.

These response objects can be accessed in the following ways:
  - ``ENSRecord[0].ens_name`` will return the first record's ens_name.
  - ``ENSRecord[i].ens_name`` retrieves the ens_name from the i-th response
  
All response objects can also be accessed as a dictionary by calling ``.to_dict()`` on them:
  - ``ENSRecord[0].to_dict()`` will return the first record as a dictionary.
  - ``ENSRecord[i].to_dict()`` retrieves the i-th record as a dictionary.
</details>

### Pagination
<details>
<summary>Pagination with the Transpose SDK.</summary>

Transpose endpoints will return a maximum of 500 results in a single query. To return the next page, simply call ``api.next()``. If ``api.next()`` returns ``None``, then there are no more pages.

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
</details>


### Bulk Requests
<details>

<summary>Bulk requesting data with the Transpose SDK</summary>
Alongside pagination, we also offer a convenience method for iterating over all pages. This method will handle pagination for you, and will return a list of all results.

#### Usage:
```python
api.bulk_request(endpoint_response, requests_per_second, results_to_fetch)
```
| Parameter           | Required | Description                                                   | Type     |
| ------------------- | -------- | ------------------------------------------------------------- | -------- |
| endpoint_response   | Yes      | The called API function, which returns a list of data models. | ``List`` |
| requests_per_second | No       | The number of requests per second to make                     | ``int``  |
| results_to_fetch    | No       | The number of results to fetch                                | ``int``  |

#### Responses
| Code | Title                 | Model                                                                                                        |
| ---- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 200  | Success               | Data Model                                                                                                   |
| 400  | Bad Request           | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |

Here is an example of how to use ``bulk_request``:

```python
all_blocks_by_miner = api.bulk_request(api.block.blocks_by_date(mined_after='2022-01-01 00:00:00', miner='0x00192Fb10dF37c9FB26829eb2CC623cd1BF599E8', limit=500))

print(len(all_blocks_by_miner))

>>> 53046
```
</details>

---

## SDK Extras
The following methods are available as extras to the Transpose SDK. 

You can import extras to your project by using:
```python
from transpose.extras import <MODULE>
```

### Plotting
<details>
<summary>Transpose Plotting Specifications</summary>

The SDK natively includes a plotting library which implements [plotly](https://plot.ly/python/). Using it, you can quickly create plots of data obtained through the Transpose API.

For a plotting example, check out the [demo](https://github.com/TransposeData/transpose-python-sdk/blob/main/demo/plotting.py) file, which will graph the past hour's gas prices in a bar chart.

![chart](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/images/plotting.png?fw)

#### Usage
Instantiating a new plot is as simple as importing the ``Plot`` class and instantiating it:

```python
from transpose.extras import Plot
chart = Plot(title="Hourly Gas Prices on Ethereum")
```

This will return an object on which you can call the following methods:

- ``Plot.plotly()``
  - Returns the current plot as a plotly object. From there, you can further customize the plot.
  
- ``Plot.show()``
  - Renders the current plot in the browser. This plot is interactive, and can be zoomed and panned.
  
- ``Plot.render(path, format)``
  - Inputs:
    - ``path`` -> The path to render the plot to.
    - ``format`` -> The format to render the plot as. Can be either ``png``, ``html``, ``jpg``, etc.

- ``Plot.add_data(data, type, shape, smoothing)``

  - Inputs:
    - ``data`` -> The data to add to the plot. Takes the following format:
      
      ```json
      {
        "x":       [],                   // List of data
        "y":       [],                   // List of data
        "y_axis":  "Gas Price (Gwei)",   // OPTIONAL: The name of the y-axis
        "x_axis":  "Time",               // OPTIONAL: The name of the x-axis
      }
      ```
    - ``type`` -> OPTIONAL: The method used to render the data to the plot. Can be either ``line`` or ``bar``.
    - ``shape`` -> OPTIONAL: The shape of the line. Can be either ``linear``, ``spline``, ``vh``, ``hv``, ``vhv``, or ``hvh``.
    - ``smoothing`` -> OPTIONAL: The number of points to smooth the data with.
      - For ``line``, this will calculate a moving average of the data with a period of ``smoothing``.
      - For ``bar``, this will group and average the data over ``smoothing`` points.
</details>