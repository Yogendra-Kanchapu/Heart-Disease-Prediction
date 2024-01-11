import streamlit as st
import numpy as np
import pickle

# load the model using pickle
with open('decision_tree_model.pkl', 'rb') as file:  
    model = pickle.load(file)

# Define the structure of your web app
def main():
    st.title("Heart Disease Prediction")

    # Define inputs
    age = st.number_input('Age', min_value=1, max_value=100, value=25)
    sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    restbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, value=120)
    chol = st.number_input('Serum Cholestoral in mg/dl', min_value=100, max_value=600, value=200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2])
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=120)
    thal = st.selectbox('Thalassemia', options=[1, 2, 3])

    # Predict button
    if st.button('Predict'):
        # Prepare the feature vector for prediction
        features = np.array([[age, sex, restbps, chol, fbs, restecg, thalach, thal]])
        prediction = model.predict(features)

        # Output the prediction
        st.success(f'The predicted class is: {prediction[0]}')
        
__main__ : main()
