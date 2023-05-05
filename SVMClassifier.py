from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm

class SVMClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.classifier = svm.SVC(kernel='linear')
        
    def train(self, documents, labels):
        # Tokenize and vectorize the documents
        X = self.vectorizer.fit_transform(documents)
        # Train the classifier on the vectorized documents
        self.classifier.fit(X, labels)
        
    def predict(self, documents):
        # Vectorize the new documents using the same vocabulary as the training data
        X_new = self.vectorizer.transform(documents)
        # Predict the labels of the new documents using the trained classifier
        return self.classifier.predict(X_new)
