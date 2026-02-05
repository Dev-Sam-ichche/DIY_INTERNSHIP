import streamlit as st
import pandas as pd

# page setup
st.set_page_config(page_title="DIY Internship Task 3", layout="wide")

st.title("DIY Internship – Task 3")
st.subheader("Interactive Data Dashboard")

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
df["Embarked"] = df["Embarked"].map({
    0: "Cherbourg",
    1: "Queenstown",
    2: "Southampton"
})

# family status
df["Family Status"] = df["sibsp"].apply(
    lambda x: "With Family" if x > 0 else "Alone"
)

st.sidebar.header("Filter Data")

# dropdown: gender
gender_option = st.sidebar.selectbox(
    "Select Gender",
    options=["All"] + df["Sex"].unique().tolist()
)

# dropdown: survival
survival_option = st.sidebar.selectbox(
    "Survival Status",
    options=["All"] + df["Survived"].unique().tolist()
)

# slider: age range
age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider(
    "Select Age Range",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max)
)

# input field: minimum fare
min_fare = st.sidebar.number_input(
    "Minimum Fare",
    min_value=0.0,
    value=0.0
)

filtered_df = df.copy()

if gender_option != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == gender_option]

if survival_option != "All":
    filtered_df = filtered_df[filtered_df["Survived"] == survival_option]

filtered_df = filtered_df[
    (filtered_df["Age"] >= age_range[0]) &
    (filtered_df["Age"] <= age_range[1]) &
    (filtered_df["Fare"] >= min_fare)
]

st.write("### Filtered Data Preview")
st.dataframe(filtered_df.head(10))

# metrics
st.write("### Key Metrics")

c1, c2, c3 = st.columns(3)

c1.metric("Total Passengers", filtered_df.shape[0])
c2.metric("Male", (filtered_df["Sex"] == "Male").sum())
c3.metric("Female", (filtered_df["Sex"] == "Female").sum())

# charts
st.write("### Visual Analysis")

col1, col2 = st.columns(2)

with col1:
    st.write("Passenger Class")
    st.bar_chart(filtered_df["PassengerClass"].value_counts().sort_index())

with col2:
    st.write("Family Status")
    st.bar_chart(filtered_df["Family Status"].value_counts())

st.write("Survival Status")
st.bar_chart(filtered_df["Survived"].value_counts())

st.success("Task 3 interactive dashboard done")
