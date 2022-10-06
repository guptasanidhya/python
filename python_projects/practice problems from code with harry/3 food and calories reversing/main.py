def rev():
    ls = [5, 4, 1]

    ls.reverse()
    print(ls)

def slice():
    ls = [5, 4, 1]
    print(ls[::-1])

def swap():
        ls = [5,4,1]
        n=len(ls)
        # print(n)
        flag=int(n/2)
        # print(flag)
        for i in range(0,flag):
            temp = ls[i]
            ls[i] = ls[n - 1]
            ls[n - 1] = temp
            # print(ls)
            n=n-1
        print(ls)

if __name__ == '__main__':
    rev()
    slice()
    swap()