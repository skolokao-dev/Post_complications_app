import streamlit as st
import xgboost as xgb
import pandas as pd
import numpy as np

# Загружаем модель
model = xgb.Booster()
model.load_model("xgboost_model.json")  # твоя модель в формате JSON

st.title("Prediction of Post-Operative Complications")

# Ввод данных пользователем
age = st.number_input("Age", min_value=0, max_value=120, value=45)
gender = st.selectbox("Gender", ["Male", "Female"])
wbc = st.number_input("WBC", value=6.5)
hct = st.number_input("HCT", value=40.2)
hb = st.number_input("Hb", value=13.8)
platelets = st.number_input("Platelets", value=250)

# Кнопка для предсказания
if st.button("Predict"):
    gender_val = 1 if gender == "Male" else 0
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender_val,
        "wbc": wbc,
        "hct": hct,
        "hb": hb,
        "platelets": platelets
    }])
    dmatrix = xgb.DMatrix(input_data)
    pred = model.predict(dmatrix)[0]
    st.success(f"Predicted probability of complications: {pred*100:.5f}%")
