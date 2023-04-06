# Welcome to the SQL API

The **SQL API** provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain. 

## Usage

You may use the SQL API within your python project as follows:

```python
api.sql.query(endpoint_url: str, paramters: dict) -> dict
```

For example:

```python
api = Transpose(api_key)
        
parameters = {
    'limit': 10,
}

response = api.endpoint.query("SELECT * FROM ethereum.logs LIMIT {{limit}}", parameters)
```

## Parameters

| Parameter | Type | Description |
| - | - | - |
| `endpoint_url` | `string` | The custom endpoint URL to query. Your team must be the creators of this query. |
| `parameters` | `dict` | The optional parameters for this call. |

## More Information

You can find more information about the Custom Endpoint API in our [documentation](https://docs.transpose.io/custom-endpoints/overview/).