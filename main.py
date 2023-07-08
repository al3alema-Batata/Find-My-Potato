import cohere
import streamlit as st
from apikey import apikey
# Writing a prompt for my model
def myPrompt(question):
    return 'You are a Friendly Tour guide in KSA that answers questions:'

def batataBot(question):
    cohere_instance = cohere.Client(apikey, '2021-11-08')
    response = cohere_instance.generate(
        model='medium',
        prompt=myPrompt(question),
        max_tokens=50,
        temperature=1
    ).generations[0].text
    return response

# Streamlit app configuration
st.set_page_config(page_title="BatataBot", layout="wide")

# Writing the app main function
def main():
    # Setting up the app title and description
    st.title("BatataBot: Your Friendly Tour Guide")
    st.write("Ask any question, and BatataBot will provide answers!")

    # Available place types for the checklist
    place_types = ['Restaurant', 'Coffee Shop', 'Activities', 'Others']

    # User selection for the type of place to visit
    selected_types = st.multiselect("Select the type of place you want to visit", place_types)

    # User input for ideal place or preferences
    user_preferences = st.text_input("Enter your ideal place or preferences")

    if st.button("Ask"):
        # Generating response from BatataBot
        response = batataBot(user_preferences)

        # Displaying the response
        st.write("BatataBot:", response)

if __name__ == "__main__":
    main()








