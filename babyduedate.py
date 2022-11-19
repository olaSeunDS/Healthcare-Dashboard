import streamlit as st
import datetime
st.header('Baby Due Date Calculator')
LMP=st.date_input("First day of your last period")
Monthly_cycle=st.selectbox('Your monthly cycle',list(range(21,46)))
def Edd_calculator (LMP,Monthly_cycle):
    z=Monthly_cycle-25
    edd=LMP+datetime.timedelta(277+z)
    st.write(f'Your expected due date is {edd}')
if st.button("Calculate"):    
    Edd_calculator(LMP,Monthly_cycle)
