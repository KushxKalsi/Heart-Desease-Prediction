import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open('heart_disease_model.plk', 'rb'))
data = pd.read_csv('heart_disease.csv')
st.header('Heart Disease Predictor')
gender = st.selectbox ('Choose Gender', data['Gender']. unique())
if gender == 'Male':
    gen = 1
else:
    gen =0

age = st.number_input("Enter Age")
currentSmoker = st.number_input("Is Patient currentSmoker")
cigsPerDay = st.number_input("Enter cigsPerDay")
BPMeds = st.number_input("Is Patient on BPMeds")
prevalentStroke = st.number_input("Is Patient Had stroke")
prevalentHyp = st.number_input("Enter prevalentHyp status")
diabetes = st.number_input("Enter diabetes status")
totChol = st. number_input("Enter totChol")
sysBP = st.number_input("Enter sysBP")
diaBP = st.number_input("Enter diaBP")
BMI = st.number_input("Enter BMI")
heartRate = st.number_input("Enter heartRate")
glucose = st.number_input("Enter glucose")
if st.button('Predict'):
    input = np.array([[gen, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes,
                       totChol, sysBP, diaBP, BMI, heartRate, glucose]])
    output = model.predict(input)
    if output [0] == 0:
        stn = 'Patient is Healthy, No heart Disease'
    else:
        stn = 'Patient May have Heart Disease'
    st.markdown (stn)