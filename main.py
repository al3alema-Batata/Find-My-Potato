import cohere

# Writing a prompt for my model
def myPrompt(question):
    return 'You are a chatbot that answers questions:'

# Providing API Key Credentials
class CoHere:
    def __init__(self, api_key):
        self.co = cohere.Client(f'{api_key}', '2021-11-08')

    # A method to generate a text
    def cohere(self, question):
        return self.co.generate(
            model='medium',
            prompt=myPrompt(question),
            max_tokens=50,
            temperature=1
        ).generations[0].text
#streamlit section
#@Reemaalt @SheikhaAr
import streamlit as st
st.header("Welcome to Find my Batata")
st.header("Choose the kind of place you want")
st.checkbox("Restaurant")
st.checkbox("Cafe")
st.checkbox("Mall")
st.checkbox("Play")
st.chat_input(placeholder="Enter your preferences for place")






