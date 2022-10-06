class employee:
    # def printdetails(self):
    #     print(f"name is {self.name}. Salary is {self.salary}.Base is {self.base}")
    def __init__(self,aname,asalary,abase):
        self.name=aname
        self.salary=asalary
        self.base=abase

# sanidhya=employee()
# mohini=employee()

# sanidhya.name="Sanidhya"
# sanidhya.salary=100000
# sanidhya.base="student"
# sanidhya.printdetails()
sanidhya=employee("Sanidhya",100000,"student")
print(sanidhya.salary)
print(sanidhya.__dict__)