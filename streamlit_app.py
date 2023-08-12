import streamlit as st
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


st.header('Student Exam Performance Prediction v2')


with st.form("Prediction_Form"):

    gender = st.selectbox(
        'Select Your Gender',
        ('male', 'female')
    )
        
    race_ethnicity = st.selectbox(
        'Select Your Race/Ethnicity',
        ('group A', 'group B', 'group C', 'group D', 'group E')
    )

    parent_edu_level = st.selectbox(
        'Select Your Parent Education Level',
        ("associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school")
    )

    lunch_type = st.selectbox(
        'Select Your Lunch Type',
        ('free/reduced', 'standard')
    )

    test_preparation = st.selectbox(
        'Select Your Test Preparation',
        ('none', 'completed')
    )


    writing_score = st.number_input('Insert your writing score', 
                                    min_value = 0, max_value=100)

    reading_score = st.number_input('Insert your rading score', 
                                    min_value = 0, max_value=100)



    submitted = st.form_submit_button("Submit")

if submitted:

    data = CustomData(
        gender= gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parent_edu_level,
        lunch=lunch_type,
        test_preparation_course= test_preparation,
        reading_score=float(reading_score),
        writing_score=float(writing_score)   
    )

    pred_df=data.get_data_as_data_frame()

    st.write(pred_df)
    st.write("Before Prediction")

    predict_pipeline=PredictPipeline()
    
    st.write("Mid Prediction")
    results=predict_pipeline.predict(pred_df)
    st.write("after Prediction")
    st.write(results[0])
   

st.write("Outside the form")