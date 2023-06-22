import streamlit as st
import pandas as pd
import requests

# API 데이터 가져오기
def get_data(api_key, param1, param2):
    url = f'KU4sbUhkqLCoOaTz0eNuf5DBCORUzbcL7XaHhqi4qSY2%2Bs%2FFvwIGBBiG4tbIxRI%2F1ftQTPvmeQstoiwXt4I2tw%3D%3D?param1={param1}&param2={param2}&api_key={api_key}'  # 실제 API 엔드포인트로 수정
    response = requests.get(url)
    data = response.json()
    return data

# streamlit 애플리케이션 생성
def main():
    # 애플리케이션 제목
    st.title('조건에 따른 차트와 지도 출력')

    # 입력 위젯
    param1 = st.selectbox('파라미터1 선택', ['값1', '값2', '값3'])
    param2 = st.slider('파라미터2 선택', 0, 100, (0, 100))

    # API 데이터 가져오기
    api_key = 'KU4sbUhkqLCoOaTz0eNuf5DBCORUzbcL7XaHhqi4qSY2%2Bs%2FFvwIGBBiG4tbIxRI%2F1ftQTPvmeQstoiwXt4I2tw%3D%3D'  
    data = get_data(api_key, param1, param2)

    # 데이터 처리 및 시각화
    df = pd.DataFrame(data)  # API 응답 데이터를 데이터프레임으로 변환
    filtered_data = process_data(df)  # 데이터 처리 함수에 따라 가공

    # 차트 또는 지도 출력
    if len(filtered_data) > 0:
        st.subheader('출력 결과')
        if st.checkbox('차트 출력'):
            st.line_chart(filtered_data)
        if st.checkbox('지도 출력'):
            show_map(filtered_data)
    else:
        st.subheader('출력 결과')
        st.write('조건에 해당하는 데이터가 없습니다.')
