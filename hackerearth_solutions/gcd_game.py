def gcd(m,n):
    return n if (m-n) == 0 else gcd(abs(m-n), min(m, n))
t = int(raw_input())
for z in range(0, t):
    string = raw_input()
    string = string.split()
    a = int(string[0])
    b = int(string[1])
    while a!=1 and b != 1:
        arijit_gcd = gcd(a, b)
        if arijit_gcd > 1:
            if b/arijit_gcd > 1:
                b = int(b/arijit_gcd)
            else:
                b = b-1
        elif arijit_gcd == 1:
            b = b-1
        chandu_gcd = gcd(a, b)
        if chandu_gcd > 1:
            if a/chandu_gcd > 1:
                a = int(a/chandu_gcd)
            else:
                a = a-1
        elif chandu_gcd == 1:
            b = b-1
    if a==1 and b==1:
        print "Draw"
    elif a==1:
        print "Chandu Don"
    elif b==1:
        print "Arijit"

