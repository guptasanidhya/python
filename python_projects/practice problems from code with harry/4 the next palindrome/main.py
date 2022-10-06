"""A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to
 that number. Your first input should be the number of test cases and then take all the cases as input
 from the user."""
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
        else:
            print(f"{sum} is already a palindrome")
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
    for i in range(no_of_input):
        value=int(input("enter the value"))
        ls.append(value)

    for val in ls:
     checkp(val) #inserting values