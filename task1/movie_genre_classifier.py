import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Load the Datasets
print("Loading dataset rows...")
train_path = "Genre Classification Dataset/train_data.txt"
test_path = "Genre Classification Dataset/test_data_solution.txt"

# Specify columns manually since the text files lack a structural header row
columns = ['ID', 'TITLE', 'GENRE', 'DESCRIPTION']

train_df = pd.read_csv(train_path, sep=' ::: ', engine='python', names=columns)
test_df = pd.read_csv(test_path, sep=' ::: ', engine='python', names=columns)

print(f"Loaded {len(train_df)} training tracks and {len(test_df)} testing tracks successfully.")

# 2. Extract Features (X) and Labels (y)
X_train = train_df['DESCRIPTION']
y_train = train_df['GENRE']

X_test = test_df['DESCRIPTION']
y_test = test_df['GENRE']

# 3. Vectorization (Convert Text to Numbers)
print("\nTransforming plot descriptions via TF-IDF...")
# stop_words='english' filters out junk words like 'the', 'is', 'at'
tfidf = TfidfVectorizer(stop_words='english', max_features=20000)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# 4. Train the Classifier
print("Training Multinomial Naive Bayes model...")
classifier = MultinomialNB(alpha=0.1)  # alpha=0.1 handles rare words cleanly
classifier.fit(X_train_tfidf, y_train)

# 5. Evaluate Performance
print("Predicting text categories...")
y_pred = classifier.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
print(f"\n======================================")
print(f" Model Accuracy: {accuracy * 100:.2f}%")
print(f"======================================\n")

print("Detailed Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# 6. Interactive Custom Inference Function
def predict_movie_genre(plot_summary):
    transformed_input = tfidf.transform([plot_summary])
    prediction = classifier.predict(transformed_input)[0]
    return prediction

print("\n--- Running Custom Predictor Verification ---")
sample_sci_fi = "In a dystopian future, a cybernetic resistance fighter travels backward through temporal rifts to stop an autonomous AI collective from erasing humanity."
predicted = predict_movie_genre(sample_sci_fi)
print(f"Test Plot: \"{sample_sci_fi}\"")
print(f"Predicted Genre Label: {predicted.upper()}")
