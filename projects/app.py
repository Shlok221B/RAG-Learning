from langchain.llms import OpenAI
import streamlit as st

OPEN_AI_KEY = ""

#Function to load OPEN AI models and get response

def get_open_ai_response(question):
    llm = OpenAI(openai_api_key=OPEN_AI_KEY,temperature=0.5)
    response = llm(question)
    return response

#Initializing Streamlet App
    
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ",key=input)
response = get_open_ai_response(input)

submit = st.button("ASK the Question")

## IF ASK button is clicked

if submit:
    st.subheader("The Response is ")
    st.write(response)