import pandas as pd

from datetime import datetime, timedelta, timezone
from transpose.extras import Plot
from transpose import Transpose

api = Transpose('API_KEY')

mined_after=(datetime.now() - timedelta(minutes=60)).astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
historical_blocks = api.block.blocks_by_date(mined_after=mined_after, order="desc", limit=500)
historical_base_gas_prices = [block.base_fee_per_gas / 1000000000 for block in historical_blocks]

chart = Plot(title="Hourly Gas Prices on Ethereum")

chart.add_data(
    data={
        "x": pd.date_range(historical_blocks[0].timestamp, historical_blocks[-1].timestamp, periods=len(historical_base_gas_prices)),
        "y": historical_base_gas_prices,
        "x_axis": "Time",
        "y_axis": "Gas Price (Gwei)",
    },
    smoothing=1,
    type="line",
    shape="spline",
    )

chart.render("a.png")