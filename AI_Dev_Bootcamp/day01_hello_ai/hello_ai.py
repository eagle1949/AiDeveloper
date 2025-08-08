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
