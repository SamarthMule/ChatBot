# Generic Chatbot Using NLP and Machine Learning

This project implements a generic chatbot using Natural Language Processing (NLP) and Machine Learning techniques. The chatbot is designed to classify user input into predefined intents and provide context-aware responses. The solution is scalable, interactive, and suitable for various domains.

---

## **Features**
- Intent classification using machine learning models.
- Preprocessing techniques like tokenization, stopword removal, and TF-IDF vectorization.
- Supports Logistic Regression, Random Forest, and SVM models.
- User-friendly web-based interface built with Streamlit.
- Scalable and adaptable for different use cases.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `nltk`: For text preprocessing (tokenization, stopword removal).
  - `scikit-learn`: For machine learning models and evaluation metrics.
  - `streamlit`: For creating the chatbot's web interface.
  - `numpy` and `pandas`: For data manipulation and analysis.

---

## **Project Structure**
```plaintext
project-directory/
│
├── app.py                  # Main Streamlit app for chatbot
├── intents.json            # Dataset containing intents, patterns, and responses
├── chatbot_model.pkl       # Trained machine learning model
├── vectorizer.pkl          # TF-IDF vectorizer
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files for Git
