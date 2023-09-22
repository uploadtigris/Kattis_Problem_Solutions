import sys

first_line = sys.stdin.readline()
input = first_line.strip()
num_lines_to_read = int(input)

i = 0

while i < num_lines_to_read:
    x = 0

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split(" ")

    num_outlets = int(line[0])
    num_plugs = line[1:]

    new_plugs = []

    for elem in num_plugs:
        new_plugs.append(int(elem))

    x += int(num_plugs[-1])
        
    rest_plugs = (num_plugs[:-1])
    for num in rest_plugs:
        x += (int(num) - 1)
    
    i+=1
    print(x)


