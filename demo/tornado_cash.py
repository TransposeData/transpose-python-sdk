import re
from typing import Any, List
import pandas as pd

from datetime import datetime, timedelta, timezone
from transpose.extras import Plot
from transpose import Transpose
import multiprocessing.pool as mpp

api = Transpose('API_KEY', True)

# get all tornado cash deposits since 2022
tornado_deposit_series = {"date": [], "usage": []}
tornado_withdrawl_series = {"date": [], "usage": []}
tornado_deposits = api.bulk_request(api.block.logs_by_date(
    emitted_after=datetime(2022, 1, 1, tzinfo=timezone.utc),
    event_signature='0xa945e51eec50ab98c161376f0db4cf2aeba3ec92755fe2fcd388bdbbb80ff196', limit=500))
tornado_withdrawls = api.bulk_request(api.block.logs_by_date(
    emitted_after=datetime(2022, 1, 1, tzinfo=timezone.utc),
    event_signature='0xe9e508bad6d4c3227e881ca19068f099da81b5164dd6d62b2eaf1e8bc6c34931', limit=500))
current_date = ""

# pull all addresses from the tornado withdrawls
recieving_addresses = []

# iterate through the tornado deposits and withdrawals and add them to the tornado series, grouping by date
for log in tornado_deposits:
    if datetime.fromisoformat(log.timestamp.split("T")[0]) == current_date:
        tornado_deposit_series['usage'][-1] += 1
    else:
        current_date = datetime.fromisoformat(log.timestamp.split("T")[0])
        tornado_deposit_series['date'].append(current_date)
        tornado_deposit_series['usage'].append(1)
for log in tornado_withdrawls:
    recieving_addresses.append("0x{}".format(log.data[26:66]))

    if datetime.fromisoformat(log.timestamp.split("T")[0]) == current_date:
        tornado_withdrawl_series['usage'][-1] += 1
    else:
        current_date = datetime.fromisoformat(log.timestamp.split("T")[0])
        tornado_withdrawl_series['date'].append(current_date)
        tornado_withdrawl_series['usage'].append(1)

# plot the tornado series
chart = Plot(title="Tornado.cash Activity Since 2022")
chart.add_data(
    name="Deposits",
    data={
        "x": tornado_deposit_series['date'],
        "y": tornado_deposit_series['usage'],
        "x_axis": "Time",
        "y_axis": "Deposits",
    },
    type="line",
    shape="spline",
    smoothing=4,
)
chart.add_data(
    name="Withdrawls",
    data={
        "x": tornado_withdrawl_series['date'],
        "y": tornado_withdrawl_series['usage'],
        "x_axis": "Time",
        "y_axis": "Deposits",
    },
    type="line",
    shape="spline",
    smoothing=4,
)
chart.render("tornado_deposit_withdrawl_over_time.png")


def get_ens_count(addresses: List[str]) -> List[str]:
    try:
        with mpp.Pool(25) as pool:
            return pool.starmap(get_ens_name, [(addresses[i:i+99],) for i in range(0, len(addresses), 99)])

    except KeyboardInterrupt:
        raise KeyboardInterrupt
    except Exception as e:
        raise e

def get_ens_name(address: str) -> Any:
    ens_names = api.ens.records_by_account(account_addresses=address)
    return len(ens_names)

# get a count of accounts with ENS names
ens_count = get_ens_count(recieving_addresses)
print("A total of {} addresses withdrew from Tornado Cash in 2022, including:\n - {} accounts with ENS names ({}%)\n - {} accounts without ENS names".format(
    len(recieving_addresses),
    sum(ens_count),
    round(sum(ens_count) / len(recieving_addresses) * 100, 2),
    len(recieving_addresses) - sum(ens_count)
))
