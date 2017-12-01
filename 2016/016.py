input_data = '10001001100000001'
minLength = 35651584

res = input_data

while(len(res) < minLength):
    temp = res + '0'
    for i in xrange(len(res)-1, -1, -1):
        if res[i] == '0':
            temp += '1'
        else:
            temp += '0'

    res = temp
    print len(temp)

# print res[:minLength]
print len(res[:minLength])
checksum = res[:minLength]
while (len(checksum)%2 == 0):
    temp = ''
    for i in xrange(0, len(checksum), 2):
        if checksum[i] == checksum[i+1]:
            temp += '1'
        else:
            temp += '0'
    checksum = temp
    print len(checksum)
print checksum
