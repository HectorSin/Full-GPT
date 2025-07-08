import streamlit as st
from datetime import datetime

today = datetime.today().strftime("%H:%M:%S")

st.write(today)

model = st.select_slider("Select a number",options=[1,2,3,4,5,6,7,8,9,10])

st.write(model)

name = st.text_input("Enter your name")

st.write(name)






    