import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Loading credit card transactions...")
train_dataset = pd.read_csv("fraudTrain.csv")
test_dataset = pd.read_csv("fraudTest.csv")

print(f"Loaded {len(train_dataset)} training items and {len(test_dataset)} testing items.")

# We only pull out numeric variables and clean categories that drive transaction patterns
core_features = ['category', 'amt', 'gender', 'city_pop', 'unix_time', 'lat', 'long', 'merch_lat', 'merch_long']

x_train = train_dataset[core_features].copy()
y_train = train_dataset['is_fraud']

x_test = test_dataset[core_features].copy()
y_test = test_dataset['is_fraud']

print("Encoding text categories into machine-readable numeric labels...")
text_columns = ['category', 'gender']

for column in text_columns:
    encoder = LabelEncoder()
    # Fit the encoder globally across both sets so it handles all possible categories safely
    encoder.fit(pd.concat([x_train[column], x_test[column]], axis=0))
    x_train[column] = encoder.transform(x_train[column])
    x_test[column] = encoder.transform(x_test[column])

print("Training the Random Forest model (this can take a moment due to data size)...")
# class_weight='balanced' ensures the model doesn't ignore rare fraud cases
fraud_detector = RandomForestClassifier(n_estimators=50, random_state=42, class_weight='balanced', n_jobs=-1)
fraud_detector.fit(x_train, y_train)

print("Evaluating transaction predictions...")
predictions = fraud_detector.predict(x_test)

print("\n" + "="*40)
print(f" Overall Accuracy Score: {accuracy_score(y_test, predictions) * 100:.2f}%")
print("="*40 + "\n")

print("Confusion Matrix (Legitimate vs Fraudulent counts):")
print(confusion_matrix(y_test, predictions))

print("\nDetailed Performance Report:")
print(classification_report(y_test, predictions))
