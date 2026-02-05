import streamlit as st
import pandas as pd

st.title("DIY Internship Task 1")
st.subheader("Dataset Loading & Preprocessing using Pandas")

# Load dataset
data = "Data/train_and_test2.csv"
df = pd.read_csv(data)

st.write("Raw Dataset")
st.dataframe(df)

# Preprocessing
st.write("Preprocessing Steps")

# 1. Check missing values
missing = df.isnull().sum()
st.write("Missing Values:", missing)

# 2. Rename columns
df.columns = [col.replace("_", " ").title() for col in df.columns]

# 3. Basic statistics
st.write("Dataset Statistics")
st.write(df.describe())

st.success("Dataset loaded and preprocessed successfully")
