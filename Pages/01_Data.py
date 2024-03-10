import streamlit as st
import pyodbc 
import pandas as pd

st.set_page_config(
    page_title='View Data',
    page_icon=' ',
    layout='wide'
)


st.title('A Telco Customer Churn Data from Vodafone')

@st.cache_resource (show_spinner='Connecting to Database....')
def initialize_connection():
    connection = pyodbc.connect("DRIVER={SQL Server};SERVER="
                                + st.secrets["SERVER"]
                                + ";DATABASE="
                                + st.secrets["DATABASE"]
                                + ";UID="
                                + st.secrets["UID"]
                                + ";PWD="
                                + st.secrets["PWD"])
    return connection
conn = initialize_connection()

def query_database(query):
    
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        df = pd.DataFrame.from_records(data=rows, columns=[column[0] for column in cur.description])
    return df

# Main function to run the Streamlit app
def main():
    # Query data from the database
    query = "SELECT * FROM LP2_Telco_churn_first_3000"
    df = query_database(query)

    # Sidebar selection widget
    option = st.sidebar.selectbox('Select display option:', ('All Features', 'Numerical Columns', 'Categorical Columns'))

    # Display selected data based on user's choice
    if option == 'All Features':
        st.write(df)
    elif option == 'Numerical Columns':
        st.write(":1234: Numeric Columns")
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        st.write(df[numerical_columns])
    elif option == 'Categorical Columns':
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        st.write(df[categorical_columns])

        # Add column descriptions under the table
    st.markdown("### Column Descriptions:")
    st.markdown("- **Gender**: Whether the customer is a male or a female")
    st.markdown("- **SeniorCitizen**: Whether a customer is a senior citizen or not")
    st.markdown("- **Partner**: Whether the customer has a partner or not (Yes, No)")
    st.markdown("- **Dependents**: Whether the customer has dependents or not (Yes, No)")
    st.markdown("- **Tenure**: Number of months the customer has stayed with the company")
    st.markdown("- **Phone Service**: Whether the customer has a phone service or not (Yes, No)")
    st.markdown("- **MultipleLines**: Whether the customer has multiple lines or not")
    st.markdown("- **InternetService**: Customer's internet service provider (DSL, Fiber Optic, No)")
    st.markdown("- **OnlineSecurity**: Whether the customer has online security or not (Yes, No, No Internet)")
    st.markdown("- **OnlineBackup**: Whether the customer has online backup or not (Yes, No, No Internet)")
    st.markdown("- **DeviceProtection**: Whether the customer has device protection or not (Yes, No, No internet service)")
    st.markdown("- **TechSupport**: Whether the customer has tech support or not (Yes, No, No internet)")
    st.markdown("- **StreamingTV**: Whether the customer has streaming TV or not (Yes, No, No internet service)")
    st.markdown("- **StreamingMovies**: Whether the customer has streaming movies or not (Yes, No, No Internet service)")
    st.markdown("- **Contract**: The contract term of the customer (Month-to-Month, One year, Two year)")
    st.markdown("- **PaperlessBilling**: Whether the customer has paperless billing or not (Yes, No)")
    st.markdown("- **Payment Method**: The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))")
    st.markdown("- **MonthlyCharges**: The amount charged to the customer monthly")
    st.markdown("- **TotalCharges**: The total amount charged to the customer")
    st.markdown("- **Churn**: Whether the customer churned or not (Yes or No)")


if __name__ == "__main__":
    main()