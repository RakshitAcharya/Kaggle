import streamlit as st
import joblib
import pandas as pd
import numpy as np
model = joblib.load('car_price.h5')

st.title("Predicting Sale value for Pre-Owned car")
st.subheader("DETAILS ABOUT THE CAR")

years=[2003,2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
       2015, 2016, 2017, 2018, 2019]
st.subheader("1. Purchase Year")
YEAR = st.selectbox("",years)

st.subheader("2. Purchase Price (in Lakhs) ")
price=st.number_input("")

st.subheader("3. Total KMs driven ")
Kms_Driven=st.number_input("",value=1)

pet={"Petrol":1,
     "Diesel":2,
     "CNG":3}
sell={"Dealer":1,
     "Individual":2}
drive={"Manual":1,
      "Automatic":2}
ownss={"Owner":0,
       "First Hand":1, 
       "Second Hand":2}

st.subheader("4. Fuel_Type ")
fuel= st.selectbox("",["Petrol","Diesel","CNG"])
fuel_type= pet[fuel]
 
st.subheader("4. Seller type")
seller=st.selectbox("",["Dealer","Individual"])
seller_type=sell[seller]

st.subheader("5. Transmission")
trans=st.selectbox("",["Manual","Automatic"])
transmission=drive[trans]

st.subheader("6. Owner")
own=st.selectbox("",["Owner","First Hand", "Second Hand"])
owner=ownss[own]

year_2= 2021- YEAR

par=[year_2,price,Kms_Driven,fuel_type,seller_type,transmission,owner]
arrays=np.array(par)

if st.button(" PREDICT THE SELLING PRICE "):
    pred = model.predict([arrays])[0]
    st.write("Your car can be sold at ", pred*100000 ," Rs ")
    