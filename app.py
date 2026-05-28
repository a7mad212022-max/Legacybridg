import streamlit as st
import google.generativeai as genai

# البرنامج يقرأ المفتاح من إعدادات الـ Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("🐑 برنامج النطحة المضحكة")

uploaded_file = st.file_uploader("ارفع صورة شخص:", type=["jpg", "png"])

if uploaded_file and st.button("اجعلها مضحكة!"):
    st.success("تم الربط بنجاح! جاري معالجة الصورة...")
