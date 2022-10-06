"""A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

676, 616, mom, 100001.

You have to take a number as an input from the user. You have to find the next palindrome corresponding to
 that number. Your first input should be the number of test cases and then take all the cases as input
 from the user."""
def nextpalindrome(n):
    n=n+1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__ == '__main__':
    no_of_input=int(input("Enter the number of input"))
    ls=[]
    for i in range(no_of_input):
        number=int(input("enter the number"))
        ls.append(number)
    for i in range(no_of_input):
        print(f"next palindrome for number {ls[i]} is {nextpalindrome(ls[i])} ")
