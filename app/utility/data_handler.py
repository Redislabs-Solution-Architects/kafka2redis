import json

from redis.commands.search.field import NumericField, TagField, TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

class DataHandler(object):

    def create_index(self, index_name, redis_client):
        try: 
            info = redis_client.ft(index_name).info()
            if info is not None:
                print("Index already exists\n")
                return
        except:
            pass

        idx_def = IndexDefinition(index_type=IndexType.JSON, prefix=['transaction:'])
        schema = [
            TextField('$.id', as_name='id'),
            TagField('$.from_account', as_name='from_account'),
            TagField('$.to_account.*', as_name='to_account'),
            TagField('$.user_id', as_name='user_id'),
            TextField('$.description', as_name='description'),
            NumericField('$.amount', as_name='amount'),
            NumericField('$.date', as_name='date'),
        ]
        result = redis_client.ft(index_name).create_index(schema, definition=idx_def)
        print(result)
        

    def ingest_data(self, redis_client):
        # Opening JSON file
        f = open('app/resources/test_data.json')
        
        # returns JSON object as a dictionary
        data = json.load(f)
        
        # Iterating through the json list
        for item in data:
            print(item)
            key = f'transaction:{item["id"]}'
            date = item["date"]
            redis_client.json().set(key, "$", item)
        
        # Closing file
        f.close()
