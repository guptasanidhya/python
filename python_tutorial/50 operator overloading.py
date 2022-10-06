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
        print(  f"name of employee is {self.name}, salary is {self.salary}, role is {self.role} ")

    def __add__(self, other):
        # return self.salary+other.salary
        return self.role + other.role
    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"employee['{self.name}',{self.salary},'{self.role}']"

    def __str__(self):
        return f"name of employee is {self.name}, salary is {self.salary}, role is {self.role} "
emp1=employee("sanidhya",100000,"consultant")
emp2=employee("mohini",100000,"programmer")
print(emp1+emp2)
print(emp1/emp2)
print(emp1)