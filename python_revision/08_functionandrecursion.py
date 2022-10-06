#1finding the greatest
"""def greatest(a,b,c):
    if(a>b and a>c):
        print(a," is greatest")
    elif (b>c and b>c):
        print(b, "is greatest")
    else:
        print(c, "is greatest")

if __name__ == '__main__':
    greatest(10,9,8)"""

#2 converting celcius to farenheit

"""def ctof(num):
    return (num * 1.8) + 32
def ftoc(num):
    return (num - 32) * 5/9

a=ctof(30)
print("30 degree celcius to farhanheit",a)
b=ftoc(86)
print("86 degree farhanheit to celcius",b)"""

#3.sum of first n natural number

"""def sum(n):
    if n<=0:
        print("not a natural number count")
    elif n==1:
        return 1
    else:
        return n+sum(n-1)

count=sum(1)
print(count)"""
#4.stars pattern
# ***
# **
# *
n=3
# def star(n):
#     if n==0:
#         return 0
#     print("* "*n)
#     return star(n-1)

# star(3)
# for i in range(n+1):
#     print("* "*(n-i))

#4.remove a word and strip the spaces

def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()


this = "        i am sanidhya gupta"
a=remove_and_strip(this,"sanidhya")
print(this)
print(this.strip())
print(a)
