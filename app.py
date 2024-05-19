import streamlit as st
import requests

# Define the Flask API endpoint
API_ENDPOINT = "https://placement-predictor-adt9.onrender.com/predict"

# Set the page configuration
st.set_page_config(page_title = "Campus Placement Prediction", layout = "wide")

# Function to submit the form data to the Flask API
def get_prediction(data):
    response = requests.post(API_ENDPOINT, json=data)
    return response.json()

# Title and description
st.title("Campus Placement Prediction")
st.markdown("Enter Details for forecast.")

# Form
with st.form(key='placement_form'):
    col1, col2, col3 = st.columns(3)

    with col1:
        ssc_p = st.number_input("SSC PR%: [45-100]", min_value=45, max_value=100, step=1)
        hsc_p = st.number_input("HSC PR%: [45-100]", min_value=45, max_value=100, step=1)
        degree_p = st.number_input("Degree PR%: [35-100]", min_value=35, max_value=100, step=1)
        etest_p = st.number_input("etest_p: [0-100]", min_value=0, max_value=100, step=1)

    with col2:
        mba_p = st.number_input("mba_p: [0-100]", min_value=0, max_value=100, step=1)
        gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
        ssc_b = st.selectbox("SSC Board", options=["Central", "Others"], index=0)
        hsc_b = st.selectbox("HSC Board", options=["Central", "Others"], index=0)

    with col3:
        hsc_s = st.selectbox("HSC Stream", options=["Arts", "Commerce", "Science"], index=0)
        degree_t = st.selectbox("Degree Type", options=["Comm&Mgmt", "Others", "Sci&Tech"], index=0)
        workex = st.selectbox("Work Experience", options=["No", "Yes"], index=0)
        specialisation = st.selectbox("Specialisation", options=["Mkt&Fin", "Mkt&HR"], index=0)

    submit_button = st.form_submit_button(label='Predict')

# Convert form inputs to appropriate format
if submit_button:
    data = {
        "ssc_p": ssc_p,
        "hsc_p": hsc_p,
        "degree_p": degree_p,
        "etest_p": etest_p,
        "mba_p": mba_p,
        "gender": 0 if gender == "Male" else 1,
        "ssc_b": 0 if ssc_b == "Central" else 1,
        "hsc_b": 0 if hsc_b == "Central" else 1,
        "hsc_s": {"Arts": 0, "Commerce": 1, "Science": 2}[hsc_s],
        "degree_t": {"Comm&Mgmt": 0, "Others": 1, "Sci&Tech": 2}[degree_t],
        "workex": 0 if workex == "No" else 1,
        "specialisation": 0 if specialisation == "Mkt&Fin" else 1
    }

    # Call the API to get the prediction
    prediction = get_prediction(data)
    prediction_text = prediction.get('prediction', 'No result')

    # Display the result
    st.header("Prediction Result")
    st.markdown(f"**Student will be:** {prediction_text}")

# Footer with project details
st.markdown("""
<br><br><br>
<div style="text-align: center;">
    <p>Project by</p>
    <h2>Gariman Singh</h2>
    <p>
	MS Physics & Data Science, IISER Mohali <br>
	Plaksha Tech Leaders Fellowship <br>
	<a href = "https://www.linkedin.com/in/gariman-singh-643b9149/"> LinkedIn </a>
    </p>

</div>
""", unsafe_allow_html=True)
