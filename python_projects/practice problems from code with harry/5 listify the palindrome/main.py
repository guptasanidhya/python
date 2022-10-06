"""You are given a list that contains some numbers. You have to print a list of next palindromes only if the number is greater than 10; otherwise, you will print that number.



Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]"""
def checkp(value):
    #palindrome function from line 2 to 8
    sum = 0
    r=value #the value user enter
    while r>0:
     a=r%10
     sum = sum*10+(a)
     r=int(r/10)

    if sum==value:
        if val!=sum:
            print(f"next palindrome for {val} is {sum}")
            ls2.append(sum)# to add value in list 2 to show to desired result

        else:
            # print(f"{sum} is already a palindrome")
            while True:
                value = value + 1
                checkp(value)  # recursion check
                break
    else:
        while True:
            value=value+1
            checkp(value) #recursion check
            break
            """if number is not palindrome or it will increase the value of palindrome by 1 and will 
            recheck in function when the value satisfy the if will work and program will go to exit"""

if __name__ == '__main__':
    no_of_input=int(input("Enter the number of input"))
    ls=[]
    ls2 = []
    for i in range(no_of_input):
        value=int(input("enter the value"))
        ls.append(value)

    # for val in ls:
    #     if val>10:
    #         checkp(val) #inserting values

    for i in range(no_of_input):
        if ls[i]<10:
            ls2.append(ls[i])
        else:
            val=ls[i]
            checkp(val)

    print(ls2)