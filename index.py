# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 20:30:08 2025

@author: Pratyush Nikam
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AI Disease Predictor", page_icon="⚕️")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://d197nivf0nbma8.cloudfront.net/uploads/2023/11/AdobeStock_573581840-1350x600.jpeg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.4);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Fade-in animation for a smoother appearance */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    body {
        animation: fadeIn 1s ease-in-out;
    }

    /* Text Styles for Readability */
    h1, h2, h3, h4, h5, h6, p, label {
        color: #ffffff !important;  /* White text for contrast */
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0); /* Soft shadow for readability */
        animation: fadeIn 1.5s ease-in-out;
        text-align: center;
    }

    /* Input Fields: Styled for Dark Background */
    [data-testid="stTextInput"], [data-testid="stNumberInput"] {
        background-color: rgba(255, 255, 255, 0.1); /* Transparent white */
        color: #ffffff;
        border: 2px solid rgba(255, 255, 255, 0.5);
        border-radius: 8px;
        padding: 8px;
        transition: all 0.3s ease-in-out;
    }

    /* Hover Effect for Input Fields */
    [data-testid="stTextInput"]:hover, [data-testid="stNumberInput"]:hover {
        background-color: rgba(255, 255, 255, 0.2);
        border-color: #4CAF50;
    }

    /* Placeholder Text */
    input::placeholder {
        color: rgba(255, 255, 255, 0.7);
        font-style: italic;
    }
    

    /* Button Styling */
    div.stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        display: block;
        margin: auto;
    }

    /* Hover Effect for Buttons */
    div.stButton > button:hover {
        background-color: #45a049;
        transform: scale(1.05);
        box-shadow: 3px 3px 8px rgba(0, 255, 0, 0.4);
    }

    /* Animation on Click */
    div.stButton > button:active {
        transform: scale(1);
    }
    
    .output-text {
        background-color: #333333;
        padding: 5px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
        font-size: 100px;
    }

    </style>
    """, unsafe_allow_html=True)
    
# loading the saved models
models = {
'diabetes' : pickle.load(open('diabetes_model.sav', 'rb')),
'heart_disease' : pickle.load(open('heart_disease_model.sav', 'rb')),
'lung_cancer': pickle.load(open('lungs_disease_model.sav', 'rb')),
'parkinsons' : pickle.load(open('parkinsons_model.sav', 'rb')),
'thyroid' : pickle.load(open('Thyroid_model.sav', 'rb')),
}

#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('AI-POWERED MEDICAL DIAGNOSIS SYSTEM',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Lung Cancer Prediction',
                            'Parkinsons Disease Prediction',
                            'Thyroid Prediction'],
                           
                           icons = ['clipboard2-pulse', 'heart-pulse', 'lungs', 'person','file-medical'],
                           default_index = 0)
    
def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('DIABETES PREDICTION USING MACHINE LEARNING (ML)')
    st.write("Enter the details below to predict diabetes:")
    
    
    col1, col2, col3 = st.columns(3)
    
    #getting the input data from the user
    with col1:
     Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    
    with col2:
     Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    
    with col3:
     BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    
    with col1:
     SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    
    with col2:
     Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    
    with col3:
     BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    
    with col1:
     DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    
    with col2:
     Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')
    
    
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.markdown(f'<p class="output-text">{diab_diagnosis}</p>', unsafe_allow_html=True)

    
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('HEART DISEASE PREDICTION USING ML')
    st.write("Enter the details below to predict heart disease:")
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
     age = display_input('Age', 'Enter age of the person', 'age', 'number')
    
    with col2:
     sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    
    with col3:
     cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    
    with col1:
     trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    
    with col2:
     chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    
    with col3:
     fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    
    with col1:
     restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    
    with col2:
     thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    
    with col3:
     exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    
    with col1:
     oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    
    with col2:
     slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    
    with col3:
     ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    
    with col1:
     thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.markdown(f'<p class="output-text">{heart_diagnosis}</p>', unsafe_allow_html=True)


if (selected == 'Lung Cancer Prediction'):
    
    #page title
    st.title('LUNG CANCER PREDICTION USING (ML)')
    st.write("Enter the details below to predict lung cancer:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
     GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
    
    with col2:
     AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
    
    with col3:
     SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
    
    with col1:
     YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
    
    with col2:
     ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
    
    with col3:
     PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
    
    with col1:
     CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
    
    with col2:
     FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
    
    with col3:
     ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
    
    with col1:
     WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
    
    with col2:
     ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
    
    with col3:
     COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
    
    with col1:
     SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
    
    with col2:
     SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
    
    with col3:
     CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.markdown(f'<p class="output-text">{lungs_diagnosis}</p>', unsafe_allow_html=True)

    
if (selected == 'Parkinsons Disease Prediction'):
    
    #page title
    st.title('PARKINSONS DISEASE PREDICTION USING (ML)')
    st.write("Enter the details below to predict parkinson's disease:")
    
    col1, col2, col3 = st.columns(3)

    with col1:
     fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    
    with col2:
     fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    
    with col3:
     flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    
    with col1:
     Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    
    with col2:
     Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    
    with col3:
     RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    
    with col1:
     PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    
    with col2:
     DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    
    with col3:
     Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    
    with col1:
     Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    
    with col2:
     APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    
    with col3:
     APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    
    with col1:
     APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    
    with col2:
     DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    
    with col3:
     NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    
    with col1:
     HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    
    with col2:
     RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    
    with col3:
     DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    
    with col1:
     spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    
    with col2:
     spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    
    with col3:
     D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
   
    with col1:
     PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')
        
    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.markdown(f'<p class="output-text">{parkinsons_diagnosis}</p>', unsafe_allow_html=True)

       
if (selected == 'Thyroid Prediction'):
    
    #page title
    st.title('THYROID PREDICTION USING (ML)')
    st.write("Enter the details below to predict thyroid:")

    col1, col2, col3 = st.columns(3)

    with col1:
     age = display_input('Age', 'Enter age of the person', 'age', 'number')
    
    with col2:
     sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    
    with col3:
     on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
    
    with col1:
     tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
    
    with col2:
     t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
    
    with col3:
     t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
   
    with col1:
     tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')
    
    thyroid_diagnosis = ''
    if st.button("Thyroid Test Result"):
        thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
        thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
        st.markdown(f'<p class="output-text">{thyroid_diagnosis}</p>', unsafe_allow_html=True)

