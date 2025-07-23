import streamlit as st
import numpy as np
import pickle

#load the trained model 
with open('house_price_prediction.pkl','rb') as file:
    model = pickle.load(file)

st.title("House Price Predictor")
st.markdown("Enter the details below to predict the house ")

CRIM = st.number_input("CRIM (per capita crime rate)",value = 0.1)
ZN = st.number_input("ZN (Proportion of residential land zoned)",value=0.0)
INDUS = st.number_input ("INDUS (Non retail business acres per town)",value = 8.0)
CHAS = st.selectbox("CHAS (Charles River dummy variable)",[0,1])
NOX = st.number_input("NOX(Nitric oxides concentration)",value =0.5)
RM = st.number_input ("AGE (Proportion to owner-occupied units built before 1940)",value = 6.0)
AGE = st.number_input("AGE (Proportion of owner-occupied units built before 1940)", value=65.0)
DIS = st.number_input ("DIS (Distance to employment centers)",value = 4.0)
RAD = st.number_input ("RAD (Accessibility to radial highways)",value=1.0)
TAX = st.number_input ("TAX (Property tax rate per $10,000)",value =300.0)
PTRATIO = st.number_input ("PTRATIO (Pupul-teacher ration)",value = 18.0)
B = st.number_input("B (1000(Bk-0.63)^2)",value = 390.0)
LSTAT = st.number_input("LSTAT(%lower status population)",value =12.0)

if st.button ("Predict House Price"):
    input_data = np.array([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ${prediction*1000:.2f}")
