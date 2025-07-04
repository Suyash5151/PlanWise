import streamlit as st
import google.generativeai as genai


api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("💰 Personal Finance Tip Generator")
with st.form("finance_form"):
    user_input = st.text_input("Describe your financial goal (Ex. Buying a car):")
    user_cost= st.number_input("What is the estimated cost to achieve this goal?",min_value=0,step=1000)
    user_salary = st.number_input("Enter your monthly salary:", min_value=0, step=1000)
    user_expenses = st.number_input("Enter your monthly expenses:", min_value=0, step=1000)
    user_investments = st.number_input("Enter your current monthly investments:", min_value=0, step=1000)
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
            f"Give a personal finance tip for achieving this goal: {user_input},with a cost of:{user_cost} "
            f"with a monthly salary of: {user_salary}, "
            f"monthly expenses: {user_expenses}, "
            f"current monthly investments: {user_investments}, "
            f"and an investing risk profile of: {user_behaviour}."
            f"Suggest mutual funds for:{user_risk}"
            f"Dont provide key considerations,how to invest,important considerations"
            f"Provide detailed explaination on how your invested money will grow at a specific rate of interest of the mutual fund and how many years it will take to achieve the goal be specific about the price of the goal user has given"
            f"Focus on the investments the user is making and not on the money that is left over that might be used for other purposes"
            
        )

        st.success("Tip:")
        st.write(response.text)