'''
Problem Statement

Given an integer N, return a square pattern of size N × N where every element is 1.

Input:

N = 4

Output:

1111
1111
1111
1111
'''

def sqr_num(n):
    for i in range(n):
        for j in range(n):
            print("1", end="")
        print()
sqr_num(4)
