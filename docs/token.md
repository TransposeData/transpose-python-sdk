![Token API Banner](https://files.readme.io/a8b9223-TRSP_DocBanner_Token_1.png)

# Welcome to the Token API

The **Token API** provides endpoints for retrieving any token, token balance, transfer, and symbol in existence, including full support for native token transfers and balances (fully supports both ERC-20 and ERC-777 tokens).

## Endpoint Overview

The **Token API** supports the following groups of endpoints:
1. *Token Info Endpoints*: Retrieve any token ever created using flexible queries, along with token metadata and symbols.
2. *Owner Endpoints*: Retrieve all owners and owner balances for a token (ordered by balance).
3. *Operator Endpoints*: Retrieve all operators and operator allowances for a token or owner.
4. *Transfer Activity Endpoints*: Retrieve all transfers, including mints, sends, and burns, for any token or individual account.
5. *Approval Activity Endpoints*: Retrieve all token approvals by token and account (supports both ERC-20 allowances and ERC-777 operators).


## Data Models

### Error Model

The **Error Model** contains the full set of information for errors on the Transpose API suite.
| Name    | Description                     | Type     |
| ------- | ------------------------------- | -------- |
| status  | The status of the request.      | `string` |
| message | A message describing the error. | `string` |

