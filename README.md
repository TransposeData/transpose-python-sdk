![Transpose Banner](https://files.readme.io/356ac19-TRSP_DocBanner.png)

# Welcome to the Transpose Python SDK
![Deployment Tests](https://github.com/TransposeData/transpose-python-sdk/actions/workflows/deployment_tests.yml/badge.svg) ![PyPI version](https://badge.fury.io/py/transpose-data.svg) ![Installations](https://img.shields.io/pypi/dd/transpose-data?color=g)

A modern python wrapper for the Transpose API Suite.

## Getting an API Key

To obtain a free Open Alpha Transpose API key, sign up on our [website](https://www.transpose.io/). API Keys are rate limited to 1 request per second and 100,000 requests per month. If you need higher rate limits for your project or business, don't hesitate to reach out on our Discord!

Join our [Discord](https://discord.gg/AKguqp3U57) to ask technical questions, share what you're building, and chat with others in the community.

## Installation

**Python 3.8 or higher is recommended**

To install the python SDK, you can run the following command:
```
python3 -m pip install -U transpose-data
```

## Simple Demo

To show just how powerful our data is, let's get the last ENS domain that expired. All we need is one API call.
```python
from transpose import Transpose

api = Transpose('transpose_api_key')

# get the most recently expired ENS domain
last_expired = api.ENS.records_by_date(type='expiration', order='desc', limit=1)
```

This returns an [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model) as a [TransposeAPIResponse](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/documentation.md#Response-Classes), which includes data which you wouldn't be able to easily get from the ENS protocol.

```json
[
  {
    "ens_name":"game-master-dit-gm.eth",
    "ens_node":"9BFFC8C1EDE1E51E4BAE137FA37A81CC0379FC08123C4AA00A931D0D983956B7",
    "contract_address":"0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85",
    "token_id":75929000750162030430773866845127925090084516346841580577625168871716954805188,
    "seq_id":407909,
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
- [SDK Documentation](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/documentation.md)
- [SDK Examples](https://github.com/TransposeData/transpose-python-sdk/tree/main/examples)
- [Transpose Documentation](https://docs.transpose.io)
- [Official Discord Server](https://discord.gg/AKguqp3U57)
