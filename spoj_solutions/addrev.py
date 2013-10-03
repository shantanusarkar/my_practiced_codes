tc = int(input())
while tc:
    tc -= 1
    s, t = [str(x) for x in raw_input().split()]
    p = [int(x) for x in s]
    q = [int(x) for x in t]
    lp = len(p)
    lq = len(q)
    if lp > lq:
        q[lq : lp] = [0] * (lp - lq)
    elif lq > lp:
        p[lp : lq] = [0] * (lq - lp)
    result = []
    carry = 0
    while p and q:
        s = p.pop(0) + q.pop(0) + carry
        carry = s / 10
        s = s % 10
        result.append(s)
    if carry:
        result.append(carry)
    while result:
        temp = result.pop(0)
        if temp != 0:
            result.insert(0, temp)
            break
    output = [str(x) for x in result]
    print ''.join(output)
