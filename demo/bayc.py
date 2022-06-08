import os
import numpy as np
from transpose import Transpose
from demo.lib.gini import gini


# initialize SDK
TRANSPOSE_KEY = os.environ['TRANSPOSE_KEY']
api = Transpose(TRANSPOSE_KEY)
bayc_contract = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"


# Cycle through pages, collect all holders
# Note: you'll need to add a sleep to avoid hitting the rate limit in the free tier
all_holders = []
all_holders.extend(api.NFT.owners_by_contract_address(bayc_contract, 500))
while(api._next):
    all_holders.extend(api.NFT.next())


# Let's check to see what we've got...
print("Number of BAYC tokens: {}\n".format(len(all_holders)))


# Add up owner totals
number_owned_per_holder = {}
for holder in all_holders:
    if holder.owner in number_owned_per_holder:
        number_owned_per_holder[holder.owner] += 1
    else:
        number_owned_per_holder[holder.owner] = 1
sorted_holders = sorted(number_owned_per_holder.items(), key=lambda x: x[1], reverse=True)


# Let's check out what we've got
print("Top 5 BAYC holders own {} BAYCs".format(sum([x[1] for x in sorted_holders[:5]])))
for i in range(5):

    # Print ENS name if we can get it, otherwise just the address
    holder_name = api.ENS.primary_ens_records_by_account(sorted_holders[i][0])
    if hasattr(holder_name, "ens_name"):
        print("{}{} owns {} BAYC tokens".format(holder_name.ens_name, " " * (15 - len(holder_name.ens_name)), sorted_holders[i][1]))
    else:
        print("{} owns {} BAYC tokens".format(sorted_holders[i][0][:12]+"...", sorted_holders[i][1]))

print("\nGini coefficient: {}".format(gini(np.array([x[1] for x in sorted_holders]))))