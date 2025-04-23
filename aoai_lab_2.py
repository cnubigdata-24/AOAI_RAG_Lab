import os
from openai import AzureOpenAI

# 설정
endpoint = "https://aoai-2025-111.openai.azure.com/"
deployment = "gpt-4o-mini"  # Azure에서 배포한 배포 이름
subscription_key = "<your-api-key>"
api_version = "2024-07-18"

# 클라이언트 생성
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# 사용자 입력 받기
query = input("저는 ChatGPT gpt-4o-mini 입니다. 무엇이든지 물어보세요: ")

# 응답 생성
response = client.chat.completions.create(
    model=deployment,  # 배포 이름
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query + "에 대해 답변해주세요."}
    ]
)

# 결과 출력
print("\n답변:", response.choices[0].message.content)
