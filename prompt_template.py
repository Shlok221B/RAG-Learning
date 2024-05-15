from langchain.chains import LLMChain
from langchain import PromptTemplate
from langchain import OpenAI  
OPEN_AI_KEY = ""
HUGGINGFACEHUB_API_TOKEN = ""


# Access the OpenAI API key
openai_api_key = OPEN_AI_KEY

# Create an instance of the OpenAI class
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.6)


prompt_template = PromptTemplate(input_variables=['country'],
template = "Tell me the capital of this this {country}")

chain = LLMChain(llm=llm,prompt=prompt_template)
print(chain.run("India"))
