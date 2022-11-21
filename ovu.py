import streamlit as st
import datetime
st.header('OVULATION CHECKER')

st.sidebar.write('''
This Ovulation checker provides an estimate of your fertile window
using your circle although each woman circle differs.
Knowing the days you are most likely to be fertile
can increase your chances of getting pregnant and it is not 
a guarantee of getting pregnant.

Use this calculator to see which days you are most active
''')

fmd=st.date_input("What is your First menstrual date")
circle=st.selectbox("What is your monthly circle",list(range(28,41)))

def Ovulation(fmd,cycle):
    e=circle-28 
    OV1=fmd+datetime.timedelta(13+e)
    OV2 =fmd+datetime.timedelta(18+e)
    st.write(f'Ovulation days is between {OV1} and {OV2}')
                   
if st.button("Calculate Ovulation Date"):
    Ovulation(fmd,circle)
    st.image('ugo.jpg')