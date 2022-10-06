# def factorial(n):
#     """iterative method for factorial"""
#     fac=1
#     for i in range(1,n):
#         fac=fac*(i+1)
#     print(fac)
# factorial(5)
# print(factozrial.__doc__)

# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n* factorial_recursive(n-1)
#
# print(factorial_recursive(5))

"""fibonachi
 0 1 1 2 3 5 8 13
"""
def fibonachi(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)
print(fibonachi(5))