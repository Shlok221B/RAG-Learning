from langchain import OpenAI  
from langchain import HuggingFaceHub



OPEN_AI_KEY = ""
HUGGINGFACEHUB_API_TOKEN = ""



llm_huggingface = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,repo_id="google/flan-t5-large",model_kwargs={"temperature":0,"max_length":64}) 

output = llm_huggingface.predict("Can you tell me the capital of Russia?")
print(output)


#EXPLAINATION#

'''
API Keys:

OPEN_AI_KEY and HUGGINGFACEHUB_API_TOKEN are set with values to authenticate with OpenAI and Hugging Face services respectively. Note: You should avoid sharing API keys publicly.
Initialize the Model:

llm_huggingface is an instance of the HuggingFaceHub class. It initializes a language model using the Hugging Face Hub API token.
repo_id="google/flan-t5-large" specifies the particular model to use from the Hugging Face model repository.
model_kwargs={"temperature":0,"max_length":64} sets parameters for the model. temperature=0 means the output will be deterministic, and max_length=64 sets the maximum length of the generated output.
Model Prediction:

The predict method is called on llm_huggingface with the prompt "Can you tell me the capital of Russia?".
The model processes the input and generates a response, which is then printed.

'''


'''
About Hugging Face
Hugging Face is a company and community known for its contributions to natural language processing (NLP) and machine learning (ML). They provide an extensive platform and repository for sharing and using pre-trained models. Here's an overview:

Model Hub:

The Hugging Face Model Hub is a central place to find, share, and use pre-trained models. It supports various model architectures such as transformers, GPT, BERT, T5, and more.
Models can be fine-tuned on specific tasks and datasets to improve performance for particular applications.
Transformers Library:

Hugging Face provides the Transformers library, which is an open-source library that allows users to easily download and use pre-trained models for various NLP tasks like text classification, translation, summarization, question-answering, and more.
The library supports integration with TensorFlow and PyTorch.
Datasets Library:

The datasets library by Hugging Face offers a wide variety of datasets for different NLP tasks. It simplifies dataset management and preprocessing.
API and Inference:

Hugging Face provides an API that allows users to interact with hosted models via simple HTTP requests. This is particularly useful for deploying models in production environments without needing extensive ML infrastructure.
The Inference API enables quick and easy access to models for tasks like text generation, translation, summarization, and more.

'''