input_data = '''rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 5
rect 4x1
rotate row y=0 by 2
rect 1x2
rotate row y=1 by 6
rotate row y=0 by 2
rect 1x2
rotate column x=32 by 1
rotate column x=23 by 1
rotate column x=13 by 1
rotate row y=0 by 6
rotate column x=0 by 1
rect 5x1
rotate row y=0 by 2
rotate column x=30 by 1
rotate row y=1 by 20
rotate row y=0 by 18
rotate column x=13 by 1
rotate column x=10 by 1
rotate column x=7 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 17x1
rotate column x=16 by 3
rotate row y=3 by 7
rotate row y=0 by 5
rotate column x=2 by 1
rotate column x=0 by 1
rect 4x1
rotate column x=28 by 1
rotate row y=1 by 24
rotate row y=0 by 21
rotate column x=19 by 1
rotate column x=17 by 1
rotate column x=16 by 1
rotate column x=14 by 1
rotate column x=12 by 2
rotate column x=11 by 1
rotate column x=9 by 1
rotate column x=8 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=4 by 1
rotate column x=2 by 1
rotate column x=0 by 1
rect 20x1
rotate column x=47 by 1
rotate column x=40 by 2
rotate column x=35 by 2
rotate column x=30 by 2
rotate column x=10 by 3
rotate column x=5 by 3
rotate row y=4 by 20
rotate row y=3 by 10
rotate row y=2 by 20
rotate row y=1 by 16
rotate row y=0 by 9
rotate column x=7 by 2
rotate column x=5 by 2
rotate column x=3 by 2
rotate column x=0 by 2
rect 9x2
rotate column x=22 by 2
rotate row y=3 by 40
rotate row y=1 by 20
rotate row y=0 by 20
rotate column x=18 by 1
rotate column x=17 by 2
rotate column x=16 by 1
rotate column x=15 by 2
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 1
rotate column x=10 by 1
rotate column x=8 by 3
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 1
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 19x1
rotate column x=44 by 2
rotate column x=40 by 3
rotate column x=29 by 1
rotate column x=27 by 2
rotate column x=25 by 5
rotate column x=24 by 2
rotate column x=22 by 2
rotate column x=20 by 5
rotate column x=14 by 3
rotate column x=12 by 2
rotate column x=10 by 4
rotate column x=9 by 3
rotate column x=7 by 3
rotate column x=3 by 5
rotate column x=2 by 2
rotate row y=5 by 10
rotate row y=4 by 8
rotate row y=3 by 8
rotate row y=2 by 48
rotate row y=1 by 47
rotate row y=0 by 40
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 4
rotate column x=43 by 2
rotate column x=42 by 3
rotate column x=41 by 2
rotate column x=38 by 5
rotate column x=37 by 5
rotate column x=36 by 5
rotate column x=33 by 1
rotate column x=28 by 1
rotate column x=27 by 5
rotate column x=26 by 5
rotate column x=25 by 1
rotate column x=23 by 5
rotate column x=22 by 1
rotate column x=21 by 2
rotate column x=18 by 1
rotate column x=17 by 3
rotate column x=12 by 2
rotate column x=11 by 2
rotate column x=7 by 5
rotate column x=6 by 5
rotate column x=5 by 4
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 3
rotate column x=0 by 4'''

screenX = 50
screenY = 6
screen = []
for x in xrange(0, screenX):
    a = []
    for y in xrange(0, screenY):
        a.append(0)
    screen.append(a)

def printScreen(screen, screenX, screenY):
    count = 0
    for yy in xrange(0, screenY):
        s = ''
        for xx in xrange(0, screenX):
            if screen[xx][yy] == 1:
                s += '#'
                count += 1
            else:
                s += '.'
        print s
    return count

def rect(screen, x, y):
    for xx in xrange(0, x):
        for yy in xrange(0, y):
            screen[xx][yy] = 1

def rotateRow(screen, screenX, screenY, y, count):
    row = []
    for xx in xrange(0, screenX):
        row.append(screen[xx][y])
    for xx in xrange(0, screenX):
        screen[xx][y] = row[(xx-count)%screenX]
        # row.append(screen[xx][y])

def rotateColumn(screen, screenX, screenY, x, count):
    column = []
    for yy in xrange(0, screenY):
        column.append(screen[x][yy])
        # row.append(screen[xx][y])
    for yy in xrange(0, screenY):
        screen[x][yy] = column[(yy-count)%screenY]

rows = input_data.split('\n')

for row in rows:
    command = row.split(' ')
    if command[0] == 'rect':
        dim = command[1].split('x')
        rect(screen, int(dim[0]), int(dim[1]))
    else:
        if command[1] == 'row':
            s = command[2].split('=')
            rotateRow(screen, screenX, screenY, int(s[1]), int(command[4]))
            printScreen(screen, screenX, screenY)
        else:
            s = command[2].split('=')
            rotateColumn(screen, screenX, screenY, int(s[1]), int(command[4]))
            printScreen(screen, screenX, screenY)

print ' '
print printScreen(screen, screenX, screenY)

#ZJHRKCPLYJ
