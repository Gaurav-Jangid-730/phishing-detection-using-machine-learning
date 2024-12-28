import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """Load the dataset from the given file path."""
    logging.info("Loading dataset from %s", file_path)
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    """Handle missing values in the dataset."""
    logging.info("Handling missing values...")
    # Replace missing values with the column mean for numerical columns
    data.fillna(data.mean(), inplace=True)
    # Replace missing categorical values with the most frequent value
    for column in data.select_dtypes(include=['object']).columns:
        data[column].fillna(data[column].mode()[0], inplace=True)
    return data

def encode_categorical_features(data):
    """Encode categorical features into numeric values using Label Encoding."""
    logging.info("Encoding categorical features...")
    label_encoder = LabelEncoder()
    for column in data.select_dtypes(include=['object']).columns:
        data[column] = label_encoder.fit_transform(data[column])
    return data

def preprocess_data(file_path):
    """Load and preprocess the dataset."""
    # Load the dataset
    data = load_data(file_path)
    
    # Handle missing values
    data = handle_missing_values(data)
    
    # Encode categorical features
    data = encode_categorical_features(data)
    
    # Separate features (X) and target label (y)
    X = data.drop(columns='phishing')
    y = data['phishing']
    
    logging.info("Data preprocessing completed.")
    return X, y

def main():
    # File path to the dataset
    file_path = Path(__file__).parent.parent / "data" / "dataset_full.csv"
    
    # Preprocess the data
    X, y = preprocess_data(file_path)
    
    # Split the dataset into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    logging.info("Data preprocessing and splitting completed.")
    
    # You can save the processed data or proceed to model training
    # X_train.to_csv('processed_data/X_train.csv', index=False)
    # X_test.to_csv('processed_data/X_test.csv', index=False)
    # y_train.to_csv('processed_data/y_train.csv', index=False)
    # y_test.to_csv('processed_data/y_test.csv', index=False)

if __name__ == "__main__":
    main()
