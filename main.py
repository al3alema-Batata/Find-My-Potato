import cohere
import streamlit as st

import requests
from apikey import apikey, apikeyG
from geopy.geocoders import GoogleV3

# Initialize Google Maps geocoder
geocoder = GoogleV3(api_key=apikeyG)


# Writing a prompt for my model
def myPrompt(question):
    return 'You are a Friendly Tour guide in KSA that answers questions:'


def search_places(query):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': apikeyG,
        'query': query
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['results']


def get_reviews(place_id):
    url = 'https://maps.googleapis.com/maps/api/place/details/json'
    params = {
        'key': apikeyG,
        'place_id': place_id,
        'fields': 'reviews'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['result']['reviews']


def get_place_map_url(place_id):
    return f"https://www.google.com/maps/place/?q=place_id:{place_id}"


def batataBot(question, search_query):
    cohere_instance = cohere.Client(api_key=apikey, version='2021-11-08')
    prompt = myPrompt(question) + f"\n\nSearch for '{search_query}' in Google Maps and provide reviews."
    response = cohere_instance.generate(
        model='medium',
        prompt=prompt,
        max_tokens=150,
        temperature=0.8
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
    place_types = ['Shopping', 'Food', 'Activities']

    # User selection for the type of places to visit
    selected_types = st.multiselect("Select the type of places you want to visit", place_types)

    # User input for preferences
    user_preferences = st.text_input("Enter your preferences")

    if st.button("Show Links"):
        if 'Shopping' in selected_types:
            # Show information related to Shopping
            st.header("Shopping Information")
            st.write("Here's a link to the shopping map:")
            st.markdown("[Shopping Map](https://goo.gl/maps/mGXjnhBZXR5CYnMMA)")

        if 'Activities' in selected_types:
            # Show information related to Activities
            st.header("Activities Information")
            st.write("Here's a link to the activities map:")
            st.markdown("[Activities Map](https://goo.gl/maps/VJpXGcpks5URY1fp9)")

        if 'Food' in selected_types:
            # Show information related to Food
            st.header("Food Information")
            st.write("Here's a link to the food map:")
            st.markdown("[Food Map](https://goo.gl/maps/mGXjnhBZXR5CYnMMA)")

    # if st.button("Search"):
    #     # Combine selected types and user preferences into a search query
    #     search_query = f"{', '.join(selected_types)} {user_preferences}"
    #
    #     # Searching for places in Google Maps
    #     places = search_places(search_query)
    #
    #     if places:
    #         st.subheader("Best Place:")
    #         selected_place = places[0]
    #         st.write(f"Name: {selected_place['name']}")
    #         st.write(f"Address: {selected_place['formatted_address']}")
    #         st.write(f"Rating: {selected_place['rating']}")
    #
    #         # Displaying the place on a map
    #         place_coordinates = selected_place['geometry']['location']
    #         st.write(f"Location: ({place_coordinates['lat']}, {place_coordinates['lng']})")
    #         map_url = get_place_map_url(selected_place['place_id'])
    #         st.markdown(f"[Show on Map]({map_url})")
    #
    #         # Getting reviews for the selected place
    #         reviews = get_reviews(selected_place['place_id'])
    #
    #         if reviews:
    #             st.subheader("Reviews:")
    #             for review in reviews:
    #                 st.write(f"- {review['text']}")
    #         else:
    #             st.write("No reviews found for this place.")
    #     else:
    #         st.write("No places found matching your preferences.")
    #
    # if st.button("Ask"):
    #     # Generating response from BatataBot
    #     response = batataBot(user_preferences, user_preferences)
    #
    #     # Displaying the response
    #     st.write("BatataBot:", response)


if __name__ == "__main__":
    main()
