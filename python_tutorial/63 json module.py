"""load(): This method is used to load data from a JSON file into a python dictionary.
Loads( ): This method is used to load data from a JSON variable into a python dictionary.
dump():This method is used to load data from the python dictionary to the JSON file.
dumps(): This method is used to load data from the python dictionary to the JSON variable."""
"""import json

data='{"var1":"harry","var2":56}'
print(data)

parsed=json.loads(data)
print(parsed)

data2= {
    "channel_name": "Sanidhya",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
jscomp=json.dumps(data2)
print(jscomp)"""
"""difference between load and loads"""
"""json.load() takes a file object and returns the json object. 
It is used to read JSON encoded data from a file and convert
 it into a Python dictionary and deserialize a file itself i.e. it accepts a file object."""
"""
import json

data = {
    "name": "Sanidhya Gupta",
    "place": "Indore",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
with open("datafile631.json", "w") as write:
    json.dump(data, write)

with open("datafile631.json", "r") as read_content:
    print(json.load(read_content)) """

"""json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. 
It is mainly used for deserializing native string, 
byte, or byte array which consists of JSON data into Python Dictionary."""
import json

# JSON string:
# Multi-line string
data = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"]
	}"""

# parse data:
res = json.loads(data)

# the result is a Python dictionary:
print(res)

