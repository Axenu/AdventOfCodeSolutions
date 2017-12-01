input_data = '''cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 85 c
jnz 91 d
inc a
inc d
jnz d -2
inc c
jnz c -5''' # res, c = 0, d = 0 a += c * d

input_data = '''cpy a b
dec b
cpy 0 d
cpy 0 c
cpy 0 d
cpy 0 c
cpy 0 d
cpy 0 d
cpy 0 c
mul a b
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 85 c
jnz 91 d
inc a
inc d
jnz d -2
inc c
jnz c -5'''

# [132, 11, 0, 0]

rows = input_data.split('\n')
#[12, 0, 0, 0]
#[132, 11, 0, 0]
#[1320, 10, 0, 0]
#[11880, 9, 0, 0]

reg = [12, 0, 0, 0]
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

print 'hello world'[:3]
first = False
while i < len(rows):
    # if i == 10:
        # print i
        # print rows[i]
        # print reg
        # if not first:
        #     first = True
        # else:
        #     break

    # print i
    words = rows[i].split(' ')
    if words[0] == 'cpy':
        val = 0
        # if i > 10:
            # print words[1]
            # print int(words[-1])
        try:
            val = int(words[1])
        except:
            val = getVal(words[1])
        # if words[1].isdigit():
        #     val = int(words[1])
        #     print 'digit'
        # else:
        #     val = getVal(words[1])
        setVal(words[2], val)
        # print reg
        i += 1
    elif words[0] == 'jnz':
        val = 0
        if words[1].isdigit():
            val = int(words[1])
        else:
            val = getVal(words[1])
        if val != 0:
            # if int(words[2]) < 0:
                # print int(words[2])
            steps = 0
            try:
                steps = int(words[2])
            except:
                steps = getVal(words[2])
            # c = int(words[2])
            i += steps
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
    elif words[0] == 'tgl':
        # print rows[i]
        val = getVal(words[1])
        index = i + val
        print reg
        print index
        if index < 26:
            cmd = rows[index][:3]
            if cmd == 'inc':
                rows[index] = 'dec' + rows[index][3:]
            elif cmd == 'dec':
                rows[index] = 'inc' + rows[index][3:]
            elif cmd == 'tgl':
                rows[index] = 'inc' + rows[index][3:]
            elif cmd == 'jnz':
                rows[index] = 'cpy' + rows[index][3:]
            elif cmd == 'cpy':
                rows[index] = 'jnz' + rows[index][3:]
            else:
                print 'unknown command'
                print cmd
        i += 1
    elif words[0] == 'mul':
        val = getVal(words[1])
        val *= getVal(words[2])
        setVal(words[1], val)
        i += 1
print reg

#479009335
#12775 # right
