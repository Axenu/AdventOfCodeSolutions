input_data = '''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 680
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''



from string import ascii_lowercase
from Queue import Queue
registry = {}

for c in ascii_lowercase:
    registry[c] = 0

rows = input_data.split('\n')

latest = 0
i = 0

def getVal(val):
    if val.isalpha():
        return registry[val]
    else:
        return int(val)

while i < len(rows):
    # print i
    row = rows[i]
    vals = row.split(' ')
    jump = 1
    if vals[0] == 'set':
        registry[vals[1]] = getVal(vals[2])
    elif vals[0] == 'add':
        registry[vals[1]] += getVal(vals[2])
    elif vals[0] == 'mul':
        registry[vals[1]] *= getVal(vals[2])
    elif vals[0] == 'mod':
        registry[vals[1]] %= getVal(vals[2])
    elif vals[0] == 'snd':
        latest = registry[vals[1]]
    elif vals[0] == 'rcv':
        if registry[vals[1]] != 0:
            break
    elif vals[0] == 'jgz':
        if getVal(vals[1]) > 0:
            jump = getVal(vals[2])
    i += jump


print latest

# part 2:
registry1 = {'a':0, 'i':0, 'p':0, 'b':0, 'f':0, 'c':0}
registry2 = {'a':0, 'i':0, 'p':1, 'b':0, 'f':0, 'c':0}
queue1 = Queue()
queue2 = Queue()

def step(registry, queue1, queue2, i):
    def getVal(val):
        if val.isalpha():
            return registry[val]
        else:
            return int(val)
    row = rows[i]
    vals = row.split(' ')
    jump = 1
    send = 0
    if vals[0] == 'set':
        registry[vals[1]] = getVal(vals[2])
    elif vals[0] == 'add':
        registry[vals[1]] += getVal(vals[2])
    elif vals[0] == 'mul':
        registry[vals[1]] *= getVal(vals[2])
    elif vals[0] == 'mod':
        registry[vals[1]] %= getVal(vals[2])
    elif vals[0] == 'snd':
        # latest = registry[vals[1]]
        send = 1
        queue1.put(getVal(vals[1]))
    elif vals[0] == 'rcv':
        if not queue2.empty():
            registry[vals[1]] = queue2.get()
        else:
            jump = 0
    elif vals[0] == 'jgz':
        if getVal(vals[1]) > 0:
            jump = getVal(vals[2])
    # i += jump
    return (i + jump, send)

pos1 = 0
pos2 = 0
total = 0
while True:
    n1, times = step(registry1, queue1, queue2, pos1)
    n2, times = step(registry2, queue2, queue1, pos2)
    if n1 == pos1 and n2 == pos2:
        break
    total += times
    pos1 = n1
    pos2 = n2

print total






#
