import pandas as pd

from datetime import datetime, timedelta, timezone
from transpose.extras import Plot
from transpose import Transpose

api = Transpose('API_KEY', debug=True)

# get all tornado cash deposits since 2022
tornado_deposit_series = {"date": [], "usage": []}
tornado_withdrawl_series = {"date": [], "usage": []}
tornado_deposits = api.bulk_request(api.block.logs_by_date(
    emitted_after=datetime(2022, 1, 1, tzinfo=timezone.utc),
    event_signature='0xa945e51eec50ab98c161376f0db4cf2aeba3ec92755fe2fcd388bdbbb80ff196', limit=500))
current_date = ""

# iterate through the tornado deposits and withdrawals and add them to the tornado series, grouping by date
for log in tornado_deposits:
    if datetime.fromisoformat(log.timestamp.split("T")[0]) == current_date:
        tornado_deposit_series['usage'][-1] += 1
    else:
        current_date = datetime.fromisoformat(log.timestamp.split("T")[0])
        tornado_deposit_series['date'].append(current_date)
        tornado_deposit_series['usage'].append(1)


# plot the tornado series
chart = Plot(title="Tornado.cash Deposits Per Day Since 2022")
chart.add_data(
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
chart.render("tornado.png")
