import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/profile.jpg")

with col2:
    st.title("Chandra Swaroop Reddy Vuppuluri")
    content = """Student in Software Engineering with extensive knowledge in software design and application development. 
    Fluent in English with excellent communication and interpersonal skills. A fast learner with strong time management and multi-tasking skills.
    Strong work ethics in team or individual settings to drive product success and process efficiency. Strong troubleshooting and problem-solving skills with an analytical mindset."""
    st.info(content)