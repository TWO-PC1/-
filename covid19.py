import pandas
import requests
import xmltodict 
import time                                   
import pandas as pd                                                                                                                                                                                                                                                                                                                                                                                                                                        
from datetime import datetime
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(

    page_title='COVID 19 현황',
    page_icon='🚑'
)
a=0
url_base = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19NatInfStateJson"
url_serviceKey = "6rxxwqzT7BrB%2FxFQz0AME5gEow0uzJTznehniRBqdD4guEMVsB67QUbhSwaVUSMQ8N%2BzgV%2BEF5EnepXIm3qIfw%3D%3D"
url_pages = "1000" #페이지당열갯수
url_start_date = "20200101" #시작날짜
url_end_date = "20200601"            #datetime.today().strftime('%Y%m%d') #오늘 날짜
url = url_base + "?serviceKey=" + url_serviceKey + "&pageNo=1&numOfRows=" + url_pages +"&startCreateDt="+ url_start_date + "&endCreateDt=" + url_end_date #요청 양식



response = requests.get(url) #get 요청
response = response.content #get 요청의내용
xmlObject = xmltodict.parse(response) #xml데이터 형식으로 변환

dict_data = xmlObject['response']['body']['items']['item'] #xml 파싱
df = pandas.DataFrame(dict_data) #데이터 형식으로 변경 
df = df[['createDt','natDeathCnt','natDefCnt','nationNm']]#필요한 파일만 정렬
df['createDt'] = pd.to_datetime((df['createDt']))#날짜 데이터 형식으로
df = df.astype(({'natDeathCnt':'int','natDefCnt':'int'}))
df = df.sort_values(by='createDt') # 날짜순으로 정렬



nationname = st.sidebar.multiselect('국가를 선택하세요',['한국','일본','중국'])


#
# south_korea = df[df['nationNm']=='한국']
# japan = df[df['nationNm']=='일본']
#

# st.write(south_korea)
# st.write(japan)
plt.rc('font',family='Malgun Gothic')

for value in nationname:
    temp = df[df['nationNm']==value]
    plt.plot(temp['createDt'], temp['natDefCnt'], label=value)

# plt.plot(south_korea['createDt'],south_korea['natDefCnt'],label='korea')
# plt.plot(japan['createDt'],japan['natDefCnt'],label='japan')
plt.legend() 
st.pyplot(plt)

