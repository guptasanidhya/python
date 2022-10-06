ls=[]
for _ in range(0,4):
    a=int(input("ENTER THE NUMBER"))
    ls.append(a)
ls.sort()
b=len(ls)
print(ls[b-1])