input_data = '''24/14
30/24
29/44
47/37
6/14
20/37
14/45
5/5
26/44
2/31
19/40
47/11
0/45
36/31
3/32
30/35
32/41
39/30
46/50
33/33
0/39
44/30
49/4
41/50
50/36
5/31
49/41
20/24
38/23
4/30
40/44
44/5
0/43
38/20
20/16
34/38
5/37
40/24
22/17
17/3
9/11
41/35
42/7
22/48
47/45
6/28
23/40
15/15
29/12
45/11
21/31
27/8
18/44
2/17
46/17
29/29
45/50'''

# input_data = '''0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10'''

rows = input_data.split('\n')
blocks = []
for row in rows:
    vals = row.split('/')
    blocks.append([int(vals[0]), int(vals[1])])

prev = 0

longest_global = 0
largest_global = 0

def test(prev, strength, used, length):
    largest = strength
    longest = length
    for alt in blocks:
        if alt[0] == prev:
            if alt not in used:
                a = test(alt[1], strength + alt[1] + alt[0], used + [alt], length+1)
                if a[1] > longest:
                    largest = a[0]
                    longest = a[1]
                elif a[1] == longest:
                    if a[0] > largest:
                        largest = a[0]
                        longest = a[1]
        elif alt[1] == prev:
            if alt not in used:
                a = test(alt[0], strength + alt[1] + alt[0], used + [alt], length+1)
                if a[1] > longest:
                    largest = a[0]
                    longest = a[1]
                elif a[1] == longest:
                    if a[0] > largest:
                        largest = a[0]
                        longest = a[1]
    return [largest, longest]







print test(0, 0, [], 0)
#2002 too high
