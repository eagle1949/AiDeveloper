import os
import zipfile

# 定义项目根目录
ROOT_DIR = "AI_Dev_Bootcamp"

# 各天目录和文件及内容定义
PROJECT_FILES = {
    "day01_hello_ai": {
        "README.md": "# Day 1 - Hello AI\n\n调用 OpenAI API，返回简单问答示例。\n\n运行:\n\n```\npython hello_ai.py\n```",
        "hello_ai.py": '''\
import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":"介绍一下人工智能"}]
    )
    print("AI回答：", response.choices[0].message.content)

if __name__ == "__main__":
    main()
'''
    },
    "day02_sentiment_analysis": {
        "README.md": "# Day 2 - 文本情感分析\n\n使用简易的IMDb影评样本做情感分类。\n\n运行:\n\n```\npython sentiment.py\n```",
        "sentiment.py": '''\
import pandas as pd

def main():
    df = pd.read_csv("datasets/imdb_sample.csv")
    print("前5条数据：")
    print(df.head())
    pos = df[df.sentiment == "positive"]
    neg = df[df.sentiment == "negative"]
    print(f"正面评论数: {len(pos)}，负面评论数: {len(neg)}")

if __name__ == "__main__":
    main()
''',
        "imdb_sample.csv": '''\
review,sentiment
"I love this movie, it's amazing!",positive
"This was a terrible film.",negative
"Quite enjoyable, would watch again.",positive
"Not my type, boring plot.",negative
"A masterpiece, highly recommended.",positive
'''
    },
    "day03_news_classifier": {
        "README.md": "# Day 3 - 新闻分类\n\n使用简易 AG News 子集做文本分类演示。\n\n运行:\n\n```\npython news_classifier.py\n```",
        "news_classifier.py": '''\
import pandas as pd

def main():
    df = pd.read_csv("datasets/agnews_sample.csv")
    print("新闻数据示例：")
    print(df.head())

if __name__ == "__main__":
    main()
''',
        "agnews_sample.csv": '''\
title,category
"Stocks rally as market rebounds",Business
"New tech gadget released today",Science/Tech
"Sports team wins championship",Sports
"Political debate heats up",World
"Movie premiere breaks records",Entertainment
'''
    },
    "day04_text_generation": {
        "README.md": "# Day 4 - 文本生成\n\n使用 OpenAI GPT API 生成文本。\n\n运行:\n\n```\npython text_gen.py\n```",
        "text_gen.py": '''\
import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    openai.api_key = api_key
    prompt = "未来科技的发展趋势是什么？"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    print("生成文本：")
    print(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
'''
    },
    "day05_cnn_image_classification": {
        "README.md": "# Day 5 - 简单 CNN 图像分类\n\n使用 PyTorch 实现 CIFAR-10 子集上的简单卷积神经网络。\n\n运行:\n\n```\npython cnn_train.py\n```",
        "cnn_train.py": '''\
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim

def main():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True)

    class SimpleCNN(nn.Module):
        def __init__(self):
            super(SimpleCNN, self).__init__()
            self.conv1 = nn.Conv2d(3, 6, 5)
            self.pool = nn.MaxPool2d(2, 2)
            self.conv2 = nn.Conv2d(6, 16, 5)
            self.fc1 = nn.Linear(16 * 5 * 5, 120)
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 10)

        def forward(self, x):
            x = self.pool(torch.relu(self.conv1(x)))
            x = self.pool(torch.relu(self.conv2(x)))
            x = x.view(-1, 16 * 5 * 5)
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = self.fc3(x)
            return x

    net = SimpleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

    for epoch in range(2):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            if i % 2000 == 1999:
                print(f"[{epoch + 1}, {i + 1}] loss: {running_loss / 2000:.3f}")
                running_loss = 0.0

    print("训练完成")

if __name__ == "__main__":
    main()
'''
    },
    "day06_speech_to_text": {
        "README.md": "# Day 6 - 语音转文字\n\n使用 OpenAI Whisper API 进行短语音转录。\n\n运行:\n\n```\npython speech_to_text.py\n```",
        "speech_to_text.py": '''\
import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    openai.api_key = api_key
    audio_file = open("sample_audio.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print("转录结果：")
    print(transcript.text)

if __name__ == "__main__":
    main()
'''
    },
    "day07_chatbot_terminal": {
        "README.md": "# Day 7 - 终端聊天机器人\n\n使用 OpenAI API 实现简单多轮聊天。\n\n运行:\n\n```\npython chatbot.py\n```",
        "chatbot.py": '''\
import os
import openai

def chat():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    openai.api_key = api_key
    history = []
    print("输入 exit 退出聊天")
    while True:
        prompt = input("你: ")
        if prompt.lower() == "exit":
            break
        history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history
        )
        answer = response.choices[0].message.content
        print("AI:", answer)
        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    chat()
'''
    },
    "day08_text_summarization": {
        "README.md": "# Day 8 - 文本摘要\n\n使用 OpenAI API 进行文本摘要演示。\n\n运行:\n\n```\npython summarization.py\n```",
        "summarization.py": '''\
import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    openai.api_key = api_key
    text = ("人工智能是计算机科学的一个分支，专注于构建能够执行智能任务的系统。"
            "这些任务包括视觉识别、语言处理和决策等。")
    prompt = f"请为以下内容写一个简短摘要：{text}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )
    print("摘要结果：")
    print(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
'''
    },
    "day09_speech_qa": {
        "README.md": "# Day 9 - 语音问答\n\n实现语音输入和文本问答的结合。\n\n运行:\n\n```\npython speech_qa.py\n```",
        "speech_qa.py": '''\
import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return

    print("示例不包含真实语音识别流程，仅模拟问答。")
    while True:
        q = input("请输入你的问题（exit退出）：")
        if q.lower() == "exit":
            break
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": q}]
        )
        print("回答：", response.choices[0].message.content)

if __name__ == "__main__":
    main()
'''
    },
    "day10_image_captioning": {
        "README.md": "# Day 10 - 图片描述生成\n\n使用简单的图片描述模型。\n\n运行:\n\n```\npython image_caption.py\n```",
        "image_caption.py": '''\
print("Day 10 的图片描述生成暂时示例版，后续可用图像模型扩展。")
'''
    },
    "day11_multimodal_search": {
        "README.md": "# Day 11 - 多模态搜索\n\n示例展示文本和图片的向量检索基础。\n\n运行:\n\n```\npython multimodal_search.py\n```",
        "multimodal_search.py": '''\
print("Day 11 多模态搜索示例，未来可接入向量数据库。")
'''
    },
    "day12_translation": {
        "README.md": "# Day 12 - 机器翻译\n\n使用 OpenAI 翻译 API 演示。\n\n运行:\n\n```\npython translation.py\n```",
        "translation.py": '''\
import os
import openai

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("请设置环境变量 OPENAI_API_KEY")
        return
    text = "Hello, how are you?"
    prompt = f"请将以下英文翻译成中文：{text}"
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )
    print("翻译结果：")
    print(response.choices[0].text.strip())

if __name__ == "__main__":
    main()
'''
    },
    "day13_web_chatbot": {
        "README.md": "# Day 13 - Web 端聊天机器人\n\n使用 Flask 搭建简单聊天接口。\n\n运行:\n\n```\npython web_chatbot.py\n```",
        "web_chatbot.py": '''\
from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(port=5000)
'''
    },
    "day14_streamlit_app": {
        "README.md": "# Day 14 - Streamlit 综合应用\n\n用 Streamlit 搭建简单聊天 UI。\n\n运行:\n\n```\nstreamlit run streamlit_app.py\n```",
        "streamlit_app.py": '''\
import streamlit as st
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Day 14 - AI 聊天应用")

if "history" not in st.session_state:
    st.session_state.history = []

def chat_api(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.history + [{"role":"user","content":user_input}]
    )
    return response.choices[0].message.content

user_input = st.text_input("请输入消息：")
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    answer = chat_api(user_input)
    st.session_state.history.append({"role": "assistant", "content": answer})

for chat in st.session_state.history:
    if chat["role"] == "user":
        st.markdown(f"**你:** {chat['content']}")
    else:
        st.markdown(f"**AI:** {chat['content']}")
'''
    },
    "datasets": {
        "imdb_sample.csv": '''\
review,sentiment
"I love this movie, it's amazing!",positive
"This was a terrible film.",negative
"Quite enjoyable, would watch again.",positive
"Not my type, boring plot.",negative
"A masterpiece, highly recommended.",positive
''',
        "agnews_sample.csv": '''\
title,category
"Stocks rally as market rebounds",Business
"New tech gadget released today",Science/Tech
"Sports team wins championship",Sports
"Political debate heats up",World
"Movie premiere breaks records",Entertainment
'''
    },
    "requirements.txt": '''\
openai
pandas
torch
torchvision
flask
streamlit
'''
}

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    ROOT_DIR = "AI_Dev_Bootcamp"
    print(f"正在生成项目文件到 {ROOT_DIR} ...")
    for folder, files in PROJECT_FILES.items():
        # requirements.txt 不在子文件夹
        if folder == "requirements.txt":
            write_file(os.path.join(ROOT_DIR, folder), files)
            print(f"写入文件: {os.path.join(ROOT_DIR, folder)}")
            continue

        for filename, content in files.items():
            file_path = os.path.join(ROOT_DIR, folder, filename)
            write_file(file_path, content)
            print(f"写入文件: {file_path}")

    # 打包成 zip 文件
    zip_name = ROOT_DIR + ".zip"
    print(f"开始打包成 {zip_name} ...")
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(ROOT_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, ROOT_DIR)
                zipf.write(file_path, arcname)
    print("打包完成！")

if __name__ == "__main__":
    main()
