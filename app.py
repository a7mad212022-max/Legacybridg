import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# إعداد الربط
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🐑 برنامج النطحة المضحكة")

uploaded_file = st.file_uploader("ارفع صورتك:", type=["jpg", "png", "jpeg"])

if uploaded_file and st.button("نطحة مضحكة!"):
    with st.spinner('جاري تحليل صورتك...'):
        try:
            # معالجة الصورة بشكل صحيح
            img = Image.open(uploaded_file)
            
            # تحويل الصورة إلى bytes لضمان عدم حدوث خطأ أثناء الإرسال
            buf = io.BytesIO()
            img.save(buf, format='JPEG')
            byte_im = buf.getvalue()
            
            # تجهيز الطلب
            image_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": byte_im
                }
            ]
            
            prompt = "صف مشهداً مضحكاً جداً لخروف ينطح الشخص الموجود في الصورة، اكتب وصفاً قصيراً ومباشراً لاستخدامه في توليد صورة."
            
            # الاتصال بـ Gemini
            response = model.generate_content([prompt, image_parts])
            
            # توليد الصورة
            image_description = response.text.replace(" ", "%20")
            image_url = f"https://image.pollinations.ai/prompt/{image_description}?width=512&height=512"
            
            st.image(image_url, caption="نطحة العيد!")
            
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
            st.write("تأكد أن مفتاح API في الـ Secrets صحيح ولا يحتوي على مسافات.")
