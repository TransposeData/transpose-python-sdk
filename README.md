![Transpose Banner](https://files.readme.io/356ac19-TRSP_DocBanner.png)

# Welcome to the Transpose Python SDK
A modern python wrapper for the Transpose API Suite.


## Installation

**Python 3.8 or higher is recommended**

To install the python SDK, you can run the following command:
```
python3 -m pip install -U transpose-data
```

## Simple Demo

To show just how powerful our data is, let's get the last ENS domain that expired. All we need is one API call.
```
from transpose import Transpose

api = Transpose('transpose_api_key')

# get the most recently expired ENS domain
last_expired = api.ENS.records_by_date(type='expiration', order='desc', limit=1)
```

This returns an [ENS Record](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs/ens.md#ENS-Record-Model) as a JSON object, which includes data which you wouldn't be able to easily get from the ENS protocol.

```
{
  "status": "success",
  "count": 1,
  "next": "https://api.transpose.io/...",
  "results": [
    {
      "ens_name": "shytoshikusama.eth",
      "ens_node": "0A70AB909E218B60E5497145DAC61F2C3F4B463C9EF6188D3F73B66958F92E29",
      "contract_address": "0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85",
      "token_id": 3.191314232205825e+76,
      "seq_id": 108357,
      "owner": "0x5C1Ca381D68044D111b11d8469B1F865Ed68783f",
      "resolver": "0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41",
      "resolved_address": "0x5C1Ca381D68044D111b11d8469B1F865Ed68783f",
      "registration_timestamp": "2021-07-21T17:15:54Z",
      "expiration_timestamp": "4271-07-22T08:15:54Z",
      "grace_period_ends": "4271-10-20T08:15:54Z",
      "premium_period_ends": "4271-11-10T08:15:54Z",
      "in_grace_period": false,
      "in_premium_period": false,
      "is_expired": false,
      "last_refreshed": "2022-05-27T02:19:17Z"
    }
  ]
}
```

## Links
- [SDK Documentation](https://github.com/TransposeData/transpose-python-sdk/tree/main/docs)
- [SDK Examples](https://github.com/TransposeData/transpose-python-sdk/tree/main/examples)
- [Transpose Documentation](https://docs.transpose.io)
- [Official Discord Server](https://discord.gg/AKguqp3U57)