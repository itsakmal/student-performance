import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Exam Performance Predictor", layout="centered")

st.title("Student Exam Performance Predictor")

st.markdown("### Enter student details:")

# Input fields
gender = st.selectbox("Gender", ["male", "female"])
ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent_education = st.selectbox("Parental Level of Education", [
    "associate's degree", "bachelor's degree", "high school", 
    "master's degree", "some college", "some high school"
])
lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])
reading_score = st.number_input("Reading Score (out of 100)", min_value=0, max_value=100, step=1)
writing_score = st.number_input("Writing Score (out of 100)", min_value=0, max_value=100, step=1)

# Prediction logic
if st.button("Predict Math Score"):
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parent_education,
        lunch=lunch,
        test_preparation_course=test_prep,
        reading_score=reading_score,
        writing_score=writing_score
    )
    input_df = data.get_data_as_data_frame()
    
    pipeline = PredictPipeline()
    result = pipeline.predict(input_df)

    st.success(f"Predicted Math Score: {result[0]}")

