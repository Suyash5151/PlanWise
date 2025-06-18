import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDbh4GAj6DzApAqtUtfbRdAl7fQ71o8oZM")  

model = genai.GenerativeModel("gemini-2.0-flash")

st.title("💰 Personal Finance Tip Generator")
with st.form("finance_form"):
    user_input = st.text_input("Describe your financial goal or situation:")
    user_cost= st.number_input("What is the estimated cost to achieve this goal?",min_value=0, step=100)
    user_salary = st.number_input("Enter your monthly salary:", min_value=0, step=100)
    user_expenses = st.number_input("Enter your monthly expenses:", min_value=0, step=100)
    user_investments = st.number_input("Enter your current monthly investments:", min_value=0, step=100)
    user_behaviour=st.selectbox("What is your investing risk profile",["Aggressive Investor","Balanced Investor","Conservative Investor"])
    submitted = st.form_submit_button("Submit")

if user_behaviour=="Aggressive Investor":
    user_risk="Suggest mutual funds with 80pcnt. equity and 20pcnt. debt (indian mutual funds only)"
elif user_behaviour=="Balanced Investor":
    user_risk="Suggest mutual funds with 50pcnt. equity and 50pcnt. debt indian mutual funds only)"
else:
    user_risk="Suggest mutual funds with 20pcnt. equity and 80pcnt. debt indian mutual funds only)"



if submitted:
    with st.spinner("Thinking..."):
        response = model.generate_content(
            f"Give a personal finance tip for achieving this goal: {user_input}, "
            f"with a monthly salary of: {user_salary}, "
            f"monthly expenses: {user_expenses}, "
            f"current monthly investments: {user_investments}, "
            f"and an investing risk profile of: {user_behaviour}."
            f"Suggest mutual funds for:{user_risk}"
            f"Dont provide key considerations,how to invest,important considerations "
        )

        st.success("Tip:")
        st.write(response.text)