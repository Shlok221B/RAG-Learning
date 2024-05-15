from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain import OpenAI  

OPEN_AI_KEY = ""

# Access the OpenAI API key
openai_api_key = OPEN_AI_KEY

# Create an instance of the ChatOpenAI class
chatllm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.6, model='gpt-3.5-turbo')

# Define the conversation messages
messages = [
    SystemMessage(content="You are a comedian AI assistant"),
    HumanMessage(content="Please provide some comedy punchlines about AI")
]

# Iterate over the messages and print their content
for message in messages:
    response = chatllm.predict(message.content)
    print(response)