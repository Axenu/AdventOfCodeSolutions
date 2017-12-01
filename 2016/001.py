input_data = 'L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4'
# input_data = 'R5, L5, R5, R3'

direction = [0,1]
position = [0,0]
visited = [[0,0]]

directions = input_data.split(', ')

for word in directions:
    if word[0] == 'L':
        nd0 = -direction[1]
        nd1 = direction[0]
        direction = [nd0, nd1]
    else:
        nd0 = direction[1]
        nd1 = -direction[0]
        direction = [nd0, nd1]
    dist = int(word[1:])
    for i in range(0, abs(direction[0] * dist)):
        position[0] += direction[0]
        new = [position[0],position[1]]
        if new in visited:
            print '==============================================='
            print new[0] + new[1]
            break
        visited.append(new)
    for i in range(0, abs(direction[1] * dist)):
        position[1] += direction[1]
        new = [position[0],position[1]]
        if new in visited:
            print '==============================================='
            print new[0] + new[1]
            break
        visited.append(new)
    # position[0] += direction[0] * dist
    # position[1] += direction[1] * dist

    print word
    print dist
    print position

# print visited
# print position
# print abs(position[0]) + abs(position[1])
