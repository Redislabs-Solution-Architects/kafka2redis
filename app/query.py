from utility import redis_conn
from redis.commands.search.query import Query

print('\n*** Retrieve All ***')
query = Query('*')
result = redis_conn.ft('transaction_idx').search(query)
print(result)