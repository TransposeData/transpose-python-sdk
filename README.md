![Transpose Banner](https://files.readme.io/c019281-Main_Docs_Banners_v1.png)

# Welcome to the Transpose Python SDK
![Deployment Tests](https://github.com/TransposeData/transpose-python-sdk/actions/workflows/deployment_tests.yml/badge.svg) ![PyPI version](https://badge.fury.io/py/transpose-data.svg) ![Installations](https://img.shields.io/pypi/dd/transpose-data?color=g)

A modern python wrapper for the Transpose API Suite.

## Getting an API Key

To obtain a free Transpose API key, sign up on our [website](https://www.transpose.io/). Free tier keys have a rate limit of 1 request per second and 250,000 credits per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord or upgrade your tier directly in the webapp!

Join our [Discord](https://discord.gg/AKguqp3U57) to ask technical questions, share what you're building, and chat with others in the community.

## Installation

**Python 3.8 or higher is recommended**

To install the python SDK, you can run the following command:
```
python3 -m pip install -U transpose-data
```

---

## Documentation
You can find specific documentation on a per-product basis below.

|  Product  | Description                                                                                                                                                                                                                  | Documentation                                                                                   |
| :-------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Block API | The Block API provides endpoints for accessing low-level blockchain data at scale, including accounts, blocks, transactions, internal transactions, and logs.                                                                | [Block API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/block.md) |
|  ENS API  | The ENS API provides endpoints for looking up ENS names (both historical and primary), resolving ENS names and records, and monitoring ENS transfers and sales.                                                              | [ENS API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/ens.md)     |
|  NFT API  | The NFT API provides endpoints for retrieving any collection and NFT in existence, as well as NFT images, operators, owners, transfers, approvals, and much more (fully supports both ERC-721 and ERC-1155 NFTs).            | [NFT API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/nft.md)     |
| Token API | The Token API provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens). | [Token API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/token.md) |
| SQL API | The SQL API provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain.  | [SQL API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/sql.md) |
| Endpoint API | The Endpoint API provides customized REST endpoints that you can create, version, and use directly in your production applications. | [Endpoint API Docs](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/endpoint.md) |

## SDK Documentation
You can learn more about the Transpose SDK and how it works below.

### SDK Helpers

#### stringify_list
Converts a list of strings into a single string, separated by a delimiter.

```python
from transpose.src.util.format import stringify_list

stringify_list(['a', 'b', 'c'], ',')
>>> 'a,b,c'
```

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

#### Response Classes (**DEPRECATED AS OF v3.1.0**)
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

---

## SDK Options
The Transpose SDK can be configured to your liking, allowing you to change the default behavior of the SDK.

### Updating Chain ID
<details>
<summary>
Updating SDK Working Chain ID
</summary>

If you want to change the chain ID of your query, you can do so by setting the `chain_id` or `chain` properties of the `Transpose` object. For example, if you want to query the Ethereum mainnet, you can do so by running the following code:

```python
from transpose import Transpose
api = Transpose(api_key="YOUR_API_KEY", chain_id=1)
```

or
```python
from transpose import Transpose
api = Transpose(api_key="YOUR_API_KEY", chain_id="ethereum")
```

if you wish to change the chain ID of an existing `Transpose` object, you can do so by running the following code:

```python
api.set_chain("ethereum")
```

or 

```python
api.set_chain(1)
```

#### Currently supported chains
| Chain ID | Chain Name |
| :------: | :--------: |
|    1     |  Ethereum  |
|   137    |  Polygon   |
</details>

### Raw JSON Responses
<details>
<summary>
Opt-in to raw JSON Responses
</summary>
If you wish to receive responses in JSON format, you can set the `json` parameter to `True` when initializing the SDK. This will return all responses as JSON objects.

**Response classes are considered deprecated as of v3.1.0 and will be removed in v4.0.0. JSON responses will become standard in v4.0.0**

```python
from transpose_sdk import Transpose
api = Transpose(api_key="YOUR_API_KEY", json=True)
```
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
| 401  | Unauthorized          | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 403  | Forbidden             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 404  | Not Found             | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |
| 500  | Internal Server Error | [Error](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/documentation.md#Error-Classes) |

Here is an example of how to use ``bulk_request``:

```python
recent_blocks_since = api.bulk_request(api.block.blocks_by_date(added_after='2022-01-01 00:00:00', limit=500))

print(len(recent_blocks_since))

>>> 500
```
</details>

---

## SDK Extras
The following methods are available as extras to the Transpose SDK. 

You can import extras to your project by using:
```python
from transpose.extras import <MODULE>
```

Some extras will require additional dependencies to be installed. If you are missing dependencies, the SDK will throw a `TransposeDependencyError` when you try to import the extra. This error will tell you what dependencies are missing, and give you the exact command to install them:

```shell
transpose.src.util.errors.TransposeDependencyError: Missing Dependencies. You can install these via `pip install plotly kaleido`
```

### Plotting
<details>
<summary>Transpose Plotting Specifications</summary>

The SDK natively includes a plotting library which implements [plotly](https://plot.ly/python/). Using it, you can quickly create plots of data obtained through the Transpose API.

For a plotting example, check out the [demo](https://github.com/TransposeData/transpose-python-sdk/blob/main/demo/plotting.py) file, which will graph the past hour's gas prices in a bar chart.

![chart](https://github.com/TransposeData/transpose-python-sdk/blob/main/docs/images/plotting.png?fw)

#### Usage
You'll first need to install the plotting dependencies using:
```shell
pip install plotly kaleido
```

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

---

## Making a Request

To get started and make your first request, make a new `Transpose` object:

```python
from transpose import Transpose

api = Transpose('transpose_api_key')
```

From there, you can call endpoints from the `api.nft`, `api.ens`, `api.token`, and `api.block` subclasses.

### Debugging Requests

You can view the raw HTTP requests the SDK is making by setting the `debug` flag to `True` when creating a new `Transpose` object. For example: 
```python
from transpose import Transpose

api = Transpose('transpose_api_key', debug=True)
```

## Simple Demo

To show just how powerful our data is, let's get the last ENS domain that expired. All we need is one API call.
```python
from transpose import Transpose

api = Transpose('transpose_api_key')

# get the most recently expired ENS domain
last_expired = api.ens.records_by_date(type='expiration', order='desc', limit=1)
```

This returns a list of [ENS Records](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model), which includes data which you wouldn't be able to easily get from the ENS protocol.

```json
[
  {
    "ens_name":"game-master-dit-gm.eth",
    "ens_node":"9BFFC8C1EDE1E51E4BAE137FA37A81CC0379FC08123C4AA00A931D0D983956B7",
    "contract_address":"0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85",
    "token_id":75929000750162030430773866845127925090084516346841580577625168871716954805188,
    "meta_block_number":407909,
    "owner":"0x2aC92629c4E0E5e4868588f87DC4356606a590b6",
    "resolver":"0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
    "resolved_address":"0x2aC92629c4E0E5e4868588f87DC4356606a590b6",
    "registration_timestamp":"2022-01-01T05:00:36Z",
    "expiration_timestamp":"2049-12-31T23:58:12Z",
    "grace_period_ends":"2050-03-31T23:58:12Z",
    "premium_period_ends":"2050-04-21T23:58:12Z",
    "in_grace_period":false,
    "in_premium_period":false,
    "is_expired":false,
    "last_refreshed":"2022-06-01T09:51:23Z"
  }
]
```

## Links

- [SDK Examples](https://github.com/TransposeData/transpose-python-sdk/tree/main/demo)
- [Transpose Documentation](https://docs.transpose.io)
- [Official Discord Server](https://discord.gg/AKguqp3U57)
