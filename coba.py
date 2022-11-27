import pickle
import streamlit as st
import pandas as pd
import numpy as np


st.sidebar.header("Pilihan kategori")
#Upluad file CSV Untuk pilihan kategori
upluad_file.st.sidebar.file_Uploader("Upload file CSV anda",type=["csv"])
if upload_file is not none:
  inputan=pd.read_csv(upload_file)
else :
  def prediction():
      Gender=st.sidebar.selectbox('Gender',('male','female'))
      Married=st.sidebar.selectbox('Marital Status',('Unmarried','Maried'))
      ApplicantIncome=st.sidebar.selectbox('Applicants monthly income',('
      LoanAmount=st.sidebar.selectbox(
      Credit_History=st.sidebar.selectbox('Credit_History',('Unclear Debts','Clear Debts'))
    (Gender, Married, ApplicantIncome, LoanAmount, Credit_History):
    
    
