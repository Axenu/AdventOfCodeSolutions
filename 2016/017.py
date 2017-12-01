input_data = 'qljzarfv'

import hashlib

pos = [0,0]

currentMoves = [['', [0,0]]]

# def doMove(history, pos):
    # if pos[0] == pos[1] == 3:
    #     print history
    #     if len(history) > 100:
    #         return
    # m = hashlib.md5()
    # m.update(input_data + history)
    # res = m.hexdigest()
    # if res[0] in ['b','c','d','e','f']:
    #     if pos[1] > 0:
    #         # up possible
    #         doMove(history+'U', [pos[0], pos[1]-1])
    # if res[1] in ['b','c','d','e','f']:
    #     if pos[1] < 3:
    #         # down possible
    #         doMove(history+'D', [pos[0], pos[1]+1])
    #         pass
    # if res[2] in ['b','c','d','e','f']:
    #     if pos[0] > 0:
    #         # left possible
    #         doMove(history+'L', [pos[0]-1, pos[1]])
    #         pass
    # if res[3] in ['b','c','d','e','f']:
    #     if pos[0] < 3:
    #         # right possible
    #         doMove(history+'R', [pos[0]+1, pos[1]])
    #         pass
#
# doMove('', pos)

maxLength = 0

def doMove(currentMoves, maxLength):
    temp = []
    for i in xrange(0, len(currentMoves)):
        history = currentMoves[i][0]
        pos = currentMoves[i][1]
        if pos[0] == pos[1] == 3:
            if len(history) > maxLength:
                maxLength = len(history)
        else:
                # print history
            m = hashlib.md5()
            m.update(input_data + history)
            res = m.hexdigest()
            if res[0] in ['b','c','d','e','f']:
                if pos[1] > 0:
                    # up possible
                    # doMove(history+'U', [pos[0], pos[1]-1])
                    temp.append([history+'U', [pos[0], pos[1]-1]])
            if res[1] in ['b','c','d','e','f']:
                if pos[1] < 3:
                    # down possible
                    # doMove(history+'D', [pos[0], pos[1]+1])
                    temp.append([history+'D', [pos[0], pos[1]+1]])
                    pass
            if res[2] in ['b','c','d','e','f']:
                if pos[0] > 0:
                    # left possible
                    # doMove(history+'L', [pos[0]-1, pos[1]])
                    temp.append([history+'L', [pos[0]-1, pos[1]]])
                    pass
            if res[3] in ['b','c','d','e','f']:
                if pos[0] < 3:
                    # right possible
                    # doMove(history+'R', [pos[0]+1, pos[1]])
                    temp.append([history+'R', [pos[0]+1, pos[1]]])
                    pass
    return temp, maxLength

i = 0
while len(currentMoves) > 0:
    # print i
    currentMoves, maxLength = doMove(currentMoves, maxLength)
    i+=1
    # print len(currentMoves)



# print currentMoves
# doMove(currentMoves)
# print currentMoves
