## Note: 
## To Run the code
## Please change the environment from global ---> local

import streamlit as st
# from langchain_ollama import ChatOllama
from  langchain_groq import ChatGroq

st.set_page_config(
    page_title='Chat Bot',
    page_icon='🤖',
    layout='centered'
)

st.title('🗨 Generative Ai Chatbot')

######## Initiate chat history #######
#Note: using this bec whenever we write any inputs it will refresh the whole page
if "chat_history" not in st.session_state:   
    st.session_state.chat_history = []

## Show chat details
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# initating llms
# llm = ChatOllama(       
#     model= 'gemma:2b',
#     temperature=0.0,        
# )
llm = ChatGroq(
    model = 'llama-3.3-70b-versatile',
    temperature=0.0,        
)
user_prompt = st.chat_input('Ask Chatbot...')

if user_prompt: 
    st.chat_message('user').markdown(user_prompt) # displayig the Query
    st.session_state.chat_history.append({'role':'user','content':user_prompt}) # saving it to chat history
    response = llm.invoke(
        input=[{'role':'system','content':'You are a healful assistant'},*st.session_state.chat_history]
    ) #sending chat history to llms

    assistant_response = response.content 
    st.session_state.chat_history.append({'role':'assistant','content':assistant_response}) #saving response inn chat history

    with st.chat_message("assistant"):  # displaying llmm response 
        st.markdown(assistant_response) 