import streamlit as st

st.title("Centralized Learning Management System")

st.sidebar.title("Menu")
menu = st.sidebar.selectbox("Select", ["Dashboard","Students","Courses"])

if menu == "Dashboard":
    st.header("Dashboard")
    st.write("Total Students: 200")
    st.write("Total Courses: 10")

elif menu == "Students":
    st.header("Students")
    st.write("Student data will appear here")

elif menu == "Courses":
    st.header("Courses")
    st.write("Course details will appear here")
