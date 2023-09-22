import sys

#output number
x = 0

#read first line
a = sys.stdin.readline()
a = int(a.strip())

#read new line and assign it to a variable
elems = []
i = 0

while i < a:
  y = sys.stdin.readline()
  y = y.strip() #keep a string for parsing

  # parse the number from the exponent
  object = [[y[:-1],y[-1]]] 
  elems += object
  i+=1

#convert to integers
new_elems = [list(map(int, i)) for i in elems]

# assign x the values of the sum of the nums raised to their exp's
for item in new_elems:
  x += item[0]**item[1]

# output x
print(x)

