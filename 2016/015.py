disks = [[1, 13], [10,19], [2,3], [1,7], [3,5], [5,17], [0, 11]]
# disks = [[4, 5], [1, 2]]

time = 0

for i in xrange(0, 10000000):
    time += 1
    for disk in disks:
        disk[0] += 1
        disk[0] = disk[0] % disk[1]

    diff = 1
    possible = True
    for disk in disks:
        newPos = disk[0]
        newPos += diff
        newPos = newPos % disk[1]
        if newPos != 0:
            possible = False
        diff += 1
    if possible:
        print time

#376777
#3903937
