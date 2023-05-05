Document SVM Classifier
This is a Python implementation of a document SVM classifier, which can be used to tokenize documents and classify them as relevant or irrelevant based on a trained SVM model.

Getting Started
To get started, follow these instructions:

Prerequisites
Python 3.x
scikit-learn library
Installing
Clone the repository to your local machine using git clone https://github.com/your-username/document-svm-classifier.git.
Install the required libraries by running pip install -r requirements.txt in the project directory.
Training the Model
To train the SVM model on your dataset, follow these steps:

Prepare your dataset as a CSV file, where each row represents a document and the last column is the label (0 for irrelevant and 1 for relevant).

Run the train.py script, passing the path to your dataset file and the name of the output model file:

css
Copy code
python train.py --dataset /path/to/dataset.csv --output model.pkl
The script will tokenize the documents, split the dataset into training and validation sets, train the SVM model using the training set, and save the trained model to the output file.

Classifying Documents
To classify new documents using the trained SVM model, follow these steps:

Prepare your documents as a text file, with each document on a separate line.

Run the classify.py script, passing the path to the input document file and the path to the trained model file:

css
Copy code
python classify.py --input /path/to/documents.txt --model model.pkl --output results.csv
The script will tokenize the documents, load the trained SVM model from the input file, classify each document as relevant or irrelevant, and save the results to the output CSV file.
