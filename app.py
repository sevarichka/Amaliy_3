import streamlit as st
import pickle
import pandas as pd

with open('drugpredict.pkl', 'rb') as file:
      model = pickle.load(file)

st.title("Dori vositalari tavsiyasi")
Age = st.number_input("Yosh", min_value=0, max_value=120, value=20)
sex = st.selectbox("Jins", ["Erkak", "Ayol"])
if sex=="Ayol":
    Sex=0
elif sex=="Erkak":
    Sex=1
bp = st.selectbox("Qon bosimi", ["PAST", "NORMAL", "YUQORI"])
if bp=="YUQORI":
    BP=0
elif bp=="PAST":
    BP=1
elif bp=="NORMAL":
    BP=2
cholesterol = st.selectbox("Qondagi xolesterol", ["NORMAL", "YUQORI"])
if cholesterol=="NORMAL":
    Cholesterol=1
elif cholesterol=="YUQORI":
    Cholesterol=0
Na_to_k = st.number_input("Organizmdagi natriy miqdorining kaliyga nisbati", min_value=0.0, value=10.0)

if st.button("Bashorat qilish"):
    df = pd.DataFrame([{
        'Age': Age, 
        'Sex': Sex, 
        'BP': BP, 
        'Cholesterol': Cholesterol, 
        'Na_to_k': Na_to_k
    }])
    prediction = model.predict(df)[0]
    st.success(f"Tavsiya etilgan dori ${prediction}$")