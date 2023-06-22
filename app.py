import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

st.title("대기 오염")

# 주어진 좌표 데이터로 DataFrame 생성
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])

# API 호출을 위한 반복문
for index, row in df.iterrows():
    lat = row['lat']
    lon = row['lon']
    
    # API 요청 보내기
    api_key = 'KU4sbUhkqLCoOaTz0eNuf5DBCORUzbcL7XaHhqi4qSY2%2Bs%2FFvwIGBBiG4tbIxRI%2F1ftQTPvmeQstoiwXt4I2tw%3D%3D'
    url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc?latlng={lat},{lon}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # 응답 데이터에서 필요한 정보 추출
    if data['status'] == 'OK':
        results = data['results']
        if results:
            address = results[0]['formatted_address']
            st.write('Latitude:', lat)
            st.write('Longitude:', lon)
            st.write('Address:', address)
            st.write('---------------------')

