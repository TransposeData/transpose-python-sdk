from transpose import Transpose
api = Transpose('transpose_api_key')

# get the most recently expired ENS domain
last_expired = api.ens.records_by_date(type='expiration', order='desc', limit=1)
print(last_expired[0].ens_name)

# pull next recently expired ENS domain
next_last_expired = api.next()
print(next_last_expired[0].ens_name) 