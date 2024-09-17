import spacy

# Loads the bc5cdr model
nlp_bc5cdr = spacy.load ("en_ner_bc5cdr_md")

# Defines a function that is used to identify the diseases and drugs within a provided text
def extract_entities (read_path):
    
    # Reads the provided file using a 'with' statement so it closes properly on completion
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
    
    # Processes the provided text using the model, using sets so as to avoid duplicates
    doc = nlp_bc5cdr (text)
    entities = {'disease': set(), 'drug': set()}
    
    # For loop for entity recognition
    for ent in doc.ents:
        if ent.label_ == 'DISEASE':
            entities ['disease'].add (ent.text)
        elif ent.label_ == 'CHEMICAL':
            entities ['drug'].add (ent.text)
    return entities

# Path to the edited text file
read_path = 'extracted_text_edited.txt'

# Extract entities from the file
entities = extract_entities (read_path)

# Output the results in alphabetical lsit
print ('\n')
print ("Detected Diseases: ", sorted(entities['disease']))
print ('\n')
print ("Detected Drugs: ", sorted(entities['drug']))
