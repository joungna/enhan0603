import streamlit as st
import pandas as pd

# 제목 설정
st.title('CSV 파일 업로드 및 데이터 표시')

# 파일 업로드 위젯
uploaded_file = st.file_uploader('CSV 파일을 업로드하세요', type='csv')

if uploaded_file is not None:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded_file)
    # 데이터프레임 표시
    st.write(df)
