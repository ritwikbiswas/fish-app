import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import plotly.express as px
import datetime as dt

st.set_page_config(layout="centered", page_icon="🐠", page_title="Tank Stats")

st.title(":fish: The Tank")

#HEATMAP
df = px.data.tips()
heatmap_fig = px.density_heatmap(df, x="total_bill", y="tip",color_continuous_scale=["rgba(255, 205, 210,0.01)", "rgba(255, 138, 128,0.4)", "rgba(211, 47, 47,0.8)"])
heatmap_fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
})
heatmap_fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
heatmap_fig.update_layout(showlegend=False)
heatmap_fig.update_xaxes(visible=False)    
heatmap_fig.update_yaxes(visible=False)
heatmap_fig.update(layout_coloraxis_showscale=False)

all_symbols = ["Clownfish","Conch","Algae Crab"]
symbols = st.multiselect("(COMING SOON) Fish activity in the tank today", all_symbols, all_symbols[:3])
st.plotly_chart(heatmap_fig, use_container_width=True)

#PAGE TABS
tab1, tab2,tab3 = st.tabs(["🧪 Chemistry", "🐡 Biology","🔬 Notes"])
df1 = pd.read_csv("testing.csv")

with tab1: #CHEMISTRY 
    df = pd.read_csv("testing.csv")
    #METRICS
    col1, col2,col3 = st.columns(3)
    with col1:
        st.metric(label="Ammonia", value="0.15 ppm", delta="-2.75")
    with col2:
        st.metric(label="pH", value="8.1", delta="-0.8")
    with col3:
        st.metric(label="Salinity", value="1.029 ppm", delta=".002")
    st.text("")
    st.text("")
    st.text("")

    #GRAPHS AND TABLE
    col10, col20 = st.columns(2)
    with col10:
        st.line_chart(df[['Date','NH3 (ppm)','NO2- (ppm)','NO3- (ppm)']],x="Date")
    with col20:
        df[['Date','Temp (F)','pH','Salt (ppm)']]

with tab2: #BIOLOGY
   df = pd.read_csv("creatures.csv")
   df['date'] = pd.to_datetime(df['date'], errors='coerce')
   now = pd.to_datetime('now')
   df['age'] = df.apply(lambda x: round(((now - x['date']).total_seconds() / (60*60*24)),1), axis=1)
   df['age_str'] = df.apply(lambda x: str(x['age']) +" days", axis=1)

   #BAR
   fig2= px.bar(df,y='species',x='number',barmode="stack",orientation='h',color_continuous_scale='viridis',title="Creatures in the Tank",color='category',text="age_str")
   fig2.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
   })
#    fig2.update_layout(showlegend=False)
   fig2.update_xaxes(visible=False)    
#    fig2.update_yaxes(visible=False)
   fig2.update(layout_coloraxis_showscale=False)
   st.plotly_chart(fig2)

   #TREEMAP
   fig = px.treemap(df, path=[px.Constant("Tank"), 'category', 'species','batch'], values='number', color='age',custom_data=['age','number'],color_continuous_scale='viridis',color_continuous_midpoint=np.average(df['age'], weights=df['number']))
#    fig.data[0].textinfo = 'parent+percent'
   fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
   fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
   })
   st.plotly_chart(fig, use_container_width=True)

with tab3: #NOTES
    st.header("Raw Data")
    st.caption("Data and chart dump from other page")
    df1
    st.header("Things to Know")
    st.caption("Notes and Useful Links")

#things left
#automate the chemical metrics update from df
#add notes page to input data and see crazy stuff