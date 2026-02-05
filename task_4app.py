import streamlit as st
import pandas as pd

# page setup
st.set_page_config(page_title="DIY Internship Task 4", layout="wide")

st.title("DIY Internship Task 4")
st.subheader("Dynamic Updates Using Streamlit Re-run Logic")

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

if "gender" not in st.session_state:
    st.session_state.gender = "All"

if "survival" not in st.session_state:
    st.session_state.survival = "All"

st.sidebar.header("Interactive Controls")

st.session_state.gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + df["Sex"].unique().tolist()
)

st.session_state.survival = st.sidebar.selectbox(
    "Survival Status",
    ["All"] + df["Survived"].unique().tolist()
)

age_min, age_max = int(df["Age"].min()), int(df["Age"].max())

age_range = st.sidebar.slider(
    "Age Range",
    age_min,
    age_max,
    (age_min, age_max)
)

min_fare = st.sidebar.number_input(
    "Minimum Fare",
    min_value=0.0,
    value=0.0
)

filtered_df = df.copy()

if st.session_state.gender != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == st.session_state.gender]

if st.session_state.survival != "All":
    filtered_df = filtered_df[filtered_df["Survived"] == st.session_state.survival]

filtered_df = filtered_df[
    (filtered_df["Age"] >= age_range[0]) &
    (filtered_df["Age"] <= age_range[1]) &
    (filtered_df["Fare"] >= min_fare)
]

st.write("### Updated Data Preview")
st.dataframe(filtered_df.head(10))

st.write("### Live Metrics")

c1, c2, c3 = st.columns(3)

c1.metric("Total Passengers", filtered_df.shape[0])
c2.metric("Male", (filtered_df["Sex"] == "Male").sum())
c3.metric("Female", (filtered_df["Sex"] == "Female").sum())

st.write("### Live Charts")

col1, col2 = st.columns(2)

with col1:
    st.write("Passenger Class")
    st.bar_chart(filtered_df["PassengerClass"].value_counts().sort_index())

with col2:
    st.write("Family Status")
    st.bar_chart(filtered_df["Family Status"].value_counts())

st.write("Survival Status")
st.bar_chart(filtered_df["Survived"].value_counts())

st.success("Task 4 completed: visuals update dynamically based on user input")
