t = int(raw_input())
for x in range(0, t):
    data = raw_input()
    data = data.split()
    food = int(data[0])
    gold = int(data[1])
    samurai = int(data[2])
    paladin = int(data[3])
    champion = int(data[4])
    total_power = int(data[5])
    samurai_num = 0
    paladin_num = 0
    champion_num = 0
    while(food > 50):
        if (food > 100):
            samurai_num += 1
            food = food - 100

        if(food > 125 and gold > 50):
            paladin_num += 1
            food = food - 125
            gold = gold - 50

        if(food > 50 and gold > 100):
            champion_num += 1
            food = food - 50
            gold = gold - 100

    power = samurai + samurai_num + paladin + paladin_num + champion + champion_num

    diff = power - total_power

    if diff > 0:
        print diff
    else:
        print "-1"
