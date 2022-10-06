from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    sides=4

    def __init__(self):
        self.length=5
        self.breadth=4

    def printarea(self):
        return self.length*self.breadth

class square(shape):
    sides=4

    def __init__(self):
        self.length=4
        self.breadth=4

    def printarea(self):
       return self.length*self.breadth
rect=rectangle()
sq=square()
# print(rect.printarea())
print(sq.printarea())