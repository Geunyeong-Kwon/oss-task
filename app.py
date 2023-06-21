import streamlit as st
import pandas as pd
import numpy as np
import graphviz as grphviz
import matplotlib.pyplot as plt

st.write('#Youtube view')
st.write('## raw')
view=[100,1500,30]
view
st.write('##bar chart')
st.bar_chart(view)
sview=pd.Series(view)
sview
