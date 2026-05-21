# Fraud Detection System using Machine Learning

An end-to-end machine learning project for detecting fraudulent financial transactions using multiple ML models and an interactive Streamlit web application.

---

## Project Overview

This project focuses on detecting fraudulent transactions using machine learning techniques on highly imbalanced financial transaction data.

The project includes:
- Data preprocessing
- Feature engineering
- Exploratory Data Analysis (EDA)
- Logistic Regression
- Random Forest Classifier
- Model comparison
- Streamlit deployment

---

## Features

- Detects potentially fraudulent transactions
- Interactive web application using Streamlit
- Compare predictions using:
  - Logistic Regression
  - Random Forest
- Displays fraud probability
- Real-time prediction system

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib

---

## Machine Learning Workflow

### Data Preprocessing
- Removed unnecessary columns
- One-hot encoding for transaction types
- Feature engineering using balance differences
- Handled imbalanced data

### Models Used
1. Logistic Regression
2. Random Forest Classifier

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

---

## Project Structure

```bash
fraud_detection/
│── app.py
│── logistic_model.pkl
│── random_forest_model.pkl
│── analysis_model.ipynb
│── requirements.txt
│── README.md
```

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/raghavvvvv21/fraud-detection-system.git
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

---

## Results

| Model | Precision | Recall | F1-score |
|---|---|---|---|
| Logistic Regression | High Recall | Lower Precision | Moderate |
| Random Forest | Better Balance | Better Precision | Strong Overall |

Random Forest provided the best balance between fraud detection capability and false positive reduction.

---

## Future Improvements

- XGBoost implementation
- Hyperparameter tuning
- Real-time transaction API integration
- Better UI/UX
- Cloud deployment

---

## Author

Raghav Sahu
