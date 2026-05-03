import streamlit as st
from openai import OpenAI
import os
from datetime import datetime


client = OpenAI(api_key="        ")


st.set_page_config(page_title="ChatBot", page_icon="🤖", layout="wide")


st.markdown("""
<style>
.main-title {
    background: rgba(128, 128, 128, 0.7);
    color: white;
    text-align: center;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 20px;
    font-size: 38px;
}
.stChatMessage.user {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    color: white;
    margin-left: auto;
}
.stChatMessage.assistant {
    background: #f1f3f4;
    color: #333;
    margin-right: auto;
}
.chat-box {
    max-height: 70vh;
    overflow-y: auto;
    padding-right: 8px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🤖 My Chatbot</div>", unsafe_allow_html=True)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def get_response(user_inp):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                *st.session_state.chat_history,
                {"role": "user", "content": user_inp},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ something went wrong: {e}"


with st.sidebar:
    st.header("Chat History")
    if st.session_state.chat_history:
        for msg in reversed(st.session_state.chat_history):
            ts = msg.get("time", "")
            role = "You" if msg["role"] == "user" else "Assistant"
            st.markdown(f"**{role} ({ts})**: {msg['content']}")
    else:
        st.info("No messages yet.")


chat_container = st.container()


with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...")
    submit = st.form_submit_button("Send")

if submit and user_input:
    timestamp = datetime.now().strftime("%H:%M %p")
    
    st.session_state.chat_history.append({"role": "user", "content": user_input, "time": timestamp})
   
    response = get_response(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": response, "time": timestamp})


with chat_container:
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        role = msg["role"]
        content = msg["content"]
        timestamp = msg.get("time", "")
        display_text = f"{content}\n*{timestamp}*" if timestamp else content
        with st.chat_message("user" if role == "user" else "assistant"):
            st.markdown(display_text)
    st.markdown('</div>', unsafe_allow_html=True)
