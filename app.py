import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="LMS Dashboard", layout="wide")

# Dark style
st.markdown("""
<style>
body{
    background-color:#0f172a;
    color:white;
}
.card {
    background-color:#1e293b;
    padding:20px;
    border-radius:10px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Centralized Learning Management System")

# Top cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Total Students", "320")

with col2:
    st.metric("📚 Total Courses", "18")

with col3:
    st.metric("📝 Assignments Submitted", "245")

st.divider()

# Charts section
col4, col5 = st.columns(2)

data = pd.DataFrame(
    np.random.randn(12,2),
    columns=["Attendance","Marks"]
)

with col4:
    st.subheader("Student Performance Trend")
    st.line_chart(data)

with col5:
    st.subheader("Assignment Statistics")
    st.bar_chart(data)

st.divider()

# Bottom charts
col6, col7 = st.columns(2)

pie_data = pd.DataFrame({
    "Type":["Assignments","Courses","Students"],
    "Count":[120,15,300]
})

with col6:
    st.subheader("System Distribution")
    st.dataframe(pie_data)

with col7:
    st.subheader("Weekly Activity")
    activity = pd.DataFrame(
        np.random.randint(10,50,(7,1)),
        columns=["Activity"]
    )
    st.bar_chart(activity)
