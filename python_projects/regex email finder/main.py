import re
mystr='''
hii i am sanidhya gupta
guptasanidhya6@gmail.com
sanidhya.gupta@gmail.com
sanidhya.gupta@hihi.tfd'''
# patt=re.compile(r"[\w.]+\@[\w]+(\.)com")
patt=re.compile(r"[\w.%+-]+\@[\w.-]+[\w]")
matches=patt.finditer(mystr)
for match in matches:
    print(match)