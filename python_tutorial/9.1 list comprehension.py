"""
Each variable x,y and z will have values of 0 or 1. All permutations of lists in the form
[i,j,k]=[[0,0,0][0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]].
sample input-1,1,1,1
Remove all arrays that sum to  to leave only the valid permutations.
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(list([i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n))