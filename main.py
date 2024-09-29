import streamlit as st

st.title("AI Scraper")
url = st.text_input("Enter the URL")    

if st.button("Scrape"):
    st.write("Scraping data from", url)