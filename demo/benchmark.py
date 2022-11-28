from datetime import datetime
from transpose import Transpose

from datetime import datetime
from transpose.extras import Plot
api = Transpose('API_KEY')

def run_benchmark(page_size: int):
    api.block.blocks_by_number(order='desc', limit=page_size)
    runs = []
    
    for _ in range(10):
        start = datetime.now()
        try:
            api.block.blocks_by_number(order='desc', limit=page_size)
        except Exception:
            pass
        end = datetime.now()
        
        ms_per_record = (end - start).total_seconds() * 1000 / page_size
        runs.append(ms_per_record)
    
    print(f'Page size: {page_size}, Avg. ms per record: {sum(runs) / len(runs)} w/ {len(runs)} runs')
    return sum(runs) / len(runs)

results = []
for i in range(100, 10000, 100):
    results.append(run_benchmark(i))
    
chart = Plot(title="Page size benchmark")

chart.add_data(
    data={
        "x": list(range(100, 10000, 100)),
        "y": results,
        "x_axis": "PAGE_SIZE",
        "y_axis": "MS PER RECORD",
    },
    type="bar",
    )

chart.render("benchmark.png")