import streamlit as st
import requests
import time

# Define the Flask API endpoint
API_ENDPOINT = "https://placement-predictor-adt9.onrender.com/predict"

# Set the page configuration
st.set_page_config(page_title="Campus Placement Prediction", layout="wide")

# Function to submit the form data to the Flask API
def get_prediction(data):
    response = requests.post(API_ENDPOINT, json=data)
    return response.json()

# Title and description
st.title("Will you be placed at Plaksha?")
st.markdown("Enter your details below to predict!")

# Form
with st.form(key='placement_form'):
    col1, col2, col3 = st.columns(3)

    with col1:
        mba_p = st.number_input("Plaksha TLF CGPA: [4-10]", min_value=4., max_value=10., step=0.1) * 10
        workex = st.selectbox("Work Experience", options=["No", "Yes"], index=0)
        degree_t = st.selectbox("UG Degree Type", options=["Comm&Mgmt", "Others", "Sci&Tech"], index=0)
        degree_p = st.number_input("UG Degree CPI: [4-10]", min_value=4., max_value=10., step=0.1) * 10

    with col2:
        hsc_s = st.selectbox("Class 12th Stream", options=["Arts", "Commerce", "Science"], index=0)
        hsc_b = st.selectbox("Class 12th Board", options=["Central", "Others"], index=0)
        hsc_p = st.number_input("Class 12th %age: [40-100]", min_value=40., max_value=100., step=1.)

    with col3:
        gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
        ssc_b = st.selectbox("Class 10th Board", options=["Central", "Others"], index=0)
        ssc_p = st.number_input("Class 10th %age: [40-100]", min_value=40., max_value=100., step=1.)
    submit_button = st.form_submit_button(label='Predict')

# Convert form inputs to appropriate format
if submit_button:
    data = {
        "ssc_p": ssc_p,
        "hsc_p": hsc_p,
        "degree_p": degree_p,
        "mba_p": mba_p,
        "gender": 0 if gender == "Male" else 1,
        "ssc_b": 0 if ssc_b == "Central" else 1,
        "hsc_b": 0 if hsc_b == "Central" else 1,
        "hsc_s": {"Arts": 0, "Commerce": 1, "Science": 2}[hsc_s],
        "degree_t": {"Comm&Mgmt": 0, "Others": 1, "Sci&Tech": 2}[degree_t],
        "workex": 0 if workex == "No" else 1,
    }

    # Clear previous prediction
    st.header("Prediction Result")
    prediction_placeholder = st.empty()
    time.sleep(0.5)  # Add a small delay for the vanishing effect

    # Call the API to get the prediction
    prediction = get_prediction(data)
    prediction_text = prediction.get('prediction', 'No result')

    # Display the new result
    prediction_placeholder.markdown(f"**Thou shall be:** {prediction_text}")

# Footer with project details
st.markdown("""
<br><br><br>
<div style="text-align: center;">
    <p>Project by</p>
    <h2>Gariman Singh</h2>
    <p>
        MS Physics & Data Science, IISER Mohali <br>
        Plaksha Tech Leaders Fellowship <br>
        <a href="https://github.com/Gariman01" target="_blank">
            GitHub
        </a>   &nbsp;
        <a href="https://www.linkedin.com/in/gariman-singh-643b9149/" target="_blank">
            Linkedin
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
