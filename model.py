import streamlit as st
from PIL import Image
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def run():
    # Header Image
    img1 = Image.open('bank.png')
    img1 = img1.resize((156, 145))
    st.image(img1)
    st.title("Bank Loan Prediction")

    # Inputs
    account_no = st.text_input("Account Number")
    fn = st.text_input("Full Name")

    gen = st.selectbox("Gender", [0,1], format_func=lambda x: ("Female","Male")[x])
    mar = st.selectbox("Marital Status", [0,1], format_func=lambda x: ("No","Yes")[x])
    dep = st.selectbox("Dependents", [0,1,2,3], format_func=lambda x: ("No","One","Two","More than Two")[x])
    edu = st.selectbox("Education", [0,1], format_func=lambda x: ("Not Graduate","Graduate")[x])
    emp = st.selectbox("Employment Status", [0,1], format_func=lambda x: ("Job","Business")[x])
    prop = st.selectbox("Property Area", [0,1,2], format_func=lambda x: ("Rural","Semi-Urban","Urban")[x])
    cred = st.selectbox("Credit Score", [0,1], format_func=lambda x: ("300-500","Above 500")[x])

    mon_income = st.number_input("Applicant Monthly Income ", 0)
    co_mon_income = st.number_input("Co-Applicant Monthly Income ", 0)
    loan_amt = st.number_input("Loan Amount", 0)

    dur_options = [60,180,240,360,480]
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_index = st.selectbox("Loan Duration", list(range(len(dur_options))), format_func=lambda x: dur_display[x])
    duration = dur_options[dur_index]

    if st.button("Submit"):
        features = np.array([[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]])
        
        prediction = model.predict(features)[0]

        if prediction == 0:
            st.error(f"Hello {fn} | Account No: {account_no} | You will NOT get the loan.")
        else:
            st.success(f"Hello {fn} | Account No: {account_no} | Congratulations! You are eligible for the loan.")

run()
