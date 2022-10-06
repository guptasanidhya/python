import re

# import operator

list = ["this is good", "this is python", "this is not python snake python", "python in python in python", "python"]
result = []
result_count = []
dict = {}
search = input("Enter the text")
patt = re.compile(search)
# print(patt)
for item in list:
 matches = patt.finditer(item)
 for match in matches:

        if item not in result:
            result.append(item)
            a = item.count(search)
            result_count.append(a)
            dict[item] = a

# print(result)
# print(result_count)
# print(dict)
# sorted_dictionary = sorted(dict.items(), key=lambda x: -x[1])
# print(sorted_dictionary)
# for items in sorted_dictionary:
#     print(items)
sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)

if len(sort_orders)!=0:
    print(f"{len(sort_orders)} results found")
    for i in sort_orders:
        print(i[0])

else:
    print("nothing found")
