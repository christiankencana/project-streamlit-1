import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title('My First Streamlit App')

# Header
st.header('Dashboard Sederhana')

# Text input
name = st.text_input('Masukkan nama Anda:')
if name:
    st.write(f'Halo, {name}!')

# Slider
age = st.slider('Pilih umur:', 0, 100, 25)
st.write(f'Umur Anda: {age}')

# Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)