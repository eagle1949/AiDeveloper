# import requests

# response =requests.get('https://api.github.com')

# print(response.status_code)
# print(response.json())


# from PIL import Image

# img = Image.open(r'e:\learn\AiDeveloper\01 python\example.png')
# img = img.resize((100, 100))
# img.save(r'e:\learn\AiDeveloper\01 python\resized_example.png')


# from rich.console import Console
# # console = Console()
# # console.print("Hello [bold magenta]World[/bold magenta]!", style="bold green")


# import openai

# openai.api_key = "your-api_key_here"

# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         {"role": "user", "content": "写一个关于AI的故事"}
#     ]
# )

# print(response)
# 这里的 "your-api_key_here" 替换为你的 OpenAI API 密

import requests

url = "https://api.siliconflow.cn/v1/chat/completions"

payload = {
    "model": "Qwen/QwQ-32B",
    "messages": [
        {
            "role": "user",
            "content": "What opportunities and challenges will the Chinese large model industry face in 2025?"
        }
    ]
}
headers = {
    "Authorization": "Bearer [your_token_here]",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
