
# Step 2: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sentence_transformers import SentenceTransformer

# Step 3: Load dataset
dataset = pd.read_csv('dataset - Sheet1 (2).tsv', delimiter = '\t', quoting = 3)

# Step 4: Drop missing values
dataset = dataset.dropna(subset=['Review', 'Liked'])  # Assume columns are 'text' and 'label'

# Step 5: Split into X and y
X = dataset['Review'].values
y = dataset['Liked'].values

# Step 6: Load a Sentence-BERT model (MiniLM is lightweight and fast)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 7: Encode the text into embeddings
X_embeddings = model.encode(X)

# Step 8: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_embeddings, y, test_size=0.2, random_state=42)

# Step 9: Train Logistic Regression
classifier = LogisticRegression(max_iter=1000)
classifier.fit(X_train, y_train)

# Step 10: Evaluate
y_pred = classifier.predict(X_test)
print("Accuracy on Test Set:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ========== Predicting New Texts ==========

def predict_new_texts_bert(new_texts):
    # Encode new texts
    new_embeddings = model.encode(new_texts)
    # Predict
    predictions = classifier.predict(new_embeddings)
    return predictions

# Step 11: Example usage
new_reviews = [
    "We are selling pure  biak-biak at discount rates.",
    "Join us for a morning yoga session in the park.",
    "You still have Marijuana?",
    "Hey Sam, yesterday our teacher told us to not use the word Marijuana"
    "Looking for the best cafes in the city!",
    "have any African Salad left for me.",
    "Mom, have you made African Salad today?"
]

results = predict_new_texts_bert(new_reviews)

# Output the results
for review, result in zip(new_reviews, results):
    classification = "Drug-Related (1)" if result == 1 else "Not Drug-Related (0)"
    print(f"Review: {review}\nPredicted: {classification}\n")
