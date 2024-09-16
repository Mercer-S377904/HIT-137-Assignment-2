from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load Biobert models and tokenizers
disease_model_name = "alvaroalon2/biobert_diseases_ner"
drug_model_name = "alvaroalon2/biobert_chemical_ner"

# Initialise tokenizers for disease and drug models
disease_tokenizer = AutoTokenizer.from_pretrained (disease_model_name)
disease_model = AutoModelForTokenClassification.from_pretrained (disease_model_name)

drug_tokenizer = AutoTokenizer.from_pretrained (drug_model_name)
drug_model = AutoModelForTokenClassification.from_pretrained (drug_model_name)

# Initialise the ner pipelines with Biobert models
disease_nlp = pipeline ("ner", model=disease_model, tokenizer=disease_tokenizer, aggregation_strategy="simple")
drug_nlp = pipeline ("ner", model=drug_model, tokenizer=drug_tokenizer, aggregation_strategy="simple")

# Function to extract entities from a provided file
def extract_entities (read_path):
    try:
        # Read the text file and associate it with the 'text' variable
        with open (read_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        # Handle file not found error
        print (f"Error: The file {read_path} was not found.")
        return
    except Exception as e:
        # Handle any other exceptions that may occur
        print (f"An error occurred: {e}")
        return
    
    # Initialize sets to store each disease and drug
    ent = {'disease': set(), 'drug': set()} 
    
    # Retrieve all the entities from the text through the ner pipelines
    disease_results = disease_nlp (text)
    drug_results = drug_nlp (text)
    
    # Filter out entities with the label '0' as its not relevent and disrupts results
    disease_results = [result for result in disease_results if result['entity_group'] != '0']
    drug_results = [result for result in drug_results if result['entity_group'] != '0']
    
    # Print all the labels for diseases and drugs
    disease_labels = set (result['entity_group'] for result in disease_results)
    drug_labels = set (result['entity_group'] for result in drug_results)
    print (f"\nDisease labels detected: \n {disease_labels}")
    print (f"Drug labels detected: \n {drug_labels}")
    
    # Print out all detected disease entities and their labels for debugging
    print ("Detected disease entities and their labels:")
    for result in disease_results:
        ent_text = result ['word']
        ent_label = result ['entity_group']
        
        print (f"\n {ent_text} ({ent_label})\n")
        
        # Map detected labels to 'disease'
        if ent_label in ['DISEASE']:
            ent ['disease'].add (ent_text)
    
    # Print out all detected drug entities and their labels for debugging
    print ("Detected drug entities and their labels:")
    for result in drug_results:
        ent_text = result ['word']
        ent_label = result ['entity_group']
        
        print (f"\n {ent_text} ({ent_label})")
        
        # Map detected labels to 'drug'
        if ent_label in ['CHEMICAL']:
            ent ['drug'].add (ent_text)
    
    return ent

# Path to your text file
read_path = 'extracted_text.txt'

# Extract entities from the file
ent = extract_entities (read_path)

# Output the results, converting sets back to sorted lists
print ("\nDetected Diseases (sorted alphabetically):\n", sorted (ent['disease']))
print ("\nDetected Drugs (sorted alphabetically):\n", sorted (ent['drug']))
