# 🩺 Liver Disease Prediction System

A Machine Learning web application that predicts the **risk of liver disease** using biochemical patient indicators.

The project combines **data analysis, machine learning, and deployment** into an interactive dashboard built with **Streamlit**.

---

#  Project Overview

Liver disease can often be detected through abnormal biochemical markers.

This project uses machine learning to analyze patient features such as:

- Age
- Bilirubin levels
- Liver enzymes (ALT, AST)
- Protein levels
- Albumin ratio

The model predicts the **probability of liver disease** and provides a risk assessment.

---

# Dataset

Dataset used: **Indian Liver Patient Dataset**

Source:
UCI Machine Learning Repository

Dataset contains:

- **583 patient records**
- **10 medical features**
- Binary classification:
  - Liver disease
  - Healthy

---

# ⚙️ Machine Learning Workflow

The project follows a full ML pipeline:

###  Data Preprocessing

- Missing value handling
- Label encoding
- Feature engineering
- Log transformation for skewed features
- Feature scaling

---

###  Exploratory Data Analysis

- Distribution analysis
- Box plots
- Correlation heatmap
- Feature importance

---

### Model Training

Multiple classifiers were trained and compared:

- Logistic Regression
- Support Vector Machine
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost

---

###  Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Best performing model:

**Tuned Gradient Boosting Classifier**

---

#  Model Pipeline
The final deployment pipeline includes:

Log Transformation → StandardScaler → Gradient Boosting Model

This ensures the model performs the **same preprocessing during inference** as during training.

---

#  Web Application

The trained model is deployed using **Streamlit**.

Features of the dashboard:

- Interactive patient input form
- Real-time liver disease prediction
- Risk probability meter
- Medical feature visualization
- Clean AI dashboard UI

---

#  Application Preview

<img src="app_preview.png" width="900">

---

# 🛠 Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
XGBoost  
Matplotlib  
Streamlit  

---

#  Project Structure

liver_disease_prediction/

│
├── app.py
├── liver_disease_pipeline.pkl
├── feature_columns.json
├── requirements.txt
├── liver_analysis.ipynb
└── README.md

# Model Performance

| Metric | Score |
|------|------|
Accuracy | 0.78 |
ROC-AUC | 0.83 |
Recall | 0.73 |
F1 Score | 0.82 |

---

# 💡 Future Improvements

- Larger dataset
- Deep learning models
- Model explainability (SHAP)
- Cloud deployment

---

# ScreenShots

<img width="1918" height="961" alt="image" src="https://github.com/user-attachments/assets/4f165f1f-0923-41bf-8ef9-b7189f4149fa" />

<img width="1910" height="955" alt="image" src="https://github.com/user-attachments/assets/fe093fba-aae0-4ac8-80a3-a2105800b73a" />


