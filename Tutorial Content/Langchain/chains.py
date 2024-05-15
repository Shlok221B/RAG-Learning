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

#EXPLAINATION#

'''
Import Required Classes:

LLMChain from langchain.chains
PromptTemplate from langchain
OpenAI from langchain
API Keys:

OPEN_AI_KEY and HUGGINGFACEHUB_API_TOKEN are set with values to authenticate with OpenAI and Hugging Face services respectively.
Access the OpenAI API Key:

The OpenAI API key is assigned to the variable openai_api_key.
Create an Instance of the OpenAI Class:

llm is an instance of the OpenAI class, initialized with the API key and a temperature parameter set to 0.6.
Create a Prompt Template:

prompt_template is an instance of PromptTemplate, which takes a list of input variables (['country']) and a template string. The template string specifies how the input variables will be used in the prompt.
Create an LLMChain:

chain is an instance of LLMChain, which takes the llm instance and the prompt_template. This chain will use the prompt template to generate a complete prompt and pass it to the language model.
Run the Chain:

chain.run("India") runs the chain with the input "India". The run method replaces {country} in the prompt template with "India" and then sends the complete prompt to the OpenAI model to get the response.

'''

'''
How to Use Chains in LangChain
Chains in LangChain can be used to create complex workflows by linking multiple steps. Here's how to use them effectively:

Define the Steps:

Identify the different steps in your workflow. Each step should be a discrete unit of work that can process input and produce output.
Create Prompt Templates:

Define prompt templates for each step. These templates should specify how the input variables will be formatted into prompts.
Instantiate Language Models:

Create instances of the language models you want to use. You can use different models for different steps if needed.
Create LLMChain Instances:

For each step, create an LLMChain instance by providing the language model and the prompt template.
Run the Chains Sequentially:

Execute the chains in the required order, passing the output of one chain as the input to the next chain.
'''