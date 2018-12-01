filename = "./input/01.txt"
input_file = open(filename, "r")
rows = []
for line in input_file:
    rows.append(line)


# rows = input_data.split('\n')

reached = {}

sum = 0
done = False

while not done:
    print sum
    for row in rows:
        sum += int(row)
        if sum in reached:
            print sum
            done = True
            break
        reached[sum] = True

print sum














#
