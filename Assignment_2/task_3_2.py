from transformers import AutoTokenizer
from collections import Counter
import re


def count_unique_tokens(text, model_name):
    # Load AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the text
    tokens = tokenizer.tokenize(
        tokenizer.encode(text, add_special_tokens=False))

    # Count token occurrences
    token_counts = Counter(tokens)

    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    return top_30_tokens


def main():
    # Read text from a .txt file
    file_path = 'combined_text.txt'  # Replace with your actual file path
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Model name (replace with the desired pre-trained model from Hugging Face)
    model_name = "bert-base-uncased"

    # Count unique tokens
    top_30_tokens = count_unique_tokens(text, model_name)

    # Print the results
    print("Top 30 tokens and their counts:")
    for token, count in top_30_tokens:
        print(f"{token}: {count}")


if __name__ == "__main__":
    main()
