import streamlit as st
from transformers import pipeline


def app():    
    
    st.subheader('Question Answering')
    context = st.text_area(label = 'Context', height = 300, placeholder = 'Enter your Context here.')
    question = st.text_input(label = 'Question', placeholder = 'Enter your Question here.')

    if st.button('Ask'):   

        model_name = "distilbert-base-cased-distilled-squad"

        nlp = pipeline('question-answering', model = model_name, tokenizer = model_name, device = -1)

        QA_input = {
        'question': question,
        'context': context
        }

        res = nlp(QA_input)
        st.markdown(res['answer'])