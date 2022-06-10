import pandas as pd

from datetime import datetime, timedelta, timezone
from transpose.extras import Plot
from transpose import Transpose, api_key


api = Transpose(api_key)

start_time = datetime.now().timestamp()
address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
native_token_transfers = api.bulk_request(api.token.native_token_transfers_by_account(account_address=address, limit=500))

balance = 0
native_token_balances = []
for transfer in native_token_transfers:
    if transfer.to == address:
        balance += transfer.quantity 
    else:
        balance -= transfer.quantity
        
    native_token_balances.append(balance / 10 ** 18)
    
chart = Plot(title="Balance over Time for {}".format(address[0:10]))

chart.add_data({
    "x": [transfer.block_number for transfer in native_token_transfers],
    "y": native_token_balances,
}, smoothing=100)

chart.render("a.png")

end_time = datetime.now().timestamp()

# time difference in seconds
print("Time taken: {}".format(end_time - start_time))