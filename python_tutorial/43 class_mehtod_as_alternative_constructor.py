class employee:
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position

    @classmethod
    def from_dash(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))


karan=employee.from_dash("karan-480-manager")
print(karan.salary)