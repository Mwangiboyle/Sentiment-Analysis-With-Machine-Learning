'''a streamlit app where a user inputs text and my model takes the input and makes predictions which is either 1 or 0. if 
0 returns negative else positive
'''
import streamlit as st
import joblib
import sklearn

# Load your models
svm = joblib.load('models\svm_pipeline.pkl')
multinomial = joblib.load('models\multinomial_pipeline.pkl')

# App title and description
st.title("Sentiment Analysis Tool")
st.write(
    '''
    Welcome to the Sentiment Analysis Tool! Enter a text and select a model to predict whether the sentiment is positive or negative.
    '''
)

# Create a selectbox for model selection
model_choice = st.selectbox(
    'Select a model to use:',
    ('svm', 'multinomial')
)

# Display selected model
st.write(f'You selected model: {model_choice}')

# Get user input
input_text = st.text_area("Enter your text here:")

# Ensure input text is not empty
if input_text.strip():  # Check if input text is not just whitespace
    if st.button('Submit'):
        try:
            # Perform prediction based on selected model
            if model_choice == 'svm':
                prediction = svm.predict([input_text])[0]
            else:
                prediction = multinomial.predict([input_text])[0]

            # Display prediction result
            if prediction == 0:
                st.error("Prediction: Negative 😢")
            else:
                st.success("Prediction: Positive 😀")
        except ValueError:
            st.error("Error: Unable to perform prediction. Please check your input.")
else:
    st.warning("Please enter some text before submitting.")
