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
