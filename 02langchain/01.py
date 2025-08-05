from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(
    openai_api_base="http://localhost:1234/v1",  # LM Studio 本地地址
    openai_api_key="lm-studio",                  # 随便写一个 key
    model_name="qwen1.5-7b-chat-q4",             # 模型名称
    temperature=0.7
)

messages = [
    SystemMessage(content="你是一个有帮助的 AI 助手"),
    HumanMessage(content="openai历史"),
]

response = llm(messages)
print(response.content)