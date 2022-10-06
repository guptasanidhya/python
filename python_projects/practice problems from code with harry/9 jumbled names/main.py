# import random
import random


def jumbled():
    pass


if __name__ == '__main__':
    name = ["Sanidhya Gupta ", "Mohini Mehrotra", "Nitin Dwivedi"]
    first = []
    last = []
    for item in name:
        x = item.split(" ")
        first.append(x[0])
        last.append(x[1])

    print(first)
    print(last)

    for i in range(len(first)):
        f = random.randint(0, len(first) - 1)
        l = random.randint(0, len(last) - 1)

        print(f"{first[f]} {last[l]}")
        first.pop(f)
        last.pop(l)
