This project is a conversational AI chatbot built using LangChain and deployed with Streamlit. The chatbot leverages large language models (LLMs) via the OpenRouter API to provide intelligent, context-aware responses to user queries.

Features:
Conversational Memory: Remembers previous messages in the session for more natural, context-aware conversations.
Modern Web Interface: User-friendly chat UI built with Streamlit, featuring a custom color palette for a visually appealing experience.
LLM Powered: Uses the mistralai/mistral-7b-instruct model (or similar) via OpenRouter for high-quality responses.
Easy Deployment: Ready to deploy on Streamlit Community Cloud or other platforms.
Customizable: Easily change the model, color theme, or add new features (like tools, APIs, or user personalization).

How it Works:
The user enters a message in the chat interface.
The message, along with the conversation history, is sent to the language model using LangChain’s ConversationChain.
The model generates a context-aware response, which is displayed in the chat.
All interactions are shown in a modern, chat-style web interface.

Tech Stack:
Python
Streamlit (for the web UI)
LangChain (for LLM orchestration and memory)
OpenRouter API (for LLM access)
