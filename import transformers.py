from transformers import AutoTokenizer
from collections import Counter

def count_and_display_top_tokens(file_path, model_name, top_n=30):
    # Load the AutoTokenizer for the specified model
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Read text from the given file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text using the AutoTokenizer
    tokens = tokenizer.tokenize(text, add_special_tokens=True)

    # Count the occurrences of each token
    token_counts = Counter(tokens)

    # Display the top N tokens
    print(f"Top {top_n} Words:")
    for token, count in token_counts.most_common(top_n):
        print(f"{token}: {count} occurrences")

# Example usage
file_path = r'C:\Users\achar\OneDrive\Desktop\num.py\myenv\output.txt'
model_name = 'bert-base-uncased'  
count_and_display_top_tokens(file_path, model_name)


