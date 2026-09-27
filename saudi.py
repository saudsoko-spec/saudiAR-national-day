import random
import streamlit as set_page_config_alias  # لضمان التوافقية
import streamlit as st

# إعداد صفحة الموقع وتصميم الثيم الفخم المستوحى من الهوية الوطنية (عزنا بطبعنا)
st.set_page_config(
    page_title="اليوم الوطني السعودي - عزنا بطبعنا",
    page_icon="🇸🇦",
    layout="centered",
)

# تخصيص التصميم والواجهة المستوحاة تماماً من قالب العرض التقديمي
st.markdown(
    """
    <style>
    /* إخفاء عناصر التحكم الافتراضية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: linear-gradient(135deg, #041410 0%, #07221b 50%, #030a08 100%);
        color: #ffffff;
        font-family: 'Tahoma', sans-serif;
    }

    /* الهيدر العام والشعار */
    .hero-container {
        background: linear-gradient(145deg, #072a22 0%, #031510 100%);
        border: 2px solid #d4af37;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.7);
    }
    .hero-title {
        color: #ffffff;
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 5px;
    }
    .hero-badge {
        background: rgba(212, 175, 55, 0.15);
        color: #ffd700;
        padding: 6px 20px;
        border-radius: 25px;
        border: 1px solid #d4af37;
        display: inline-block;
        font-size: 18px;
        font-weight: bold;
        margin-top: 8px;
    }

    /* الثيم المستوحى من إطار الباوربوينت المرفق لصفحات الأسئلة */
    .ppt-question-frame {
        background-color: #073027;
        border: 3px solid #d4af37;
        padding: 35px 30px;
        border-radius: 25px;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 30px rgba(0,0,0,0.6);
        margin-bottom: 25px;
        text-align: center;
    }

    /* تصميم الأزرار الموحدة */
    .stButton>button {
        background: linear-gradient(135deg, #0d382e 0%, #08261e 100%);
        color: #ffffff;
        border: 1px solid #d4af37;
        border-radius: 12px;
        font-size: 17px;
        font-weight: bold;
        width: 100%;
        padding: 14px 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #d4af37 0%, #b3922f 100%);
        color: #051612;
        border: 1px solid #ffffff;
        transform: translateY(-2px);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# قاعدة بيانات الأسئلة (3 أسئلة مختارة بدقة لكل موضوع)
topics_data = {
    "أسئلة عامة عن اليوم الوطني السعودي": [
        {
            "q": "ما هو الشعار الرسمي المعتمد لليوم الوطني السعودي؟",
            "options": ["عزنا بطبعنا", "نحلم ونحقق", "همة حتى القمة", "رؤيتنا تهندس المستقبل"],
            "answer": "عزنا بطبعنا",
        },
        {
            "q": "في أي عام ميلادي تم إعلان توحيد المملكة العربية السعودية؟",
            "options": ["1932", "1902", "1950", "1920"],
            "answer": "1932",
        },
        {
            "q": "ما هو التاريخ الميلادي الثابت للاحتفال باليوم الوطني كل عام؟",
            "options": ["23 سبتمبر", "1 يناير", "15 أغسطس", "30 نوفمبر"],
            "answer": "23 سبتمبر",
        },
    ],
    "مدن المملكة العربية السعودية": [
        {
            "q": "ما هي العاصمة الإدارية والسياسية للمملكة العربية السعودية؟",
            "options": ["الرياض", "جدة", "مكة المكرمة", "الدمام"],
            "answer": "الرياض",
        },
        {
            "q": "ما هي المدينة التي تُلقب بـ 'عروس البحر الأحمر'؟",
            "options": ["جدة", "ينبع", "الخبر", "أملج"],
            "answer": "جدة",
        },
        {
            "q": "ما هو الاسم الإداري للمنطقة التي تقع فيها مدينة حائل؟",
            "options": ["منطقة حائل", "منطقة القصيم", "منطقة تبوك", "منطقة الجوف"],
            "answer": "منطقة حائل",
        },
    ],
    "تاريخ وحضارة السعودية": [
        {
            "q": "في أي عام تم تأسيس الدولة السعودية الأولى (إمارة الدرعية)؟",
            "options": ["1727", "1932", "1785", "1688"],
            "answer": "1727",
        },
        {
            "q": "من هو مؤسس الدولة السعودية الأولى؟",
            "options": [
                "الإمام محمد بن سعود",
                "الملك عبد العزيز",
                "الإمام تركي بن عبد الله",
                "الإمام سعود الكبير",
            ],
            "answer": "الإمام محمد بن سعود",
        },
        {
            "q": "ما هو الحي التاريخي الشهير في الدرعية والذي يُعد مسجلاً في اليونسكو؟",
            "options": ["حي الطريف", "حي البجيري", "حي المربع", "حي السفارات"],
            "answer": "حي الطريف",
        },
    ],
    "مدن السعودية": [
        {
            "q": "ما هي المدينة التاريخية التي تضم موقع 'مدائن صالح' (الحجر) الأثري؟",
            "options": ["العلا", "تبوك", "حائل", "المدينة المنورة"],
            "answer": "العلا",
        },
        {
            "q": "ما هو الجبلين الشهيرين اللذين يقترنان بذكر مدينة حائل دائماً في الشعر والموروث؟",
            "options": ["أجا وسلمى", "أحد وثبير", "طويق وجبل قانون", "السروات ولبن"],
            "answer": "أجا وسلمى",
        },
        {
            "q": "ما هي المدينة الملقبة بـ 'بوابة الحرمين الشريفين' الكبرى للقادمين بحراً وجواً؟",
            "options": ["جدة", "الرياض", "الدمام", "الجبيل"],
            "answer": "جدة",
        },
    ],
    "ثقافة المملكة العربية السعودية": [
        {
            "q": "ما هي الرقصة الشعبية الرسمية الأولى في المملكة التي تُؤدى بالسيف؟",
            "options": [
                "العرضة السعودية",
                "السامري",
                "الدحّة",
                "المزكاة أو الخبيتي",
            ],
            "answer": "العرضة السعودية",
        },
        {
            "q": "ما هو اللباس التقليدي الأصيل للرجل السعودي في المناسبات الوطنية؟",
            "options": [
                "الثوب والشماغ (أو الغترة)",
                "البشت والعمامة فقط",
                "الملابس الغربية الرسمية",
                "العباءة والملابس الرياضية",
            ],
            "answer": "الثوب والشماغ (أو الغترة)",
        },
        {
            "q": "ما هي المشروبات التقليدية التي تُعد رمزاً أصيلاً للكرم والضيافة السعودية؟",
            "options": [
                "القهوة السعودية (بالهيل والقرنفل)",
                "القهوة الفرنسية",
                "الشاي الأسود الثقيل فقط",
                "عصير الفواكه الطازجة",
            ],
            "answer": "القهوة السعودية (بالهيل والقرنفل)",
        },
    ],
}

# تهيئة المتغيرات
if "page" not in st.session_state:
    st.session_state.page = "home"
if "current_topic" not in st.session_state:
    st.session_state.current_topic = None
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = []
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "shuffled_options_cache" not in st.session_state:
    st.session_state.shuffled_options_cache = {}

# --- الصفحة الرئيسية ---
if st.session_state.page == "home":
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 10px;">
            <span style="background-color: #0b352b; color: #d4af37; padding: 6px 18px; border-radius: 15px; border: 1px solid #d4af37; font-weight: bold; font-size: 15px;">
                🎓 University of Hail — مشروع اليوم الوطني
            </span>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="hero-container">
            <h1 class="hero-title">اليوم الوطني السعودي</h1>
            <div class="hero-badge">عِزُّنا بطبِعنا</div>
            <p style="font-size: 16px; color: #cfdcd6; margin-top: 12px; line-height: 1.5;">
                منصة تفاعلية وطلبية لاختبار المعلومات. امسح الرمز أدناه للانتقال للموقع فوراً من هاتفك!
            </p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    # عرض QR Code خفيف ونظيف مرتبط بموقعك السحابي
    col_qr1, col_qr2, col_qr3 = st.columns([1, 2, 1])
    with col_qr2:
        st.markdown(
            "<div style='text-align: center; color: #d4af37; font-weight: bold; margin-bottom: 8px;'>📱 رمز الاستجابة السريعة (QR Code):</div>",
            unsafe_allow_html=True,
        )
        # ضع رابط موقعك السحابي الحقيقي هنا لكي يعمل الكود بدقة عند الزوار
        live_app_url = "https://saudiar-national-day-bjjwdthbwqune7uudg3ssm.streamlit.app/"
        qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data={live_app_url}"
        st.markdown(
            f"""
            <div style="text-align: center; background: #073027; padding: 15px; border-radius: 15px; border: 2px solid #d4af37; display: inline-block; width: 100%;">
                <img src="{qr_api_url}" alt="QR Code" style="border-radius: 8px;">
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<h3 style='text-align: center; color: #d4af37; margin: 25px 0 15px 0;'>✨ اختر موضوع التحدي (3 أسئلة سريعة) ✨</h3>",
        unsafe_allow_html=True,
    )

    topics_list = list(topics_data.keys())
    for i, topic in enumerate(topics_list, 1):
        if st.button(
            f"الموضوع ({i}) ⟵  {topic}", key=f"topic_btn_{i}", use_container_width=True
        ):
            st.session_state.current_topic = topic
            q_list = topics_data[topic].copy()
            random.shuffle(q_list)
            st.session_state.shuffled_questions = q_list
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.shuffled_options_cache = {}
            st.session_state.page = "quiz"
            st.rerun()

# --- صفحة الأسئلة ---
elif st.session_state.page == "quiz":
    topic = st.session_state.current_topic
    q_list = st.session_state.shuffled_questions
    idx = st.session_state.q_index
    total_q = len(q_list)

    st.progress((idx + 1) / total_q)

    st.markdown(
        f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="color: #d4af37; font-weight: bold; font-size: 19px;">{topic}</span>
            <div style="color: #a3c1ad; font-size: 14px; margin-top: 3px;">السؤال {idx + 1} من {total_q}</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    current_q = q_list[idx]

    st.markdown(
        f"""
        <div class="ppt-question-frame">
            <h2 style="color: #ffffff; line-height: 1.6; margin: 0; font-size: 22px;">{current_q['q']}</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if idx not in st.session_state.shuffled_options_cache:
        opts = current_q["options"].copy()
        random.shuffle(opts)
        st.session_state.shuffled_options_cache[idx] = opts

    shuffled_opts = st.session_state.shuffled_options_cache[idx]

    selected_choice = st.radio(
        "اختر الإجابة المناسبة:", shuffled_opts, key=f"q_choice_{idx}"
    )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("التالي ⬅️", use_container_width=True):
            if selected_choice == current_q["answer"]:
                st.session_state.score += 1

            if idx + 1 < total_q:
                st.session_state.q_index += 1
                st.rerun()
            else:
                st.session_state.page = "result"
                st.rerun()

    with col2:
        if st.button("🏠 الرئيسية", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()

# --- صفحة النتيجة ---
elif st.session_state.page == "result":
    score = st.session_state.score
    total = len(st.session_state.shuffled_questions)

    st.markdown(
        f"""
        <div class="ppt-question-frame" style="padding: 40px;">
            <h1 style="color: #d4af37; margin-bottom: 10px;">نتيجتك النهائية</h1>
            <div class="hero-badge" style="margin-bottom: 15px;">عِزُّنا بطبِعنا</div>
            <h2 style="color: #ffffff; font-size: 30px; margin-top: 10px;">
                حققت <span style="color: #ffd700; font-size: 42px;">{score}</span> من <span style="color: #ffd700; font-size: 42px;">{total}</span>
            </h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    if score == total:
        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #134e3e 0%, #061c16 100%); padding: 25px; border-radius: 15px; text-align: center; border: 2px solid #ffd700; margin-top: 20px;">
                <h2 style="color: #ffd700; margin-bottom: 10px;">🎉 مبروك مليون! إنجاز وطني مشرف! 🎉</h2>
                <p style="font-size: 18px; color: #ffffff; line-height: 1.6;">
                    أبدعت وحصلت على الدرجة الكاملة بجدارة فائقة!<br>
                    <b>عِزُّنا بطبِعنا</b> ومعلوماتك الوطنية مصدر فخر واعتزاز.
                </p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.balloons()
    else:
        st.markdown(
            """
            <div style="background: rgba(7, 48, 39, 0.7); padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px; border: 1px solid #d4af37;">
                <p style="font-size: 17px; color: #dcdcdc; margin: 0;">مشاركة متميزة جداً! استمر في الاختبار وحاول مرة أخرى لتحقيق الدرجة الكاملة.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 إعادة المحاولة", use_container_width=True):
            q_list = topics_data[st.session_state.current_topic].copy()
            random.shuffle(q_list)
            st.session_state.shuffled_questions = q_list
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.shuffled_options_cache = {}
            st.session_state.page = "quiz"
            st.rerun()

    with col2:
        if st.button("🏠 العودة للرئيسية", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
