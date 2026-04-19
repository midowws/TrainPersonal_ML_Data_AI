import streamlit as st
import joblib
import pandas as pd

model_rf = joblib.load('model_random_forest.pkl')

st.title("Iris Species Predictor")

sl = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sw = st.slider("Sepal Width", 2.0, 4.4, 3.5)
pl = st.slider("Petal Length", 1.0, 7.0, 1.4)
pw = st.slider("Petal Width", 0.1, 2.5, 0.2)

data_list = [[sl, sw, pl, pw]]

nama_bunga = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

if st.button("Predict"):
    prediksi = model_rf.predict(data_list)
    st.success(f"Predicted Iris Species: {nama_bunga[prediksi[0]]}")
    