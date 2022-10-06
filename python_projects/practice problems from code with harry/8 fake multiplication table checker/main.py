import random
def multable():
    j = random.randint(5,9)#generating a randim index for random index fraud
    for i in range(1,11):
        if i==j:#fraud point if random index become equal to loop index
            table.append(a)

        else:
            table.append(6*i)


def iscorrect(table):
    for i in range(1,11):
        correct.append(6*i)
    for i in range(0,10):
        if table[i] != correct[i]:#comparing both table values data
            print(f"there is a problem at index {i+1} and corrected form is {correct[i]} ")

    pass


if __name__ == '__main__':
    table=[]
    correct=[]
    a=random.randint(6,60)
    multable()#rohan table call
    print(table)
    iscorrect(table)#correction table call
    print(correct)