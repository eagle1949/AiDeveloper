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
