valA = 703
valB = 516

# valA = 1352636452
# valB = 1233683848
found = 0
for x in xrange(0,5000000):
    if valA % 65536 == valB % 65536:
        found += 1
        # print valA % 65536
        # print valB % 65536
    valA = (valA * 16807) % 2147483647
    valB = (valB * 48271) % 2147483647
    while valA % 4 != 0:
        valA = (valA * 16807) % 2147483647
    while valB % 8 != 0:
        valB = (valB * 48271) % 2147483647


print found
