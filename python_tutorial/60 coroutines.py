import time
"""coroutines are used to search data when you need  """
"""They only run in response to the next() and send() methods. 
Coroutine requires the use of the next statement first so it may start its execution. 
Without a next() it will not start executing. 
We can search a coroutine by sending it the keywords as input using object name along with send(). 
The keywords to be searched are send inside the parenthesis. 
 close() — to close the coroutine"""
def searcher():
    data="This is sanidhya gupta.Nice to meet you"
    time.sleep(4)
    while True:
        text=(yield)
        if text in data:
            print("value is available")
        else:
            print("value is not available")


search=searcher()
next(search)
search.send("this".capitalize())
search.close()

