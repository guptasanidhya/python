ls=[]
while True:
    user=input("input name")
    a=int(input("enter the no. of items you want to add:"))
    for i in range(a):
        add=input()
        ls.append(add)

    type=int(input("type 1 for list comprehension,2 for dictionary comprehension,3 for set comprehension"))

    if type==1:
     lst=[item for item in ls ]
     print(lst)
    elif type==2:
        dict1={f" {item+1}.{user} ":i for item,i in enumerate(ls)}
        print(dict1)
    elif type==3:
        set1={i for i in ls}
        print(set1)