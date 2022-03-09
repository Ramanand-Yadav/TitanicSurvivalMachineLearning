# %%writefile app.py
import streamlit as st
import pandas as pd
import pickle 
from PIL import Image

model = pickle.load(open('titanicModel.pkl', 'rb'))

def run():

    img1 = Image.open('img1.jpg')
    st.image(img1)

    st.title(
      """
      Titanic - Machine Learning from Disaster
      **Predicting survival on the Titanic and getting familiar with ML.**
      """
    )

    # Enter Name
    name = st.text_input('Enter Name')
   
    # Pclass
    Pclass = st.number_input("Ticket Class", min_value=1, max_value=3, value=1)
   
    #Gender
    sex = st.selectbox("Select Gender", ('Male', 'Female'))

    #Age
    age = st.number_input("Enter Your Age", min_value=1, max_value=80, value = 1)
    #st.write(age)

    #SibSp
    SibSp = st.selectbox("Number of child", (0, 1, 2, 3, 4, 5, 8))
    st.write(SibSp)

    #Parch
    Parch = st.selectbox("Number of guardian",(0, 1, 2, 3, 4, 5, 6))
    # st.write(Parch)

    #Fare
    Fare = st.number_input("Ticket Price", min_value=0.0, max_value=512.3292)
    # st.write(Fare)

    #Embarked
    Embarked = st.selectbox("Port of Embarkation", ('S', 'C', 'Q'))
    # st.write(Embarked)

    #CabinLetter
    CabinLetter = st.selectbox("Choose Cabin Latter", ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'Unknown'))
    # st.write(CabinLetter)

    #relatives
    relatives = st.selectbox("No. of relatives", (0, 1, 2, 3, 4, 5, 6, 7, 10))
    # st.write(relatives) 

    df = pd.DataFrame({'Pclass':Pclass, 'Sex':sex, 'Age':age, 'SibSp':SibSp, 'Parch':Parch, 'Fare':Fare,
                        'Embarked':Embarked, 'CabinLetter':CabinLetter, 'relatives':relatives}, index=[0])

    
    # st.write(df)

    if st.button('Check'):
        prediction = model.predict(df)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        
        if ans == 0:
            st.error(
                "Sorry! Rest in Peace"
            )
        else:
            st.success(
                "congrats you are safe!"
            )




  


run()