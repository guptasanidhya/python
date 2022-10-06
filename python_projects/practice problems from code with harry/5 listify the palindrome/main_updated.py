"""You are given a list that contains some numbers.
 You have to print a list of next palindromes only if the number is greater than 10; otherwise,
  you will print that number.



Input:
[1, 6, 87, 43]

Output:
[1, 6, 88, 44]"""
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
    # for i in range(no_of_input):
    #     if ls[i]>10:
    #         print(f"next palindrome for number {ls[i]} is {nextpalindrome(ls[i])} ")
    #     else:
    #         print(f"{ls[i]} is less than 10")

      #to add the palindrome in another list
    ls2=[]
    for i in range(no_of_input):
        if ls[i]<10:
            ls2.append(ls[i])
        else:
            ls2.append(nextpalindrome(ls[i]))
    print(ls)
    print(ls2)




