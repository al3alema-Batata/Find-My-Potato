import cohere
import apikey

# initialize the Cohere Client with an API Key
cohere.api_key=apikey.apiKey



#from chatGPT trying to open a chat model
#Define a function that interacts with the Cohere API to generate a response
def generate_response(input_text):
    prompt = "Your bot prompt: " + input_text
    model = 'gpt-3.5-turbo'
    response = cohere.Completion.create(prompt=prompt, model=model)
    return response['choices'][0]['text']

#Create a function that handles incoming messages and generates a response using the Cohere API:
def handle_message(message):
    response = generate_response(message)
    print("Bot:", response)

#In the main function, prompt the user for input and call the handle_message function:
def main():
    while True:
        user_input = input("You: ")
        handle_message(user_input)

if __name__ == "__main__":
            main()
