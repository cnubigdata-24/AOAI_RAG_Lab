from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

# 1. Azure AI Search 설정
search_service_name = "<azure ai search name>"
search_api_key = "<azure search api key>"
index_name = "<azure search index name>"
search_endpoint = f"https://{search_service_name}.search.windows.net"

search_client = SearchClient(
    endpoint=search_endpoint,
    index_name=index_name,
    credential=AzureKeyCredential(search_api_key)
)

# 2. Azure OpenAI 설정
client = AzureOpenAI(
    api_key="<ai foundry: aoai api key>",
    api_version="<ai foundry: aoai api version>",
    azure_endpoint="<ai foundry: aoai endpoint url>"
)

# 3. 사용자 질문
query = "방수 기능이 뛰어난 텐트를 3개 추천해줘"

# 4. 검색 실행
search_results = search_client.search(query)
retrieved_docs = []

for result in search_results:
    # 각 검색 결과에서 제품 설명 추출
    doc = f"- 제품명: {result['name']}, 브랜드: {result['brand']}, 설명: {result['description']}"
    retrieved_docs.append(doc)

if not retrieved_docs:
    retrieved_docs = ["검색된 제품 정보가 없습니다."]

# 5. 검색 결과를 문맥으로 넣고 OpenAI에게 답변 생성 요청
context = "\n".join(retrieved_docs)

response = client.chat.completions.create(
    model="my-gpt-4o-mini",  # Azure에 배포된 모델 이름
    messages=[
        {"role": "system", "content": "너는 캠핑 용품 전문가 AI야. 사용자에게 제품을 설명하고 추천해줘."},
        {"role": "user", "content": f"질문: {query}\n\n검색된 제품 정보:\n{context}"}
    ],
    temperature=0.7,
    max_tokens=800
)

# 6. 결과 출력
print("\nAI 응답:\n", response.choices[0].message.content)
