#Filip.py
#Kattis Problem

# Tigris Mendez

import sys

#Read input
input = sys.stdin.readline()
input = input.strip()
print(input)

#Parse each number into two list (A and B)
numsA = input[0:3]
numsB = input[4:]

#Compare the last object in each to each other.
numsA_rev = []
numsB_rev = []

if numsA[2] > numsB[2]:
    numsA_rev = numsA[::-1] #Reverse order of newly created object and output.
    print(numsA_rev)
elif numsA[2] < numsB[2]:
    numsB_rev = numsB[::-1] #Reverse order of newly created object and output.
    print(numsB_rev)
elif numsA[2] == numsB[2]:
    if numsA[1] > numsB[1]:
        numsA_rev = numsA[::-1]
        print(numsA_rev)
    elif numsA[1] < numsB[1]:
        numsB_rev = numsB[::-1]
        print(numsB_rev)
    elif numsA[1] == numsB[1]:
        if numsA[0] > numsB[0]:
            numsA_rev = numsA[::-1]
            print(numsA_rev)
        elif numsA[0] < numsB[0]:
            numsB_rev = numsB[::-1]
            print(numsB_rev)

else:
    print('bruh enter a number')

