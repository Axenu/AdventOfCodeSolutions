input_data = '''cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 13 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5'''

rows = input_data.split('\n')

reg = [0, 0, 1, 0]
i = 0

def getVal(regName):
    if regName == 'a':
        return reg[0]
    elif regName == 'b':
        return reg[1]
    elif regName == 'c':
        return reg[2]
    elif regName == 'd':
        return reg[3]


def setVal(regName, val):
    if regName == 'a':
        reg[0] = val
    elif regName == 'b':
        reg[1] = val
    elif regName == 'c':
        reg[2] = val
    elif regName == 'd':
        reg[3] = val

while i < len(rows):
    words = rows[i].split(' ')
    if words[0] == 'cpy':
        val = 0
        if words[1].isdigit():
            val = int(words[1])
        else:
            val = getVal(words[1])
        setVal(words[2], val)
        i += 1
    elif words[0] == 'jnz':
        val = 0
        if words[1].isdigit():
            val = int(words[1])
        else:
            val = getVal(words[1])
        if val != 0:
            c = int(words[2])
            i += c
        else:
            i += 1
    elif words[0] == 'dec':
        val = getVal(words[1])
        setVal(words[1], val-1)
        i += 1
    elif words[0] == 'inc':
        val = getVal(words[1])
        setVal(words[1], val+1)
        i += 1
print reg
