import streamlit as st
import pandas as pd
import joblib

lr_model = joblib.load('logistic_model.pkl')
rf_model = joblib.load('logistic_model.pkl')

st.title("Fraud Detection App")

st.markdown(
    "Enter the transaction details below and click the Predict button."
)

st.divider()

model_choice = st.selectbox(
    "Choose Model",
    ["Logistic Regression", "Random Forest"]
)

transaction_type = st.selectbox(
    "Transaction Type",
    ['CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER', 'DEPOSIT']
)

amount = st.number_input(
    'Amount',
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    'Old Balance Origin',
    min_value=0.0,
    value=5000.0
)

newbalanceOrig = st.number_input(
    'New Balance Origin',
    min_value=0.0,
    value=4000.0
)

oldbalanceDest = st.number_input(
    'Old Balance Destination',
    min_value=0.0,
    value=2000.0
)

newbalanceDest = st.number_input(
    'New Balance Destination',
    min_value=0.0,
    value=3000.0
)

balanceDiffOrig = oldbalanceOrg - newbalanceOrig
balanceDiffDest = newbalanceDest - oldbalanceDest

st.write("Balance Difference Origin:", balanceDiffOrig)
st.write("Balance Difference Destination:", balanceDiffDest)

if st.button("Predict Fraud"):

    type_CASH_OUT = 1 if transaction_type == "CASH_OUT" else 0
    type_DEBIT = 1 if transaction_type == "DEBIT" else 0
    type_PAYMENT = 1 if transaction_type == "PAYMENT" else 0
    type_TRANSFER = 1 if transaction_type == "TRANSFER" else 0

    input_data = pd.DataFrame([{
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'balanceDiffOrig': balanceDiffOrig,
        'balanceDiffDest': balanceDiffDest,
        'type_CASH_OUT': type_CASH_OUT,
        'type_DEBIT': type_DEBIT,
        'type_PAYMENT': type_PAYMENT,
        'type_TRANSFER': type_TRANSFER
    }])

    if model_choice == "Logistic Regression":
        model = lr_model
    else:
        model = rf_model

    prediction = model.predict(input_data)[0]
    prediction_prob = model.predict_proba(input_data)[0][1]

    st.subheader(f"Model Used: {model_choice}")

    if prediction == 1:
        st.error("Fraudulent Transaction Detected")
    else:
        st.success("Transaction Looks Safe")

    st.write(f"Fraud Probability: {prediction_prob:.2%}")

    with st.expander("View Input Data"):
        st.write(input_data)