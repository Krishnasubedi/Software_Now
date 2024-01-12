
"""
Group Members:
[Name: Krishna Prasad Subedi] -[ID: S371919]
[Name: Saurav Ghimire] -[ID: S375203]
[Name: Rabi Acharya] -[ID: S372977]
[Name: Ranjit Kunwar] -[ID: S375204]
[Name: Muhammad Waqas Ashraf]- [ID: S374681]
"""

import re
import csv
from collections import Counter


def count_words(text):
    # Use regular expression to extract words from the text
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


def main():
    # Read text from a .txt file
    file_path = 'combined_text.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Count word occurrences
    word_counts = count_words(text)

    # Get the top 30 most common words
    top_30_words = word_counts.most_common(30)

    # Store the results in a CSV file

    csv_file_path = 'top_30_words_counts.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header
        csv_writer.writerow(['Word', 'Count'])

        # Write data
        for word, count in top_30_words:
            csv_writer.writerow([word, count])

    print(f'Top 30 words and their counts are saved to: {csv_file_path}')


if __name__ == "__main__":
    main()
