import streamlit as st
import pandas as pd

st.write('#Youtube view')
st.write('## raw')
view=[100,1500,30]
view
st.write('##bar chart')
st.bar_chart(view)
sview=pd.Series(view)
sview
