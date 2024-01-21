import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Anbarasan Muthu")
    content = """I'm Anbarasan Muthu, a recent graduate in Information Technology. 
    My passion for continuous learning drives me to explore new horizons, whether it's through reading books or staying updated on the latest technologies. 
    As a junior Python developer, I'm excited to apply my skills and contribute to the dynamic field of IT with a focus on Python development."""
    st.info(content)