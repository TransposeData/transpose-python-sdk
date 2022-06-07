from matplotlib import pyplot as plt
from transpose import Transpose

api = Transpose('HT1XOCJ3Bw6jRRWZU8fSuanhyWdhJQXxaFdueiBz')


blocks = api.Block.blocks_by_number(order='desc', limit=500)
fig, ax = plt.subplots()
ax.plot([x.number for x in blocks], [x.gas_used for x in blocks])