import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="eJustice Bot", page_icon="⚖️")
st.title("⚖️ eJustice – Legal Aid Chatbot")

st.markdown("""
Welcome to **eJustice**, your legal help companion.  
Ask questions like:
- What are my rights?
- How to file an FIR?
- Tell me about RTI or consumer complaints.

---
""")

# Session state to preserve chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your legal question here...")

if user_input:
    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    response = get_response(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
