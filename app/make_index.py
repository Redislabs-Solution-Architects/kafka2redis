from utility import data_handler, redis_conn

maker = data_handler.DataHandler()

maker.create_index("transaction_idx", redis_conn)