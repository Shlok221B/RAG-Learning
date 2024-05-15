from langchain import OpenAI  
OPEN_AI_KEY = ""
HUGGINGFACEHUB_API_TOKEN = ""


# Access the OpenAI API key
openai_api_key = OPEN_AI_KEY

# Create an instance of the OpenAI class
llm_instance = OpenAI(openai_api_key=openai_api_key, temperature=0.6)

text = "What is capital of India?"

print(llm_instance.predict(text))
