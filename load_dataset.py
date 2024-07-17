import json
from datasets import Dataset

# Load the extracted data
with open('langchain_data.json', 'r') as f:
    raw_data = json.load(f)

# Process the data (remove duplicates and filter low-quality content)
unique_data = {entry['content']: entry for entry in raw_data}.values()

# Create the Hugging Face dataset
data_dict = {
    "text": [entry['content'] for entry in unique_data],
    "url": [entry['url'] for entry in unique_data]
}

dataset = Dataset.from_dict(data_dict)

# Save the dataset locally and optionally push to Hugging Face Hub
dataset.save_to_disk('processed_langchain_dataset')
# dataset.push_to_hub("your-username/your-dataset-name")
