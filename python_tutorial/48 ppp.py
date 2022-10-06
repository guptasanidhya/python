class employee:
    var=1
    _pro=2
    __pri=3

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

sandy=employee("SANIDHYA",100000,"boss")
print(sandy.var)
print(sandy._pro)
print(sandy._employee__pri)