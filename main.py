import streamlit as st
from latitude import AI
from bs4 import BeautifulSoup

st.title("Response Brief")

customer = st.text_input("Customer Name", placeholder="Doofenshmirtz Evil Inc.")
transcript = st.file_uploader("Upload Interview Transcript", type=["txt", "docx"], accept_multiple_files=True)
products = st.text_input("Additional Products", placeholder="Product A: Description ")

if st.button("Generate Response Brief") and transcript:
    merged_transcript = ""
    for i, file in enumerate(transcript):
        merged_transcript += f"<transcript>{file.getvalue().decode("utf-8")}</transcript>\n"

    ai = AI()
    audience_understand = BeautifulSoup(ai.get_audience_understand(merged_transcript, customer), 'html.parser').find("response").get_text()
    audience_believe = BeautifulSoup(ai.get_audience_believe(merged_transcript, products, customer), 'html.parser').find("response").get_text()
    products = BeautifulSoup(ai.get_products(merged_transcript, products, customer), 'html.parser').find("response").get_text()
    
    with st.spinner("Generating Response Brief..."):
        with st.expander("What Is The One Thing We Want The Audience To Understand?"):
            st.write(audience_understand)
        with st.expander("Why Should They Believe This?"):
            st.write(audience_believe)
        with st.expander("What Products/Services Should Be Featured in the Story?"):
            st.write(products)