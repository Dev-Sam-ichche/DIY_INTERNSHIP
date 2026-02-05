import streamlit as st
import pandas as pd

# page setup
st.set_page_config(
    page_title="DIY Internship Task 6",
    layout="wide"
)

# custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    h1, h2, h3 {
        color: #1f2937;
    }
    .metric-container {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# title
st.title("DIY Internship – Task 6")
st.subheader("Improved UI with CSS & Better Layout")

# load data
df = pd.read_csv("Data/train_and_test2.csv")

# fix column names
df.rename(
    columns={
        "2urvived": "Survived",
        "Pclass": "PassengerClass"
    },
    inplace=True
)

# decode columns
df["Sex"] = df["Sex"].map({0: "Male", 1: "Female"})
df["Survived"] = df["Survived"].map({0: "Not Survived", 1: "Survived"})

# family status
df["Family Status"] = df["sibsp"].apply(
    lambda x: "With Family" if x > 0 else "Alone"
)

# sidebar
st.sidebar.header("Filters")
gender = st.sidebar.selectbox("Gender", ["All"] + df["Sex"].unique().tolist())

# filter data
filtered_df = df.copy()
if gender != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == gender]

# metrics
st.write("### Key Metrics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Total Passengers", filtered_df.shape[0])

with c2:
    st.metric("Male", (filtered_df["Sex"] == "Male").sum())

with c3:
    st.metric("Female", (filtered_df["Sex"] == "Female").sum())

# charts
st.write("### Visual Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("Passenger Class Distribution")
    st.bar_chart(filtered_df["PassengerClass"].value_counts().sort_index())

with col2:
    st.write("Survival Status")
    st.bar_chart(filtered_df["Survived"].value_counts())

st.write("Family Status")
st.bar_chart(filtered_df["Family Status"].value_counts())

st.success("Task 6 completed: improved visual appeal and usability")
