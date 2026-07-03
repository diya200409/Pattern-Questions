''' You are given an integer n. 
Your task is to return a square pattern of size n x n made up of the character '*',
 represented as a list of strings'''

def square(n):
    pattern = []
    for i in range(n):
        row=""
        for j in range(n):
            row = row + "*"
        pattern.append(row)
    return pattern
print(square(3))
