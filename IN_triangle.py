def inc_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+ 1):
            print(j, end="")
        print()
inc_triangle(4)


'''Problem Statement

Given an integer N, print numbers from 1 to the row number in each row.

Input

N = 4

Output

1
12
123
1234
'''