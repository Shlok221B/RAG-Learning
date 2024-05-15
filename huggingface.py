from langchain import OpenAI  
from langchain import HuggingFaceHub

OPEN_AI_KEY = ""
HUGGINGFACEHUB_API_TOKEN = ""



llm_huggingface = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64}) 

output = llm_huggingface.predict("Can you tell me the capital of Russia?")
print(output)
