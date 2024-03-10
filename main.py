import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


# Set Streamlit page config
st.set_page_config(
    page_title='About',
    layout='wide',
    page_icon='🏠'
)

# Load configuration from YAML file
try:
    with open('C:/Users/HP/Desktop/P4-Churn App/Churn-App-P4/config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Config file not found. Please check the file path.")

# Authenticate users
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# User authentication
name, authentication_status, username = authenticator.login(location='sidebar')


if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar', key='logout-button')

    # Main content
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

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Enter username and password to use the app.')
    st.code("""
            Test Account
            Username: nyambura
            Password: 123456""")
