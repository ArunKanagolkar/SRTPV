import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import streamlit as st

st.title("Estimating SRTPV Capacity")
st.subheader('Solar rooftop PV module')
sl = st.slider('Select the consumer sectioned load in KW',)
area = st.slider('Select the rooftop space available for SRTPV in Sq.mm')
sytm = st.selectbox('Select type of system',['Single Phase','Three Phase'])
if st.button('Max.SRTPV Plant Capacity'):
  st.write('Max.Capacity is:')
  st.write(sl)
if st.button('Estimate SRTPV Capacity'):
  et = area/8
  st.write('Your Estimated SRTPV capacity in kWp:')
  st.write(et)                    
if st.button('Check power evacuation'):
 if sl > 150:
   st.write('Proposed SRTPV capacity is morethan 150KW, the consumer shall convert existing distribution system into 11KV')
 else:
   st.write('Proposed SRTPV capacity is lessthan 150KW, the consumer shall not convert existing distribution system into 11KV')
if st.buttom('Get SLD'):
  if sytm == 'Single Phase':
    with open("flower.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=SRTPV,
        file_name="Gross%20metering.jpeg",
        mime="Gross%20metering/jpeg",
    )
                    
