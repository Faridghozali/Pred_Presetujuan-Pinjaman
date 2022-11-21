import pickle
import streamlit as st
  
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

with st.sidebar:
    with st.echo():
         st.write("This code will be printed to the sidebar.")

st.set_page_config(
    page_title="Prediksi Pinjaman",
    page_icon="💵",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")
      
st.image('home.png')

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
  
