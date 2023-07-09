"""
Chitchat
Now you're going to leave the simple EchoBot behind and create a bot which can answer simple questions such as "What's your name?" and "What's today's weather?"

You'll use a dictionary with these questions as keys and the correct responses as values.

This means the bot will only respond correctly if the message matches exactly, which is a big limitation. In later exercises you will create much more robust solutions.

The send_message() function has already been defined for you, as well as the bot_template and user_template variables.

Instructions 1/2
50 XP
1
2
Define a respond() function which takes in a message argument, checks if the message has a pre-defined response, and returns the response in the responses dictionary if there is a match, or the "default" message otherwise.
Instructions 2/2
Well Done! Your bot is now able to answer some simple questions. Hit 'Run Code' and call send_message() (which utilizes the new respond() function) in the IPython Shell with the following questions:
"what's today's weather?"
"what's your name?"
"what's your favorite color?"
Hit 'Submit Answer' when you are done.
"""
bot_template = "BOT : {0}"
user_template = "USER : {0}"


# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

send_message("what's today's weather?")
send_message("what's your name?")
send_message("default")
