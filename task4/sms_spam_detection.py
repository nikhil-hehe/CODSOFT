import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Loading SMS logs...")
# latin-1 encoding prevents crashes from special text symbols or emojis in text messages
raw_sms_data = pd.read_csv('spam.csv', encoding='latin-1')

# Clean up trailing blank columns that Kaggle sometimes adds to this dataset
clean_data = raw_sms_data.dropna(how='any', axis=1)
clean_data.columns = ['label', 'message']

print(f"Loaded {len(clean_data)} messages.")
print("Class distributions:\n", clean_data['label'].value_counts())

# Split the data into an 80/20 train/test split. Stratify keeps the spam ratio balanced in both sets.
x_train, x_test, y_train, y_test = train_test_split(
    clean_data['message'], 
    clean_data['label'], 
    test_size=0.2, 
    random_state=42, 
    stratify=clean_data['label']
)

print("\nConverting message strings into text vector weights...")
text_vectorizer = TfidfVectorizer(stop_words='english')

x_train_vectors = text_vectorizer.fit_transform(x_train)
x_test_vectors = text_vectorizer.transform(x_test)

print("Training Naive Bayes spam classifier...")
spam_filter = MultinomialNB()
spam_filter.fit(x_train_vectors, y_train)

print("Running testing metrics...")
predictions = spam_filter.predict(x_test_vectors)

print("\n" + "="*40)
print(f" Overall Filtering Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")
print("="*40 + "\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nDetailed Performance Evaluation:")
print(classification_report(y_test, predictions))


# Helper function to instantly pass text messages to check if they flag as spam
def analyze_message(text_string):
    vectorized_msg = text_vectorizer.transform([text_string])
    flag = spam_filter.predict(vectorized_msg)[0]
    return flag

print("--- Running Live Verification Examples ---")
spam_example = "FREE text alerts! Win a brand new cash prize right now! Text claim to 88400 immediately."
legit_example = "Hey, are you free to grab a coffee tomorrow morning around 10?"

print(f"Message 1: \"{spam_example}\" -> Result: {analyze_message(spam_example).upper()}")
print(f"Message 2: \"{legit_example}\" -> Result: {analyze_message(legit_example).upper()}")
