import streamlit as st
import pickle
import pandas as pd
import sklearn as skl

st.set_page_config("Titanic Survival")

st.title("Titanic Survival Prediction")
filename = 'model.pkl'
with open(filename,"rb") as file:
    LR=pickle.load(file)

st.header("Input Features")

Pclass=st.radio("Pclass", options=[1,2,3],index=0)
SibSp=st.text_input("SibSp")
Parch=st.slider("Parch",min_value=0,max_value=10)
Fare=st.text_input("Fare",value="0.0")
Age=st.text_input("Age")
cabin=st.radio("Cabin",options=[0,1],format_func=lambda x:"No" if x==0 else "Yes")
Embarked=st.radio("Embarked",options=["Southampton","Cherbourg","Queenstown"])
Sex_encoded=st.radio("Sex_Encoded",options=[0,1],format_func=lambda x:"Female" if x==0 else "Male")

embarked_mapping={
    "Southampton":0.339009,
    "Cherbourg":0.553571,
    "Queenstown":0.389610
}
embarked_encoded=embarked_mapping[Embarked]

test_input={
    "Pclass":[Pclass],
    "SibSp":[SibSp],
    "Parch":[Parch],
    "Fare":[Fare],
    "Age":[Age],
    "Cabin":[cabin],
    "Embarked":[embarked_encoded],
    "Sex":[Sex_encoded]
}

test_df=pd.DataFrame(test_input)

#prediction
if st.button("Predict"):
    prediction=LR.predict(test_df)
    prediction_proba=LR.predict_proba(test_df)

    st.subheader("Prediction")
    if int(prediction[0])==0:
        st.markdown("# Passenger is Died!!")
    else:
        st.markdown("# Passenger is Survived!!")


    st.subheader("prediction probability")
    st.write("Probability of each class:",prediction_proba)


