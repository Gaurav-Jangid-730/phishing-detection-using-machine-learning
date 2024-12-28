import pandas as pd

# Load the dataset (replace 'your_dataset.csv' with your actual dataset file path)
dataset_path = 'C:\\Users\\Gaurav.Googlly\\Desktop\\phishing-domain-detection\\data\\dataset_full.csv'
df = pd.read_csv(dataset_path)

# Get the column names (fields)
fields = df.columns.tolist()

# Display the fields (columns) in the dataset
print("Dataset Fields:")
for field in fields:
    print(field)

# Display the first few rows to understand the structure
print("\nFirst few rows of the dataset:")
print(df.head())

# Optionally, check the data types of the columns to understand their nature
print("\nData types of the columns:")
print(df.dtypes)
