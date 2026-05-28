import streamlit as st
import openai

# إعدادات الواجهة
st.set_page_config(page_title="LegacyBridge MVP", page_icon="🚀")
st.title("🚀 LegacyBridge: تحديث الأنظمة القديمة")
st.subheader("حوّل كودك القديم إلى لغة حديثة في ثوانٍ")

# إدخال مفتاح الـ API (لجعل البرنامج يعمل)
api_key = st.sidebar.text_input("أدخل مفتاح OpenAI API", type="password")

# اختيار اللغات
source_lang = st.selectbox("اللغة القديمة", ["COBOL", "VB6", "Fortran", "C"])
target_lang = st.selectbox("اللغة الحديثة المطلوبة", ["Python", "Java", "Go", "Node.js"])

# منطقة رفع الكود
legacy_code = st.text_area("ضع الكود القديم هنا:", height=200)

if st.button("تحويل الآن"):
    if not api_key:
        st.error("يرجى إدخال مفتاح API أولاً.")
    elif not legacy_code:
        st.warning("يرجى وضع كود للتحويل.")
    else:
        try:
            openai.api_key = api_key
            prompt = f"قم بتحويل الكود التالي من {source_lang} إلى {target_lang}. قدم الكود فقط:"
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "أنت خبير في إعادة هندسة البرمجيات."},
                          {"role": "user", "content": f"{prompt}\n\n{legacy_code}"}]
            )
            
            st.success("تم التحويل بنجاح!")
            st.code(response.choices.message.content, language=target_lang.lower())
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
