import os
import sys
import joblib

# Add the path to the 'packages' directory
sys.path.append(os.path.abspath("C:\\Users\\elkus\\OneDrive\\Desktop\\fish\\packages"))

# Import the data processor and model trainer modules
import data_processor as dp
import model_trainer as mt

# Set the working directory
os.chdir("C:\\Users\\elkus\\OneDrive\\Desktop\\fish")

# Define the path to the data
path_to_data = 'data/Phishing_Email.csv'

# Prepare the data
prepared_data = dp.prepare_data(path_to_data, encoding="latin-1")

# Create training and testing datasets
train_test_data, vectorizer = dp.create_train_test_data(prepared_data['text'],
                                                        prepared_data['label'],
                                                        test_size=0.33,
                                                        random_state=2021)

# Run training
model = mt.run_model_training(train_test_data['x_train'], train_test_data['x_test'],
                              train_test_data['y_train'], train_test_data['y_test'])

# Save the trained model and vectorizer
joblib.dump(model, './models/my_phishing_model.pkl')
joblib.dump(vectorizer, open("./vectors/my_vectorizer.pickle", "wb"))
