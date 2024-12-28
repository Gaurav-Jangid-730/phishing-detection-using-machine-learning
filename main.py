import logging
import pandas as pd
from pathlib import Path
from src.data_preprocessing import preprocess_data
from src.feature_engineering import extract_features
from src.model import train_model, save_model, load_model, evaluate_model
from sklearn.model_selection import train_test_split
from joblib import load

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the phishing domain detection workflow...")
    
    # Step 1: Load and preprocess the data
    file_path = Path(__file__).parent.parent / "phishing-domain-detection" / "data" / "dataset_full.csv"  # Update this with the actual dataset path
    X, y = preprocess_data(file_path)
    logging.info("Data preprocessing completed.")
    
    # Step 2: Perform feature engineering
    # features = extract_features(X)
    # features.to_csv("extracted_features.csv", index=False)
    # logging.info("Feature engineering completed.")
    
    # Step 3: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)
    logging.info("Data split into training and testing sets.")

    # Step 4: Train the model
    model = train_model(X_train, y_train)
    logging.info("Model training completed.")

    # After training the model, save the feature names
    feature_names = X_train.columns.tolist()
    feature_names_df = pd.DataFrame(feature_names, columns=['Feature Names'])  # Specify a column name
    feature_names_df.to_csv("feature_names.csv", index=False)
    
    # Step 5: Evaluate the model
    evaluation_results = evaluate_model(model, X_test, y_test)
    logging.info("Model evaluation completed. Results: %s", evaluation_results)
    
    # Step 6: Save the trained model
    save_model(model, 'best_model.pkl')
    logging.info("Trained model saved as best_model.pkl")
    
    # Step 7: Make predictions (optional)
    test_sample = pd.DataFrame([X_test.iloc[0]])  # Use the first sample from the test set
    prediction = model.predict(test_sample)
    logging.info("Prediction for test sample: %s", prediction[0])

    # Workflow completed
    logging.info("Phishing domain detection workflow completed successfully.")

def predict_url(model, url):
    import pandas as pd
    from src.feature_engineering import extract_features

    # Extract features for the given URL
    features = extract_features(url)
    
    # Load the saved feature names
   # Load the saved feature names, skipping the first row
    saved_feature_names = pd.read_csv("feature_names.csv", header=None, skiprows=1)[0].tolist() 

    # Convert extracted features into a DataFrame
    features_df = pd.DataFrame([features])  # Create DataFrame from features dictionary

    # Ensure the DataFrame has the same columns as the training set
    features_df = features_df.reindex(columns=saved_feature_names, fill_value=0)
    # Get the predicted probabilities for the positive class (phishing)
    probabilities = model.predict_proba(features_df)[:, 1]  # Get the probability of being phishing

    # Set a threshold for classification
    threshold = 0.6  # Adjust this threshold as needed

    # Make prediction based on the threshold
    prediction = (probabilities > threshold).astype(int)[0]
    probability_percent = probabilities[0] * 100
    print(probability_percent)
    return "Legitimate" if prediction == 1 else "Phishing"

if __name__ == "__main__":
    main()
    model = load("best_model.pkl")
    # Accept user input for URL prediction
    user_url = input("Enter a URL to check if it's phishing or legitimate: ")
    result = predict_url(model, user_url)
    print(f"The URL '{user_url}' is classified as: {result}")
