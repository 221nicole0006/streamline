import streamlit as st

# Title
st.title("Input and Output Boxes")

# Input box
user_input = st.text_input("Enter some text:")

# Output box
st.write("Output:", user_input)
