import streamlit as st
st.title("my first streamlit app")
name=st.txt_input("enter your name")

if st.buttons("submit"):
  st.write("hello,{name}")
