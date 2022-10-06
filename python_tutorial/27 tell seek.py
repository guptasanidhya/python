f=open("daily_data.txt")
print(f.readline())
"""read one line with extra \n"""
print(f.tell())
"""tell where the pointer is"""
print(f.readline())
print(f.readline())
print(f.seek(20))
"""put the pointer to desired position"""
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
