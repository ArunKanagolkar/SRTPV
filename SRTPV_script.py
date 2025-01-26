import numpy as np
import pandas as pd
import streamlit as st
df = pd.read_csv('SRTPV_Fees.csv')
st.title("SRTPV Quick Estimator App")
st.write('*:green[This is the SRTPV Quick Estimator App. It provides a basic estimation of the cost and capacity of a solar rooftop photovoltaic plant. Additionally, it offers useful information on government regulations and norms.]*')
st.image("srtpv.jpeg", caption="Sunrise for the clean energy")
all = st.selectbox('**Allowed area for SRTPV installation**',['Residential','Non-Residential','Apartments','Carport','Others'],index=None,
    placeholder="Select Allowed area...")
st.write("You selected:",all)
if st.button('Check Govt.Subsidy'):
    if all=='Residential':
        st.write('*Qualified to receive SRTPV installation subsidies under the PM Surya Ghar Scheme*:sunglasses:')
    else:
        st.write('*No subsidy is available*')
st.write('**Application & Facilitation Fees**')
if st.button('Fees'):
   st.write("Below is a Fees details:",df)
sl = st.slider('Select the consumer sectioned load in KW',1,500)
area = st.slider('Select the rooftop space available for SRTPV in Sq.mtrs',1,500)
sytm = st.selectbox('Select type of system',['Single Phase','Three Phase'])
ty = st.selectbox('Select type of SRTPV',['Off grid','ON grid'])
if ty =='Off grid':
  st.write(" No need PPA from Resp.DISCOM")
else:
  st.write("Required Net-metering and Gross-metering PPA from Resp.DISCOM")
  
if st.button('Sectioned Capacity'):
  st.write("Govt.allowable SRTPV capacity upto:",sl,"kWp")
 

if st.button('Maximum Capacity'):
  et = area/8
  st.write('Your roof area can be used to install SRTPVs up to',et,'kWp')
pc = st.slider('Select Proposed SRTPV Capacity',1,500)
if pc > sl:
    st.write(':red[WARNING]',' *:PROPOSED SRTPV MORETHAN SECTIONED LOAD*')
if st.button('PPA Excecution Authority'):
    if pc < 500:
        st.write("AEE(Ele), O&M Sub-Division")
    else:
        st.write("EE(Ele), O&M Sub-Division")
st.write('**Metering arrangement**')
ma = st.selectbox("Select consumer category",["Domestic","Hospital","Educational","Industrial","Commercial"],index=None,placeholder="Select consumer...")
if ma == 'Domestic':
    st.write(':orange[Above consumer Eligible for both Gross & Net Metering arrangements]')
elif ma =='Hospital':
    st.write(':orange[Above consumer Eligible for both Gross & Net Metering arrangements]')
elif ma =='Educational':
    st.write(':orange[Above consumer Eligible for both Gross & Net Metering arrangements]')
else:
    st.write(':orange[Above consumer Eligible for Net Metering arrangements only]')
        
        
if st.button("How much solar energy is produced each year?"):
  eg = pc*4*365
  st.write(pc,"kWp",":",eg,"kWhrs")
con = st.selectbox('Choose type of consumer',['LT Consumer','HT Consumer'],index=None,placeholder="Select consumer...")
st.write("You selected:",con)
if st.button('Check power evacuation'):
 if pc > 150:
   st.write("Proposed SRTPV capacity is morethan **150kWp**, the consumer shall be sync SRTPV system to 11kV distribution system only and line current does not exceed :red[80%] of the rated current capacity of line and The billing meter shall be BDM HT meter and solar meter will be 3Ph LT CT(For Net Meter arrangement)")
 else:
   st.write('Proposed SRTPV capacity is lessthan **150kWp**, the consumer shall not convert existing distribution system into 11KV')
st.write('**Get SLDs**')
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
st.write('**SRTPV Cost**')

st.write("Estimated cost for",sl,"kWp")
if st.button('**Cost**'):
  cost = sl*48000
  st.write(cost)
