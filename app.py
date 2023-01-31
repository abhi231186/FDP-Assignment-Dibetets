import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
pickle_in = open("decision_model.pkl","rb")
model=pickle.load(pickle_in)

def predict_note_authentication(Pregnancies ,Glucose,BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
  output= model.predict([[Pregnancies ,Glucose,BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
  print("Purchased", output)
  if output==[1]:
    prediction="He will be diabetic"
  else:
    prediction="He will not be diabetic"
  print(prediction)
  return prediction
def main():
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering and Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Dibetic prediction by Abhishek Dadhich</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"> Project Deployment under the guidence of Mr. Deepak Moud</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Dibetes Prediction")
    Pregnancies = st.number_input("Pregnancies",0,17)
    Glucose = st.number_input("Glucose",0,199)
    BloodPressure = st.number_input("BloodPressure",0,122)
    SkinThickness = st.number_input("SkinThickness",0,99)
    Insulin= st.number_input("Insulin",0,846)
    BMI= st.number_input("BMI",0,68)
    DiabetesPedigreeFunction= st.number_input("DiabetesPedigreeFunction",0,67)
    Age = st.number_input("Insert Age",18,60)
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(Pregnancies ,Glucose,BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
      st.success('Model has predicted {}'.format(result))
    if st.button("About"):
      st.subheader("Developed by Abhishek Dadhich")
      st.subheader(" Developer")

if __name__=='__main__':
  main()
   
