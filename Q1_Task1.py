#Question 1 Task 1

import zipfile # Allows program to work with zipfile
import pandas as pd # Library for data analysis


# Creating a function that extracts the text from the CSV files
# Arguments are path to zip file being extracted and path to output .txt file

def extract_text (zip_path, output_path):

    # Opens zip file in read mode and assigns it to zip_ref, the with statement will ensure it is closed after executed
    with zipfile.ZipFile (zip_path, 'r') as zip_ref:

        # Creates a for loop to read each .csv in the zip file and returns a list
        for csv_info in zip_ref.infolist():
            # Vereifies if the contents of the zip folder is .csv
            if csv_info.filename.endswith('.csv'):
                # Try block to catch handle exceptions
                try:
                    # Opens .csv file from zip folder for reading and assigns it to 'read_file'
                    with zip_ref.open (csv_info) as read_file:
                        # Deliminiter that seperates data fields
                        if csv_info.filename == 'CSV1.csv':
                            df = pd.read_csv (read_file, delimiter=',', engine='python', quotechar='"')
                        else:
                            df = pd.read_csv (read_file, delimiter=',', engine='python', quotechar='"')

                        # Debugging line that outputs the list of column names for each .csv file
                        print (f"Columns in {csv_info.filename}: {df.columns.tolist()}")

                        # Extract text based on column names for each .csv file
                        # Verifies 'SHORT-TEXT' exists in CSV1 and extracts onto the list 'csv_text_data'
                        # if not found, will move on to the next file and look for 'TEXT'
                        if csv_info.filename == 'CSV1.csv':
                            if 'SHORT-TEXT' in df.columns:
                                csv_text_data = df ['SHORT-TEXT'].tolist() 
                            else:
                                print (f"'SHORT-TEXT' column not found in {csv_info.filename}")
                                continue
                        else:
                            if 'TEXT' in df.columns:
                                csv_text_data = df ['TEXT'].tolist()
                            else:
                                print (f"'TEXT' column not found in {csv_info.filename}")
                                continue
                        # Opens output .txt file in append mode and makes sure added text goes at the end
                        # Of pre existing text
                        with open (output_path, 'a', encoding='utf-8') as outfile:
                            for text in csv_text_data:
                                outfile.write (text + '\n')
                # Catches any exceptions found in the try block
                except Exception as e:
                    print (f"Error processing file {csv_info.filename}: {e}")

# Path of zip folder being extracted and path of produced .txt file
zip_path = 'CSV.zip'
output_path = 'extracted_text.txt'

# Calls the function
extract_text (zip_path, output_path)
