import cohere
from langchain.prompts import prompt
import apikey
# initialize the Cohere Client with an API Key
cohere.api_key=apikey.apiKey
######
def test (topic):
  import cohere
  print("hi")
  co = cohere.Client(apikey.apiKey) ;print("hi")
  print("hi")  # This is your trial API key
  response = co.generate(
  model='command',
  prompt='give me top reated hotels in saudi arabia \"{topic}\"',
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[], 
  return_likelihoods='NONE')
  print("hi")
  print('Prediction: {}'.format(response.generations[0].text))
#print('Prediction: {}'.format(response.generations[0].text))

test("AI")
