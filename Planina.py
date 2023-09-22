
import sys
import math

# create variables
num_points = 2

N = int(input())


#create a for loop
i = 0
while i <= N-1:
    y = (num_points * 2 - 1)**2
    y = int(y)
    num_points = math.sqrt(y)
    i+=1
    print(y)

