import streamlit as st
from transformers import pipeline


def app():    
    
    st.subheader('Summarization')
    article = st.text_area(label = 'Article', height = 300, placeholder = 'Enter your article here.')

    if st.button('Summarize'):
        
        summarizer = pipeline("summarization", model = "sshleifer/distilbart-cnn-6-6", device = -1)

        summary = summarizer(article)

        st.write(summary[0]['summary_text'])
