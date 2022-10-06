# minus=lambda x,y:x-y
# print(minus(3,4))
# def minus(a,b):
#     return a-b

# def a_first(a):
#      return a[1]
a=[[1,5],[24,2],[5,4]]
# a.sort(key=a_first)
a.sort(key=lambda a:a[1])
print(a)
