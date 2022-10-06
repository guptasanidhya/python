import pickle
"""
pickle.dump():Write the pickled representation of the object obj to the open 
file object file. This is equivalent to Pickler(file, protocol).dump(obj).

pickle.dumps():Return the pickled representation of the object obj as a bytes object, 
instead of writing it to a file.

pickle.load():Read the pickled representation of an object from the open file object file and 
return the reconstituted object hierarchy specified therein. This is equivalent to Unpickler(file).load().

pickle.loads():Return the reconstituted object hierarchy of the pickled representation data of an object. 
data must be a bytes-like object.
"""

# cars=["audi","BMW","maruti suzuki"]
# file="mycar.pkl"
# fileobj= open(file,"wb")
# mycar=pickle.dump(cars,fileobj)
# # mycar=pickle.dumps(cars)
# # print(mycar)
# fileobj.close()

fileobj=open("mycar.pkl",'rb')
mycar=pickle.load(fileobj)
print(mycar)
# mrcar=pickle.loads(mycar)
# print(mrcar)

