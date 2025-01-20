import streamlit as st

st.header('this is my first st.button')

if st.button('click here'):
     st.write('say hello?')
else:
     st.write('goodbye')
