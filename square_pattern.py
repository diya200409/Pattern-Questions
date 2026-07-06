def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
square(4)


'''Problem Statement

Given an integer N, return a square pattern of size N × N made up of the character '*'.

Input:

N = 4

Output:

****
****
****
****
'''