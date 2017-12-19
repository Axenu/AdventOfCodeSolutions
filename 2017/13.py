import copy, itertools

input_data = '''0: 4
1: 2
2: 3
4: 5
6: 8
8: 4
10: 6
12: 6
14: 6
16: 10
18: 6
20: 12
22: 8
24: 9
26: 8
28: 8
30: 8
32: 12
34: 12
36: 12
38: 8
40: 10
42: 14
44: 12
46: 14
48: 12
50: 12
52: 12
54: 14
56: 14
58: 14
60: 12
62: 14
64: 14
68: 12
70: 14
74: 14
76: 14
78: 14
80: 17
82: 28
84: 18
86: 14'''
# input_data = '''0: 3
# 1: 2
# 4: 4
# 6: 4'''

rows = input_data.split('\n')

arr = [(0,0,1)] * 87
pos = -1

for row in rows:
    val = map(int, row.split(': '))
    arr[val[0]] = (val[1], 0, 1)


start = copy.deepcopy(arr)

def test(arr):
    fail = 0
    pos = -1

    for i in xrange(0, 86):
        pos += 1
        # if pos == 6:
            # print pos
            # print arr[pos]
            # print arr[0:10]
        if arr[pos][0] != 0 and arr[pos][1] == 0:
            # print pos
            # print arr[pos]
            fail += pos*arr[pos][0]
            fail += 1
        # forward
        ind = 0
        for ind in xrange(0,86):
            v = arr[ind]
            if v[0] != 0:
                if v[2] == 1:
                    if v[1] == v[0]-1:
                        arr[ind] = (v[0], (v[1]-v[2]), -1)
                    else:
                        arr[ind] = (v[0], (v[1]+v[2]), 1)
                else:
                    if v[1] == 0:
                        arr[ind] = (v[0], (v[1]-v[2]), 1)
                    else:
                        arr[ind] = (v[0], (v[1]+v[2]), -1)
                ind += 1
        # print arr[0:4]

    return fail

print test(arr)

lines = [line.split(': ') for line in rows]

heights = {int(pos): int(height) for pos, height in lines}

def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)
print part1

part2 = next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))
print part2

l = {pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0}
print l

# steps = 1
#
# arr = copy.deepcopy(start)
# res = test(arr)
#
# while res != 0:
#     arr = copy.deepcopy(start)
#     #step arr
#     for ind in xrange(0,86):
#         v = arr[ind]
#         if v[0] != 0:
#             if v[2] == 1:
#                 if v[1] == v[0]-1:
#                     arr[ind] = (v[0], (v[1]-v[2]), -1)
#                 else:
#                     arr[ind] = (v[0], (v[1]+v[2]), 1)
#             else:
#                 if v[1] == 0:
#                     arr[ind] = (v[0], (v[1]-v[2]), 1)
#                 else:
#                     arr[ind] = (v[0], (v[1]+v[2]), -1)
#             ind += 1
#     steps += 1
#     start = copy.deepcopy(arr)
#     # print arr
#     res = test(arr)
#     # print res
#     if (steps % 1000) == 0:
#         print steps
#     # print start
#     # break
# print steps-1
