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
#pages
st.set_page_config(
 page_title=" Loan Prediction ML App",
 page_icon="💵",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")   

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
