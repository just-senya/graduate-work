filename = input()
array = []

with open(filename, "r") as file:
    for x in file:
        array.append([int(number) for number in x.split()])


open(filename, 'w')
res = sorted(array, key = lambda x: x[2])
for x in res:
    print(x[0], x[1], x[2], x[3], sep=' ', file=open(filename, "a"))