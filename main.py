import streamlit as st
from latitude import AI
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from io import StringIO

st.title("Story Brief")

AI = AI()
transcript = st.file_uploader("Upload Interview Transcript", type=["txt", "docx", "pdf"])
speakers = st.text_input("Speakers", placeholder="Speaker A, Speaker B")
material1 = st.file_uploader("Upload Material 1", type=["docx", "txt", "pdf"])
material2 = st.file_uploader("Upload Material 2", type=["docx", "txt", "pdf"])
material3 = st.file_uploader("Upload Material 3", type=["docx", "txt", "pdf"])

if st.button("Generate Story Brief") and transcript:
    transcript_text = transcript.getvalue().decode("utf-8")
    material1_text = StringIO(material1.getvalue().decode("utf-8")).read() if material1 else ""
    material2_text = StringIO(material2.getvalue().decode("utf-8")).read() if material2 else ""
    material3_text = StringIO(material3.getvalue().decode("utf-8")).read() if material3 else ""
    brief = AI.get_story_brief(transcript_text, speakers, material1_text, material2_text, material3_text)

    brief = BeautifulSoup(brief, 'html.parser').find("response").get_text()
    st.markdown(brief)