import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.title("Estimating SRTPV Capacity")
st.subtitle('Solar rooftop PV module')
sl = st.slider('Select the consumer sectioned load',)
area = st.slider('Select the rooftop space available for SRTPV in Sq.mm')
sytm = st.selectbox('Select type of system',['Single Phase','Three Phase']
if sl < 150:
