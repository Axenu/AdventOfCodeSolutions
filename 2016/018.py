input_data = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'

safe = 0

row = ''
nextRow = ''
print input_data
for i in xrange(0, len(input_data)):
    center = input_data[i]
    if input_data[i] == '.':
        safe += 1
    left = ''
    if i == 0:
        left = '.'
    else:
        left = input_data[i-1]
    right = ''
    if i == len(input_data)-1:
        right = '.'
    else:
        right = input_data[i+1]
    if (left == '^' and right == '.') or (left == '.' and right == '^'):
        nextRow += '^'
    else:
        nextRow += '.'
        safe += 1

# print nextRow
row = nextRow
for i in xrange(0, 399998):
    nextRow = ''
    for i in xrange(0, len(row)):
        left = '.'
        if i != 0:
            left = row[i-1]
        right = '.'
        if i != len(row)-1:
            right = row[i+1]
        if (left == '^' and right == '.') or (left == '.' and right == '^'):
            nextRow += '^'
        else:
            nextRow += '.'
            safe += 1
    row = nextRow
    # print row

print safe
