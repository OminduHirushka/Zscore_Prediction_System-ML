import numpy as np
import streamlit as st
import pickle

# load the model
model = pickle.load(open("model.pickle", "rb"))

# page configuration
st.set_page_config(page_title="Z-score Predictor", layout="centered")
st.title("GCE A/L Exam Z-score Predector")
st.markdown(
    """
    **WELCOME!**
    
    Predict Z-scores based on student performance in the GCE AL Exam 2020 (Sri Lanka)
    <hr>
    """, unsafe_allow_html=True
)
st.markdown("<div class='front-title'>Input Details</div>", unsafe_allow_html=True)

# mapping
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

with st.form("prediction_form"):
    stream = st.selectbox("Select Value:", streamMap.keys())

    sub1 = st.selectbox("Subject 1:", subMap.keys())
    sub1_r = st.selectbox("Subject 1 Grade:", gradeMap.keys())

    sub2 = st.selectbox("Subject 2:", subMap.keys())
    sub2_r = st.selectbox("Subject 2 Grade:", gradeMap.keys())

    sub3 = st.selectbox("Subject 3:", subMap.keys())
    sub3_r = st.selectbox("Subject 3 Grade:", gradeMap.keys())

    syllabus = st.selectbox("Syllabus:", syllabusMap.keys())
    gender = st.selectbox("Gender:", genderMap.keys())

    submitted = st.form_submit_button("Predict")

if submitted:
    inp = np.array([[
        streamMap[stream],
        subMap[sub1],
        gradeMap[sub1_r],
        subMap[sub2],
        gradeMap[sub2_r],
        subMap[sub3],
        gradeMap[sub3_r],
        syllabusMap[syllabus],
        genderMap[gender]
    ]])
    
    try:
        prediction = model.predict(inp)
        st.success(f"Estimated Z-score: **{prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"An error occured: {e}")
