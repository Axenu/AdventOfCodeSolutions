input_data = 'ngcjuoqr'
# input_data = 'abc'

import hashlib

needed_fives = []
keys = []

found = 0

i = 0

def hashStretch(input_data):
    m = hashlib.md5()
    m.update(input_data)
    res = m.hexdigest()
    for i in xrange(0, 2016):
        m = hashlib.md5()
        m.update(res)
        res = m.hexdigest()
    return res

# print hashStretch('abc22859')

while found < 80:
    res = hashStretch(input_data + str(i))
    # m = hashlib.md5()
    # m.update(input_data + str(i))
    # res = m.hexdigest()
    foundThree = False
    y = 0

    while y < len(needed_fives):
        if needed_fives[y][1] > 1000:
            del needed_fives[y]
            y -= 1
        else:
            needed_fives[y][1] += 1
            if needed_fives[y][0] in res:
                found += 1
                print found
                print needed_fives[y]
                keys.append(needed_fives[y])
                del needed_fives[y]
                y -= 1

        y += 1
    for x in xrange(0, len(res)-2):
        if res[x] == res[x+1] and res[x+1] == res[x+2] and not foundThree:
            needed_fives.append([res[x]+res[x]+res[x]+res[x]+res[x], 0, i, res])
            # print i
            # print res
            # print(res[x]+res[x]+res[x]+res[x]+res[x])
            foundThree = True
            break
    i += 1
print len(keys)
print keys[63]
print keys
