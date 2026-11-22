import streamlit as st

st.set_page_config(
    page_title="Steviana Nutrition",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 STEVIANA")
st.subheader("مساعدك الذكي للتغذية ومتابعة الوزن")
st.write("أهلاً بك في عالم التغذية الصحية بنكهة سعودية 🇸🇦")

st.divider()

st.header("بيانات المستخدم")

name = st.text_input("الاسم")
age = st.number_input("العمر", 18, 100, 30)
gender = st.selectbox("الجنس", ["ذكر", "أنثى"])
weight = st.number_input("الوزن (كجم)", 30.0, 250.0, 80.0)
height = st.number_input("الطول (سم)", 100.0, 230.0, 170.0)

goal = st.selectbox(
    "ما هدفك؟",
    ["تخفيف الوزن", "المحافظة على الوزن", "زيادة الوزن"]
)

if st.button("احصل على نتيجتك"):
    bmi = weight / ((height / 100) ** 2)

    st.success(f"مرحباً {name}، أهلاً بك مع ستيفيانا!")

    st.metric("مؤشر كتلة الجسم BMI", round(bmi, 1))

    if bmi < 18.5:
        st.info("المؤشر ضمن فئة نقص الوزن.")
    elif bmi < 25:
        st.info("المؤشر ضمن فئة الوزن الطبيعي.")
    elif bmi < 30:
        st.info("المؤشر ضمن فئة زيادة الوزن.")
    else:
        st.info("المؤشر ضمن فئة السمنة.")

    st.subheader("نصيحتنا لك")

    if goal == "تخفيف الوزن":
        st.write("اهتم بتوازن الوجبات والبروتين والخضار والنشاط البدني.")
    elif goal == "المحافظة على الوزن":
        st.write("حافظ على تنوع الطعام وانتظام النشاط البدني.")
    else:
        st.write("اهتم بالوجبات المتوازنة وزيادة مصادر البروتين والطاقة.")

    st.divider()
    st.subheader("🍽️ وصفات سعودية صحية مقترحة")

    recipes = {
        "الفطور": "فول وخبز بر وخضار",
        "الغداء": "كبسة دجاج بكمية أرز معتدلة وسلطة",
        "العشاء": "تونة مع خبز أسمر وزبادي"
    }

    for meal, recipe in recipes.items():
        st.write(f"**{meal}:** {recipe}")

    st.caption("هذه معلومات إرشادية وليست بديلاً عن استشارة أخصائي التغذية.")

st.divider()
st.write("🌿 Steviana | صحتك تبدأ باختياراتك")
