import os
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from azure.identity import DefaultAzureCredential

openai_api_key = os.getenv("OPENAI_API_KEY")

# # Set up Azure Cosmos DB client
# credential = DefaultAzureCredential()
# client = CosmosClient(endpoint='your_cosmosdb_endpoint', credential=credential)

# # Set up database and container
# database_name = 'your_database_name'
# database = client.get_database_client(database_name)
# container_name = 'your_container_name'
# container = database.get_container_client(container_name)

# # Set up AAD authentication
# tenant_id = 'your_tenant_id'
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'
