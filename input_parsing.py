import sys
with open(sys.argv[1], "r") as file:
    n= int (file.readline().strip())
    L= int (file.readline().strip())
    length_sticks = list(map(int, file.readline().strip().split()))
    weights_sticks= list(map(int, file.readline().strip().split()))
