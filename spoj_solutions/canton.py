import math

tc = int(raw_input())

while tc: 
    tc -= 1
    term = int(raw_input())
    row_p = float((-1 + (1 + 8 * term) ** 0.5) / 2.0)
    row = int(math.ceil(row_p))

    pos = term - (row * (row - 1)) / 2;

    a = row - pos + 1
    if row % 2 == 0:
        print 'TERM %d IS %d/%d' % (term, pos, a)

    else:
        print 'TERM %d IS %d/%d' % (term, a, pos)
