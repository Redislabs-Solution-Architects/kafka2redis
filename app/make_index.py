from utility.create_index import CreateIndex
from utility import redis_conn

maker = CreateIndex()

maker.create_index(redis_conn, 'transaction_idx')