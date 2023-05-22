l=(5,6,7,8,9)
s=set(l)

#print(type(s))
#set=(1,2,3,4,5)
#print(set)
#print(s)
"""s.add(1)
print(s)
s.add(5)
print(s)
s.remove(1)
print(s)"""
# s1=s.union({1,2,3})
# print(s,s1)
# s1=s.intersection({1,2,3,5})
# print(s1)
# s1={1,2,3,4,5}
# print(s.isdisjoint(s1))
# s1.remove(5)
# print(s.isdisjoint(s1))

#finding second largest
arr=[10,10,5]
arr.sort()
max=arr[-1]

for num in reversed(range(len(arr)-1)) :
	if(max!=arr[num]):
		print(arr[num])
		break;
	else:
		continue;
