def RN_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print()
RN_triangle(4)
'''
Pattern 5: Row Number Triangle
Problem Statement

Given an integer N, print the row number repeated i times in the i-th row.

Input

N = 4

Output

1
22
333
4444
'''