import streamlit as st
from multiapp import MultiApp
from apps import qna, summary

st.title("""
QnA and Summarizer tool

""")

app = MultiApp()
app.add_app("QnA", qna.app)
app.add_app("Summarizer", summary.app)
app.run()
