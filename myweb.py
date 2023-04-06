import random
import streamlit as st
st.set_page_config(
    page_title="회원가입 시스템&가위바위보 게임",
    page_icon="😎"
)
class User:
    def __init__(self, name,password):
        self.name = name
        self.password = password


if 'user_Data' not in st.session_state:
    st.session_state['user_Data'] = []

if 'login' not in st.session_state:
    st.session_state['login'] = 'false'

if 'Game_Data' not in st.session_state:
    st.session_state['Game_Data'] = []

if 'Game_Point' not in st.session_state:
    st.session_state['Game_Point'] = 0

if st.session_state['login'] != 'true':
    register_user_name = st.sidebar.text_input(label="User Name")
    register_user_password = st.sidebar.text_input(label="User password",type="password")
if st.session_state['login'] != 'true':
    if st.sidebar.button('회원가입'):
        st.write('성공적으로 회원가입 했습니다!')
        st.session_state['user_Data'] = User(register_user_name, register_user_password)

if st.session_state['login'] == 'true':
    st.sidebar.write(f'환영합니다! {str(st.session_state["user_Data"].name)} 님!')
    st.sidebar.image('img.png')
    st.write(f'환영합니다! {str(st.session_state["user_Data"].name)} 님!')
    st.write(f"점수:{st.session_state['Game_Point']}점")

if st.session_state['login'] != 'true':
    login_user_name = st.sidebar.text_input(label="User Name", key=2)
    login_user_password = st.sidebar.text_input(label="User password",type="password" ,key=3)
    if st.sidebar.button('로그인') and st.session_state['user_Data'] != []:
        if st.session_state['user_Data'].name == login_user_name:
            if st.session_state['user_Data'].password == login_user_password:
                st.session_state['login'] = 'true'
                st.sidebar.write(f"환영합니다! {st.session_state['user_Data'].name} 님!")
                st.sidebar.image('img.png')
                st.write(f'환영합니다 {str(st.session_state["user_Data"].name)} 님!')
            else:
                st.sidebar.write('비밀번호가 다릅니다')
        else:
            st.sidebar.write('아이디가 다릅니다.')

if st.session_state['login'] == 'true':
    if st.button('게임 시작') or st.session_state['Game_Data'] !=[]:
        a = random.randrange(1, 4) #1은 가위 2는 바위 3은 보
        user_input = st.text_input(label="가위,바위,보 중 하나를 입력하세요!", key=4)
        if a == 1:
            b="가위"
        elif a == 2:
            b="바위"
        elif a == 3:
            b="보"

        if st.button('전송') or st.session_state['Game_Data'] ==[]:
            st.session_state['Game_Data'] = user_input

            if user_input == '가위':
                if a == 1:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('무승부!')
                elif a == 2:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('패배!')
                elif a == 3:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('승리!')
                    st.session_state['Game_Point'] = st.session_state['Game_Point'] + 1
            elif user_input == '바위':
                if a == 1:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('승리!')
                    st.session_state['Game_Point'] = st.session_state['Game_Point'] + 1
                elif a == 2:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('무승부!')
                elif a == 3:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('패배!')
            elif user_input == '보':
                if a == 1:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('패배!')
                elif a == 2:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('승리!')
                    st.session_state['Game_Point'] = st.session_state['Game_Point'] + 1
                elif a == 3:
                    st.write(f' 상대는{b}를 냈습니다!')
                    st.write('무승부!')




    # id = st.sidebar.text_input('아이디')
    # options = st.multiselect("좋아하는 음식",("치킨","피자"),("치킨"))
    # st.write(options)
    # option = st.selectbox("좋아하는 음식",("치킨","피자"))
    # st.write(option)
    # 장소 = st.radio("좋아하는 곳은",("집","학교","학원"),horizontal=True,disabled=True)




