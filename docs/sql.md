# Welcome to the SQL API

The **SQL API** provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain. 

## Usage

### Calling a SQL Query

You may use the SQL API within your python project as follows:

```python
api.sql.query(sql_query: str, parameters: dict) -> dict
```

For example:

```python
api = Transpose(api_key)
        
parameters = {
    'limit': 10,
}

response = api.sql.query("SELECT * FROM ethereum.logs LIMIT {{limit}}", parameters)
```

#### Parameters

| Parameter | Type | Description |
| - | - | - |
| `sql_query` | `string` | The SQL query to call. |
| `parameters` | `dict` | The optional parameters for this call. |

### Getting the SQL Schema

You may fetch our internal SQL schema as a dictionary with the following method:

```python
api.sql.schema() -> dict
```

For example:

```python
api = Transpose(api_key)

response = api.sql.schema()

print(response)

# {
#     "schema": {
#         "ethereum": {
#             "settlement_layer": [
#                 {
#                     "accounts": {
#                         "meta": {
#                             "table": "accounts",
#                             "description": "The `ethereum.accounts` table provides indexed views of all accounts, including both externally-owned accounts (colloquially referred to as wallets) and contracts.",
#                             "indexes": [
#                                 [
#                                     "created_timestamp",
#                                     "address"
#                                 ],
#                                 ...
#                             ]
#                         },
#                         "schema": [
#                             {
#                                 "column": "address",
#                                 "type": "text",
#                                 "description": "The address of the account."
#                             },
#                             ...
#                         ]
#                     }
#                 },
#                 ...
#             ]
#         },
#         ...
#     }
# }
```

#### Parameters

| Parameter | Type | Description |
| - | - | - |
| `text` | `string` | The text to generate a query from. Explain to the AI what you want to do, and it will generate a query for you. |
| `chain` | `string` | The optional chain to generate a query for. Defaults to `ethereum`. Valid chains are `ethereum`, `goerli`, `arbitrum`, `canto`, `scroll`, or `polygon`. |

## More Information

You can find more information about the SQL API in our [documentation](https://docs.transpose.io/sql/overview/).