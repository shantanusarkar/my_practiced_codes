n = int(raw_input())
array = raw_input()
array = array.split()
q = int(raw_input())
for x in range(0, q):
    queries = raw_input()
    queries = queries.split()
    l = int(queries[0])
    r = int(queries[1])
    x = int(queries[2])
    for y in range(l-1, r-1):
        num = int(array[y])
        k = num
        xor = num ^ x
        low = 0
        for z in range(l-1, r-1):
            num1 = int(array[z])
            if xor > num1:
                low = 1
                break
        if low == 0:
            break
    range_value = []
    for t in range(l-1, r-1):
        range_value.append(array[t])
    occ = range_value.count('1')
    print num