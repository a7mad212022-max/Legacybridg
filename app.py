import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد Gemini
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🐑 برنامج النطحة المضحكة")

uploaded_file = st.file_uploader("ارفع صورتك:", type=["jpg", "png"])

if uploaded_file and st.button("نطحة مضحكة!"):
    with st.spinner('جاري تحليل صورتك وتجهيز المشهد...'):
        # 1. تحليل الصورة بواسطة Gemini للحصول على وصف
        img = Image.open(uploaded_file)
        prompt = "أعطني وصفاً دقيقاً ومضحكاً لصورة تحتوي على خروف ينطح هذا الشخص، اجعل الوصف مناسباً لمولد صور."
        response = model.generate_content([prompt, img])
        
        # 2. إنشاء رابط الصورة المضحكة باستخدام Pollinations AI
        # هذا الرابط يحول الوصف إلى صورة فوراً
        image_description = response.text.replace(" ", "%20")
        image_url = f"https://image.pollinations.ai/prompt/{image_description}?width=512&height=512"
        
        st.subheader("النتيجة:")
        st.image(image_url, caption="نطحة العيد!")
        st.success("تم إنتاج المشهد بنجاح!")
