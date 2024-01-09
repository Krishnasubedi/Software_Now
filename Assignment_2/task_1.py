import pandas as pd
import re

# List of CSV files
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Output text file
output_file = 'combined_text.txt'

# Initialize an empty list to store cleaned text values
all_texts = []

# Define a regular expression pattern to match only letters and spaces
text_pattern = re.compile(r'[a-zA-Z\s]+')

# Iterate through each CSV file
for file in csv_files:
    try:
        # Read the CSV file with encoding specified
        df = pd.read_csv(file, encoding='utf-8')

        # Get all column names in the DataFrame
        all_columns = df.columns.tolist()

        # Check if either 'SHORT-TEXT' or 'TEXT' column exists in the DataFrame
        if 'SHORT-TEXT' in all_columns or 'TEXT' in all_columns:
            # Select the appropriate column based on availability
            selected_column = 'SHORT-TEXT' if 'SHORT-TEXT' in all_columns else 'TEXT'

            # Extract only text (excluding numbers and special characters)
            cleaned_text = df[selected_column].astype(str).apply(
                lambda x: ' '.join(text_pattern.findall(str(x))))

            # Extend the list with the cleaned text values
            all_texts.extend(cleaned_text.tolist())

        # If neither 'SHORT-TEXT' nor 'TEXT' is present, print an error message
        else:
            print(
                f"Error: 'SHORT-TEXT' and 'TEXT' columns not found in {file}")

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Write the combined cleaned texts to a text file
with open(output_file, 'w', encoding='utf-8') as txt_file:
    for text in all_texts:
        txt_file.write(text + '\n')

print(f"Combined cleaned texts written to {output_file}")
