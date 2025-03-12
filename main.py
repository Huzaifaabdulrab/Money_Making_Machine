import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1,100)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amout = generate_money()
    st.success(f"you made ${amout}")

def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustles?apiKey=12345')
        if response.status_code==200:
            hustles = response.json()
            return hustles['side_hustle']
        else :
            return ("Freelancing")
    except:
        return "Something went wrong"
    
st.subheader("Side Hustle Ideas")
if st.button("Get Side Hustle Ideas"):
    idea = fetch_side_hustle()
    st.success(idea)

def fetch_money_quotes():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes?apikey=12345')
        if response.status_code==200:
            moneyquotes = response.json()
            return moneyquotes['money_quote']
        else :
            return("Not Available")
    except:
        return "Something went wrong"
    
st.subheader("Money Quotes idea")
if st.button("Get Money Quotes Ideas"):
    idea= fetch_money_quotes()
    st.info(idea)