import numpy as np
import pandas as pd
import streamlit as st

st.title("Estimating SRTPV Capacity")
st.subheader('Solar rooftop PV module')
st.image("srtpv.jpeg", caption="Sunrise for the clean energy")
st.write('Allowed area for SRTPV installation')
all = st.selectbox('Allowed area',['Residential','Non-Residential','Apartments','Carport'])
if all=='Residential':
  st.write('*Avail for PM Surya Ghar Scheme subsidy for SRTPV installation*:sunglasses:')
else:
  st.write('*No subsidy is available*')
st.write('Application & Facilitation Fees')
if st.button('Fees'):
  df = pd.read_excel(r'https://github.com/ArunKanagolkar/SRTPV/blob/main/SRTPV_Fees.xlsx')
  st.write("Below is a Fees details:",df)
sl = st.slider('Select the consumer sectioned load in KW',1,500)
area = st.slider('Select the rooftop space available for SRTPV in Sq.mtrs',1,500)
sytm = st.selectbox('Select type of system',['Single Phase','Three Phase'])
ty = st.selectbox('Select type of SRTPV',['Off grid','ON grid'])
if ty =='Off grid':
  st.write(" No need PPA from DISCOM")
else:
  st.write("Required PPA from DISCOM")
  
if st.button('Max.allowed SRTPV'):
  st.write("Govt.allowable Max.Capacity is kWp:",sl,"kWp")
 
if st.button("How much solar energy is produced each year?"):
  eg = sl*4*365
  st.write(eg,"Units")
if st.button('Max.Space SRTPV'):
  et = area/8
  st.write('Space available for SRTPV installation on roof in kWp:')
  st.write(et)                    
if st.button('Check power evacuation'):
 if sl > 150:
   st.write('Proposed SRTPV capacity is morethan 150KW, the consumer shall convert existing distribution system into 11KV')
 else:
   st.write('Proposed SRTPV capacity is lessthan 150KW, the consumer shall not convert existing distribution system into 11KV')
st.subheader('Get SLDs')
with open("HT consumer.jpeg", "rb") as file:
  btn = st.download_button(
        label="Download HT SRTPV SLD",
        data=file,
        file_name="HT consumer.jpeg",
        mime="HT consumer/jpeg",
    )

with open("LT consumer.jpeg", "rb") as file:
  btn = st.download_button(
        label="Download LT SRTPV SLD",
        data=file,
        file_name="LT consumer.jpeg",
        mime="LT consumer/jpeg",
    )

with open("Gross metering.jpeg", "rb") as file:
  btn = st.download_button(
        label="Download Grossmetering SRTPV SLD",
        data=file,
        file_name="Gross metering.jpeg",
        mime="Gross metering/jpeg",
    )

with open("procedure.jpeg", "rb") as file:
  btn = st.download_button(
        label="Download SRTPV procedure",
        data=file,
        file_name="procedure.jpeg",
        mime="procedure/jpeg",
    )
st.subheader('SRTPV Cost')

st.write("Estimated cost for",sl,"kWp")
if st.button('Cost'):
  cost = sl*48000
  st.write(cost)
