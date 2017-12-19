input_data = 335
# input_data = 3

arr = [0]
pos = 0

for i in xrange(1, 2018): # 2018
    pos += input_data
    pos %= len(arr)
    arr.insert(pos+1, i)
    pos += 1
    # print arr

print arr[pos+1]


# part 2

after = 0
pos = 0
length = 1
for i in xrange(1, 50000000):
    pos += input_data
    pos %= length
    length += 1
    if pos == 0:
        after = i
    pos += 1

print after
