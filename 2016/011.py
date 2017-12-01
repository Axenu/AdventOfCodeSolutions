floors = [['01','11'], ['00'], ['10']]
elevator = 0

from copy import deepcopy

def compatible(floor):
    found_G = False
    for unit in floor:
        if unit[1] == '0':
            found_G = True

    for unit in floor:
        if unit[1] == '1':
            if unit[0] + '0' not in floor and found_G:
                return False
    return True

def hashMove(move):
    hashV = str(move[1])
    floors = move[0]
    floors[0].sort()
    floors[1].sort()
    floors[2].sort()
    floors[3].sort()
    hashV += '0' + ''.join(floors[0])
    hashV += '1' + ''.join(floors[1])
    hashV += '2' + ''.join(floors[2])
    hashV += '3' + ''.join(floors[3])
    return hashV

def doMove(move):
    temp = []
    for move in moves:
        floors = move[0]
        elevator = move[1]
        history = move[2]
        if len(floors[3]) == 4:
            # print 'done!'
            pass
            # print move
        else:
            movedPair = False
            for unit in floors[elevator]:
                for unit2 in floors[elevator]:
                    if unit == unit2:
                        # found move with one
                        # move stuff
                        # remove unit from elevator and move up or down
                        f = deepcopy(floors)
                        f[elevator].remove(unit)
                        if elevator > 0:
                            f[elevator-1].append(unit)
                            h = hashMove([f, elevator+1])
                            if h not in history:
                                if compatible(f[elevator-1]):
                                    hi = deepcopy(history)
                                    hi[h] = 'd'
                                    temp.append([f, elevator-1, hi])
                        f = deepcopy(floors)
                        f[elevator].remove(unit)
                        if elevator < 3:
                            f[elevator+1].append(unit)
                            # test if state is already used:
                            h = hashMove([f, elevator+1])
                            if h not in history:
                                if compatible(f[elevator+1]):
                                    hi = deepcopy(history)
                                    hi[h] = 'd'
                                    temp.append([f, elevator+1, hi])
                    else:
                        if not movedPair:
                            if unit[0] == unit2[0]:
                                movedPair = True
                            if compatible([unit, unit2]):
                                f = deepcopy(floors)
                                f[elevator].remove(unit)
                                f[elevator].remove(unit2)
                                if elevator > 0:
                                    f[elevator-1].append(unit)
                                    f[elevator-1].append(unit2)
                                    h = hashMove([f, elevator+1])
                                    if h not in history:
                                        if compatible(f[elevator-1]):
                                            hi = deepcopy(history)
                                            hi[h] = 'd'
                                            temp.append([f, elevator-1, hi])
                                f = deepcopy(floors)
                                f[elevator].remove(unit)
                                f[elevator].remove(unit2)
                                if elevator < 3:
                                    f[elevator+1].append(unit)
                                    f[elevator+1].append(unit2)
                                    h = hashMove([f, elevator+1])
                                    if h not in history:
                                        if compatible(f[elevator+1]):
                                            hi = deepcopy(history)
                                            hi[h] = 'd'
                                            temp.append([f, elevator+1, hi])
    return temp


moves = [[[['01','11'], ['00'], ['10'], []], 0, {}]]
print hashMove(moves[0])
moves = [[[['01','11'], ['00'], ['10'], []], 0, {}]]
print hashMove(moves[0])
print moves
for i in xrange(0, 20):
    moves = doMove(moves)
    # print moves
    print len(moves)

# pairs = [[1, 0], [2, 0]]
# elevator = 0
#
# def doMove(move):
#     temp = []
#     for move in moves:
#         pairs = move[0]
#         elevator = move[1]
#         # if len(floors[3]) == 4:
#         #     print 'done!'
#         # for unit in floors[elevator]:
#         #     for unit2 in floors[elevator]:
#         #         if unit == unit2:
#         #             # found move with one
#         #             # move stuff
#         #             # remove unit from elevator and move up or down
#         #             f = deepcopy(floors)
#         #             f[elevator].remove(unit)
#         #             if elevator > 0:
#         #
#         #             pass
#         #         else:
#         #             # found move with two
#         #             pass
