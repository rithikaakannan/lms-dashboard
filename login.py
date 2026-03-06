import streamlit as st

st.set_page_config(page_title="LMS Login", layout="centered")

# Student and Faculty login data
students = {
    "student1": "1234",
    "student2": "abcd"
}

faculty = {
    "faculty1": "admin",
    "faculty2": "pass123"
}

st.title("📚 Centralized Learning Management System")
st.subheader("Login Portal")

role = st.selectbox("Login as", ["Student", "Faculty"])

username = st.text_input("Username")
password = st.text_input("Password", type="password")

login = st.button("Login")

if login:

    if role == "Student":
        if username in students and students[username] == password:
            st.success("Student Login Successful")
            st.write("Open dashboard file to view LMS dashboard")
        else:
            st.error("Invalid Student ID or Password")

    if role == "Faculty":
        if username in faculty and faculty[username] == password:
            st.success("Faculty Login Successful")
            st.write("Open dashboard file to view LMS dashboard")
        else:
            st.error("Invalid Faculty ID or Password")
