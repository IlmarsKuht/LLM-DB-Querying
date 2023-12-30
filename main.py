import streamlit as st
from langchain_helper import get_answer

st.title("T Shirts: Database Q&A")

question = st.text_input("Question: ")

if question:
    answer = get_answer(question)

    st.header("Answer")
    st.write(answer)






