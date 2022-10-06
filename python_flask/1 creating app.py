from flask import Flask
app = Flask(__name__)
#In this first we are importing a class named Flask from flask module then we are making a variable named
# ‘app’ which takes a string argument.
# It is nothing but file name,
#If instead of “__name__” i write file name in string format, it works perfectly fine. So,
# we can write it like
#app = Flask(“filename”)
@app.route("/")
#In third line, route is a decorator. We give it a string as
# argument and that string is our end point. In this case URL is “www.websitename.com/”.
def hello():
    return "hello World!"

@app.route("/sanidhya")
def sanidhya():
    return "Hii this is sanidhya"


# app.run()
#This is an argument which we can give in app.run(). We
# don't want to restart our app everytime we make changes so it is used to automatically restart the app.
app.run(debug=True)

# print(type(app))
# print(app)