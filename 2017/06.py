input_data=''''''

rows = input_data.split('\n')

total = 0

# arr = [0] * 16
banks = [5,1,10,0,1,7,13,14,3,12,8,10,7,12,0,6]
# banks = [0,2,7,0]

seen = [tuple(banks)]
count = 0
last = ''
while True:
    #reallocate
    highest = 0
    index = 0
    # print max(banks)
    highest = banks.index(max(banks))

    val = banks[highest]
    # print val
    banks[highest] = 0
    index = highest + 1
    while val > 0:
        banks[(index)%len(banks)] += 1
        index += 1
        val -= 1

    s = tuple(banks)
    if s in seen:
        print len(seen)
        print len(seen) - seen.index(s)
        last = s
        break
    seen.append(s)
    count += 1

# count = 1
# while True:
#     #reallocate
#     highest = 0
#     index = 0
#     for bank in xrange(0, len(banks)):
#         if banks[bank] > banks[highest]:
#             highest = bank
#
#     val = banks[highest]
#     # print val
#     banks[highest] = 0
#     index = highest + 1
#     while val > 0:
#         banks[(index)%len(banks)] += 1
#         index += 1
#         val -= 1
#
#     s = ''
#     for i in xrange(0,len(banks)):
#         s += str(banks[i]) + ','
#     # print s
#     if s == last:
#         print s
#         print count
#         break
#     # seen.append(s)
#     count += 1

# for row in rows:
    # values = row.split(' ')


# print
