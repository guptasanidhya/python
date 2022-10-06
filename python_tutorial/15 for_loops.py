list1=[["Sanidhya",1],["chiku",2],["mohini",3],["nitin",4]]

for item,number in list1:
    print(item,number)
dict1=dict(list1)
print(dict1)
for item,number in dict1.items():
    print(item ,"favorite number is", number)
# for item,number in dict1:
#     print(item ,"favorite number is", number)
list2=[4,"name","sanidhya","gupta",6,7,8,9,10]

for item in list2:
    if str(item).isnumeric() and item > 6:
        print(item)
        print(type(item))

for i in range(1,11,2):
    print(i)
# raspberry_jam, double_chocolate, cream_cheese, blueberry, chocolate = [2.00, 2.50, 2.30, 2.10, 2.20]
# print(blueberry)