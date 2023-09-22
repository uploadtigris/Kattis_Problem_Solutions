import sys

input = sys.stdin.readline()
input = input.strip()
inputs = input.split(" ")

int_inputs = []

for i in inputs:
    int_inputs.append(int(i))


# first num is N; first die faces
# second num is M; second die num faces

die_1 = [0] * int_inputs[0]
die_2 = [0] * int_inputs[0]

i = 0
while i < int_inputs[0]:
    die_1[i] += i+1
    die_2[i] += i+1
    i+=1


if int_inputs[0] == int_inputs[1]:
    print(int_inputs[0]+1)
elif int_inputs[0] != int_inputs[1]:
    #find compare inputs as max or min
  min = min(int_inputs)
  max = max(int_inputs)

  #subtract min from max
  diff = max - min 

  #find the range of min to (min + (max - min)); all nums are most occuring
  j = min+1

  while j <= (min+1) + diff:
      print(j)
      j += 1





