import streamlit as st

st.title("power calculator")
st.write("enter a number to get its square , cube and 5th power ")

n = st.number_input('Enter an integer ', value=1,step=1)

square = n ** 2
cube = n ** 3
fifthpow = n ** 5

st.write(f" square of {n} is {square} ")
st.write(f" cube of {n} is {cube} ")
st.write(f" fifth power of {n} is {fifthpow} ")
 