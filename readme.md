# Langchain Dataset

## Description
This dataset contains text data extracted from [Langchain Documentation](https://python.langchain.com/). It has been cleaned and processed for LLM fine-tuning.

## Source
- URL: https://python.langchain.com/

## Preprocessing
- HTML tags removed
- Duplicate entries removed
- Low-quality content filtered out
- Only specific HTML elements (paragraphs, headers, list items) are included
- Very short paragraphs are excluded
- URL patterns and depth limitations applied to ensure relevance

## Dataset Creation
the [instruct dataset](https://github.com/mshojaei77/langchain_crawler/blob/main/instruct_dataset.json) was created by `Gemeni 1.5 pro` using this system prompt
```
You are a data engineer tasked with creating an "instruction tuning" dataset in Alpaca format from unstructured data. Your dataset should consist of instruction, input, and output components. The instruction should be a clear and concise command or question, the input is the data or context needed to answer the instruction, and the output is the expected response or result.

Your task is to extract relevant information from the unstructured data and transform it into a structured format that follows the Alpaca format. This may involve parsing, cleaning, and organizing the data, as well as generating appropriate instructions and outputs.
```

## Usage
This dataset can be used for fine-tuning language models on technical documentation data.

## License
Ensure that the data is used in compliance with copyright laws and the source website's terms of service.
