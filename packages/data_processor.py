from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

def prepare_data(path_to_data, encoding="latin-1"):
    # Read data from path
    data = pd.read_csv(path_to_data, encoding=encoding)
    
    # Drop rows where 'Email Text' is NaN
    data = data.dropna(subset=['Email Text'])
    
    # Ensure 'Email Text' is of string type
    data['Email Text'] = data['Email Text'].astype(str)

    # Encode labels
    data['label'] = data['Email Type'].map({'Safe Email': 0, 'Phishing Email': 1})

    X = data['Email Text']
    y = data['label']

    return {'text': X, 'label': y}


def create_train_test_data(X, y, test_size, random_state):
    # Initialize CountVectorizer
    cv = CountVectorizer()
    
    # Transform text data into feature vectors
    X = cv.fit_transform(X)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=test_size, 
                                                        random_state=random_state)
    
    return {'x_train': X_train, 'x_test': X_test,
            'y_train': y_train, 'y_test': y_test}, cv

