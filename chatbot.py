import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Handling SSL certificate issues
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# Load intents
file_path = "intents.json"
with open(file_path, "r", encoding="utf-8") as file:
    intents = json.load(file)

# Data Preprocessing
tags, patterns = [], []
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

# Training the model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)
clf = LogisticRegression(random_state=0, max_iter=10000)
clf.fit(X, tags)

# Chatbot Response Function
def chatbot(input_text):
    transformed_input = vectorizer.transform([input_text])
    tag = clf.predict(transformed_input)[0]
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

# Streamlit UI
def main():
    st.title("AI Chatbot using NLP")

    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Chat with the AI bot by typing your message below.")

        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv.writer(csvfile).writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        user_input = st.text_input("You:")
        if user_input:
            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=100)

            # Save conversation to CSV
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv.writer(csvfile).writerow([user_input, response, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    elif choice == "Conversation History":
        st.header("Conversation History")
        if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    st.text(f"User: {row[0]}")
                    st.text(f"Chatbot: {row[1]}")
                    st.text(f"Timestamp: {row[2]}")
                    st.markdown("---")

    elif choice == "About":
        st.subheader("About the Project")
        st.write("This chatbot uses NLP techniques and Logistic Regression for intent recognition. Built with Streamlit for interaction.")

if __name__ == '__main__':
    main()
