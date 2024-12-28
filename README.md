# Phishing Domain Detection

This project aims to detect phishing websites based on various features extracted from the URL. By utilizing machine learning algorithms, this model classifies a given URL as either a phishing or legitimate website.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Evaluation](#model-evaluation)
6. [Project Structure](#project-structure)
7. [Technologies Used](#technologies-used)
8. [License](#license)

## Overview

Phishing websites attempt to deceive users into providing sensitive information such as passwords, credit card details, or personal data. The goal of this project is to classify websites based on URLs and associated features as either phishing or legitimate. This model has been trained on various machine learning algorithms and can classify URLs effectively.

## Features

The following types of features are used for the phishing website classification:

### 1. URL-Based Features:
- Length of URL
- Special characters
- Presence of "@" or "-" in the URL
- Domain age and number of subdomains

### 2. Domain-Based Features:
- WHOIS information
- Domain registration duration

### 3. Page-Based Features:
- Response codes from the website
- Page loading time

### 4. Content-Based Features:
- Keywords in HTML content
- Number of external links

## Installation

### Prerequisites

Ensure that Python 3.x is installed on your system. The following libraries are required for the project:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask logging dvc
```
Additionally, you may want to use virtualenv or conda to create a virtual environment for your project.

Clone the Repository
```bash
git clone https://github.com/yourusername/phishing-domain-detection.git
cd phishing-domain-detection
```
Install Dependencies
Once inside the project directory, install the required dependencies by running:

```bash
pip install -r requirements.txt
```
## Usage
1. Command-Line Usage (Interactive Script)
To predict whether a URL is phishing or legitimate using the command line, run the following command:

```bash
python main.py
```
You will be prompted to enter a URL. For example:

```css
Enter a URL to check if it's phishing or legitimate: http://www.example.com
```
The model will classify the URL as either Phishing or Legitimate and display the result.

2. Flask API Usage
You can also run the Flask web application to get predictions via a POST request.

Run the Flask app:

```bash
python app.py
The app will start a local server at http://127.0.0.1:5000. You can send a POST request with a JSON payload like:
```
```bash
POST http://127.0.0.1:5000/predict
{
    "url": "http://www.example.com"
}
```
The response will include the classification result:

```json
{
    "url": "http://www.example.com",
    "prediction": "Legitimate"
}
```
Model Evaluation
The model is evaluated using the following metrics:

Accuracy
Precision
Recall
F1-Score
ROC-AUC Score
These metrics are calculated after training the model using various algorithms, including Logistic Regression, Decision Trees, Random Forest, XGBoost, and Support Vector Machines (SVM).

Project Structure
The project is structured as follows:

```plaintext
phishing-domain-detection/
├── data/                  # Contains dataset for training and testing
├── notebooks/             # Jupyter notebooks for data exploration and model building
├── src/                   # Source code for feature engineering, model building, and preprocessing
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── utils.py
├── logs/                  # Directory for logging information
├── tests/                 # Unit tests for the project
├── README.md              # This readme file
├── requirements.txt       # List of dependencies
├── app.py                 # Flask API for URL prediction
├── main.py                # Command-line script for URL prediction
└── config.yaml            # Configuration file for various settings
```
Technologies Used
  - Python: The primary language for this project.
  - Flask: For building the API to make predictions.
  - scikit-learn: For implementing machine learning algorithms.
  - pandas: For data manipulation and feature engineering.
  - matplotlib and seaborn: For visualizing the data and evaluation results.
  - joblib: For saving and loading the trained model.
  - dvc: For version control of data and models.
License
This project is licensed under the MIT License - see the LICENSE file for details.

---

### Key Points:
1. **Overview**: A brief description of the project, its goal, and use case.
2. **Features**: A breakdown of the different features used for classification.
3. **Installation**: Instructions for setting up the project, including dependencies and cloning the repo.
4. **Usage**: Details on how to use the project either via the command line or Flask API.
5. **Model Evaluation**: Information about the evaluation metrics used to assess the model’s performance.
6. **Project Structure**: Description of the folder structure and what each folder/file contains.
7. **Technologies Used**: A list of the libraries and frameworks used in the project.
8. **License**: Mention the project’s license.

This README provides an in-depth overview of the project and helps users set up and run the project easily.
