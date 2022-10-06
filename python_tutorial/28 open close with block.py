"""to open file in open close both no need to write close at the end"""
with open("daily_data.txt") as f:
    a = f.read(38)
    print(a)
# f=open("daily_data.txt","rt")
# A=f.readline()
# print(A)33
# f.close()
