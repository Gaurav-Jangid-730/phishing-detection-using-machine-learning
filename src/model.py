import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
import joblib
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """Load dataset from the given path."""
    logging.info("Loading dataset from %s", file_path)
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the dataset (features and labels)."""
    # Assume the dataset has features and a 'label' column for phishing (1) or legitimate (0)
    X = data.drop(columns='phishing')
    y = data['phishing']
    return X, y

def train_model(X_train, y_train, model_type="RandomForest"):
    """Train a model based on the specified type."""
    if model_type == "RandomForest":
        model = RandomForestClassifier(n_estimators=100, random_state=42)
    elif model_type == "LogisticRegression":
        model = LogisticRegression(random_state=42)
    elif model_type == "SVM":
        model = SVC(probability=True, random_state=42)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
    
    logging.info("Training %s model...", model_type)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance on the test set."""
    logging.info("Evaluating model...")
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    
    logging.info(f"Accuracy: {accuracy:.4f}")
    logging.info(f"Precision: {precision:.4f}")
    logging.info(f"Recall: {recall:.4f}")
    logging.info(f"F1-Score: {f1:.4f}")
    logging.info(f"ROC-AUC: {roc_auc:.4f}")
    
    return accuracy, precision, recall, f1, roc_auc

def save_model(model, file_path):
    """Save the trained model to a file."""
    logging.info("Saving model to %s", file_path)
    joblib.dump(model, file_path)

def load_model(file_path):
    """Load a saved model from a file."""
    logging.info("Loading model from %s", file_path)
    return joblib.load(file_path)

def main():
    # Load dataset
    data_path = Path(__file__).parent.parent / "data" / "dataset_full.csv"
    data = load_data(data_path)
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a RandomForest model
    model = train_model(X_train, y_train, model_type="RandomForest")
    
    # Evaluate the model
    evaluate_model(model, X_test, y_test)
    
    # Save the model
    save_model(model, "best_model.pkl")
    
if __name__ == "__main__":
    main()
