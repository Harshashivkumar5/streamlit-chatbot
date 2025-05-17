import streamlit as st
st.title("Streamlit chatbot")
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import os

# Set API key from Streamlit secrets or environment variable
os.environ["GOOGLE_API_KEY"] = st.secrets.get("GOOGLE_API_KEY", "AIzaSyBSogoSKFPTkumcCTE_QePkHD4qFSv18fE")

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("💬 Chat with Gemini (LangChain + Streamlit)")

# Display the chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)

# Input box
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Get model response
    result = llm.invoke(user_input)

    # Append the model's reply
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.session_state.messages.append(AIMessage(content=result.content))

    # Display model reply
    st.chat_message("assistant").markdown(result.content)

