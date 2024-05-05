import streamlit as st

# Title
st.title("Input and Output Boxes")

# Input box
user_input = st.text_input("Emotion Detection based on Text and Emojis")

# Output box
st.write("Output:", user_input)
