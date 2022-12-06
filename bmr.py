

import streamlit as st
st.header("BASAL METABOLIC CALCULATOR")

category = st.selectbox("Select Your Gender Category", [
                        "Select your catergory", "Male", "Female", "Others"])
weightInKg = st.number_input("What is your Weight in KG", step=0.0)
heightInCm = st.number_input("What is your Height in CM", step=0.0)
age = st.number_input("What is your age", step=1)

if st.button("Calculate"):

    if category == "Male":
        bmr = (66 + (6.23 * weightInKg) +
               (12.7 * heightInCm) - (6.8 * age))
        st.write("your BMR IS:")
        st.success(bmr)
        st.write("Your category is: MALE")

    elif category == "Female":
        bmr = (655 + (4.35 * weightInKg) +
               (4.7 * heightInCm) - (4.7 * age))
        st.write("your BMR IS:")
        st.success(bmr)
        st.write("Your category is:FEMALE")

    elif category == "Others":

        bmr = (655 + (4.35 * weightInKg) +
               (4.7 * heightInCm) - (4.7 * age))
        st.write("Your BMR IS:")
        st.success(bmr)
        st.write("Your category is: OTHERS")
    elif category == "Select your catergory":
        st.write("Please make your selection and continue")
else:
    st.write("Please check your values before your click CALCULATE BUTTON")
