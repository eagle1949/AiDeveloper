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

# import requests

# url = "https://api.siliconflow.cn/v1/chat/completions"

# payload = {
#     "model": "Qwen/QwQ-32B",
#     "messages": [
#         {
#             "role": "user",
#             "content": "What opportunities and challenges will the Chinese large model industry face in 2025?"
#         }
#     ]
# }
# headers = {
#     "Authorization": "Bearer [your_token_here]",
#     "Content-Type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.json())


import openai

openai.api_base = "http://localhost:1234/v1"  # LM Studio 的本地地址
openai.api_key = "lm-studio"  # 随便写一个 key，它不会校验

response = openai.ChatCompletion.create(
    model="qwen1.5-7b-chat-q4",  # 你在 LM Studio 里加载的模型名称（注意大小写）
    messages=[
        {"role": "system", "content": "你是一个资深ai架构师，python架构师，擅长模块化设计和项目分层。同时精通ai开发和应用。你乐于助人，回答的问题要详细且专业。会把技术每个细节都讲解清楚。"},
        {"role": "user", "content": "我需要开发一个ai应用，是Ai私人助手，需要学习的技术有哪些，才能做出这个应用。"},
    ],
    temperature=0.7
)

print(response["choices"][0]["message"]["content"])
