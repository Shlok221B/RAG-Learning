from langchain.chains import LLMChain, SimpleSequentialChain
from langchain import PromptTemplate, OpenAI

OPEN_AI_KEY = ""

# Access the OpenAI API key
openai_api_key = OPEN_AI_KEY

# Create an instance of the OpenAI class
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.6)

# Define the prompt templates
capital_template = PromptTemplate(
    input_variables=['country'],
    template="Please tell me the capital of {country}"
)

famous_template = PromptTemplate(
    input_variables=['capital'],
    template="Suggest some amazing places to visit in {capital}"
)

# Create LLM chains for each step
capital_chain = LLMChain(llm=llm, prompt=capital_template)
famous_chain = LLMChain(llm=llm, prompt=famous_template)

# Combine the chains into a SimpleSequentialChain
chain = SimpleSequentialChain(chains=[capital_chain, famous_chain])

# Run the chain with the input "India"
result = chain.run("Pune")
print(result)