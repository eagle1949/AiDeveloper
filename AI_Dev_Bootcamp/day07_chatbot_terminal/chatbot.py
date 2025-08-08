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
