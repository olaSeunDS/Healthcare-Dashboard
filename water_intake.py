import streamlit as st

age=st.sidebar.number_input('what is your age',step=1)
gender=st.sidebar.selectbox('what is your gender',['male','female'])
m=st.sidebar.number_input('How many minutes do you exercise',step=1)
st.sidebar.image('water-cup.jpg')
def DWC(age,gender,w,m):
    if age < 30:
        f=0.642
    elif 30<age<51:
        f=0.56
    else:
        f=0.481

    if gender=='female':
        g=0.73
    else:
        g=1
        
    w=w*2.2
    
    c=(w*f*g+(12*m/30))/8
    st.write (f'Please take about {round(c,1)} cups')
    
if st.button('Calculate water intake'):
    DWC(age,gender,w,m)
    
    
