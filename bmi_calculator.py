

import streamlit as st
import streamlit .components.v1 as com
import time
com.html(""" <div>
<style>
h1.heading{
    background-color:blueviolet;
    color:lightyellow;
    border-radius:20px;
    text-align: center;
}
marquee{
color: green;
}
div{
    text-align:center;
}
</style>
<h1 class = "heading">*BMI CALCULATEOR*</h1>
</div> <marquee>... healthy body is better than gold</marquee><hr>""", width=600,)


height = st.number_input("Enter your height in M:", step=0.1)
weight = st.number_input("Enter your Weight in KG:", step=0.1)

if st.button("Calculate BMI"):
    if weight != 0.0 and height != 0.0:
        if weight != st.empty() and height != st.empty():
            value = weight/(height**2)
            format_string = "{:.2f}".format(value)
            bmi = float(format_string)

        else:
            st.wirte("please enter the values")
        if bmi >= 18.6 and bmi <= 24.9:
            st.success(f" Your BMI is: {bmi}")
            st.success("Your BMI is normal, congratulation,Keep your body fit ")
        if bmi > 24.9:
            st.success(f" Your BMI is: {bmi}")
            st.subheader("Caution!!!")
            st.write("Please watch your WEIGHT")
            st.write("Please adhere to the following instructions")
            st.write("1. Engage yourself on constant daily exercise ")
            st.write("2. Take atleast 10liter of water every day")
            st.write("3. Eat more of fruits ")
            st.write("4. Avoid any thing alcohol and sugar")
        elif bmi == 24:
            st.success(f" Your BMI is: {bmi}")
            st.write("Your weight is not too bad, but keep watch on it ")
        elif bmi >= 0 and bmi < 18.6:
            st.success(f" Your BMI is: {bmi}")
            st.write(
                "You are underweight , Peasse eat good diet and avoid much stress")

    else:

        st.markdown("Error!!! , Please Check the value of weight and height")


if st.checkbox("Read more about BMI  and Your Health"):
    st.subheader(""" What is BMI and why is it important?""")
    st.markdown(""" Body Mass Index (BMI) is a person's weight in kilograms (or pounds) divided by 
the square of height in meters (or feet). A high BMI can indicate high body fatness. BMI screens 
for weight categories that may lead to health problems, but it does not diagnose the body 
fatness or health of an individual.""")

    st.markdown("""
BMI is an estimate of body fat and a good gauge of your risk for diseases that can occur with more 
body fat. The higher your BMI, the higher your risk for certain diseases such as heart disease, high 
blood pressure, type 2 diabetes, gallstones, breathing problems, and certain cancers. """)
    st.subheader(""" NOTE THE FOLLOWING""")
    st.markdown(""" BMI ranges For most adults are as follows""")
    st.markdown("If your BMI is:")
    st.markdown("1. Below 18.5  you're in the underweight range")
    st.markdown("2. 18.5 and 24.9 you're in the healthy weight range")
    st.markdown("3. Between 25 and 29.9 you're in the overweight range")
    st.markdown("4. Between 30 and 39.9  you're in the obese range")


com.html("""<hr><div>
<style>

p{
background-color:blueviolet;
color:lightyellow;
border-radius:20px;
text-align:right;
}
div{
    text-algin:center;
}
</style>
<p>...@all right reserved for DataLab</p>
</div>""", width=600, height=-500,)
st.markdown(
    "<style>#MainMenu, footer{visibility: hidden}.css-12oz5g7{background-color:lightblue}.css-1x8cf1d{color:blueviolet; border redius:50px;}</style>", unsafe_allow_html=True)
