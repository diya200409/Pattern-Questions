'''
Problem Statement

Given an integer N, print a triangle where the i-th row contains i stars.

Input

N = 4

Output

*
**
***
****

'''

def triangle(n):
    for i in range(1, n+1):
     print("*" * i)
    print()
triangle(4)