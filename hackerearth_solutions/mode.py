t = int(raw_input())
for x in range(0, t):
    length = int(raw_input())
    string = raw_input()
    string = ''.join(sorted(string))
    a = []
    ans = []
    rep = 0
    b = 0
    for y in range(0, length):
        count = string.count(string[y])
        if count == rep:
            if string[y] not in ans:
                ans.append(string[y])
        if count > rep:
            b = 0
            rep = count
            res = string[y]
    if b == 0:
        print res
    else:
        print ans