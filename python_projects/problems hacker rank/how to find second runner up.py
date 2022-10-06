
lis =[1,2,3,4,5]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(max(lis))

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # print(arr)
#     arr.sort()
#     arr.reverse()
#     for i in range(len(arr)):
#         if arr[0]>arr[i+1]:
#             print(arr[i+1])
#             break