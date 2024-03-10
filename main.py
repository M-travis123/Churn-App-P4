import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Display the icon and page name using HTML formatting
st.markdown("<h1 style='text-align: center; color: black;'>🏠 Home Page</h1>", unsafe_allow_html=True)

# Define the login page content
def login_page():
    st.title("Login to Vodafone Churn Predictor")
    username = st.text_input("Username", value="username")
    password = st.text_input("Password", type="password", value="password")
    if st.button("Login"):
        if username == "username" and password == "password":
            st.success("Login successful!")
            st.session_state.is_authenticated = True
        else:
            st.error("Authentication failed. Please try again.")

# Define the main page content
# Define the main page content
# Define the main page content
def main():
    # Title/Header
    st.title("Welcome to Vodafone Churn Predictor")
    st.write("This app helps predict customer churn and provides insights into customer data.")

    # Introduction
    st.markdown("## Introduction")
    st.write("""
    Customer churn is a critical concern for businesses. Predicting churn accurately can help businesses implement proactive retention strategies. 
    With the Vodafone Churn Predictor, you can explore customer data, visualize trends, make predictions, and track historical churn rates.
    """)

    # Page Overview
    st.markdown("## Page Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Data Page")
        st.write("View the data used for prediction, including both numerical and categorical columns.")

        st.subheader("🔮 Predict Page")
        st.write("Make predictions on customer churn based on selected features.")

    with col2:
        st.subheader("📈 Dashboard")
        st.write("Explore visualizations and metrics to gain insights into churn rates and customer behavior.")

        st.subheader("📅 History Page")
        st.write("Track historical churn rates and predictions.")

    # Quick Start Guide
    st.markdown("## Quick Start Guide")
    st.write("""
    1. Log in with your credentials.
    2. Explore the Data Page to view the dataset and make predictions on the Predict Page.
    3. Navigate to the Dashboard to explore visualizations and metrics.
    4. Track historical churn rates and predictions on the History Page.
    5. For support or inquiries, contact us at monica.nyambura@azubiafrica.org
    """)

# Check if the user is authenticated
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

# Show login page if not authenticated, otherwise show main page
if not st.session_state.is_authenticated:
    login_page()
else:
    main()
