"""Intent classification with regex I
You'll begin by implementing a very simple technique to recognize intents - looking for the presence of keywords.

A dictionary, keywords, has already been defined. It has the intents "greet", "goodbye", and "thankyou" as keys, and lists of keywords as the corresponding values. For example, keywords["greet"] is set to "["hello","hi","hey"].

Also defined is a second dictionary, responses, indicating how the bot should respond to each of these intents. It also has a default response with the key "default".

The function send_message(), along with the bot and user templates, have also already been defined. Your job in this exercise is to create a dictionary with the intents as keys and regex objects as values.

Instructions
100 XP
Instructions
100 XP
Iterate over the keywords dictionary, using intent and keys as your iterator variables.
Use '|'.join(keys) to create regular expressions to match at least one of the keywords and pass it to re.compile() to compile the regular expressions into pattern objects. Store the result as the value of the patterns dictionary."""
# Define a dictionary of patterns
import re

keywords={'greet': ['hello', 'hi', 'hey'], 'goodbye': ['bye', 'farewell'], 'thankyou': ['thank', 'thx']}
patterns = {}

# Iterate over the keywords dictionary
for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

# Print the patterns
print(patterns)