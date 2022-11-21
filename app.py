import pickle
import streamlit as st
 
  html_temp = """ 
    		<header id="header" class="" data-scroll-index="0">

			<div id="header-wrap">

				<div class="container">
					<div class="row">
						<div class="col-md-12">
							<a class="logo logo-header" href="#">
								<img src="static/logo1.png" data-logo-alt="static/logo1.png" alt="">
								<h3><span class="colored">Gajiku</span></h3>
								<span>HTML Template</span>
							</a><!-- .logo end -->
							<div class="header-menu-and-meta">
								<div class="header-meta">
									<nav>
										<a href="biodata.html">About me</a>
									</nav>
								</div><!-- .header-meta end -->								
								<!-- <div class="clearfix"></div> -->
							</div><!-- .header-menu-and-meta end -->

						</div><!-- .col-md-12 end -->
					</div><!-- .row end -->
				</div><!-- .container end -->

			</div><!-- #header-wrap end -->

		</header><!-- #header end -->

		<!-- Banner
		============================================= -->
		<section id="banner" data-scroll-index="0">

			<div class="banner-parallax">
				<img src="images/files/parallax-bg/img-1.jpg" alt="">
				<div class="overlay-colored" data-bg-color="#000" data-bg-color-opacity="0.65"></div><!-- .overlay-colored end -->
				<div class="slide-content">

					<div class="container">
						<div class="row">
							<div class="col-md-10 col-md-offset-1">

								<div class="banner-center-box text-white text-center">
									<h1>Diabetes adalah penyakit kronis yang ditandai dengan tingginya kadar gula darah. </h1>
									<div class="description">
                    Glukosa merupakan sumber energi utama bagi sel tubuh manusia. Akan tetapi, pada penderita diabetes, glukosa tersebut tidak dapat digunakan oleh tubuh. Kadar gula (glukosa) dalam darah dikendalikan oleh hormon insulin yang diproduksi pankreas. Namun, pada penderita diabetes, pankreas tidak mampu memproduksi insulin sesuai kebutuhan tubuh. Tanpa insulin, sel-sel tubuh tidak dapat menyerap dan mengolah glukosa menjadi energi.
										<br>
									</div>
									<a class="scroll-to btn xx-large colorful hover-dark mt-30" href="#our-services">syarat dan kriteria</a>
								</div><!-- .banner-center-box end -->

							</div><!-- .col-md-10 end -->
						</div><!-- .row end -->
					</div><!-- .container end -->

				</div><!-- .slide-content end -->
			</div><!-- .banner-parallax end -->

		</section><!-- #banner end -->
    """
  
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
     
if __name__=='__main__': 
    main()
