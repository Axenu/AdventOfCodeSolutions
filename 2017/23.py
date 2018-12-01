input_data = '''set b 84
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
    set f 1 # jump -23
    set d 2
        set e 2 # jump -13
            set g d # jump -8
            mul g e
            sub g b
            jnz g 2
            set f 0
            sub e -1
            set g e
            sub g b
            jnz g -8
        sub d -1
        set g d
        sub g b
        jnz g -13
    jnz f 2
    sub h -1
    set g b
    sub g c
    jnz g 2
    jnz 1 3
    sub b -17
    jnz 1 -23'''

a = 1
h = 0
b = (84 * 100) + 100000
g = 0
f = 0
c = b + 17000

for b in xrange(108400, 125417, 17):
    f = 1
    for d in xrange(2, b):
        if b % d == 0:
            f = 0
    if f == 0:
        h += 1
print h
