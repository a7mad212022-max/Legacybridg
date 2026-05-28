import streamlit as stimport streamlit as st
import google.generativeai as genai

# البرنامج سيقرأ المفتاح تلقائياً من إعدادات المنصة
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("🐑 برنامج النطحة المضحكة")

uploaded_file = st.file_uploader("ارفع صورة شخص:", type=["jpg", "png"])

if uploaded_file and st.button("اجعلها مضحكة!"):
    st.success("تم الربط بنجاح! جاري معالجة الصورة...")
    # هنا سيتم لاحقاً إضافة كود معالجة الصورة عبر Gemini

import google.generativeai as genai

# البرنامج سيقرأ المفتاح تلقائياً من إعدادات المنصة
api_key = st.secrets["AIzaSyBzs_9BlEr9P_gIYgY8p9sBRD50tdqL91M"]
genai.configure(api_key=api_key)

st.title("🐑 برنامج النطحة المضحكة")

uploaded_file = st.file_uploader("ارفع صورة شخص:", type=["jpg", "png"])

if uploaded_file and st.button("اجعلها مضحكة!"):
    st.success("تم الربط بنجاح! جاري معالجة الصورة...")
    # هنا سيتم لاحقاً إضافة كود معالجة الصورة عبر Gemini
