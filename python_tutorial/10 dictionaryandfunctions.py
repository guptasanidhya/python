d1={"Sanidhya":"pasta","nitin":"MCD hai","mohini":{"drink":"chai"}}
# d2={}
# print(type(d2))
# print(d1)
print(d1.items())
print(d1.keys())
d1["mehak"]="starbucks"
print(d1)
del d1["mehak"]
print(d1["Sanidhya"])
print(d1["mohini"]["drink"])
d1.update({"nitin":"Namkeen"})
print(d1["nitin"])
d3=d1.copy()
# del d3["mehak"]
print(d3)
print(d1)
d3["sandeep"]="samosa"
print(d3)
print(d1)
print(d1.values());