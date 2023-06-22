import streamlit as st
import pandas as pd
import requests

st.title("독거 노인 수")
url = 'http://apis.data.go.kr/1352000/ODMS_STAT_24/callStat24Api'
params ={'serviceKey' : 'http://apis.data.go.kr/1352000/ODMS_STAT_24', 'pageNo' : '1', 'numOfRows' : '10', 'apiType' : 'XML', 'year' : '2019' }

response = requests.get(url, params=params)
print(response.content)



