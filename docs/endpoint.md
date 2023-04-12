# Welcome to the Endpoint API

The **Endpoint API** provides customized REST endpoints that you ca n create, version, and use directly in your production applications

## Usage

You may use the Endpoint API within your python project as follows:

```python
api.endpoint.query(endpoint_url: str, parameters: dict) -> dict
```

For example:

```python
api = Transpose(api_key)
        
parameters = {
    'start_date': datetime.now().isoformat().split("T")[0],
    'time_interval': '1 day',
    'token_address': '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
}

response = api.endpoint.query('ohlc', parameters)
```

## Parameters

| Parameter | Type | Description |
| - | - | - |
| `endpoint_url` | `string` | The custom endpoint URL to query. Your team must be the creators of this query. |
| `parameters` | `dict` | The optional parameters for this call. |

## More Information

You can find more information about the Custom Endpoint API in our [documentation](https://docs.transpose.io/custom-endpoints/overview/).
