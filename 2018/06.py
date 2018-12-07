input_data = '''59, 110
127, 249
42, 290
90, 326
108, 60
98, 168
358, 207
114, 146
242, 170
281, 43
233, 295
213, 113
260, 334
287, 260
283, 227
328, 235
96, 259
232, 177
198, 216
52, 115
95, 258
173, 191
156, 167
179, 135
235, 235
164, 199
248, 180
165, 273
160, 297
102, 96
346, 249
176, 263
140, 101
324, 254
72, 211
126, 337
356, 272
342, 65
171, 295
93, 192
47, 200
329, 239
60, 282
246, 185
225, 324
114, 329
134, 167
212, 104
338, 332
293, 94'''

size = 1000

rows = input_data.split('\n')
locations = []
sizes = [0] * len(rows)

grid = [[-1] * size] * size
i = 0
for row in rows:
    x, y = row.split(', ')
    x = int(x) + 100
    y = int(y) + 100
    locations.append((x, y))
    grid[x][y] = i
    i += 1


for x in xrange(size):
    for y in xrange(size):
        closest = 0
        crange = 99999999
        i = 0
        equal = False
        for (xx, yy) in locations:
            if abs(x - xx) + abs(y - yy) < crange:
                closest = i
                crange = abs(x - xx) + abs(y - yy)
                equal = False
            elif abs(x - xx) + abs(y - yy) == crange:
                equal = True
            i += 1
        if not equal:
            grid[xx][yy] = closest
            sizes[closest] += 1

row = ''
for x in xrange(size):
    if grid[x][0] != -1:
        # if grid[x][0] in sizes:
        sizes[grid[x][0]] = -1
    if grid[x][size-1] != -1:
        # if grid[x][size-1] in sizes:
        sizes[grid[x][size-1]] = -1

for y in xrange(size):
    if grid[0][y] != -1:
        # if grid[0][y] in sizes:
        sizes[grid[0][y]] = -1
    if grid[size-1][y] != -1:
        # if grid[size-1][y] in sizes:
        sizes[grid[size-1][y]] = -1

print max([(i, sizes[i]) for i in xrange(len(sizes))], key=lambda i: i[1])

distances = {}

res = 0

for x in xrange(size):
    for y in xrange(size):
        dist = 0
        for (xx, yy) in locations:
            dist += abs(x - xx) + abs(y - yy)

        if dist < 10000:
            res += 1
print res
