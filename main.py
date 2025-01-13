import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import time

st.title('Estimation')

# if st.session_state.reset == True:
#     st.session_state.reset = False

# st.session_state
with st.form('form', clear_on_submit=True):
    option1 = st.selectbox(
            "smoker",
            ("","yes","no"),)
    if option1 != "":
        if option1 == "yes":
            smoker = 1
        if option1 == "no":
            smoker = 0
    option2 = st.selectbox(
        "number of kids",
        ("","0","1-4","more than 5"),)
    if option2 != "":
        if option2 == "0":
            nokid = 1
            kids = 0
        if option2 == "1-4":
            nokid = 0
            kids = 1
        if option2 == "more than 5":
            nokid = 0
            kids = 0
    option3 = st.selectbox(
    "region",
    ("","northeast","southeast","southwest", "northwest"),)
    if option3 != "":
        if option3 == "northeast":
            is_north = 1
            is_east = 1
        if option3 == "southeast":
            is_north = 0
            is_east = 1
        if option3 == "southwest":
            is_north = 0
            is_east = 0
        if option3 == "northwest":
            is_north = 1
            is_east = 0
    option4 = st.selectbox(
    "sex",
    ("","male","female"),)   
    bmi = st.number_input(label="enter bmi")
    age = st.number_input("enter age", min_value=0, max_value=90,step=1)
    if bmi < 18:
        underweight = 1
        overweight = 0
        severlyoverweight = 0
    if bmi > 38:
        underweight = 0
        overweight = 0
        severlyoverweight = 1
    if bmi >= 18 and bmi <= 38:
        severlyoverweight = 0
        underweight = 0
        overweight = 1
    if age != 0:
        if age > 60 and option3 == "female":
            elderfemale = 1
        else:
            elderfemale = 0

    if st.form_submit_button("submit") :
        X = list((smoker, age, is_east, bmi, is_north, underweight, overweight, severlyoverweight, nokid, kids, elderfemale))
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        X= np.asarray([1,(age-39.222139117427076)/14.044332734156425,1,(bmi-30.66345175766642)/6.100468409615801, 0,0, 0,0, 0,1, 0])
        X=X.reshape(1,-1)
        poly = PolynomialFeatures(degree=2)
        poly_variables = poly.fit_transform(X)
        y_pred = model.predict(poly_variables)
        st.write(y_pred)
