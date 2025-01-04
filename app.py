import streamlit as st
import pickle
from nltk.tokenize import word_tokenize
import json
import random
# Load the model and vectorizer
with open('chatbot_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return ' '.join([word for word in tokens if word.isalnum()])

# Streamlit app
st.title("ML Chatbot")
st.write("Ask your question:")

user_input = st.text_input("You:")
if st.button("Submit"):
    processed_input = preprocess_text(user_input)
    input_vector = vectorizer.transform([processed_input])
    predicted_tag = model.predict(input_vector)[0]

    # Load intents to generate responses
    with open("intents.json", "r") as file:
        intents = json.load(file)

    for intent in intents:
        if intent['tag'] == predicted_tag:
            response = random.choice(intent['responses'])
            st.write(f"Chatbot: {response}")
            break
