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
