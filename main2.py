import streamlit as st
from latitude import AI
from bs4 import BeautifulSoup
from exa_py import Exa
from streamlit_card import card
from datetime import datetime, timedelta

if 'all_posts' not in st.session_state:
    st.session_state.all_posts = []

st.title("Brainstorming")
exa = Exa(api_key="e906685b-1d9a-4f8e-9cf5-5d4720d06cf3")

sectors = st.multiselect("Select Sectors", ["Construction", "Healthcare", "Finance", "Technology", "Retail", "Education", "Manufacturing", "Transportation", "Hospitality", "Energy", "Agriculture", "Media", "Government", "Nonprofit"])
platform = st.pills("Select Platform", [{"Reddit": "reddit.com"}, {"Twitter": "twitter.com"}, {"LinkedIn": "linkedin.com"}, {"Web Article":""}], format_func=lambda x: list(x.keys())[0])

def get_ideas(sectors, platform):
    all_posts = []
    for sector in sectors:
        search_query = f"Here are some popular stories in the field of {sector} in the last 1 month"
        if list(platform.keys())[0] == "Web Article":
            response = exa.search_and_contents(
                search_query,
                type="auto",
                num_results=10,
                summary=True
            )
        else:
            response = exa.search_and_contents(
                search_query,
                type="auto",
                include_domains=list(platform.values()),
                num_results=10
            )
        posts = response.results
        all_posts.extend(posts)
    return all_posts

if st.button("Generate Brainstorming Ideas") and sectors:
    ai = AI()
    with st.spinner("Generating Brainstorming Ideas..."):
        st.session_state.all_posts = get_ideas(sectors, platform)

num_columns = 3  # Number of columns in the grid
columns = st.columns(num_columns)
for i, post in enumerate(st.session_state.all_posts):
    col = columns[i % num_columns]
    with col:
        res = card(
            title=post.title,
            text=datetime.strptime(post.published_date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%B %d, %Y"),
            url=post.url,
            image="https://placekitten.com/500/500",  # Placeholder image
            styles={
                "card": {
                    "width": "100%",
                    "height": "140px",
                    "border-radius": "12px",
                    "box-shadow": "0 2px 4px rgba(0,0,0,0.08)",
                    "margin": "16px",
                    "padding": "24px",
                    "text-align": "left",
                    "transition": "all 0.2s ease",
                    "cursor": "pointer"
                },
                "title": {
                    "font-size": "12px",
                    "font-weight": "600",
                    "margin-bottom": "8px",
                    "line-height": "1.4",
                    "color": "black"
                },
                "text": {
                    "font-size": "15px",
                    "margin-bottom": "8px",
                    "line-height": "1.5",
                    "color": "grey"
                },
                "url": {
                    "font-size": "14px",
                    "color": "grey",
                    "text-decoration": "none",
                    "display": "inline-block"
                },
                 "filter": {
                    "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
                }
            }
        )