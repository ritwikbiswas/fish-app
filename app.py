import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="centered", page_icon="🐠", page_title="Aquarium Stats")

st.title("🐠 Aquarium Cycling")
# x 
col10, col20 = st.columns(2)
df = pd.read_csv("testing.csv")


with col10:
   st.line_chart(df[['Date','pH','Ammonia (ppm)','Nitrite (ppm)','Nitrate (ppm)']],x="Date")

with col20:
    st.area_chart(df[['Date','Temperature (F)','Salinity (ppt)']],x="Date")

df