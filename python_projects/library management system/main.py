#library management system
#create using class
#lend book-who owns the book if book is not present
#add book
#return book
#S_library = library(listofbooks,library_name)
#dictionary -books-name of person
class library:
    def __init__(self,listofbooks,lname,ls,lsuser):
        self.listofbooks=listofbooks
        self.lname=lname
        self.ls=ls
        self.lsuser=lsuser
    def add(self,bname):
        self.listofbooks.append(bname)
        print("book is added")
    def lend(self):
        lend = input("enter the book name")
        for i in ls:
            if lend==i:
                index=ls.index(i)

                print(f"book has been taken by {self.lsuser[index]}")
                break
        else:
             user = input("name of user who lend the book")
             lsuser.append(user)
             ls.append(lend)
             print("Book Lend")

    def returnbook(self):
        return_book=input("which book do you want to return")
        for i in ls:
            if i==return_book:
                index=ls.index(i)
                lsuser.pop(index)
                ls.pop(index)
                print("book is returned")

    def takenbookdetails(self):
        a=len(ls)
        for i in range(0,a):
            print(f"{i+1}.{ls[i]}:{lsuser[i]}")




if __name__ == '__main__':
    listofbooks=["ramayan","mahabharat","geeta"]
    ls=[]
    lsuser=[]
    print("Welcome to Library")
    lname=input("To enter your library enter your name")
    sanidhya = library(listofbooks, lname,ls,lsuser)
    while True:
        print("What you want to do !\npress 1 to show book in your library\n"
              "press 2 to add book in your library\n"
              "press 3 to lend book\n"
              "press 4 for returning book\n"
              "press 5 for book details which lend by someone")
        value=int(input())
        if value==1:
            print(listofbooks)
            print(ls)
            print(lsuser)
        elif value==2:
            add_book=input("enter the book name:")
            sanidhya.add(add_book)
        elif value==3:
         sanidhya.lend()
         sanidhya.takenbookdetails()
        elif value==4:
            sanidhya.returnbook()
        elif value==5:
            sanidhya.takenbookdetails()





