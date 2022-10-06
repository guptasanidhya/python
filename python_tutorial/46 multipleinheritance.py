class employee:
    var=9
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


class player:
    var=10
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def print_game(self):
        print(self.game)
    def print_detailss(self):
        print(f"name is {self.name}, game  is {self.game}")


# ankit=player("ankit",['volleyball','cricket'])
# print(ankit.game)
sanidhya=player("sanidhya",['basketball'])

class cool_programmer(employee,player):

    language="c++"
    def printlanguage(self):
        print(self.language)
sanidhya=cool_programmer("sanidhya",100000,"Boss")
sanidhya.printlanguage()



print(sanidhya.var)