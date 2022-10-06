#1.making a dictionary with hindi words
"""dt={"hello":"namaste","help":"madad","tap":"dhakkan"}
search=input("enter the word")
if search in dt.keys():
        print(dt[search])
"""
#2.print the unique numbers
"""a=set()
a.add(20)
a.add(20.0)
a.add("20")
print(len(a))
print(a)
"""
#3.ADDDING SOMETHING TO DICTIONARY
"""dt={}
for i in range(0,2):
    name=input("enter the name")
    lang=input("enter the language")
    dt[name]=lang
print(dt)
"""
#4.can you change set values
s={1,"harry"}
ls=[1,2,3]
s.update(ls)
print(s)