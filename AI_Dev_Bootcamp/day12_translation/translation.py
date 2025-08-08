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
