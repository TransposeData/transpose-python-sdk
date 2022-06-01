from transpose import Transpose

api = Transpose('transpose_api_key')

# get the most recently expired ENS domain
last_expired = api.ENS.records_by_date(type='expiration', order='desc', limit=1)

print(last_expired.ens_name)

# pagination !
next_last_expired = api.ENS.next()

print(next_last_expired.ens_name) 

last_expired = api.ENS.previous()

# Response:
# 
# >>> 'jbecker.eth'
# >>> 'alex101.eth'
# >>> 'jbecker.eth'