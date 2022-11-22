import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.header('PREGNANCY WEIGHT GAIN CALCULATOR')
st.sidebar.title('ABOUT WEIGHT GAIN CALCULATOR')
st.sidebar.subheader("The pregnancy weight gain calculator estimates a schedule for healthy weight gain based on Body Mass Index (BMI) of the individual before pregnancy. It provides schedule on weekly basis of the pregnancy. The pregnancy weight gain calaculator gives the estimate of your expected weight gain. Kindly note that pregnant individuals are also expect to see their doctors, midwife or other health care providers for general advice.")
weight_b = st.number_input("weight before pregnancy in kg\n")
height_b = st.number_input("height in metres \n")
preg_du = st.number_input("Pregnancy Period, number of weeks of pregnancy \n")
is_twins = st.selectbox("Expecting Twins?", ['no', 'yes'])

if st.button('Calculate Weigh Gain') :    
    def PWGC(weight_b, height_b, preg_du, is_twins) : 

        BMI_b = (weight_b/(height_b**2))
        l1 = []
        l2 = []
        if is_twins == 'yes':
            if BMI_b < 18.5 :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Underweight")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.8, 3)
                            w2 = round(w2+0.8, 3)
                        else :
                            w1 = round(w1+0.8, 3)
                            w2 = round(w2+0.9, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1

                        l1.append(w1)
                        l2.append(w2)                


            elif 18.5 < BMI_b < 24.9 :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Normal")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.8, 3)
                            w2 = round(w2+0.8, 3)
                        elif 28 < n < 40 :
                            w1 = round(w1+0.7, 3)
                            w2 = round(w2+0.8, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1
                        l1.append(w1)
                        l2.append(w2)

            elif 25 < BMI_b < 29 :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Overweight")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.6, 3)
                            w2 = round(w2+0.6, 3)
                        elif 28 < n < 40 :
                            w1 = round(w1+0.5, 3)
                            w2 = round(w2+0.6, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1
                        l1.append(w1)
                        l2.append(w2)

            else :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Obese")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.5, 3)
                            w2 = round(w2+0.5, 3)
                        else :
                            w1 = round(w1+0.5, 3)
                            w2 = round(w2+0.6, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1
                        l1.append(w1)
                        l2.append(w2)


        else:
            if BMI_b < 18.5 :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Underweight")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.5, 3)
                            w2 = round(w2+0.5, 3)
                        else :
                            w1 = round(w1+0.5, 3)
                            w2 = round(w2+0.6, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1                                
                        l1.append(w1)
                        l2.append(w2)

            elif 18.5 < BMI_b < 24.9 :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Normal")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.5, 3)
                            w2 = round(w2+0.5, 3)
                        elif 28 < n < 40 :
                            w1 = round(w1+0.4, 3)
                            w2 = round(w2+0.5, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1
                        l1.append(w1)
                        l2.append(w2)

            elif 25 < BMI_b < 29 :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Overweight")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.3, 3)
                            w2 = round(w2+0.3, 3)
                        elif 28 < n < 40 :
                            w1 = round(w1+0.2, 3)
                            w2 = round(w2+0.3, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1
                        l1.append(w1)
                        l2.append(w2)

            else :
                st.write(f"your BMI is: {round(BMI_b, 1)}")
                st.write(f"Obese")
                st.write(f"Below is the estimated weight gain for your pregnancy")
                if preg_du < 40:
                    i = 40 - preg_du        
                    w1 = weight_b
                    w2 = weight_b
                    n = 1
                    while n < 41:
                        if 0 < n < 13 :
                            w1 = round(w1+0.04, 3)
                            w2 = round(w2+0.15, 3)
                        elif 12 < n < 29 :
                            w1 = round(w1+0.2, 3)
                            w2 = round(w2+0.2, 3)
                        else :
                            w1 = round(w1+0.2, 3)
                            w2 = round(w2+0.3, 3)

                        st.write(f"week {n} \n", w1,"-", w2)

                        n=n+1
                        l1.append(w1)
                        l2.append(w2)



        ndict = {'low limit':l1, 'high limit':l2}
        df = pd.DataFrame(ndict)
        x = range(1,41)
        fig=plt.figure(figsize=(12,8))
        plt.plot(x,l1,  c='#00ff00')
        plt.plot(x,l2,  c='red')
        plt.xticks(list(range(1,41)))
        plt.title('Pregnancy Weight Gain', color='#000000', fontsize=16, fontweight='bold')
        plt.xlabel('Weeks of Pregnancy', color='#000000', fontsize=16)
        plt.ylabel('Expect Weight', color='#000000', fontsize=16)
        st.pyplot(fig)
        st.write(f"The Red line indicates the maximum expected weight gain, while the green line indicates the minimum expected weight gain on weekly basis. Any weight higher than the maximum or lower than the minimum is outrageous.")

    PWGC(weight_b, height_b, preg_du, is_twins)
