maxX = 40
maxY = 40

def isWall(x, y, num):
    sum = x*x + 3*x + 2*x*y + y + y*y
    sum += num
    binary = bin(sum)[2:]
    if binary.count('1') % 2 == 0:
        return False
    else:
        return True

def testPos(x, y, grid, length):
    if x < 0 or x > maxX:
        return
    if y < 0 or y > maxY:
        return
    if grid[x][y] == '.':
        grid[x][y] = str(length)
        length += 1
        testPos(x + 1, y, grid, length)
        testPos(x - 1, y, grid, length)
        testPos(x, y + 1, grid, length)
        testPos(x, y - 1, grid, length)
    elif grid[x][y].isdigit():
        if int(grid[x][y]) > length:
            grid[x][y] = str(length)
            length += 1
            testPos(x + 1, y, grid, length)
            testPos(x - 1, y, grid, length)
            testPos(x, y + 1, grid, length)
            testPos(x, y - 1, grid, length)

def printGrid():
    count = 0
    for y in xrange(0, maxY+1):
        row = ''
        for x in xrange(0, maxX +1):
            row += grid[x][y]
            if grid[x][y].isdigit():
                if int(grid[x][y]) <= 50:
                    count += 1
        print row
    print count

favNum = 1352

grid = []

for x in xrange(0, maxX+1):
    col = ''
    arr = []
    for y in xrange(0, maxY+1):
        if isWall(x, y, favNum) == True:
            col += '#'
            arr.append('#')
        else:
            col += '.'
            arr.append('.')
    grid.append(arr)

position = [1,1]
printGrid()
testPos(1, 1, grid, 0)
# testPos(position[0] + 1, position[1], grid, length)
# testPos(position[0] - 1, position[1], grid, length)
# testPos(position[0], position[1] + 1, grid, length)
# testPos(position[0], position[1] - 1, grid, length)
print ' '
printGrid()
print grid[31][39]
