import json
import random
import re

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

# Clean and tokenize text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()

# Main function to get response
def get_response(user_input):
    user_words = clean_text(user_input)

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = clean_text(pattern)
            if set(user_words).intersection(set(pattern_words)):
                return random.choice(intent["responses"])

    return "Sorry, I do not understand. Please rephrase your question."

__all__ = ['get_response']
