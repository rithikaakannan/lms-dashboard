import streamlit as st

st.set_page_config(page_title="LMS Login", layout="centered")

# Sample users
students = {
    "student1": "1234",
    "student2": "abcd"
}

faculty = {
    "faculty1": "admin",
    "faculty2": "pass123"
}

# Session login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = ""

# Login page
if not st.session_state.logged_in:

    st.title("📚 LMS Login")

    role = st.selectbox("Login As", ["Student", "Faculty"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    login = st.button("Login")

    if login:

        if role == "Student":
            if username in students and students[username] == password:
                st.session_state.logged_in = True
                st.session_state.role = "Student"
                st.success("Student Login Successful")
                st.rerun()
            else:
                st.error("Invalid Student ID or Password")

        if role == "Faculty":
            if username in faculty and faculty[username] == password:
                st.session_state.logged_in = True
                st.session_state.role = "Faculty"
                st.success("Faculty Login Successful")
                st.rerun()
            else:
                st.error("Invalid Faculty ID or Password")

# Dashboard after login
else:

    st.sidebar.success(f"Logged in as {st.session_state.role}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("📊 LMS Dashboard")

    if st.session_state.role == "Student":
        st.write("Welcome Student 👨‍🎓")
        st.write("View Courses, Assignments, Attendance")

    if st.session_state.role == "Faculty":
        st.write("Welcome Faculty 👩‍🏫")
        st.write("Manage Students, Upload Assignments, Track Attendance")import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="LMS Dashboard", layout="wide")

# ---------- Compact Styling ----------
st.markdown("""
<style>
h1 {font-size:22px !important;}
h2 {font-size:16px !important;}
h3 {font-size:14px !important;}

.block-container{
    padding-top:0.5rem;
    padding-bottom:0rem;
}

div[data-testid="metric-container"] {
    padding:5px;
}

</style>
""", unsafe_allow_html=True)

st.title("📚 LMS Dashboard")

# ---------- Top Metrics ----------
c1, c2, c3, c4 = st.columns(4)

c1.metric("Students", "320")
c2.metric("Courses", "18")
c3.metric("Assignments", "245")
c4.metric("Attendance", "89%")

# ---------- Data ----------
marks = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May"],
    "Marks":[70,75,80,78,85]
})

attendance = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Attendance":[85,90,88,92,87]
})

courses = pd.DataFrame({
    "Course":["Web","AI","Cloud","ML"],
    "Students":[110,80,70,60]
})

assignments = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Submissions":[20,30,25,35,40]
})

# ---------- Charts ----------
col1, col2, col3 = st.columns(3)

with col1:
    fig1 = px.line(marks, x="Month", y="Marks", markers=True)
    fig1.update_layout(height=180, margin=dict(l=0,r=0,t=20,b=0), font=dict(size=9))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(attendance, x="Day", y="Attendance", color="Attendance")
    fig2.update_layout(height=180, margin=dict(l=0,r=0,t=20,b=0), font=dict(size=9))
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = px.pie(courses, names="Course", values="Students", hole=0.5)
    fig3.update_layout(height=180, margin=dict(l=0,r=0,t=20,b=0), font=dict(size=9))
    st.plotly_chart(fig3, use_container_width=True)

# ---------- Bottom Section ----------
col4, col5 = st.columns(2)

with col4:
    fig4 = px.area(assignments, x="Day", y="Submissions")
    fig4.update_layout(height=180, margin=dict(l=0,r=0,t=20,b=0), font=dict(size=9))
    st.plotly_chart(fig4, use_container_width=True)

with col5:
    table = pd.DataFrame({
        "Student":["Ravi","Anitha","Karthik","Divya","Arun"],
        "Attendance %":[90,85,95,88,92]
    })

    st.dataframe(table, height=180, use_container_width=True)
