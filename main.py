import streamlit as st
from latitude import AI
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from io import StringIO

st.title("Story Brief")

AI = AI()
transcript = st.text_area("Interview Transcript", placeholder="00:00 Hey There!")
speakers = st.text_input("Speakers", placeholder="Speaker A, Speaker B")
material1 = st.text_area("Material 1", placeholder="Material 1 Content")
material2 = st.text_area("Material 2", placeholder="Material 2 Content")
material3 = st.text_area("Material 3", placeholder="Material 3 Content")


if st.button("Generate Story Brief") and transcript:
    with st.spinner("Generating Story Brief..."):
        brief = AI.get_story_brief(transcript, speakers, material1, material2, material3)

        brief = BeautifulSoup(brief, 'html.parser').find("response").get_text()
        st.markdown(brief)