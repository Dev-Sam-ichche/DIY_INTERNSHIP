import streamlit as st
import pandas as pd
import numpy as np

# page setup
st.set_page_config(page_title="DIY Internship Task 2", layout="wide")

st.title("DIY Internship Task 2")
st.subheader("Basic Dashboard & Data Analysis")

# load data
df = pd.read_csv("Data/train_and_test2.csv")

# fix column name
df.rename(columns={"2urvived": "Survived"}, inplace=True)
df.rename(columns={"Pclass": "PassengerClass"}, inplace=True)

# decode columns
df["Sex"] = df["Sex"].map({0: "Male", 1: "Female"})
df["PassengerClass"] = df["PassengerClass"].map({1:"First Class",2:"Second class",3:"Third class"})
df["Survived"] = df["Survived"].map({0: "Not Survived", 1: "Survived"})

df["Embarked"] = df["Embarked"].map({
    0: "Cherbourg",
    1: "Queenstown",
    2: "Southampton"
})

# family status
df["Family Status"] = df.apply(
    lambda x: "With Family" if x["sibsp"] > 0 else "Alone",
    axis=1
)


# show data
st.write("### Dataset Preview")
st.dataframe(df.head(10))

# metrics
st.write("### Key Metrics")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Passengers", df.shape[0])
c2.metric("Male", (df["Sex"] == "Male").sum())
c3.metric("Female", (df["Sex"] == "Female").sum())
c4.metric("Survived", (df["Survived"] == "Survived").sum())
c5.metric("Not Survived", (df["Survived"] == "Not Survived").sum())

# charts
st.write("### Analysis Charts")

col1, col2 = st.columns(2)

with col1:
    st.write("Gender Distribution")
    st.bar_chart(df["Sex"].value_counts())

with col2:
    st.write("Passenger Class")
    st.bar_chart(df["PassengerClass"].value_counts().sort_index())

col3, col4 = st.columns(2)

with col3:
    st.write("Survival Status")
    st.bar_chart(df["Survived"].value_counts())

with col4:
    st.write("Family Status")
    st.bar_chart(df["Family Status"].value_counts().sort_index())

st.success("Task 2 completed successfully")