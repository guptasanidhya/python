class employee:

    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role


    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    def print_details(self):
        print(f"name of employee is {self.name}, salary is {self.salary}, role is {self.role} ")

    @classmethod
    def from_slash(cls,string):
        return cls(*string.split("/"))

    @staticmethod
    def astatic(string):
        print("this is good "+string)


sanidhya=employee("sanidhya",1000000,"Boss")
mohini=employee.from_slash("mohini/1000000/CEO")
print(mohini.salary)
mohini.print_details()

class programmer(employee):
    def __init__(self,name,salary,role,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages=languages


    def print_prog(self):
        print(f"name of employee is {self.name}, salary is {self.salary}, role is {self.role}, languages:{self.languages} ")

nitin=programmer("nitin",1000000,"sendev",['c++','python'])
nitin.print_prog()
