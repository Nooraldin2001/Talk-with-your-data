import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import huggingface_pipeline
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import torch

# Load the data
df = pd.read_csv('data/Dataset.csv')
df['Time'] = pd.to_datetime(df['Time'])

# Load Llama 2 model and tokenizer
model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name, model_max_tokens=2048,
                                          token='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',)

model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto",
                                             token='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')

# Create a HuggingFace pipeline
hf_pipeline = pipeline(
    "text-generation",
    model=model, 
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.1,
    top_p=0.95,
    repetition_penalty=1.15
)

# Create a LangChain wrapper for the pipeline
llm = huggingface_pipeline(pipeline=hf_pipeline)

# Create a Pandas DataFrame agent
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

def query_data():
    while True:
        query = input("Enter your question about the data (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        response = agent.run(query)
        print(f"Answer: {response}\n")

# Run the query interface
query_data()