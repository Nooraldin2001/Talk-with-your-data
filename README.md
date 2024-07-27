# Talk-with-your-data

## Project Overview

This project is aimed at interacting with your dataset using natural language processing techniques. We are leveraging the spaCy library and the `en_core_web_sm` model to build an application that allows for querying and analyzing the dataset. Additionally, we are working on fine-tuning the LLaMA model using generated data to enhance robustness and versatility.

## File Structure

```
C:\project\
│   .gitignore
│   app.py
│   LICENSE
│   preprocessing.ipynb
│   README.md
│
├───data
│       data.csv
│       Dataset.csv
│       data_generating.py
│
└───models
        train.py
```

## Getting Started

### Setting Up the Environment

1. **Clone the repository**:

    ```sh
    git clone https://github.com/Nooraldin2001/Talk-with-your-data.git
    cd Talk-with-your-data
    ```

2. **Set up a virtual environment**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

### Generating Data

We have a script called `data_generating.py` which is used to generate prompt and response data from the numerical dataset `Dataset.csv`. This data is crucial for fine-tuning the LLaMA model.

To generate the data, run:

```sh
python data/data_generating.py
```

### Running the Application

The main application is in `app.py`. This application uses spaCy to allow you to interact with your data through natural language queries.

To run the application, use:

```sh
python app.py
```

### Fine-Tuning the Model

We are working on fine-tuning the LLaMA model using the data generated by `data_generating.py`. This is done in `train.py`.

Due to some technical issues, the fine-tuning process is currently on hold. For simplicity and because we have a small dataset, we are using the spaCy solution until the fine-tuning process is complete.

To start the fine-tuning process, use:

```sh
python models/train.py
```

## Future Work

Future work involves continuing the fine-tuning process using the generated data and improving the robustness of the application.

## Resources

- [How Large Language Model Work with Numerical Data](https://medium.com/@manoharanagi99/how-large-language-model-work-with-numerical-data-4c90b20792f6)
- [PyReft on GitHub](https://github.com/nicknochnack/PyReft)
- [LLaMA Model on Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
- [PyReft Paper](https://arxiv.org/pdf/2404.03592)
- [LangChain Documentation](https://api.python.langchain.com/en/latest/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html#langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent)

---

Thank you for using Talk-with-your-data! If you have any questions or issues, please feel free to reach out.