import streamlit as st
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import time


st.title("Prediction de prime d'assurance")

if st.button("Revenir à la Page principale"):
    st.query_params["key"] = "principal"

with st.form('form', clear_on_submit=True):
    option1 = st.selectbox(
            "Fumeur",
            ("","Oui","Non"),)
    if option1 != "":
        if option1 == "Oui":
            smoker = 1
        if option1 == "Non":
            smoker = 0
    option2 = st.selectbox(
        "Nombre d'enfants",
        ("","0","1","2","3","4","plus que 5"),)
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
        if option2 == "plus que 5":
            nokid = 0
            onekid = 0
            twokid = 0
            threekid = 0
            fourkid = 0
            fivekid = 1
    option3 = st.selectbox(
    "Région",
    ("","Nord-Est","Sud-Est","Sud-Ouest", "Nord-Ouest"),)
    if option3 != "":
        if option3 == "Nord-Est":
            is_north = 1
            is_east = 1
        if option3 == "Sud-Est":
            is_north = 0
            is_east = 1
        if option3 == "Sud-Ouest":
            is_north = 0
            is_east = 0
        if option3 == "Nord-Ouest":
            is_north = 1
            is_east = 0
    option4 = st.selectbox(
    "Genre",
    ("","Homme","Femme"),)
    if option4 == "Homme":
        sex = 1
    if option4 == "Femme":
        sex = 0
    bmi = st.number_input(label="IMC")
    age = st.number_input("Age", min_value=0, max_value=90,step=1)
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


    if st.form_submit_button("Soumettre") :
        X = list(('smoker','normal', 'is_east','is_north','underweight', 'overweight','severlyoverweight','ogre','nokid', 'onekid', 'twokid','fourkid', 'fivekid','test','elderfemale','middleagefemale', 'youngerfemale', 'youngfemale', 'teens', 'sex'))
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        X= np.asarray([smoker, normal, is_east,is_north, underweight, overweight, severlyoverweight, ogre, nokid, onekid, twokid,fourkid, fivekid,test,elderfemale,middleagefemale, youngerfemale, youngfemale, teens, sex])
        X=X.reshape(1,-1)
        poly = PolynomialFeatures(degree=2)
        poly_variables = poly.fit_transform(X)
        y_pred = model.predict(poly_variables)
        st.write(y_pred)