from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

table_service = TableService(account_name='a1sbdatrsg01diag', account_key='Pa4udt0XaZdIJBfX5mnzrw6UqEZLj6r4kvsK1h1K6k04V0A/AYPOk27tGX0Nv7GvXHhslIU6mF82vLpoVXAMvg==')


table_service = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=a1sbdatrsg01diag;AccountKey=Pa4udt0XaZdIJBfX5mnzrw6UqEZLj6r4kvsK1h1K6k04V0A/AYPOk27tGX0Nv7GvXHhslIU6mF82vLpoVXAMvg==;EndpointSuffix=core.windows.net')

#table_service.create_table('')

task = {'PartitionKey': 'Myblock', 'RowKey': '3',
        'api_team': 'Take out the trash'}
table_service.insert_entity('Myblockmobile', task)

'''task = Entity()
task.PartitionKey = 'Myblock'
task.RowKey = '2'
task.api_team = '567'
table_service.insert_entity('tasktable', task)'''