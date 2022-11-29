import pickle
import streamlit as st
import pandas as pd
import numpy as np
  
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
  
st.set_page_config(
    page_title="Prediksi Pinjaman",
    page_icon="💵",
)

st.image("home.png")
st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")
with st.sidebar:
  st.write("[Data Pinjaman Online](https://github.com/Faridghozali/Pred_Presetujuan-Pinjaman/blob/main/prediksiloan.csv)")
  st.write("[pre-processing](https://colab.research.google.com/drive/1M5BLquVoCbl9KyfmfvcsNd_MEGfVRD3B)")
  st.write("[Source Code](https://github.com/Faridghozali/Pred_Presetujuan-Pinjaman/blob/main/app.py)")
  st.write("[Biodata](https://mybiodata.21-119farid.repl.co/biodata.html)")
  st.write("-----------------")
  st.header("Penjelasan Fitur") 
  st.text("> Gender adalah untuk peminjam memasukkan jenis kelamin")
  st.text("> Marital Status adalah untuk peminjam memasukkan Status perkawinan ")
  st.text("> Applicants monthly income adalah untuk peminjam mesukkan pendapatan setiap bulan ")
  st.text("> Total loan amount adalah untuk peminjam mesukkan total jumlah pinjaman")
  st.text("> Credit_History adalah untuk mesukkan riwayat kredit peminjam")
  st.write("-----------------")
  st.header("Tentang Aplikasi")
  st.write("Jumlah Pinjaman dan Jangka Waktu Pinjaman, yang memberi tahu saya jumlah pinjaman dalam ribuan dan jangka waktu pinjaman masing-masing dalam bulan.")
  st.write("Riwayat Kredit menunjukkan apakah pelanggan memiliki hutang yang tidak jelas sebelumnya atau tidak.")
  st.write("Selain itu, saya juga memiliki detail pelanggan, seperti Jenis Kelamin, Status Perkawinan, pendapatan. Dengan menggunakan fitur-fitur tersebut, saya akan membuat model prediksi yang akan memprediksi variabel target yaitu Status Pinjaman yang mewakili apakah pinjaman akan disetujui atau tidak.")

# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
    st.header("FAQ > Masalah Pinjaman")
    st.image("info.png")
    

if __name__=='__main__': 
    main()
