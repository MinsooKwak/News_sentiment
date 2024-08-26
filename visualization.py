# MongoDB 있는 데이터 > 끄집어냄

import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['project1']
collection = db['NewsAnalysis1']

# Collection 안 데이터 가져오기
data = list(collection.find())
#print(data)
#print(data[0]['sentiments'])

# 필요 부분만 활용
sentiments = []
for item in data:
    sentiments.extend(item['sentiments'])

#print(sentiments)

df = pd.DataFrame(sentiments)
df['seendate'] = pd.to_datetime(df['seendate'])

#### streamlit

# title
st.title("기업별 날짜에 따른 감성 지수 변화")

# 기업 선택
#org_lst = df['organization']
#organization = st.selectbox("기업을 선택하세요", org_lst)
organization = st.selectbox("기업을 선택하세요", ['Apple','Microsoft','OpenAI'])

# 선택한 기업의 데이터 필터링 + 날짜가 index 
selected_df = df.loc[df['organization'] == organization].set_index('seendate')

# 감성지수 차트 (score들만)
st.line_chart(selected_df[['positive','negative','neutral']])