class library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendict = {}

    def display(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def addbook(self, book):
        self.booklist.append(book)
        print("Book is added")

    def lendbook(self, book):
        if book not in self.lendict.keys():
            user = input("Enter the name of the user")
            self.lendict.update({book: user})
            print("Lender book database updated. You can take the book now")
        else:
            print(f"book has been taken by {self.lendict[book]}")

    def returnbook(self, book):
        self.lendict.pop(book)
        print("book is returned")

    def listlendbook_users(self):
        print(self.lendict)


if __name__ == '__main__':
    booklist = ["python", "c++", "java"]
    sanidhya = library(booklist, "sanidhya")
    while True:
        print(f"Welcome to Library {sanidhya.name}")
        print("1.Display Book")
        print("2.Add Book")
        print("3.Lend Book")
        print("4.Return Book")
        print("5.Display Lend Books with users")
        option = int(input("Choose option"))
        print(option)
        optionlist = [1, 2, 3, 4, 5]
        if option not in optionlist:
            print("Enter proper option number")
        elif option == 1:
            sanidhya.display()
        elif option == 2:
            book = input("Enter the name of book to be added")
            sanidhya.addbook(book)
        elif option == 3:
            book = input("Enter the name of book to be lend")
            sanidhya.lendbook(book)
        elif option == 4:
            book = input("Enter the name of book to be returned")
            sanidhya.returnbook(book)
        elif option == 5:
            sanidhya.listlendbook_users()

        print("press q to quit and c to continue")
        option1 = ""
        while (option1 != "c" and option1 != "q"):
            option1 = input()
            if option1 == "q":
                exit()
            elif option1 == "c":
                continue
