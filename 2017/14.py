input_data = 'wenycdww'
# input_data = 'flqrgnkx'

def knot_hash(lengths):
    lengths += [17, 31, 73, 47, 23]
    val = range(0, 256)
    # print lengths

    currentPos = 0
    skip = 0

    def iterate(val, lengths, currentPos, skip):
        for length in lengths:
            l = int(length)
            start = currentPos
            rev = val[currentPos:l+currentPos]
            if currentPos + l > len(val):
                rev += val[0:(currentPos + l - len(val))]
            # print rev
            rev = list(reversed(rev))

            ll = currentPos + l
            if ll > len(val):
                ll = len(val) - currentPos

            # print ll
            val[currentPos:l+currentPos] = rev[0:ll]
            if currentPos + l > len(val):
                val[0:(currentPos + l - len(val))] = rev[ll:]
            # print val
            # print rev

            currentPos += l + skip
            currentPos = currentPos % len(val)
            skip += 1
        return (currentPos, skip)

    for i in xrange(0, 64):
        (currentPos, skip) = iterate(val, lengths, currentPos, skip)

    res = []
    hexa = ''
    for i in xrange(0, 256, 16):
        # print i
        s = val[i]
        for x in xrange(1, 16):
            # print x
            s ^= val[i+x]
        res.append(s)
        hexa += chr(s).encode("hex")

    return hexa

ones = 0

arr = []
for x in xrange(0, 128):
    a = [0] * 128
    arr.append(a)

for i in xrange(0, 128):
    inp = input_data + '-' + str(i)
    # print inp
    inp = [ord(c) for c in inp]
    hash_val = knot_hash(inp)
    hash_b = ''
    # for c in hash_val:
        # hash_b += bin(int(c, 16))[2:]
    hash_bin = bin(int(hash_val, 16))[2:].zfill(128)
    # print hash_bin
    for c in hash_bin:
        if c == '1':
            ones += 1

    # print hash_bin
    # print hash_b
    for j in xrange(0, 128):
        arr[i][j] = int(hash_bin[j])

print ones

groups = 0

def markGroup(x, y, arr, groups):
    if arr[x][y] == 1:
        arr[x][y] = groups + 2
        if x < 127:
            markGroup(x+1, y, arr, groups)
        if x > 0:
            markGroup(x-1, y, arr, groups)
        if y < 127:
            markGroup(x, y+1, arr, groups)
        if y > 0:
            markGroup(x, y-1, arr, groups)
        return True
    else:
        return False

for x in xrange(0,128):
    for y in xrange(0, 128):
        if markGroup(x, y, arr, groups):
            groups += 1

print groups
# print arr
for row in arr:
    print row


#8108 too low

#1242

#
