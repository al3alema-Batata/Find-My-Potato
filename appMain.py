#second attempt here tyrying just to add chat

import json
import cohere

# Read API key from JSON config file
with open('config.json') as config_file:
    config = json.load(config_file)
cohere.api_key = config['cohere_api_key']

# Rest of your code
def generate_response(input_text):
    prompt = "User: " + input_text + "\nOptions: Option 1, Option 2, Option 3"
    model = 'gpt-3.5-turbo'
    response = cohere.Completion.create(prompt=prompt, model=model)
    return response['choices'][0]['text']

def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("Chatbot:", response)
#meaningthe program will only run if the if statements are true
if __name__ == "__main__":
    main()
