def hollow_rec(m,n):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if (i==1 or i==n or j==1 or j==m):
                print("* ",end="")
            else:
                print("  ",end="")
        print()

if __name__ == '__main__':

    hollow_rec(3,4)