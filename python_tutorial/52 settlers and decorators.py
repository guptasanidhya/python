class employee:

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}.{self.lname}@email.com"
    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return f"no email available "
        else:
            return f"{self.fname}.{self.lname}@email.com"

    @email.setter
    def email(self,string):
        print("setting now")
        names=string.split("@")[0]
        self.fname=string.split(".")[0]
        self.lname=string.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


sanidhya_Gupta=employee("Sanidhya","Gupta")
print(sanidhya_Gupta.email)
sanidhya_Gupta.fname="Shanu"
print(sanidhya_Gupta.email)
sanidhya_Gupta.email="A.B@email.com"
print(sanidhya_Gupta.email)
sanidhya_Gupta.fname="hello"
print(sanidhya_Gupta.email)
del sanidhya_Gupta.email
print(sanidhya_Gupta.email)
sanidhya_Gupta.email="sanidhya.gupta@email.com"