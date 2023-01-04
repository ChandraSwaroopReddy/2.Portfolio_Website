import streamlit as st
import pandas

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
    st.write("Address: 4 Robin CT, Hicksville, New York, 11801")
    st.write("Phone no: +1 (516)-513-4576")
    st.write("Mail: swarp039@gmail.com")
    st.write("LinkedIn: www.linkedin.com/in/chandra-vuppuluri")
    st.write("GitHub: https://github.com/ChandraSwaroopReddy")

st.title("Project Experience")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for inder, row in df[10:].iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
