import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

# Set your OpenRouter API key and base
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

# Initialize LLM and memory
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7
)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

st.title("🤖 LangChain Chatbot")
st.write("Ask me anything!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message...", key="input")

if st.button("Send") and user_input:
    response = conversation.predict(input=user_input)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", response))
    st.rerun()

for speaker, message in st.session_state.chat_history:
    if speaker == "user":
        with st.chat_message("user"):
            st.markdown(f"**You:** {message}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**Bot:** {message}")
