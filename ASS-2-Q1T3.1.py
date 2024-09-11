# Question 1 Task 3 Part 1
import pandas as pd # Library for data analytics
from collections import Counter # Imports Counter class
import re # Regular Expression module for pattern matching
from nltk.corpus import stopwords # Imports stopwords module for the filtered list

# Used to find the top 30 words all inclusive and stores output in a .csv file
# Arguments are the file path for the text you want analysed and output is the resultant list
def top_30 (read_path, output_path):
    
    # Read text file using a 'with' statement to ensure it closes on completion 
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

    # Uses regular expressions to find all the words and convert to lower case
    words = re.findall (r'\b\w+\b', text.lower())  

    # Counts the number of occurances for each word using the counter object
    word_counter = Counter (words)

    # Produces a list of the top 30 words
    top_30_words = word_counter.most_common (30)

    # Converts top 30 words and their number eof occurances into a data frame with two columns
    # Writes the data frame to a .csv file
    df = pd.DataFrame (top_30_words, columns=['Word', 'Count'])
    df.to_csv(output_path, index=False)


    print (f"Top 30 words (all inclusive) are recorded on {output_path}")

# Used to find the top 30 words removing stop words and numbers and stores output in a .csv file
# Arguments are the file path for the text you want analysed and output is the resultant list 
def top_30_filtered (read_path, output_path):

    # Read text file using a 'with' statement to ensure it closes on completion 
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

    # Uses regular expressions to find all the words and convert to lower case
    words = re.findall (r'\b\w+\b', text.lower()) 

    # Removes stop words and numbers
    stop_words = set (stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words and not word.isdigit()]

    # Counts the number of occurances for each word using the counter object
    word_counts = Counter (filtered_words)

    # Produces a list of the top 30 words excluding stop words and numbers 
    top_30_words = word_counts.most_common (30)

    # Converts top 30 words and their number eof occurances into a data frame with two columns
    # Writes the data frame to a .csv file
    df = pd.DataFrame (top_30_words, columns=['Word', 'Count'])
    df.to_csv (output_path, index=False)

    print (f"Top 30 words (exempting stop words and numbers) are recorded on {output_path}")




read_path = 'extracted_text_edited.txt'  # Path to the text file generated from Task 1
output_csv_path1 = 'top_30_words.csv'  # Path to store the Top 30 words and their counts
output_csv_path2 = 'top_30_filtered_words.csv'  # Path to store the Top 30 filtered words and their counts

# Calls functions
top_30 (read_path, output_csv_path1)
top_30_filtered (read_path, output_csv_path2)
