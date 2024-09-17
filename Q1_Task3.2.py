# Question 1 Task 3 Part 2
import pandas as pd
from collections import Counter
from transformers import AutoTokenizer


# Used to find the top 30 tokens using autotokenizer and stores them on a .csv file
# Arguments are the input path, output path and the model used
def top_30 (read_path, output_path, model ='dmis-lab/biobert-v1.1'):

    # Loads tokenizer from the identified model
    tokenizer = AutoTokenizer.from_pretrained (model)

    # Opens the text file using a 'with' statement to ensure it closes properly on completion
    try:
        # Read the text file and associate it with the 'text' variable
        with open(read_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: The file {read_path} was not found.")
        return
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")
        return

    # Tokenizes the text
    tokens = tokenizer.tokenize (text)

    # Counts the occurances of each token
    token_count = Counter (tokens)

    # Identifies the top 30 most common tokens
    top_30_tokens = token_count.most_common (30)

    # Stores top 30 on a .csv file under the headings token and count
    df = pd.DataFrame (top_30_tokens, columns=['Token', 'Count'])
    df.to_csv (output_path, index=False)

    print (f"Top 30 tokens are recorded on {output_path}")


read_path = 'extracted_text_edited.txt'  # Path to the edited text file
output_path = 'top_30_tokens.csv'  # Path to store the Top 30 tokens and their counts

# Calls function
top_30 (read_path, output_path)
