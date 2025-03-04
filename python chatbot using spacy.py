##############################################
# File: basic_chatbot.py
# Description: A simple conversational chatbot
#              using spaCy for basic NLP.
#              Now handles multiple entity types.
##############################################

import spacy

# Load the small English language model
nlp = spacy.load("en_core_web_sm")

def get_entities(text):
    """
    Extract named entities from user input.
    Returns a dictionary of entity types and their text values.
    """
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)
    return entities

def generate_response(user_input):
    """
    Generate a response based on user input.
    Uses spaCy for named entity recognition and responds to various entity types.
    """
    # Convert user input to lowercase for simpler checks
    user_input_lower = user_input.lower()

    # If the user wants to exit
    if any(word in user_input_lower for word in ["exit", "quit", "bye"]):
        return "It was nice chatting with you! Goodbye!"

    # Basic fallback responses for greetings and farewells
    greetings = ["hello", "hi", "hey"]
    farewells = ["bye", "goodbye"]

    if any(greet in user_input_lower for greet in greetings):
        return "Hello there! How can I help you today?"
    elif any(farewell in user_input_lower for farewell in farewells):
        return "Take care! Have a great day!"

    # Extract entities using spaCy
    entities = get_entities(user_input)

    # Mapping of entity types to response templates
    entity_response_mapping = {
        "GPE": "I see you're talking about {entity}. I'd love to visit there someday!",
        "PERSON": "Oh, you're talking about {entity}. Interesting!",
        "ORG": "{entity} is definitely worth discussing!",
        "NORP": "It seems you're referring to {entity} as a nationality or group.",
        "FAC": "That facility, {entity}, sounds notable.",
        "LOC": "The location {entity} sounds fascinating.",
        "PRODUCT": "Product {entity} is quite popular.",
        "EVENT": "Event {entity} sounds exciting!",
        "WORK_OF_ART": "The work of art {entity} is truly captivating!",
        "LAW": "The law {entity} plays an important role in society.",
        "LANGUAGE": "The language {entity} is fascinating!",
        "DATE": "That date, {entity}, holds significance.",
        "TIME": "The time {entity} is noted.",
        "PERCENT": "That's {entity} percent!",
        "MONEY": "The amount {entity} sounds impressive!",
        "QUANTITY": "Quantity {entity} is recorded.",
        "ORDINAL": "Ordinal {entity} is in order.",
        "CARDINAL": "Cardinal number {entity} is noted."
    }

    responses = []
    # Loop over the defined entity types in the mapping order.
    for entity_type, response_template in entity_response_mapping.items():
        if entity_type in entities:
            # Join multiple entities of the same type with a comma
            entity_values = ", ".join(entities[entity_type])
            responses.append(response_template.format(entity=entity_values))
    
    # If at least one entity was recognized, return the combined response.
    if responses:
        return " ".join(responses)

    # Default fallback if no keywords or entities matched
    return "That's interesting! Could you tell me more?"

def main():
    """
    Main function to run the chatbot in a loop.
    """
    print("Chatbot: Hello! I am your basic chatbot. Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ")
        if not user_input.strip():
            # Skip empty input
            continue

        response = generate_response(user_input)
        print(f"Chatbot: {response}")

        # Break out if the user wants to exit
        if response.lower().startswith("it was nice chatting") or "goodbye" in response.lower():
            break

if __name__ == "__main__":
    main()
