import streamlit as st
import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title='View Data',
    page_icon='📈',
    layout='wide'
)

st.title(' :bar_chart: My Customer Churn Dashboard')


# Load the data

df = pd.read_csv(r'C:\Users\HP\Desktop\P4-Churn App\Churn-App-P4\data\training_data.csv')


# Define a function to display visualizations
def display_visualizations(df):
    st.subheader('Visualizations')

    # Set style
    sns.set_style('whitegrid')

    # Create columns layout
    col1, col2 = st.columns(2)

    # Chart for Gender
    with col1:
        st.write("### Gender Distribution")
        gender_counts = df['gender'].value_counts()
        fig_gender = plt.figure(figsize=(10, 6))
        gender_plot = sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='pastel')
        gender_plot.set_title('Gender Distribution')
        gender_plot.set_xlabel('Gender')
        gender_plot.set_ylabel('Count')
        st.pyplot(fig_gender)

    # Chart for Tenure
    with col2:
        st.write("### Tenure Distribution")
        fig_tenure = plt.figure(figsize=(10, 6))
        tenure_plot = sns.histplot(df['tenure'], bins=20, kde=True, color='skyblue')
        tenure_plot.set_title('Tenure Distribution')
        tenure_plot.set_xlabel('Tenure')
        tenure_plot.set_ylabel('Frequency')
        st.pyplot(fig_tenure)

         #  Display the heatmap using Streamlit
    with col1:
        st.write('### Correlation Matrix Heatmap')
        correlation_matrix = df[['tenure', 'MonthlyCharges', 'TotalCharges']].corr()
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        st.pyplot(heatmap.figure)

    with col2:
        # Display the distribution of SeniorCitizen
        st.write("### Distribution of SeniorCitizen")
        senior_citizen_counts = df['SeniorCitizen'].value_counts()
        plt.figure(figsize=(8, 6))
        senior_citizen_plot = sns.barplot(x=senior_citizen_counts.index, y=senior_citizen_counts.values, palette='pastel')
        senior_citizen_plot.set_title('Distribution of SeniorCitizen')
        senior_citizen_plot.set_xlabel('SeniorCitizen')
        senior_citizen_plot.set_ylabel('Count')
        senior_citizen_plot.grid(False)
        st.pyplot(plt)

def display_kpi_dashboard(df):
    st.subheader('Visualizations')

    # Display in two columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Senior Citizen vs. Churn")

        senior_churn_counts = df.groupby('SeniorCitizen')['Churn'].value_counts().unstack()
        fig, ax = plt.subplots()
        senior_churn_counts.plot(kind='bar', stacked=False, ax=ax)
        ax.set_xlabel('Senior Citizen')
        ax.set_ylabel('Count')
        ax.set_title('Senior Citizen vs. Churn')
        ax.grid(False)  # Remove grid lines
        st.pyplot(fig)

        # Contract Type vs. Churn
        st.write("### Contract Type vs. Churn")
        contract_churn_counts = df.groupby('Contract')['Churn'].value_counts().unstack()
        fig, ax = plt.subplots()
        contract_churn_counts.plot(kind='bar', stacked=False, ax=ax)
        ax.set_xlabel('Contract Type')
        ax.set_ylabel('Count')
        ax.set_title('Contract Type vs. Churn')
        ax.grid(False)  # Remove grid lines
        st.pyplot(fig)

        # Payment Method vs. Churn
        st.write("### Payment Method vs. Churn")
        payment_churn_counts = df.groupby('PaymentMethod')['Churn'].value_counts().unstack()
        fig, ax = plt.subplots()
        payment_churn_counts.plot(kind='bar', stacked=False, ax=ax)
        ax.set_xlabel('Payment Method')
        ax.set_ylabel('Count')
        ax.set_title('Payment Method vs. Churn')
        ax.grid(False)  # Remove grid lines
        st.pyplot(fig)

    with col2:
        # Gender vs. Churn
        st.write("### Gender vs. Churn")
        gender_churn_counts = df.groupby('gender')['Churn'].value_counts().unstack()
        fig, ax = plt.subplots()
        gender_churn_counts.plot(kind='bar', stacked=False, ax=ax)
        ax.set_xlabel('Gender')
        ax.set_ylabel('Count')
        ax.set_title('Gender vs. Churn')
        ax.grid(False)  # Remove grid lines
        st.pyplot(fig)

        # pie chart for churn percentage
        st.write('### Churn vs. No Churn Percentage')
        churn_counts = df['Churn'].value_counts()
        labels = ['No', 'Yes']
        values = churn_counts.values
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
        ax.axis('equal')
        ax.set_title('Churn vs. No Churn Percentage')
        ax.grid(False)
        st.pyplot(fig)



# Dashboard menu at the top
dashboard_option = st.sidebar.radio("Select Dashboard", ["EDA Dashboard", "KPI Dashboard"])

# Content of the selected dashboard
if dashboard_option == "EDA Dashboard":
    st.write("This is the EDA Dashboard")
    display_visualizations(df)
elif dashboard_option == "KPI Dashboard":
    st.write("This is the KPI Dashboard")
    display_kpi_dashboard(df)