
import streamlit as st
import pandas as pd

def run():
    st.title("📊 Budget Visualizer")
    uploaded_file = st.file_uploader("Upload budget CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.bar_chart(df.set_index(df.columns[0]))
