import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="LMS Dashboard", layout="wide")

# Smaller fonts and colorful background
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-size:14px;
}
.main {
    background-color:#0f172a;
}
.metric-box{
    background: linear-gradient(90deg,#6366f1,#22c55e);
    padding:10px;
    border-radius:10px;
    text-align:center;
    color:white;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Centralized Learning Management System")

# Top metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("👨‍🎓 Students", "320")
col2.metric("📚 Courses", "18")
col3.metric("📝 Assignments", "245")
col4.metric("📅 Attendance Avg", "89%")

# Sample data
days = ["Mon","Tue","Wed","Thu","Fri"]
attendance = [85,90,88,92,87]

marks_data = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May"],
    "Average Marks":[70,75,80,78,85]
})

activity = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri"],
    "Submissions":[20,30,25,35,40]
})

course_data = pd.DataFrame({
    "Course":["AI","ML","Cloud","Web"],
    "Students":[80,60,70,110]
})

# Charts
col5, col6, col7 = st.columns(3)

with col5:
    st.subheader("📈 Student Performance")
    fig = px.line(marks_data, x="Month", y="Average Marks", markers=True,
                  color_discrete_sequence=["#22c55e"])
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("📊 Attendance Trend")
    fig2 = px.bar(x=days, y=attendance,
                  color=attendance,
                  color_continuous_scale="viridis")
    st.plotly_chart(fig2, use_container_width=True)

with col7:
    st.subheader("📚 Course Distribution")
    fig3 = px.pie(course_data,
                  names="Course",
                  values="Students",
                  hole=0.5,
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig3, use_container_width=True)

# Bottom charts
col8, col9 = st.columns(2)

with col8:
    st.subheader("📝 Assignment Activity")
    fig4 = px.area(activity,
                   x="Day",
                   y="Submissions",
                   color_discrete_sequence=["#6366f1"])
    st.plotly_chart(fig4, use_container_width=True)

with col9:
    st.subheader("📋 Attendance Table")

    table = pd.DataFrame({
        "Student":["Ravi","Anitha","Karthik","Divya","Arun"],
        "Attendance %":[90,85,95,88,92]
    })

    st.dataframe(table, use_container_width=True)
