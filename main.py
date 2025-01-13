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
        ("","0","1","2","3","4","more than 5"),)
    if option2 != "":
        if option2 == "0":
            nokid = 1
            onekid = 0
            twokid = 0
            threekid = 0
            fourkid = 0
            fivekid = 0
        if option2 == "1":
            nokid = 0
            onekid = 1
            twokid = 0
            threekid = 0
            fourkid = 0
            fivekid = 0
        if option2 == "2":
            nokid = 0
            onekid = 0
            twokid = 1
            threekid = 0
            fourkid = 0
            fivekid = 0
        if option2 == "3":
            nokid = 0
            onekid = 0
            twokid = 0
            threekid = 1
            fourkid = 0
            fivekid = 0
        if option2 == "4":
            nokid = 0
            onekid = 0
            twokid = 0
            threekid = 0
            fourkid = 1
            fivekid = 0
        if option2 == "more than 5":
            nokid = 0
            onekid = 0
            twokid = 0
            threekid = 0
            fourkid = 0
            fivekid = 1
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
    if option4 == "male":
        sex = 1
    if option4 == "female":
        sex = 0
    bmi = st.number_input(label="enter bmi")
    age = st.number_input("enter age", min_value=0, max_value=90,step=1)
    if bmi > 45.5:
        underweight = 0
        normal = 0
        overweight = 0
        severlyoverweight = 0
        ogre = 1
    if bmi < 17.85:
        underweight = 1
        normal = 0
        overweight = 0
        severlyoverweight = 0
        ogre = 0
    if bmi >= 17.85 and bmi < 30.5:
        underweight = 1
        normal = 0
        overweight = 0
        severlyoverweight = 0
        ogre = 0
    if bmi >= 30.5 and bmi <= 37.5:
        underweight = 0
        normal = 0
        overweight = 1
        severlyoverweight = 0
        ogre = 0
    if bmi >= 37.5 and bmi <= 45.5:
        underweight = 0
        normal = 0
        overweight = 0
        severlyoverweight = 1
        ogre = 0
    if age > 60.75:
        teens = 0
        test = 0
        youngfemale = 0
        youngerfemale = 0
        middleagefemale = 0
        elderfemale = 1
    if age > 46.5 and age <= 60.75:
        teens = 0
        test = 0
        youngfemale = 0
        youngerfemale = 0
        middleagefemale = 1
        elderfemale = 0
    if age > 42.5 and age <= 46.5:
        teens = 0
        test = 0
        youngfemale = 0
        youngrfemale = 1
        middleagefemale = 0
        elderfemale = 0
    if age < 21.75:
        teens = 1
        test = 0
        youngfemale = 0
        youngerfemale = 0
        middleagefemale = 0
        elderfemale = 0
    if age > 21.5 and age <= 31:
        teens = 0
        test = 1
        youngfemale = 0
        youngerfemale = 0
        middleagefemale = 0
        elderfemale = 0
    if age > 31 and age <= 39.5:
        teens = 0
        test = 0
        youngfemale = 0
        youngerfemale = 1
        middleagefemale = 0
        elderfemale = 0


    if st.form_submit_button("submit") :
        X = list(('smoker','normal', 'is_east','is_north','underweight', 'overweight','severlyoverweight','ogre','nokid', 'onekid', 'twokid','fourkid', 'fivekid','test','elderfemale','middleagefemale', 'youngerfemale', 'youngfemale', 'teens', 'sex'))
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        X= np.asarray([smoker, normal, is_east,is_north, underweight, overweight, severlyoverweight, ogre, nokid, onekid, twokid,fourkid, fivekid,test,elderfemale,middleagefemale, youngerfemale, youngfemale, teens, sex])
        X=X.reshape(1,-1)
        poly = PolynomialFeatures(degree=2)
        poly_variables = poly.fit_transform(X)
        y_pred = model.predict(poly_variables)
        st.write(y_pred)
