import streamlit as st
import google.generativeai as genai

# هذه الخانة ستظهر في التطبيق ليتمكن المستخدم من وضع المفتاح
api_key = st.sidebar.text_input("AIzaSyBzs_9BlEr9P_gIYgY8p9sBRD50tdqL91M", type="password")

if api_key:
    genai.configure(api_key=api_key)
    st.success("تم ربط Gemini بنجاح!")
