import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from collections import Counter

def extract_entities_spacy(file_path, model_name):
    nlp = spacy.load(model_name)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    doc = nlp(text)

    diseases = set()
    drugs = set()

    for ent in doc.ents:
        if ent.label_ == 'DISEASE':
            diseases.add(ent.text)
        elif ent.label_ == 'CHEMICAL':
            drugs.add(ent.text)

    return diseases, drugs

def extract_entities_biobert(file_path, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)

    predictions = torch.argmax(outputs.logits, dim=2)

    diseases = set()
    drugs = set()

    for token, prediction in zip(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0]), predictions[0]):
        if model.config.id2label[prediction] == 'B-DISEASE':
            current_entity = [token]
        elif model.config.id2label[prediction] == 'I-DISEASE':
            current_entity.append(token)
        elif model.config.id2label[prediction] == 'B-CHEMICAL':
            current_entity = [token]
        elif model.config.id2label[prediction] == 'I-CHEMICAL':
            current_entity.append(token)
        else:
            current_entity = []

        if current_entity:
            entity_text = tokenizer.convert_tokens_to_string(current_entity).replace(' ##', '')
            if 'DISEASE' in model.config.id2label[prediction]:
                diseases.add(entity_text)
            elif 'CHEMICAL' in model.config.id2label[prediction]:
                drugs.add(entity_text)

    return diseases, drugs

def compare_results(set1, set2):
    common_entities = set1.intersection(set2)
    difference_set1 = set1 - set2
    difference_set2 = set2 - set1

    return common_entities, difference_set1, difference_set2

def get_most_common_words(entities_set, top_n=10):
    words = [word for entity in entities_set for word in entity.split()]
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

# Example usage
file_path = 'combined_text.txt'  

# Using en_core_sci_sm
model_name_spacy = 'en_core_sci_sm'
diseases_spacy, drugs_spacy = extract_entities_spacy(file_path, model_name_spacy)

# Using biobert
model_name_biobert = 'monologg/biobert_v1.1_pubmed'
diseases_biobert, drugs_biobert = extract_entities_biobert(file_path, model_name_biobert)

# Comparing results
common_diseases, difference_diseases_spacy, difference_diseases_biobert = compare_results(diseases_spacy, diseases_biobert)
common_drugs, difference_drugs_spacy, difference_drugs_biobert = compare_results(drugs_spacy, drugs_biobert)

# Display results
print("Entities detected by both models:")
print("Common Diseases:", common_diseases)
print("Common Drugs:", common_drugs)

print("\nEntities detected by en_core_sci_sm only:")
print("Diseases:", difference_diseases_spacy)
print("Drugs:", difference_drugs_spacy)

print("\nEntities detected by biobert only:")
print("Diseases:", difference_diseases_biobert)
print("Drugs:", difference_drugs_biobert)

# Display most common words
print("\nMost common words in diseases detected by both models:")
print("Common Diseases:", get_most_common_words(common_diseases))

print("\nMost common words in drugs detected by both models:")
print("Common Drugs:", get_most_common_words(common_drugs))
