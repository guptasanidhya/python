# ls=[]
# for i in range (100):
#     if i%3==0:
#         ls.append(i)
#
# print(ls)
"""list comprehension"""
"""ls=[i for i in range(100) if i%2==0]
print(ls)"""

#dict comprehension
"""dict1={i:f"item{i}" for i in range(5)}
print(dict1)
dict2={value:key for key,value in dict1.items()}
print(dict2)"""

#sets comprehension
"""dresses={dress for dress in ["dress1","dress2","dress1","dress2"]}
print(type(dresses))
print(dresses)"""

#generator comprehension
"""evens=(i for i in range(100) if i%2==0)
print(evens.__next__())
for item in evens:
    print(item)"""
ls=[]
a=int(input("enter the no. of items you want to add:"))
for i in range(a):
    add=input()
    ls.append(add)


type=int(input("type 1 for list comprehension,2 for dictionary comprehension,3 for set comprehension"))
if type==1:
    lst=[item for item in ls ]
    print(lst)
elif type==2:
    dict1={f"item {item+1} ":i for item,i in enumerate(ls)}
    print(dict1)
elif type==3:
    set1={i for i in ls}
    print(set1)