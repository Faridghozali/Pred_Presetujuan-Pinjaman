import pickle
import streamlit as st
import aspose.words as aw

  
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
    page_title="Loan Prediction ML App",
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
    <h1 style ="color:black;text-align:center;">Loan Prediction ML App</h1> 
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
     
if __name__=='__main__': 
    main()
    
# Load the license
wordToHtml = aw.License()
wordToHtml.set_license("Aspose.Total.lic")

# Create an empty document and instantiate DocumentBuilder with it
wordDoc = aw.Document()
docBuilder = aw.DocumentBuilder(wordDoc)

# Set flag to add a different header for the first page
docBuilder.page_setup.different_first_page_header_footer = True

# Create different headers
docBuilder.move_to_header_footer(aw.HeaderFooterType.HEADER_FIRST)
docBuilder.write("First page header")
docBuilder.move_to_header_footer(aw.HeaderFooterType.HEADER_PRIMARY)
docBuilder.write("Primary header for all common pages")

# Move control to the first section of the document
docBuilder.move_to_section(0)

# Add multiple pages with some text and add page breaks to observe the functionality
for x in range(6):
    docBuilder.writeln("Page " + str(x + 1))
    docBuilder.insert_break(aw.BreakType.PAGE_BREAK)

# Save the output file
wordDoc.save("Output.docx")

print ("Header added successfully")
