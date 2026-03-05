import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="LMS Dashboard", layout="wide")

# ---------- Styling ----------
st.markdown("""
<style>
h1 {font-size:26px !important;}
h2 {font-size:18px !important;}
h3 {font-size:16px !important;}
.block-container{
    padding-top:1rem;
    padding-bottom:0rem;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Centralized Learning Management System")

# ---------- Top Metrics ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", "320")
col2.metric("Courses", "18")
col3.metric("Assignments", "245")
col4.metric("Avg Attendance", "89%")

# ---------- Sample Data ----------
marks_data = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May"],
    "Marks":[70,75,80,78,85]
})

attendance_data = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Attendance":[85,90,88,92,87]
})

course_data = pd.DataFrame({
    "Course":["Web","AI","Cloud","ML"],
    "Students":[110,80,70,60]
})

assignment_data = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Submissions":[20,30,25,35,40]
})

# ---------- Charts Row ----------
col5, col6, col7 = st.columns(3)

with col5:
    st.subheader("Student Performance")
    fig1 = px.line(marks_data,
                   x="Month",
                   y="Marks",
                   markers=True,
                   color_discrete_sequence=["#00f5a0"])

    fig1.update_layout(height=250,font=dict(size=10))
    st.plotly_chart(fig1,use_container_width=True)

with col6:
    st.subheader("Attendance Trend")
    fig2 = px.bar(attendance_data,
                  x="Day",
                  y="Attendance",
                  color="Attendance",
                  color_continuous_scale="viridis")

    fig2.update_layout(height=250,font=dict(size=10))
    st.plotly_chart(fig2,use_container_width=True)

with col7:
    st.subheader("Course Distribution")
    fig3 = px.pie(course_data,
                  names="Course",
                  values="Students",
                  hole=0.5)

    fig3.update_layout(height=250,font=dict(size=10))
    st.plotly_chart(fig3,use_container_width=True)

# ---------- Bottom Row ----------
col8, col9 = st.columns(2)

with col8:
    st.subheader("Assignment Activity")
    fig4 = px.area(assignment_data,
                   x="Day",
                   y="Submissions",
                   color_discrete_sequence=["#6366f1"])

    fig4.update_layout(height=250,font=dict(size=10))
    st.plotly_chart(fig4,use_container_width=True)

with col9:
    st.subheader("Attendance Table")

    table = pd.DataFrame({
        "Student":["Ravi","Anitha","Karthik","Divya","Arun"],
        "Attendance %":[90,85,95,88,92]
    })

    st.dataframe(table,use_container_width=True)
