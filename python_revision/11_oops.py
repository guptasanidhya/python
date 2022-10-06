#1oops program for entry of employee at microsoft
"""class employee:
    company="microsoft"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def print_Details(self):
        print(f"employee name:{self.name},salary:{self.salary},company:{self.company}")
sanidhya=employee("Sanidhya",100000)
mohini=employee("Mohini",100000)
sanidhya.print_Details()
mohini.print_Details()"""

#2creating class calculator ,square,cube,sqrt
"""import math


class calculator:
    def __init__(self,value):
        self.value=value
    def square(self):
        return self.value**2
    def cube(self):
        return self.value**3
    def sqrt(self):
        return math.sqrt(self.value)
    @staticmethod
    def greet():
        print("Hello People ans is")
asquare=calculator(4)
asquare.greet()
a=asquare.square()
acube=calculator(4)
b=acube.cube()
acube.greet()
asqrt=calculator(4)
c=asqrt.sqrt()
asqrt.greet()
print(a,b,c)"""
#3.creating a railway booking system
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def bookticket(self):
        print(f"seats available in {self.name} is {self.seats}")
        booking=input("do you want to book seat\n type yes or no")
        if(booking=="yes"):
            if(self.seats>0):
                no_of_seats=int(input("how many seats do you want to book?\n"
                                      "You can book max 6 seats in one go"))
                if(no_of_seats<=6 and no_of_seats>=0):
                    self.seats=self.seats-no_of_seats
                    print(f"total booked seats {no_of_seats} and now available seats are {self.seats}")
                else:
                    print("type value between 0 to 6")
            else:
                print("seats not available")


nametrain=input("enter train name")
nametrain=Train(nametrain,500,5)
nametrain.bookticket()