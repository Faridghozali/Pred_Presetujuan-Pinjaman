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

st.title("")

def main_page():
    st.markdown("# Home🎈")
    st.sidebar.markdown("# Main page 🎈")
    st.image('home.png')

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Aplikasi Prediksi Pinjaman</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Jenis Kelamin',("Pria","Wanita"))
    Married = st.selectbox('Status Pernikahan',("Belum Menikah","Menikah")) 
    ApplicantIncome = st.number_input("Penghasilan Bulanan") 
    LoanAmount = st.number_input("Total Jumlah Pinjaman")
    Credit_History = st.selectbox('Riwayat Kredit',("pernah","tidak pernah"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Prediksi"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)

    st.title("FAQ > Masalah Pinjeman")
    st.image('info.png')
        
     
if __name__=='__main__': 
    main()
  
