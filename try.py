from flask import Flask, Response
import base64

app = Flask(__name__)

@app.route('/')
def home():
    text = """# 1. Import libraries
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 2. Load dataset (selecting 4 categories)
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
print('Start Training...')
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True)
print('Start testing...')
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True)

print("Number of training documents:", len(twenty_train.data))
print("Number of test documents:", len(twenty_test.data))
print("Target names (categories):", twenty_train.target_names)
print("\nSample training document:\n", twenty_train.data[0])
print("Category of sample document:", twenty_train.target_names[twenty_train.target[0]])

# 3. Preprocessing: Convert text to TF-IDF features
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# 4. Train Naïve Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)

# 5. Transform test data and predict
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

predicted = clf.predict(X_test_tfidf)

# 6. Evaluate the model
print("\n--- Evaluation ---")
print("Accuracy:", accuracy_score(twenty_test.target, predicted))
print("\nClassification Report:\n", classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))

cm = confusion_matrix(twenty_test.target, predicted)
print("Confusion Matrix:\n", cm)
"""
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return Response(encoded_bytes, mimetype='text/plain')

if __name__ == '__main__':
    # Run the server on all available interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)
