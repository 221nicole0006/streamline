import streamlit as st

# Title and Image for Introduction
st.title("Emotion Detection based on Text and Emojis")
st.image("intro.png", use_column_width=True)

# Input box
user_input = st.text_input("Enter some text:")

# Output box
st.write("Output:", user_input)

# Image for Features
st.image("features.png", use_column_width=True)
