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
