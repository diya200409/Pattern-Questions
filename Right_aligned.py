# Right-Aligned Triangle

for i in range(1, 6):
    # Print spaces
    for j in range(5 - i):
        print(" ", end="")

    # Print stars
    for k in range(i):
        print("*", end="")

    print()