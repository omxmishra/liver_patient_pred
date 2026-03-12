import streamlit as st
import pandas as pd
import joblib
import json

# -----------------------------
# Page config
# -----------------------------

st.set_page_config(
    page_title="Liver Disease AI",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Styling
# -----------------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
color:white;
}

[data-testid="stSidebar"]{
background: linear-gradient(180deg,#0f172a,#1e293b);
}

h1,h2,h3{
color:white;
}

.stButton>button{
background: linear-gradient(90deg,#36d1dc,#5b86e5);
color:white;
border-radius:10px;
height:45px;
width:150px;
font-size:16px;
border:none;
}

.stButton>button:hover{
background: linear-gradient(90deg,#5b86e5,#36d1dc);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load model
# -----------------------------

model = joblib.load("liver_disease_pipeline.pkl")

with open("feature_columns.json") as f:
    feature_columns = json.load(f)

# -----------------------------
# Sidebar Inputs
# -----------------------------

st.sidebar.title("Patient Information")

age = st.sidebar.slider("Age",1,90,35)

gender = st.sidebar.selectbox(
"Gender",
["Male","Female"]
)

gender = 1 if gender=="Male" else 0

total_bilirubin = st.sidebar.number_input(
"Total Bilirubin",0.0,80.0,0.8
)

direct_bilirubin = st.sidebar.number_input(
"Direct Bilirubin",0.0,20.0,0.2
)

alk_phos = st.sidebar.number_input(
"Alkaline Phosphotase",50.0,2200.0,180.0
)

alt = st.sidebar.number_input(
"ALT",10.0,2000.0,32.0
)

ast = st.sidebar.number_input(
"AST",10.0,5000.0,28.0
)

total_proteins = st.sidebar.number_input(
"Total Proteins",2.0,10.0,6.5
)

albumin = st.sidebar.number_input(
"Albumin",0.5,6.0,3.8
)

ag_ratio = st.sidebar.number_input(
"Albumin & Globulin Ratio",0.1,3.0,1.2
)

predict = st.sidebar.button("Predict")

# -----------------------------
# Title
# -----------------------------

st.title("🩺 Liver Disease Prediction System")

st.write(
"""
This AI system predicts the **risk of liver disease** using machine learning  
based on patient biochemical indicators.
"""
)

st.markdown("---")

# -----------------------------
# Input dataframe
# -----------------------------

input_data = pd.DataFrame([[
age,
gender,
total_bilirubin,
direct_bilirubin,
alk_phos,
alt,
ast,
total_proteins,
albumin,
ag_ratio
]],columns=feature_columns)

# -----------------------------
# Layout
# -----------------------------

col1,col2 = st.columns([1.2,1])

# -----------------------------
# Patient Data
# -----------------------------

with col1:

    st.subheader("Patient Data")

    st.dataframe(input_data)

# -----------------------------
# Prediction
# -----------------------------

with col2:

    st.subheader("Prediction Result")

    if predict:

        probability = model.predict_proba(input_data)[0][1]
        prediction = model.predict(input_data)[0]

        if prediction==1:
            st.error("⚠ High Risk of Liver Disease")
        else:
            st.success("✅ Low Risk of Liver Disease")

        st.write("### Probability of Liver Disease")

        st.write(f"# {probability*100:.2f}%")

        st.progress(float(probability))

    else:

        st.info("Enter patient data and click Predict")

st.markdown("---")

# -----------------------------
# Model Metrics
# -----------------------------

st.subheader("Model Performance")

m1,m2,m3,m4 = st.columns(4)

m1.metric("Accuracy","77.8%")
m2.metric("ROC-AUC","0.83")
m3.metric("Recall","0.73")
m4.metric("F1 Score","0.82")

st.markdown("---")

st.caption(
"Tuned Gradient Boosting Model • Built with Streamlit"
)