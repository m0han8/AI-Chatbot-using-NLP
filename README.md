# AI-Chatbot-using-NLP

This project implements an AI-driven chatbot that leverages Natural Language Processing (NLP) and Machine Learning (ML) to classify user intents and provide intelligent, human-like responses. The chatbot is deployed using Streamlit for real-time interaction via a user-friendly web interface.

Introduction
Chatbots have become an integral part of modern-day applications, playing a crucial role in customer service, automated assistants, and AI-driven interaction models. This project aims to develop a chatbot that understands natural language, classifies intents, and provides meaningful responses based on predefined datasets. Unlike traditional rule-based chatbots, this AI chatbot uses Machine Learning algorithms to learn from user inputs and improve its responses dynamically.

Why AI Chatbots?
1. Limitations of Traditional Rule-Based Chatbots
Traditional chatbots rely on if-else statements or keyword-based matching, which makes them:
❌ Rigid - Cannot handle new or unexpected user inputs.
❌ Limited - Require manual programming for every possible response.
❌ Not Scalable - Cannot adapt to different conversation styles or tones.

2. Advantages of AI-Powered Chatbots
✅ Intent Recognition - Uses NLP techniques to classify user inputs based on their intent.
✅ Dynamic Response Generation - Generates meaningful and contextually relevant replies.
✅ Self-Learning - Improves over time with enhanced datasets.
✅ Scalable - Can be deployed in multiple domains (customer support, virtual assistants, etc.).

Key Features of This Chatbot
✅ Utilizes NLP for Text Processing (Tokenization, Lemmatization, Stopword Removal).
✅ Uses TF-IDF Vectorization for Feature Extraction to convert text into numerical representations.
✅ Employs Logistic Regression for Intent Classification.
✅ Provides a Web-Based Chat Interface using Streamlit.
✅ Stores Conversation History for Future Training.
✅ Can be Expanded for Different Domains and Use Cases.

Project Architecture
The chatbot consists of multiple components, each responsible for a specific function.

1. Text Preprocessing (NLP Pipeline)
Before processing user inputs, the chatbot performs text preprocessing to clean and normalize the text.

Tokenization: Splits text into words (e.g., "Hello, how are you?" → ["Hello", "how", "are", "you"]).
Lemmatization: Converts words to their base form ("running" → "run").
Stopword Removal: Removes common words like "is", "the", "and" to retain important keywords.
2. Feature Extraction (TF-IDF Vectorization)
TF-IDF (Term Frequency - Inverse Document Frequency) is used to convert textual data into a numerical format suitable for Machine Learning.

Term Frequency (TF): Measures how frequently a word appears in a sentence.
Inverse Document Frequency (IDF): Reduces the importance of common words appearing in multiple sentences.
Final TF-IDF Score: Helps extract the most relevant words for training the model.
3. Intent Classification Using Machine Learning
A Logistic Regression model is trained on labeled datasets to classify user inputs into specific intents.

Step 1: Convert user input into a TF-IDF vector.
Step 2: Use the trained Logistic Regression model to predict the intent.
Step 3: Retrieve the best matching response from intents.json.
4. Response Generation
Based on the classified intent, the chatbot retrieves a response from the predefined dataset (intents.json).
If no suitable intent is found, the chatbot returns a fallback response like "I’m sorry, I don’t understand.".
5. User Interface (Streamlit Web App)
The chatbot is deployed as a web application using Streamlit.
Users can interact with the chatbot by typing queries and receiving real-time responses.
The chat history is logged for future improvements.
Project Structure
bash
Copy
Edit
AI_Chatbot/
│── chatbot.py                  # Main Python script for chatbot execution
│── ImplementationofChatBot.ipynb  # Jupyter Notebook with detailed steps
│── intents.json                 # Dataset containing user intents and responses
│── chat_log.csv                 # File to store chat history
│── README.md                    # Project documentation
│── requirements.txt             # Required Python dependencies
Installation & Setup
Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/RGS-AI/Chatbot_using_NLP_AICTE_Cycle4.git
cd Chatbot_using_NLP_AICTE_Cycle4
Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Run the Chatbot
Option 1: Run in Jupyter Notebook
Execute ImplementationofChatBot.ipynb step by step to understand the chatbot workflow.

Option 2: Run the Streamlit Web Interface
bash
Copy
Edit
streamlit run chatbot.py
This will launch the chatbot in your default web browser, allowing real-time interaction.
Example Usage
User Input:
sql
Copy
Edit
Hello! How are you?
Chatbot Response:
vbnet
Copy
Edit
Hi there! I'm doing well. How can I assist you today?
User Input:
vbnet
Copy
Edit
Can you help me with budgeting?
Chatbot Response:
css
Copy
Edit
To create a budget, track your income and expenses and allocate wisely.
Future Enhancements
🚀 Implement Speech-to-Text for voice-based chatbot interaction.
🚀 Expand Dataset to improve accuracy and response variety.
🚀 Deploy on Cloud Services for scalability.
🚀 Integrate Multi-Turn Conversations for deeper interaction.
🚀 Add Sentiment Analysis to adjust responses based on user emotions.

Conclusion
This chatbot demonstrates how NLP and Machine Learning can be used to create an intelligent conversational agent. It can be further enhanced and expanded for real-world applications, such as customer support, AI-powered assistants, and voice-based interactions.





![4b36753c-66e7-4d02-b5a4-07f001da2f3e](https://github.com/user-attachments/assets/2632ee25-4fc7-4cfb-a578-01cc90d15148)
