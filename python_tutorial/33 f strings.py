from sympy.physics.units import seconds

me="Sanidhya Gupta"
# print("%s"%me)
i="Shanu Gupta"
# print("%s"%me,"%s"%i)
# print("This is %s %s"%(me,i))
# a="THis is {} {} "
# b=a.format(me , i)
# print(b)
#fstring
import math
a=f"this is {me} {i} {math.cos(0)}"
print(a)
import time
"""difference of time from 1 Jan 1970 00:00:00 (UTC)"""
# print(time.time())
# print(time.localtime())
# print(time.localtime().tm_year)
# print(time.localtime().tm_mon)
# print(time.localtime().tm_mday)
# print(time.gmtime(1618062972.6))
# print(time.mktime(time.localtime()))
# for i in range(5):
#     time.sleep(5)
#     # print(time.localtime())
#     # print(time.time())
#     print(time.ctime())
# print(time.ctime(1200000000))
print(time.strftime("%d %m %Y"))
print(time.strftime("%x"))
print(time.strftime("%X"))
print(time.tzname)
print(time.timezone)
print(time.timezone/3600)