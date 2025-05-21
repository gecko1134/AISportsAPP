
import streamlit as st
import pandas as pd

def run():
    st.title("📄 PDF Report Generator")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        st.write("✅ Ready to generate PDF (mock preview)")
