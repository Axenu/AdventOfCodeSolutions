input_data = 3017957
# input_data = 5

import math
elfs = []

# for i in xrange(0, input_data):
#     elfs.append([1, i+1])
#
# i = 0
# allZero = True

# while len(elfs) > 1:
#     if elfs[i][0] == 1:
#         elfs[(i+1)%len(elfs)][1] = 0
#         allZero = False
#         print i
#     i+=1
#     if i > len(elfs):
#         i = 0
#         allZero = True
#         # print i
#
# print elfs

last= 0

elfs = []
zeroes = 0
once = True

elfs.append([1, input_data-1])
for i in xrange(1, input_data-1):
    elfs.append([i+1, i-1])

elfs.append([0, input_data-2])

# print elfs

i = 0
j = int(math.floor(input_data/2))
last = 0

double = True

while elfs[j][0] != j:
# for i in xrange(0, 5):
    # print j
    # print elfs
    # print double
    # last = j
    # prev = j-1
    # if prev < 0:
        # prev += input_data
    # print prev
    if double:
        d = j
        j = elfs[elfs[j][0]][0]
        # remove d
        # prev =
        elfs[elfs[d][1]][0] = elfs[d][0]
        # next
        elfs[elfs[d][0]][1] = elfs[d][1]

        double = False
    else:
        d = j
        j = elfs[j][0]
        # remove d
        # prev =
        elfs[elfs[d][1]][0] = elfs[d][0]
        # next
        elfs[elfs[d][0]][1] = elfs[d][1]

        double = True
    # i = elfs[i]
    last = j
    # print elfs
    # print j



# while i < len(elfs):
#     print elfs
#     if elfs[i][0] == 1:
#         # elfs[(i+1)%len(elfs)][0] = 0 # find next and flag
#         zeroes += 1
#         last = i
#     i+=1
#     if i >= len(elfs):
#         if once:
#             i = 0
#             once = False
#         if zeroes <= 1:
#             print last
#             i = 9999999999999
#         # print zeroes
#         # print elfs
#         print i
#         zeroes = 0

print last+1

# first = 0 + floor(5/2) (+1) # 3
# second = 1 + floor(4/2) (+1) # 4%4 = 0
# third =
