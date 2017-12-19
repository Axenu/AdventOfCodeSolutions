input_data = '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'
# input_data = '3,4,1,5'

lengths = input_data.split(',')

lengths = [ord(c) for c in input_data]


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
            # if currentPos + l > len(val):
            #     start =
            # start1 = currentPos
            # start2 = 0
            # end1 = (currentPos+l)
            # end2 = 0
            # if end1 > len(val):
            #     end1 = len(val)
            #     end2 = l - (start1 - end1)
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

    # print iterate(val, lengths, currentPos, skip)

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

print knot_hash(lengths)
# print val

#c5fc60997b6ea80adb5a809f42c3543c
#a2582a3a0e66e6e86e3812dcb672a272
# e1462100a34221a7f0906da15c1c979a -- correct

# print val[0] * val[1]
