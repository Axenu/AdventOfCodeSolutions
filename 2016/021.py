input_data = '''move position 0 to position 3
rotate right 0 steps
rotate right 1 step
move position 1 to position 5
swap letter h with letter b
reverse positions 1 through 3
swap letter a with letter g
swap letter b with letter h
rotate based on position of letter c
swap letter d with letter c
rotate based on position of letter c
swap position 6 with position 5
rotate right 7 steps
swap letter b with letter h
move position 4 to position 3
swap position 1 with position 0
swap position 7 with position 5
move position 7 to position 1
swap letter c with letter a
move position 7 to position 5
rotate right 4 steps
swap position 0 with position 5
move position 3 to position 1
swap letter c with letter h
rotate based on position of letter d
reverse positions 0 through 2
rotate based on position of letter g
move position 6 to position 7
move position 2 to position 5
swap position 1 with position 0
swap letter f with letter c
rotate right 1 step
reverse positions 2 through 4
rotate left 1 step
rotate based on position of letter h
rotate right 1 step
rotate right 5 steps
swap position 6 with position 3
move position 0 to position 5
swap letter g with letter f
reverse positions 2 through 7
reverse positions 4 through 6
swap position 4 with position 1
move position 2 to position 1
move position 3 to position 1
swap letter b with letter a
rotate based on position of letter b
reverse positions 3 through 5
move position 0 to position 2
rotate based on position of letter b
reverse positions 4 through 5
rotate based on position of letter g
reverse positions 0 through 5
swap letter h with letter c
reverse positions 2 through 5
swap position 7 with position 5
swap letter g with letter d
swap letter d with letter e
move position 1 to position 2
move position 3 to position 2
swap letter d with letter g
swap position 3 with position 7
swap letter b with letter f
rotate right 3 steps
move position 5 to position 3
move position 1 to position 2
rotate based on position of letter b
rotate based on position of letter c
reverse positions 2 through 3
move position 2 to position 3
rotate right 1 step
move position 7 to position 0
rotate right 3 steps
move position 6 to position 3
rotate based on position of letter e
swap letter c with letter b
swap letter f with letter d
swap position 2 with position 5
swap letter f with letter g
rotate based on position of letter a
reverse positions 3 through 4
rotate left 7 steps
rotate left 6 steps
swap letter g with letter b
reverse positions 3 through 6
rotate right 6 steps
rotate based on position of letter c
rotate based on position of letter b
rotate left 1 step
reverse positions 3 through 7
swap letter f with letter g
swap position 4 with position 1
rotate based on position of letter d
move position 0 to position 4
swap position 7 with position 6
rotate right 6 steps
rotate based on position of letter e
move position 7 to position 3
rotate right 3 steps
swap position 1 with position 2'''

passw = ['a','b','c','d','e','f','g','h']

rows = input_data.split('\n')

def indexOf(char, arr):
    for i in xrange(0, len(arr)):
        if arr[i] == char:
            return i

for row in rows:
    words = row.split(' ')
    if words[0] == 'swap':
        if words[1] == 'position':
            temp = passw[int(words[2])]
            passw[int(words[2])] = passw[int(words[5])]
            passw[int(words[5])] = temp
        else:
            i1 = indexOf(words[2], passw)
            i2 = indexOf(words[5], passw)
            temp = passw[i1]
            passw[i1] = passw[i2]
            passw[i2] = temp
    elif words[0] == 'rotate':
        if words[1] == 'left':
            old = passw[:]
            steps = int(words[2])
            for i in xrange(0, len(passw)):
                newPos = i-steps
                if newPos < 0:
                    newPos += len(passw)
                passw[newPos] = old[i]
        elif words[1] == 'right':
            old = passw[:]
            steps = int(words[2])
            for i in xrange(0, len(passw)):
                newPos = i+steps
                if newPos >= len(passw):
                    newPos -= len(passw)
                passw[newPos] = old[i]
        else:
            old = passw[:]
            steps = indexOf(words[6], passw)
            if steps >= 4:
                steps += 1
            steps += 1
            # print row
            # print steps
            for i in xrange(0, len(passw)):
                newPos = i+steps
                while newPos >= len(passw):
                    newPos -= len(passw)
                # print newPos
                passw[newPos] = old[i]
    elif words[0] == 'reverse':
        toRot = passw[int(words[2]):int(words[4])+1]
        passw[int(words[2]):int(words[4])+1] = toRot[::-1]
    else:
        i1 = int(words[2]) # from
        i2 = int(words[5]) # to
        temp = passw.pop(i1)
        passw.insert(i2, temp)



# dechagfb
print ''.join(passw)

print 'part 2'

passw = ['f','b','g','d','c','e','a','h']
print passw


for row in reversed(rows):
    words = row.split(' ')
    if words[0] == 'swap':
        if words[1] == 'position':
            temp = passw[int(words[2])]
            passw[int(words[2])] = passw[int(words[5])]
            passw[int(words[5])] = temp
        else:
            i1 = indexOf(words[2], passw)
            i2 = indexOf(words[5], passw)
            temp = passw[i1]
            passw[i1] = passw[i2]
            passw[i2] = temp
    elif words[0] == 'rotate':
        if words[1] == 'right':
            old = passw[:]
            steps = int(words[2])
            for i in xrange(0, len(passw)):
                newPos = i-steps
                if newPos < 0:
                    newPos += len(passw)
                passw[newPos] = old[i]
        elif words[1] == 'left':
            old = passw[:]
            steps = int(words[2])
            for i in xrange(0, len(passw)):
                newPos = i+steps
                if newPos >= len(passw):
                    newPos -= len(passw)
                passw[newPos] = old[i]
        else:
            # print row
            # print passw
            old = passw[:]
            index = indexOf(words[6], passw)
            steps = 0
            # print index
            for i in xrange(0, len(passw)):
                # figure out where c began.
                # test all possible starting positions and move appropiatley.
                d = i
                if d >= 4:
                    d += 1
                d += 1
                d += i
                while d >= len(passw):
                    d -= len(passw)
                if d == index:
                    # print i
                    steps = i-index
                # print i
                # print d
                # # while d+i > len(passw):
                # #     d -= len(passw)
                # if d + i == index:
                #     steps = i
            # if steps >= 4:
            #     steps += 1
            # steps += 1
            # print row
            # print steps
            for i in xrange(0, len(passw)):
                newPos = i+steps
                while newPos < 0:
                    newPos += len(passw)
                while newPos >= len(passw):
                    newPos -= len(passw)
                # print newPos
                passw[newPos] = old[i]
            # print passw
    elif words[0] == 'reverse':
        toRot = passw[int(words[2]):int(words[4])+1]
        passw[int(words[2]):int(words[4])+1] = toRot[::-1]
    else:
        # print row
        i1 = int(words[2]) # from
        i2 = int(words[5]) # to
        # temp = passw.pop(i1)
        # passw.insert(i2, temp)
        # print passw
        temp = passw.pop(i2)
        passw.insert(i1, temp)
        # print passw

print ''.join(passw)
#ceagfdhb
#bdcaegfh
# ebdachgf
