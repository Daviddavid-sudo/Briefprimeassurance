import streamlit as st
import pickle

st.title('Estimation')

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
            if option4 != "":
                bmi = st.number_input(label="enter bmi")
                if bmi != 0:
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

                        st.write(smoker, age, is_east, bmi, is_north, underweight, overweight, severlyoverweight, nokid, kids, elderfemale)
                        st.write("Estimation = ")
                        with open('model.pkl', 'rb') as f:
                            model = pickle.load(f)

                        st.write(model)