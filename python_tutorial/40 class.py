class student:
    no_of_lives=10
sanidhya=student()
mohini=student()
sanidhya.name="sanidhya"
sanidhya.std=12
mohini.std=9
print(sanidhya,mohini)
print(sanidhya.std,mohini.std)

sanidhya.no_of_lives=11
print(sanidhya.no_of_lives)
print(sanidhya.__dict__)
print(student.__dict__)