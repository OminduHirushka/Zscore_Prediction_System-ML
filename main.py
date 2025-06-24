import numpy as np
import streamlit as st
import pickle
from PIL import Image

# Load the model
model = pickle.load(open("model.pickle", "rb"))

# Initialize session state for theme
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# Page configuration
st.set_page_config(
    page_title="Z-score Predictor",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded",
)


# Theme toggle function
def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode


def get_theme_css():
    if st.session_state.dark_mode:
        return """
        <style>
            .stApp {
                background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3e 100%);
            }
            .main-container {
                background: rgba(30, 30, 46, 0.9);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 2rem;
                margin: 1rem 0;
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            }
            .front-title {
                font-size: 22px;
                font-weight: 700;
                color: #a6e3a1;
                margin: 20px 0 15px 0;
                padding: 10px 0;
                border-bottom: 3px solid #89b4fa;
                text-align: center;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            }
            .main-header {
                color: #cdd6f4;
                text-align: center;
                margin-bottom: 1rem;
                font-size: 3rem;
                font-weight: 800;
                text-shadow: 0 4px 8px rgba(0,0,0,0.3);
                background: linear-gradient(45deg, #89b4fa, #a6e3a1);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .subheader {
                color: #bac2de;
                text-align: center;
                margin-bottom: 2rem;
                font-size: 1.2rem;
                opacity: 0.9;
            }
            .stSelectbox > div > div {
                background-color: rgba(49, 50, 68, 0.8);
                border: 1px solid #585b70;
                border-radius: 12px;
                color: #cdd6f4;
            }
            .stSelectbox > div > div:hover {
                border-color: #89b4fa;
                box-shadow: 0 0 10px rgba(137, 180, 250, 0.3);
            }
            .stButton > button {
                background: linear-gradient(45deg, #89b4fa, #a6e3a1);
                color: #1e1e2e;
                font-weight: bold;
                padding: 0.8rem 2rem;
                width: 100%;
                border: none;
                border-radius: 12px;
                font-size: 1.1rem;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(137, 180, 250, 0.3);
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(137, 180, 250, 0.4);
            }
            .success-box {
                background: linear-gradient(135deg, rgba(166, 227, 161, 0.1), rgba(137, 180, 250, 0.1));
                padding: 1.5rem;
                border-radius: 15px;
                border-left: 5px solid #a6e3a1;
                margin-top: 1rem;
                border: 1px solid rgba(166, 227, 161, 0.2);
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            }
            .success-box h3 {
                color: #a6e3a1;
                margin-bottom: 1rem;
            }
            .success-box p {
                color: #cdd6f4;
            }
            .error-box {
                background: linear-gradient(135deg, rgba(243, 139, 168, 0.1), rgba(235, 160, 172, 0.1));
                padding: 1.5rem;
                border-radius: 15px;
                border-left: 5px solid #f38ba8;
                margin-top: 1rem;
                border: 1px solid rgba(243, 139, 168, 0.2);
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            }
            .error-box h3 {
                color: #f38ba8;
                margin-bottom: 1rem;
            }
            .error-box p {
                color: #cdd6f4;
            }
            .theme-toggle {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1000;
                background: rgba(137, 180, 250, 0.2);
                border: 1px solid rgba(137, 180, 250, 0.3);
                border-radius: 50px;
                padding: 10px 15px;
                backdrop-filter: blur(10px);
                color: #cdd6f4;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            .theme-toggle:hover {
                background: rgba(137, 180, 250, 0.3);
                transform: scale(1.05);
            }
            .info-card {
                background: rgba(137, 180, 250, 0.1);
                border: 1px solid rgba(137, 180, 250, 0.2);
                border-radius: 12px;
                padding: 1rem;
                margin: 1rem 0;
                backdrop-filter: blur(10px);
                color: #cdd6f4;
            }
            .stSpinner > div {
                border-top-color: #89b4fa !important;
            }
            /* Custom select dropdown styling */
            .stSelectbox label {
                color: #cdd6f4 !important;
                font-weight: 600;
            }
        </style>
        """
    else:
        return """
        <style>
            .stApp {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .main-container {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 2rem;
                margin: 1rem 0;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            }
            .front-title {
                font-size: 22px;
                font-weight: 700;
                color: #2c3e50;
                margin: 20px 0 15px 0;
                padding: 10px 0;
                border-bottom: 3px solid #3498db;
                text-align: center;
                text-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .main-header {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 1rem;
                font-size: 3rem;
                font-weight: 800;
                text-shadow: 0 4px 8px rgba(0,0,0,0.1);
                background: linear-gradient(45deg, #3498db, #2ecc71);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            .subheader {
                color: #7f8c8d;
                text-align: center;
                margin-bottom: 2rem;
                font-size: 1.2rem;
                opacity: 0.9;
            }
            .stSelectbox > div > div {
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid #bdc3c7;
                border-radius: 12px;
                transition: all 0.3s ease;
            }
            .stSelectbox > div > div:hover {
                border-color: #3498db;
                box-shadow: 0 0 10px rgba(52, 152, 219, 0.3);
            }
            .stButton > button {
                background: linear-gradient(45deg, #3498db, #2ecc71);
                color: white;
                font-weight: bold;
                padding: 0.8rem 2rem;
                width: 100%;
                border: none;
                border-radius: 12px;
                font-size: 1.1rem;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
            }
            .stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(52, 152, 219, 0.4);
            }
            .success-box {
                background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(52, 152, 219, 0.1));
                padding: 1.5rem;
                border-radius: 15px;
                border-left: 5px solid #2ecc71;
                margin-top: 1rem;
                border: 1px solid rgba(46, 204, 113, 0.2);
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            .success-box h3 {
                color: #27ae60;
                margin-bottom: 1rem;
            }
            .error-box {
                background: linear-gradient(135deg, rgba(231, 76, 60, 0.1), rgba(235, 87, 87, 0.1));
                padding: 1.5rem;
                border-radius: 15px;
                border-left: 5px solid #e74c3c;
                margin-top: 1rem;
                border: 1px solid rgba(231, 76, 60, 0.2);
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            .error-box h3 {
                color: #c0392b;
                margin-bottom: 1rem;
            }
            .theme-toggle {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 1000;
                background: rgba(52, 152, 219, 0.2);
                border: 1px solid rgba(52, 152, 219, 0.3);
                border-radius: 50px;
                padding: 10px 15px;
                backdrop-filter: blur(10px);
                color: #2c3e50;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            .theme-toggle:hover {
                background: rgba(52, 152, 219, 0.3);
                transform: scale(1.05);
            }
            .info-card {
                background: rgba(52, 152, 219, 0.1);
                border: 1px solid rgba(52, 152, 219, 0.2);
                border-radius: 12px;
                padding: 1rem;
                margin: 1rem 0;
                backdrop-filter: blur(10px);
                color: #2c3e50;
            }
            .stSpinner > div {
                border-top-color: #3498db !important;
            }
            /* Custom select dropdown styling */
            .stSelectbox label {
                color: #2c3e50 !important;
                font-weight: 600;
            }
        </style>
        """


# Apply theme CSS
st.markdown(get_theme_css(), unsafe_allow_html=True)

# Theme toggle button
theme_icon = "🌙" if not st.session_state.dark_mode else "☀️"
theme_text = "Dark Mode" if not st.session_state.dark_mode else "Light Mode"

# Create a container for the theme toggle
col1, col2, col3 = st.columns([1, 1, 1])
with col3:
    if st.button(f"{theme_icon} {theme_text}", key="theme_toggle"):
        toggle_theme()
        st.rerun()

# Mapping dictionaries
subMap = {
    "ACCOUNTING": 0,
    "AGRICULTURAL SCIENCE": 1,
    "AGRO TECHNOLOGY": 2,
    "ART": 3,
    "BIO SYSTEMS TECHNOLOGY": 4,
    "BIO-RESOURCE TECHNOLOGY": 5,
    "BIOLOGY": 6,
    "BUDDHISM": 7,
    "BUDDHIST CIVILIZATION": 8,
    "BUSINESS STATISTICS": 9,
    "BUSINESS STUDIES": 10,
    "CARNATIC MUSIC": 11,
    "CHEMISTRY": 12,
    "CHRISTIAN CIVILIZATION": 13,
    "CHRISTIANITY": 14,
    "CIVIL TECHNOLOGY": 15,
    "COMBINED MATHEMATICS": 16,
    "COMMUNICATION & MEDIA STUDIES": 17,
    "DANCING(BHARATHA)": 18,
    "DANCING(INDIGENOUS)": 19,
    "DRAMA AND THEATRE (SINHALA)": 20,
    "ECONOMICS": 21,
    "ELECTRICAL,ELECTRONIC AND IT": 22,
    "ENGINEERING TECHNOLOGY": 23,
    "ENGLISH": 24,
    "FOOD TECHNOLOGY": 25,
    "GEOGRAPHY": 26,
    "GREEK & ROMAN CIVILIZATION": 27,
    "HIGHER MATHEMATICS": 28,
    "HINDU CIVILIZATION": 29,
    "HINDUISM": 30,
    "HISTORY OF EUROPE": 31,
    "HISTORY OF INDIA": 32,
    "HISTORY OF MODERN WORLD": 33,
    "HISTORY OF SRI LANKA & EUROPE": 34,
    "HISTORY OF SRI LANKA & INDIA": 35,
    "HISTORY OF SRI LANKA & MODERN WORLD": 36,
    "HOME ECONOMICS": 37,
    "INFORMATION & COMMUNICATION TECHNOLOGY": 38,
    "ISLAM": 39,
    "ISLAMIC CIVILIZATION": 40,
    "LOGIC & SCIENTIFIC METHOD": 41,
    "MATHEMATICS": 42,
    "MECHANICAL TECHNOLOGY": 43,
    "ORIENTAL MUSIC": 44,
    "PALI": 45,
    "PHYSICS": 46,
    "POLITICAL SCIENCE": 47,
    "SINHALA": 48,
    "TAMIL": 49,
    "WESTERN MUSIC": 50,
}

streamMap = {
    "ARTS": 1,
    "BIOLOGICAL SCIENCE": 2,
    "BIOSYSTEMS TECHNOLOGY": 3,
    "COMMERCE": 4,
    "ENGINEERING TECHNOLOGY": 5,
    "NON": 6,
    "PHYSICAL SCIENCE": 7,
}

gradeMap = {"A": 0, "Absent": 1, "B": 2, "C": 3, "F": 4, "S": 5, "Withheld": 6}
genderMap = {"Major error": 0, "Unknown": 1, "female": 2, "male": 3}
syllabusMap = {"new": 0, "old": 1}

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Header section
st.markdown("<h1 class='main-header'>📊 Z-score Predictor</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subheader'>Predict your Z-score based on your performance in the GCE A/L Exam 2020 (Sri Lanka)</p>",
    unsafe_allow_html=True,
)

# Try to load and display a logo (optional)
try:
    logo = Image.open("logo.png")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(logo, width=150)
except:
    pass

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Form container
with st.form("prediction_form"):
    # Student Information Section
    st.markdown(
        "<div class='front-title'>👤 Student Information</div>", unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        stream = st.selectbox(
            "🎓 Stream:", streamMap.keys(), help="Select your study stream"
        )
        gender = st.selectbox("⚧ Gender:", genderMap.keys(), help="Select your gender")
    with col2:
        syllabus = st.selectbox(
            "📚 Syllabus:", syllabusMap.keys(), help="Select your syllabus type"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Subject Results Section
    st.markdown(
        "<div class='front-title'>📋 Subject Results</div>", unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Subject 1**")
        sub1 = st.selectbox("Subject:", subMap.keys(), key="sub1")
        sub1_r = st.selectbox("Grade:", gradeMap.keys(), key="sub1_r")

    with col2:
        st.markdown("**Subject 2**")
        sub2 = st.selectbox("Subject:", subMap.keys(), key="sub2")
        sub2_r = st.selectbox("Grade:", gradeMap.keys(), key="sub2_r")

    with col3:
        st.markdown("**Subject 3**")
        sub3 = st.selectbox("Subject:", subMap.keys(), key="sub3")
        sub3_r = st.selectbox("Grade:", gradeMap.keys(), key="sub3_r")

    st.markdown("<br>", unsafe_allow_html=True)

    # Submit button
    submitted = st.form_submit_button(
        "🔮 Predict My Z-score", help="Click to calculate your predicted Z-score"
    )

# Results section
if submitted:
    with st.spinner("🔄 Calculating your Z-score..."):
        inp = np.array(
            [
                [
                    streamMap[stream],
                    subMap[sub1],
                    gradeMap[sub1_r],
                    subMap[sub2],
                    gradeMap[sub2_r],
                    subMap[sub3],
                    gradeMap[sub3_r],
                    syllabusMap[syllabus],
                    genderMap[gender],
                ]
            ]
        )

        try:
            prediction = model.predict(inp)

            # Display result with animation-like effect
            st.markdown(
                f"""
                <div class='success-box'>
                    <h3>🎉 Prediction Result</h3>
                    <p style='font-size: 28px; font-weight: bold; text-align: center; margin: 1rem 0;'>
                        Estimated Z-score: <span style='color: #2ecc71;'>{prediction[0]:,.2f}</span>
                    </p>
                    <p style='text-align: center; font-style: italic; opacity: 0.8;'>
                        This prediction is based on historical data and may vary from actual results.
                    </p>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # Additional information based on Z-score with enhanced styling
            if prediction[0] > 1.5:
                st.markdown(
                    """
                    <div class='info-card'>
                        <h4>🎯 Excellent Performance!</h4>
                        <p>Based on your predicted Z-score, you have excellent chances for university admission in highly competitive fields.</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
            elif prediction[0] > 0:
                st.markdown(
                    """
                    <div class='info-card'>
                        <h4>👍 Good Performance!</h4>
                        <p>Your predicted Z-score suggests you may qualify for university admission in various fields.</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    """
                    <div class='info-card'>
                        <h4>💪 Keep Working!</h4>
                        <p>Consider discussing your options with an education counselor for the best path forward.</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

        except Exception as e:
            st.markdown(
                f"""
                <div class='error-box'>
                    <h3>❌ Error</h3>
                    <p>An error occurred while processing your request:</p>
                    <code>{e}</code>
                    <p>Please check your inputs and try again.</p>
                </div>
            """,
                unsafe_allow_html=True,
            )
