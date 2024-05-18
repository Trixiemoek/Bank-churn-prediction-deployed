# -*- coding: utf-8 -*-
"""streamlit_app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HezOaSkEhs5kepRz57UJHmBGYrRuJbfg
"""

# Importing relevant packages
import pandas as pd
import streamlit as st
from joblib import load

# Load pre-trained model
model = load('model.pkl')

# Define function to make predictions using the model
def predict_churn(input_df):
    predictions = model.predict(input_df)
    return ['Yes' if prediction == 1 else 'No' for prediction in predictions]

# Main function for Streamlit web app
def main():
    # Set page title
    st.set_page_config(page_title="Bank Customer Churn Prediction")

    # Display header
    st.title("Bank Customer Churn Prediction App")

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        input_df = pd.read_csv(uploaded_file)

        # Display the input DataFrame
        st.write("Uploaded CSV file:")
        st.write(input_df)

        # Make predictions when button is clicked
        if st.button("Predict Churn"):
            churn_predictions = predict_churn(input_df)
            input_df['Churn Prediction'] = churn_predictions
            st.write("Predictions:")
            st.write(input_df)

# Run the main function if the script is executed
if __name__ == '__main__':
    main()
# Importing relevant packages
import pandas as pd
import streamlit as st
from joblib import load

# Load pre-trained model
model = load('model.pkl')

# Define function to make predictions using the model
def predict_churn(input_df):
    predictions = model.predict(input_df)
    return ['Yes' if prediction == 1 else 'No' for prediction in predictions]

# Main function for Streamlit web app
def main():
    # Set page title
    st.set_page_config(page_title="Bank Customer Churn Prediction")

    # Display header
    st.title("Bank Customer Churn Prediction App")

    # File upload
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        input_df = pd.read_csv(uploaded_file)

        # Display the input DataFrame
        st.write("Uploaded CSV file:")
        st.write(input_df)

        # Make predictions when button is clicked
        if st.button("Predict Churn"):
            churn_predictions = predict_churn(input_df)
            input_df['Churn Prediction'] = churn_predictions
            st.write("Predictions:")
            st.write(input_df)

# Run the main function if the script is executed
if __name__ == '__main__':
    main()