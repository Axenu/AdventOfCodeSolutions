input_data = '''....##.#.#.#...#.##.##.#.
##.####..###..#.#.#.###.#
.#.#...#.##....#......###
...#.....##.###....##.###
#.########.#.#####..##.#.
.#..#..#.#..#....##.#...#
.....#.##..#.#.....##..##
....###....###....###.#..
..#..#..#..#.##.#.#..##.#
.##......#...##.#.#.##.#.
.#####.#.#.##...###...#..
#..###..#....#....##..#..
###..#....#.##.##.....#..
##.##..#.##.#..#####.#.#.
#....#.######.#.#.#.##.#.
###.##.#.######.#..###.#.
#...###.#.#..##..####....
###...##.###..###..##..#.
..##.###...#.....##.##.##
..##..#.###.###.....#.###
#..###.##.#.###......####
#.#...#..##.###.....##.#.
#..#.##...##.##....#...#.
..#.#..#..#...##.#..###..
......###....#.....#....#'''

# input_data = '''..#
# #..
# ...'''

infected = {}


start = [0,0]
direction = [0,1]

rows = input_data.split('\n')
size = (len(rows)-1)/2

def turnLeft(direction):
    if direction[0] == 0:
        if direction[1] == 1:
            return [-1, 0]
        else:
            return [1, 0]
    elif direction[0] == 1:
        return [0, 1]
    else:
        return [0, -1]

def turnRight(direction):
    if direction[0] == 0:
        if direction[1] == 1:
            return [1, 0]
        else:
            return [-1, 0]
    elif direction[0] == 1:
        return [0, -1]
    else:
        return [0, 1]

def reverse(direction):
    if direction[0] == 1:
        return [-1, 0]
    elif direction[0] == -1:
        return [1,0]
    elif direction[1] == 1:
        return [0, -1]
    else:
        return [0, 1]

print size
count_infected = 0
for x in xrange(0, len(rows)):
    for y in xrange(0, len(rows)):
        # print rows[y][x]
        if rows[y][x] == '#':
            # print y, x
            # print size
            # print len(rows)
            # print 2 - y - size
            xx = x-size
            yy = len(rows) - 1 - y - size
            if xx not in infected:
                infected[xx] = {}

            infected[xx][yy] = '#'
            # infected[str(x-size) + ',' + str(] = '#'

print infected
max_x = 0
max_y = 0
min_x = 0
min_y = 0

for i in xrange(0, 10000000):
    name = (str(start[0]) + ',' + str(start[1]))
    # print name
    if name in infected:
        if infected[name] == '#':
            # do infected
            direction = turnRight(direction)
            infected[name] = 'F'
            start[0] += direction[0]
            start[1] += direction[1]
        elif infected[name] == 'F':
            # do infected
            direction = reverse(direction)
            del infected[name]
            start[0] += direction[0]
            start[1] += direction[1]
        elif infected[name] == 'W':
            # do infected
            # direction = turnRight(direction)
            infected[name] = '#'
            count_infected += 1
            start[0] += direction[0]
            start[1] += direction[1]
    else:
        # do free
        direction = turnLeft(direction)
        infected[name] = 'W'
        start[0] += direction[0]
        start[1] += direction[1]

    if start[0] > max_x:
        max_x = start[0]
        # print max_x
    if start[1] > max_y:
        max_y = start[1]
    if start[0] < min_x:
        min_x = start[0]
        # print max_x
    if start[1] < min_y:
        min_y = start[1]
        # print max_y
    # print start
    # print infected
    # print direction

# print infected
# print start
# print max_x
# print max_y
# print min_x
# print min_y
print count_infected







#
