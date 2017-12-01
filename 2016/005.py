input_data = 'reyedfim'

import hashlib

i = 0
foundC = 0
running = True
password = list('        ')
while running:
    m = hashlib.md5()
    m.update('reyedfim' + str(i))
    res = m.hexdigest()
    if res[0:5] == '00000':
        print res[5]
        print res[6]
        if res[5].isdigit():
            if int(res[5]) <= 7:
                if password[int(res[5])] == ' ':
                    password[int(res[5])] = res[6]
                    print password
                    foundC += 1
                    if foundC > 7:
                        running = False
    i += 1
#f97c354d

#c3ae76f4
