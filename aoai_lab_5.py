import requests
import json

# Endpoint
endpoint_url = "https://azml-20251115-qdjrv.southcentralus.inference.ml.azure.com/score"

# API Key
api_key = "<your api key>"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Question
data = {
    "chat_history": [
        {
            "inputs": {
                "chat_input": "Hi"
            },
            "outputs": {
                "chat_output": "Hello! How can I assist you today?"
            }
        }
    ],
    "chat_input": "국가 AI 역량 강화방안의 추진 방향과 차별점을 설명해줘. 한글로"
}

json_data = json.dumps(data, ensure_ascii=False)

# Request REST API
response = requests.post(endpoint_url, headers=headers, data=json_data)

print("Response Code:", response.status_code)

try:
    response_json = response.json()
    print("Response:")
    print(json.dumps(response_json, indent=4, ensure_ascii=False))
except json.JSONDecodeError:
    print("JSON Decoding Fail:")
    print(response.text)
