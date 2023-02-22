import json
import random

# Load the intents and responses from the JSON file
with open('intents.json') as file:
    data = json.load(file)

# Define a function to get a random response for an intent
intents = 'goodbye'
def get_response(intents):
    responses = data[intents]['responses']
    return random.choice(responses)

# Define a function to get the intent for a user input
def get_intent(user_input):
    for intents in data:
        for pattern in data[intents]['patterns']:
            if pattern in user_input:
                return intents
    return 'not_found'

# Start the conversation with the user
print('Chatbot: Hello, how can I help you?')
while True:
    user_input = input('You: ')
    intents = get_intent(user_input)
    if intents == 'not_found':
        print('Chatbot: Sorry, I didn\'t understand that.')
    else:
        response = get_response(intents)
        print('Chatbot:', response)
