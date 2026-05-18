import streamlit as st
import requests

st.set_page_config(page_title="CreditCheck MVP", page_icon="🛡️")

# עיצוב בסיסי ב-CSS כדי שהכפתורים ייראו טוב
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ CreditCheck AI")
st.write("מערכת ניתוח אשראי למשכירים - דמו למשקיעים")

# טופס להזנת נתונים
with st.form("credit_form"):
    st.header("פרטי השוכר והנכס")
    
    full_name = st.text_input("שם מלא של השוכר")
    income = st.number_input("הכנסה חודשית", min_value=0)
    
    st.markdown("---")
    st.header("העלאת מסמכים")
    credit_report = st.file_uploader("העלה דוח אשראי (PDF)", type="pdf")
    id_photo = st.file_uploader("העלה צילום תעודת זהות (JPG/PNG)", type=["jpg", "png", "pdf"])

    submitted = st.form_submit_button("שלח לבדיקה והפק דוח")

# לוגיקה של בדיקה ושליחה
if submitted:
    # 1. בדיקה שכל השדות מולאו
    if not full_name or not email_to or not credit_report:
        st.error("❌ חסרים פרטים! חובה למלא שם, מייל ולהעלות דוח אשראי.")
    else:
        with st.spinner('מעבד נתונים ושולח למייל...'):
            # כתובת ה-API של Formspree (תחליף בכתובת שתקבל מהם)
            # לבינתיים זה ישלח "הצלחה" מדומה למשקיעים
            formspree_url = "https://formspree.io/f/maqknejk" # כאן תדביק את הלינק שתייצר
            
            data = {
                "name": full_name,
                "income": income,
                "email_target": "email@g.com",
                "status": "Submitted for analysis"
            }
            
            # הדמיה של שליחה מוצלחת
            st.success(f"✅ תודה {full_name}! הקבצים נבדקו ונשלחו לכתובת {email_to}")
            st.balloons()
            
            st.info("במערכת המלאה, כאן יופיע ניתוח אוטומטי של הדגלים האדומים מה-PDF.")