input_data = 347991

posX = 300
posY = 300

# posX += 1
#
# posY += 1
#
# posX -= 1
# posX -= 1
#
# posY -= 1
# posY -= 1
#
# posX += 1
# posX += 1
# posX += 1
#
# posY += 1
# posY += 1
# posY += 1
#
# posX -= 1
# posX -= 1
# posX -= 1
# posX -= 1
#
# posY -= 1
# posY -= 1
# posY -= 1
# posY -= 1
#
# posX += 1
# posX += 1
# posX += 1
# posX += 1
# posX += 1

data = [0] * 600
for i in xrange(0, 600):
    data[i] = [0] * 600

index = 1

direction = 0
amount = 1

data[posX][posY] = 1

def calculateArray(posX, posY):
    val = 0
    val += data[posX+1][posY]
    val += data[posX+1][posY+1]
    val += data[posX][posY+1]
    val += data[posX-1][posY+1]
    val += data[posX-1][posY]
    val += data[posX-1][posY-1]
    val += data[posX][posY-1]
    val += data[posX+1][posY-1]
    data[posX][posY] = val
    # print val
    if val >= input_data:
        print val
        input("Press Enter to continue...")

while index < input_data:
    # print index
    # print posX
    # print posY
    if direction == 0:
        for i in xrange(0, amount):
            posX += 1
            index += 1
            calculateArray(posX, posY)
            if index >= input_data:
                break
        if index == input_data:
            break

    elif direction == 1:
        for i in xrange(0, amount):
            posY += 1
            index += 1
            calculateArray(posX, posY)
            if index >= input_data:
                break
        amount += 1
        if index == input_data:
            break
    elif direction == 2:
        for i in xrange(0, amount):
            posX -= 1
            index += 1
            calculateArray(posX, posY)
            if index >= input_data:
                break
        if index == input_data:
            break
    elif direction == 3:
        for i in xrange(0, amount):
            posY -= 1
            index += 1
            calculateArray(posX, posY)
            if index >= input_data:
                break
        amount += 1
        if index == input_data:
            break

    direction += 1
    direction = direction % 4

print index
print posX
print posY
