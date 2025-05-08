import streamlit as st

st.title("CHAT WINDOW")

with st.chat_message("assistant"):
    st.write("Hello I am your AI assistant, how can I help you today?")

with st.chat_message("user"):
    st.markdown("I am Planing a vacation to Dubai.")

message = st.chat_input("How you are planning to travel?")

if message:
    with st.chat_message("user"):
        st.markdown(message)

    with st.chat_message("assistant"):
        st.markdown("I can help you with that. What are the dates of your travel?")
