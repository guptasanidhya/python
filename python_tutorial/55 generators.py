"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""


def getnum(x):
    for i in range(x):
        yield i


seq = getnum(10)
print(type(getnum))
print(type(seq))
print(seq.__next__())
print(seq.__next__())
# print(seq.__next__())

lst = list(seq)
print(type(lst))
print(lst)
"""there is nothing left behind in the list thats why list is empty"""
for i in seq:
    print(seq)
    """it also doesnt print anything because nothing left in the iterable zone"""
