input_data = ''''''

rows = input_data.split('\n')
count = 0

values = ['0']
pos = 0
step = 0

state = 'A'

for i in xrange(0, 12994925):
    if state == 'A':
        if values[pos] == '0':
            values[pos] = '1'
            pos += 1
            state = 'B'
        else:
            values[pos] = '0'
            pos -= 1
            state = 'F'
    elif state == 'B':
        if values[pos] == '0':
            pos += 1
            state = 'C'
        else:
            values[pos] = '0'
            pos += 1
            state = 'D'
    elif state == 'C':
        if values[pos] == '0':
            values[pos] = '1'
            pos -= 1
            state = 'D'
        else:
            pos += 1
            state = 'E'
    elif state == 'D':
        if values[pos] == '0':
            pos -= 1
            state = 'E'
        else:
            values[pos] = '0'
            pos -= 1
    elif state == 'E':
        if values[pos] == '0':
            pos += 1
            state = 'A'
        else:
            pos += 1
            state = 'C'
    elif state == 'F':
        if values[pos] == '0':
            values[pos] = '1'
            pos -= 1
            state = 'A'
        else:
            pos += 1
            state = 'A'

    if pos < 0:
        pos += 1
        values = ['0'] + values

    if pos >= len(values):
        values.append('0')

count = 0
for c in values:
    if c == '0':
        count += 1

print count







#
