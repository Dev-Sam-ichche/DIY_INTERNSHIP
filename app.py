import streamlit as st

from task_1app import task1
from task_2app import task2
from task_3app import task3
from task_4app import task4
from task_5app import task5
from task_6app import task6

st.set_page_config(page_title="DIY Internship Dashboard", layout="wide")

st.title("DIY Internship Complete Dashboard")

# sidebar navigation
page = st.sidebar.radio(
    "Select Task",
    [
        "Task 1: Data Loading",
        "Task 2: Analysis",
        "Task 3: Interactivity",
        "Task 4: Dynamic Filters",
        "Task 5: Structure",
        "Task 6: UI & UX"
    ]
)

if page == "Task 1: Data Loading":
    task1()

elif page == "Task 2: Analysis":
    task2()

elif page == "Task 3: Interactivity":
    task3()

elif page == "Task 4: Dynamic Filters":
    task4()   

elif page == "Task 5: Structure":
    task5()

elif page == "Task 6: UI & UX":
    task6()
