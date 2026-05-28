import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد الربط
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🐑 برنامج النطحة المضحكة")

uploaded_file = st.file_uploader("ارفع صورتك:", type=["jpg", "png", "jpeg"])

if uploaded_file and st.button("نطحة مضحكة!"):
    with st.spinner('جاري تحليل صورتك...'):
        try:
            # 1. فتح الصورة باستخدام PIL مباشرة
            img = Image.open(uploaded_file)
            
            # 2. إرسال الصورة مباشرة إلى Gemini (بدون تحويل معقد)
            prompt = "صف مشهداً مضحكاً لخروف ينطح الشخص في هذه الصورة. اكتب وصفاً دقيقاً ومباشراً."
            response = model.generate_content([prompt, img])
            
            # 3. توليد الصورة
            description = response.text.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{description}?width=512&height=512"
            
            st.image(image_url, caption="نطحة العيد!")
            st.success("تم!")
            
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
