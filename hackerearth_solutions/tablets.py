n = int(raw_input())
total = []
sum = 0
for x in range(0, n):
    health_score = int(raw_input())
    if health_score not in total:
        total.append(health_score)
    else:
        total.append(int('1'))
for y in range(0, n):
    sum = sum + total[y]
print sum