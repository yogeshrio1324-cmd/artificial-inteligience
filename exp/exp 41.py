
# Simple Chatbot using NLP

import nltk
import random
import string

from nltk.chat.util import Chat, reflections

# Define chatbot conversation patterns
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi! Nice to meet you."]
    ],

    [
        r"what is your name?",
        ["I am a simple NLP chatbot."]
    ],

    [
        r"how are you?",
        ["I am fine. Thank you!", "I am doing great!"]
    ],

    [
        r"what can you do?",
        ["I can answer simple questions and chat with you."]
    ],

    [
        r"what is python?",
        ["Python is a popular programming language."]
    ],

    [
        r"what is NLP?",
        ["NLP stands for Natural Language Processing."]
    ],

    [
        r"thank you|thanks",
        ["You're welcome!", "Happy to help!"]
    ],

    [
        r"bye|goodbye",
        ["Goodbye! Have a nice day."]
    ],

    [
        r"(.*)",
        ["Sorry, I don't understand. Can you ask something else?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
print("================================")
print("       NLP CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.")

# Start conversation
chatbot.converse()
