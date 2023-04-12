# Welcome to the SQL API

The **SQL API** provides direct SQL access to our entire ecosystem of indexed blockchain data. Paired with our robust indexing pipeline, SQL access gives unlimited flexibility in how you mix, aggregate, and query activity across the blockchain. 

## Usage

### Calling a SQL Query

You may use the SQL API within your python project as follows:

```python
api.sql.query(sql_query: str, paramters: dict) -> dict
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

### Generating queries with the AI Query Assistant

You may generate SQL queries with the AI Query Assistant as follows:

```python
api.sql.generate_query(self, text: str, chain: str='ethereum') -> dict:
```

For example:

```python
api = Transpose(api_key)

response = api.sql.generate_query('Give me the most recently updated ENS name that is 3 characters long. Since all ens names end in ".eth", you\'ll need to add 4 to the search length. Optimize this query as much as possible.')

print(response)

# {
#    "options": [
#        "SELECT\n    ens_name, last_refreshed\nFROM\n    ethereum.ens_names\nWHERE\n    LENGTH(ens_name) = 7 AND ens_name LIKE '%.eth'\nORDER BY\n    last_refreshed DESC\nLIMIT 1;"
#    ]
# }
```

#### Parameters

| Parameter | Type | Description |
| - | - | - |
| `text` | `string` | The text to generate a query from. Explain to the AI what you want to do, and it will generate a query for you. |
| `chain` | `string` | The optional chain to generate a query for. Defaults to `ethereum`. Valid chains are `ethereum`, `goerli`, `arbitrum`, `canto`, `scroll`, or `polygon`. |

## More Information

You can find more information about the SQL API in our [documentation](https://docs.transpose.io/sql/overview/).