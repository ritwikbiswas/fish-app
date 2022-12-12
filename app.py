import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import plotly.express as px
from datetime import datetime
today=datetime.today()

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

all_symbols = ["Clownfish","Other Fish"]
symbols = st.multiselect("Fish activity in the tank today", all_symbols, all_symbols[:3])
st.plotly_chart(heatmap_fig, use_container_width=True)

#PAGE TABS
tab1, tab2 = st.tabs(["🧪 Chemistry", "🐡 Biology"])

with tab1: #CHEMISTRY 
    df = pd.read_csv("testing.csv")

    #METRICS
    col1, col2,col3 = st.columns(3)
    with col1:
        st.metric(label="Ammonia", value="0.75 ppm", delta="0")
    with col2:
        st.metric(label="pH", value="8.9", delta="0.8")
    with col3:
        st.metric(label="Salinity", value="1.027 ppm", delta="-.002")
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
   #TREEMAP
   d = {'num': [1,4, 2], 'species': ['conch', 'algae crab', 'clownfish'], 'category': ['cleanup crew','cleanup crew','fish'],'date':['12/10','12/17','12/12'],'age':[3,4,1]}
   df = pd.DataFrame(data=d)
   fig = px.treemap(df, path=[px.Constant("Tank"), 'category', 'species'], title="Current Creatures in the Tank",values='num', color='age', color_continuous_scale='aggrnyl',color_continuous_midpoint=np.average(df['age'], weights=df['num']))
   fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
   fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)'
   })
   st.plotly_chart(fig, use_container_width=True)

