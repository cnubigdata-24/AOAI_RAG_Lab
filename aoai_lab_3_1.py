# pip install azure-search-documents

from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# SEARCH_SERVICE_NAME
search_service_name = "<your ai search service name>"

#SEARCH_API_KEY"
search_api_key = "<your api key>"

# INDEX_NAME
index_name = "azureblob-index" 

# Initialize SearchClient
search_endpoint = f"https://{search_service_name}.search.windows.net"
search_client = SearchClient(endpoint=search_endpoint, \
                             index_name=index_name, \
                             credential=AzureKeyCredential(search_api_key))

# Execute search query
query = "방수 텐트"
search_results = search_client.search(query)

# Print search results
for result in search_results:
    print(f"Product Name: {result['name']}")
    print(f"Category: {result['category']}")
    print(f"Brand: {result['brand']}")
    print(f"Description: {result['description']}")
    print("-" * 50)
