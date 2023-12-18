from redis.commands.search.field import NumericField, TagField, TextField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

class CreateIndex(object):

    def create_index(self, client, index_name):
        try: 
            client.ft(index_name).dropindex()
        except:
            pass

        idx_def = IndexDefinition(index_type=IndexType.JSON, prefix=['transaction:'])
        schema = [
            TextField('$.id', as_name='id'),
            TagField('$.type', as_name='type'),
            TagField('$.from_account', as_name='from_account'),
            TagField('$.to_account.*', as_name='to_account'),
            TagField('$.user_id', as_name='user_id'),
            TextField('$.description', as_name='description'),
            NumericField('$.amount', as_name='amount'),
            NumericField('$.date', as_name='date'),
        ]
        result = client.ft(index_name).create_index(schema, definition=idx_def)
        print(result)
        
