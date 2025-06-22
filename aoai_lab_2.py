import os
from openai import AzureOpenAI

# 설정
endpoint = "https://aoai-2025-111.openai.azure.com/"
subscription_key = "<your api key>"
api_version = "2024-12-01-preview"

# 클라이언트 생성
client = AzureOpenAI(
    api_key=subscription_key,
    api_version=api_version,
    azure_endpoint=endpoint,
)

# 사용자 입력 받기
query = input("저는 ChatGPT gpt-4o-mini 입니다. 무엇이든지 물어보세요: ")

# 응답 생성
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Azure 배포 이름
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
    ],
    temperature=1.0,
    top_p=1.0
)

# 결과 출력
print("\n답변:", response.choices[0].message.content)
