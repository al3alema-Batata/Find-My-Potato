import cohere
import apikey

# initialize the Cohere Client with an API Key
co = cohere.Client(apikey.apiKey)


# generate a prediction for a prompt
# prediction = co.generate(
#             model='large',
#             prompt='co:here',
#             max_tokens=10)

# print the predicted text
# print('prediction: {}'.format(prediction.generations[0].text))