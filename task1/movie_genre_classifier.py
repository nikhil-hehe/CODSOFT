import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Setup file paths
TRAIN_FILE = "Genre Classification Dataset/train_data.txt"
TEST_FILE = "Genre Classification Dataset/test_data_solution.txt"
DATA_COLUMNS = ['id', 'title', 'genre', 'description']

print("Reading movie files...")
# The dataset uses a non-standard ' ::: ' separator instead of normal commas
train_data = pd.read_csv(TRAIN_FILE, sep=' ::: ', engine='python', names=DATA_COLUMNS)
test_data = pd.read_csv(TEST_FILE, sep=' ::: ', engine='python', names=DATA_COLUMNS)

print(f"Loaded {len(train_data)} training movies and {len(test_data)} testing movies.")

# Separate our text features from the target genre labels
x_train = train_data['description']
y_train = train_data['genre']
x_test = test_data['description']
y_test = test_data['genre']

print("Converting plot descriptions into numeric text vectors...")
# Clean up junk words using standard English stop words and cap vocabulary at 20,000 words
text_vectorizer = TfidfVectorizer(stop_words='english', max_features=20000)

x_train_vectors = text_vectorizer.fit_transform(x_train)
x_test_vectors = text_vectorizer.transform(x_test)

print("Training the Naive Bayes model...")
# alpha=0.1 helps smooth out probabilities for words the model hasn't seen before
genre_classifier = MultinomialNB(alpha=0.1)
genre_classifier.fit(x_train_vectors, y_train)

print("Running predictions on the test set...")
predictions = genre_classifier.predict(x_test_vectors)

# Show final accuracy metrics
final_score = accuracy_score(y_test, predictions)
print("\n" + "="*40)
print(f" Overall Model Accuracy: {final_score * 100:.2f}%")
print("="*40 + "\n")

print("Detailed Breakdown per Genre:")
print(classification_report(y_test, predictions, zero_division=0))


# Helper function to manually test the model with custom ideas
def check_custom_movie(plot_text):
    vectorized_input = text_vectorizer.transform([plot_text])
    guessed_genre = genre_classifier.predict(vectorized_input)[0]
    return guessed_genre

print("--- Testing Live Custom Inference ---")
sample_plot = "A brilliant detective chases a mysterious criminal mastermind through the rainy streets of London."
result = check_custom_movie(sample_plot)
print(f"Sample Plot: '{sample_plot}'")
print(f"Predicted Genre: {result.upper()}")
