class dad():
    basketball=1

class son(dad):
    football=1
    def lover(self):
        return f"hello this is football lover {self.football}"

class grandson(son):
    cricket=1
    def lover(self):
        return f"cricket lover in the house {self.cricket}"

a=dad()
b=son()
c=grandson()

print(c.lover())
print(c.basketball)
