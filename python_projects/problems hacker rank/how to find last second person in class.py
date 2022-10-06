"""There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    ls=[]
    marks=[]
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name,score])
    # print(ls)
    """
    second solution
    ls = sorted(ls, key=lambda x: x[1]);#lambdA function for comparing
    for x in range(1, len(ls)):
        if(ls[x][1] != ls[x-1][1]):#if numbers are not same at initial and next position then 
          score = ls[x][1]
          break
ls = sorted(ls);
for x in range(len(ls)):
    if(ls[x][1] == score):
        print (ls[x][0])
        """
    for i in range(len(ls)):
        marks.append(ls[i][1])
    # print(marks)
    z = min(marks)
    while min(marks) == z:
     marks.remove(min(marks))#removing the lowest marks so we can take second lowest on first

    # print(min(marks))
    for i in range(len(ls)):
        if ls[i][1]==min(marks):#comparing the marks in list of names
            names.append(ls[i][0])#appending the matched names in a list
    names.sort()#sorting the name list
    for name in names:
        print(name)#printing the name