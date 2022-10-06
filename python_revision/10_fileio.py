#1.WRite a program to find word in a poem using IO
# def find(word,c):
#         if word in c:
#             print("yes")
#         else:
#             print("no")
#
# with open("high_score" )as f:
#         c=f.read()
# find("20",c)

#2.previous high score

"""def game(score):
    with open("high_score", "a") as f:
        f.write(f"game:{count}\nHigh-score was {score}\n")
        print("Score updated")
        return score
count=0
while(True):
    count=count+1
    print("game:",count)
    score=int(input("Enter the score"))
    last=game(score)
    print("high score was",last)"""
#3.table of 2 to 5

"""def table(count):
    for i in range(1,11):
        with open(f"table of {count}.txt","a") as f:
            f.write(f"{count} X {i} = {count*i}\n")

table(1)
table(2)"""
#4.replace donkey with ### in a file
"""word="donkey"
with open("sample.txt","r+") as f:
    data=f.read()
data= data.replace("donkey", "####")
with open("sample.txt","w") as f:
    f.write(data)
"""
#5.replacing list words
"""def censored(word):
    with open("sample.txt", "r+") as f:
        data = f.read()
    data = data.replace(word, "####")
    with open("sample.txt", "w") as f:
        f.write(data)
ls=["Sanidhya","gupta"]
for i in range(0,len(ls)):
    censored(ls[i])"""


#use string.lower to lower all the cases
#6. finding python in line
# data=True
# i=1
# with open("sample.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if "python" in data.lower():
#             print(data)
#             print("present in line ",i)
#         i += 1
#7,rename the file
"""import os

oldfile="sample4.txt"
newfile="sample2.txt"

with open(oldfile) as f:
    data=f.read()
with open(newfile,"w") as f:
    f.write(data)

os.remove(oldfile)

"""