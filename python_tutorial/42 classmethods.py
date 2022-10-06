class employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,aposition):
        self.name=aname
        self.salary=asalary
        self.position=aposition

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

sanidhya=employee("Sanidhya",100000,"boss")
print(sanidhya.name)
mohini=employee("mohini",100000,"Boss")
print(mohini.position)
print(sanidhya.no_of_leaves)
mohini.change_leaves(40)
print(mohini.no_of_leaves)



