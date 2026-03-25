# app.py
import streamlit as st
from logic import calculate_bmi_logic 

st.title("حاسبة مؤشر كتلة الجسم 🩺")

w = st.number_input("الوزن (kg):", value=70.0)
l = st.number_input("الطول (cm):", value=170.0)

if st.button("احسب الآن"):
   
    bmi_val, category = calculate_bmi_logic(w, l)
    
    st.metric("الـ BMI الخاص بك", f"{bmi_val:.2f}")
    st.success(f"التصنيف: {category}")