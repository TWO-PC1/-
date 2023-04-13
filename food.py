import pandas
import requests
import xmltodict
import time
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(

    page_title='급식 알리미',
    page_icon='🍽'
)
a=0
url_base = "https://open.neis.go.kr/hub/mealServiceDietInfo"
url_serviceKey = "4fd1b8ffaf4d45c78840b37c69589756"
지역코드 = 'D10'
schoolcode = '7240056'

url = url_base+'?KEY='+url_serviceKey+"&Type=xml&pIndex=1&pSize=10&ATPT_OFCDC_SC_CODE="+지역코드+"&SD_SCHUL_CODE="+schoolcode
url = url+'&MLSV_FROM_YMD=20230410&MLSV_TO_YMD=20230414'


response = requests.get(url) #get 요청
response = response.content #get 요청의내용
xmlObject = xmltodict.parse(response) #xml데이터 형식으로 변환
inputdata = st.sidebar.date_input("날짜를 입력하세요")
inputdata = inputdata.strftime("%Y%m%d")

dict_data = xmlObject['mealServiceDietInfo']['row'] #xml 파싱
df = pandas.DataFrame(dict_data) #데이터 형식으로 변경
df = df[['DDISH_NM','MLSV_YMD']]
df = df[df['MLSV_YMD']==inputdata]

temp= df.iloc[0]['DDISH_NM'].split('<br/>')
st.write(temp)