
# Sentiment Analysis using NLP

from textblob import TextBlob

# Function to perform sentiment analysis
def analyze_sentiment(text):

    # Create TextBlob object
    analysis = TextBlob(text)

    # Get polarity score
    polarity = analysis.sentiment.polarity

    # Classify sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return polarity, sentiment


# Input text from user
text = input("Enter a sentence: ")

# Perform sentiment analysis
polarity, sentiment = analyze_sentiment(text)

# Display results
print("\nSentiment Analysis Result")
print("-------------------------")
print("Input Text:", text)
print("Polarity Score:", polarity)
print("Sentiment:", sentiment)
