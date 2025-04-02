# pip install openai

import openai

openai.api_key = "<your api key>"
openai.azure_endpoint = "https://aoai-instance-001.openai.azure.com"
openai.api_type = "azure"
openai.api_version = "2024-07-18"

query = input("저는 ChatGPT gpt-4o-mini 입니다. 무엇이든지 물어보세요: ")

result = openai.chat.completions.create(
model="my-gpt-4o-mini",  # engine = "deployment_name"
messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query + "에 대해 답변해주세요."}
    ]
)

print(result.choices[0].message.content)
