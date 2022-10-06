list=[1,2,3,4]
reverse1=list[:]#making copy
reverse1.reverse()
print(f"The reverse of list {list} is {reverse1}")
reverse2=list[::-1]#slicing
print(f"The reverse of list {list} is {reverse2}")
reverse3=list[:]
for i in range(len(reverse3)//2):#swapping
    reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
print(f"the reverse of list {list} is {reverse3}")

if reverse1==reverse2 and reverse3==reverse2:
    print("all list are equal")


