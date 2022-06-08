from matplotlib import pyplot as plt
from transpose import Transpose

api = Transpose('API_KEY')


blocks = api.Block.blocks_by_number(order='desc', limit=500)
fig, ax = plt.subplots()
ax.plot([x.number for x in blocks], [x.gas_used for x in blocks])