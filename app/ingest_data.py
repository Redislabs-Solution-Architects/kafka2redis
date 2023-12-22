from utility.data_handler import DataHandler
from utility import redis_conn

maker = DataHandler()

maker.ingest_data(redis_conn)