import streamlit as st
import pandas as pd


def task5():
    # page setup
    st.set_page_config(page_title="DIY Internship Task 5", layout="wide")

    st.title("DIY Internship – Task 5")
    st.subheader("Multi-Tab Dashboard for Structured Analysis")

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

    # create tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Overview", "Gender & Class", "Survival", "Family"]
    )


    # TAB 1: Overview

    with tab1:
        st.header("Overview")
        st.metric("Total Passengers", df.shape[0])
        st.write("Dataset Preview")
        st.dataframe(df.head(10))

    # TAB 2: Gender & Class

    with tab2:
        st.header("Gender & Passenger Class Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Gender Distribution")
            st.bar_chart(df["Sex"].value_counts())

        with col2:
            st.write("Passenger Class Distribution")
            st.bar_chart(df["PassengerClass"].value_counts().sort_index())

    # TAB 3: Survival

    with tab3:
        st.header("Survival Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Survival Status")
            st.bar_chart(df["Survived"].value_counts())

        with col2:
            st.write("Survival by Gender")
            st.bar_chart(df.groupby("Sex")["Survived"].value_counts().unstack())


    # TAB 4: Family

    with tab4:
        st.header("Family Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Family Status")
            st.bar_chart(df["Family Status"].value_counts())

        with col2:
            st.write("Survival by Family Status")
            st.bar_chart(
                df.groupby("Family Status")["Survived"]
                .value_counts()
                .unstack()
            )

    st.success("Task 5 completed: dashboard structured using multiple tabs")
