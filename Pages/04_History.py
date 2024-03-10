import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='View Data',
    page_icon=' ',
    layout='wide'
)

# Function to load historic predictions
def show_historic_predictions():
    csv_path = "./data/history.csv"
    df = pd.read_csv(csv_path)
    return df

if __name__ == "__main__":
    st.title('Prediction History')
    historic_df = show_historic_predictions()
    st.dataframe(historic_df)