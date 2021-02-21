import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import helper
from helper import *


admin = False
c1 = st.sidebar.checkbox('Admin Mode', False)

st.title('Crunchbase Analysis (Streamlit Inspired by other teams dashboards)')
st.sidebar.markdown('**By:** Team Crunchbase')



if c1:
    admin = True
else:
    admin = False

    
#load_data
@st.cache(persist=True, allow_output_mutation=True)
def load_data():
    orgs,dummycolumns=helper.load_data(nrows=100)
    events,founders,degrees,orgs=add_features(orgs,nrows=100)
    return(orgs,dummycolumns,events,founders,degrees)

import re

st.header('Data')
data_load_state = st.text('Loading data...')
orgs,dummycolumns,events,founders,degrees = load_data()
data_load_state.text("Done! (using st.cache)")
c1 = st.checkbox("Show/Hide Raw Data", True)

if c1:
    st.header('Organizations')
    st.write(orgs)
    st.header('Events')
    st.write(events)
    st.header('Founders')
    st.write(founders)
    st.header('degrees')
    st.write(degrees)
    

c2 = st.checkbox("Show/Hide Report", True)

if c2:
    HtmlFile = open("reportcrunchbase.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, width=1000, height=20000)
