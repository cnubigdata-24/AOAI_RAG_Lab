import openai
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Configure Azure AI Search
search_service_name = "az-ai-search-001"
search_api_key = "<your search api key>"
index_name = "azureblob-index"

# Configure OpenAI API
openai.api_key = "<your api key>"
openai.azure_endpoint = "https://aoai-instance-001.openai.azure.com"
openai.api_type = "azure"
openai.api_version = "2024-07-18"

# Initialize SearchClient
search_endpoint = f"https://{search_service_name}.search.windows.net"
search_client = SearchClient(endpoint=search_endpoint, 
                             index_name=index_name, 
                             credential=AzureKeyCredential(search_api_key))

def search_documents(query):
    """Retrieve relevant documents from Azure AI Search"""
    search_results = search_client.search(query)
    retrieved_docs = [result['description'] for result in search_results if 'description' in result]
    
    if not retrieved_docs:
        return ["관련 정보를 찾을 수 없습니다."]
    return retrieved_docs

def generate_answer(query, retrieved_docs):
    """Generate an AI answer using OpenAI and retrieved search results"""
    context = "\n".join(retrieved_docs)
    
    response = openai.chat.completions.create(
        model="my-gpt-4o-mini",  # Model Name
        messages=[
            {"role": "system", "content": "너는 제품 정보 제공 AI야."},
            {"role": "user", "content": f"질문: {query}\n\n참고 자료:\n{context}"}
        ],
        temperature=0.7,
        max_tokens=800
    )
    
    return response.choices[0].message.content

# Test
user_query = "방수 기능이 뛰어난 텐트를 추천해줘"
retrieved_docs = search_documents(user_query)  # 1. Search Document
answer = generate_answer(user_query, retrieved_docs)  # 2. Create OpenAI Response based on Search Result
print("AI 응답:", answer)
