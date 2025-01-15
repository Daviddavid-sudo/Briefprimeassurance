import streamlit as st

if st.query_params.get("key") == "page2":
    exec(open("st/page2.py").read())
else:
    st.title('Bienvenue sur notre interface de prédiction !')
    st.image("st/logo.png")

    if st.button("Cliquez pour effectuer une prédiction"):
        st.query_params["key"] = "page2"

