from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()
initial_message = [
        {"role": "system", "content": "You are a Trip planner in India. You are an expert in Indian Tourism, Locations, Food, Events, Hotels, etc. You are able to guide users to plan their vacation to India. You should respond professionally. Your name is Gafoor, NickName Gafoorkka. Response should be 200 or less words. Always ask questions to the user and help them to plan their trip. Finally, give them a day-wise itinerary. Deal with the user professionally."},
        {
            "role": "assistant",
            "content": "Hello, I am Gafoorkka, Your Expert Indian Trip Planner. How can I help you?"
        }
    ]

def get_response_llm(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = initial_message

    st.title("Indian Trip Assistant")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

user_message = st.chat_input("How are you planning to travel?")
if user_message:
   new_message = {
       "role": "user", "content": user_message
   }
   st.session_state.messages.append(new_message)
   with st.chat_message(new_message["role"]):
       st.write(new_message["content"])
   response = get_response_llm(st.session_state.messages)
   if response:
       response_message = {
           "role": "assistant", "content": response
       }
       st.session_state.messages.append(response_message)
       with st.chat_message(response_message["role"]):
           st.write(response_message["content"])