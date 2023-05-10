# document-svm-classifier
This is a repo that contains a document classifier to identify relevant documents using an SVM Machine Learning model.

# Example usage
```python 
docs = ['The quick brown fox jumps over the lazy dog', 'The lazy dog slept in the sun', 'The quick brown fox ate a rabbit']
labels = ['relevant', 'relevant', 'unrelevant']
test_docs = ['The quick brown fox is a very fast animal', 'The lazy cat slept in the sun']
svm_classifier = SVMClassifier()
svm_classifier.train(docs, labels)
predicted_labels = svm_classifier.predict(test_docs)
print(predicted_labels) # Output: ['animal' 'animal']
```
