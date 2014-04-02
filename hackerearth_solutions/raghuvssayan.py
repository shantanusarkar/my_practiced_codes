##Raghu Vs Sayan Max. Marks100
##Raghu and Sayan both like to eat (a lot) but since they are also looking
##after their health, they can only eat a limited amount of calories per day.
##So when Kuldeep invites them to a party, both Raghu and Sayan decide to
##play a game. The game is simple, both Raghu and Sayan will eat the dishes
##served at the party till they are full, and the one who eats maximum number
##of distinct dishes is the winner. However, both of them can only eat a
##dishes if they can finish it completely i.e. if Raghu can eat only 50 kCal
##in a day and has already eaten dishes worth 40 kCal, then he can't eat a
##dish with calorie value greater than 10 kCal.
##Given that all the dishes served at the party are infinite in number, (
##Kuldeep doesn't want any of his friends to miss on any dish) represented by
##their calorie value(in kCal) and the amount of kCal Raghu and Sayan can eat
##in a day, your job is to find out who'll win, in case of a tie print “Tie” (
##quotes for clarity).
##
##Input:
##First line contains number of test cases T.
##Each test case contains two lines.
##First line contains three integers A, B and N.
##where A and B is respectively the maximum amount of kCal Raghu and Sayan
##can eat per day, respectively and N is the number of dishes served at the
##party.
##Next line contains N integers where ith integer is the amount of kCal ith
##dish has.

##Output:
##For each test case print "Raghu Won" (quotes for clarity) if Raghu wins
##else if print "Sayan Won" (quotes for clarity) if Sayan wins else print
##"Tie" (quotes for clarity) if both eat equal number of dishes.

##Constraints:
##1 ≤ T ≤ 100
##1 ≤ N ≤ 10000
##1 ≤ kCal value of each dish ≤ 100000
## 1 ≤ A, B ≤ 1000000000


t = int(raw_input())
for x in range(0, t):
    m = raw_input()
    m = m.split()
    a = int(m[0])
    b = int(m[1])
    n = int(m[2])
    dish = raw_input()
    dish = dish.split()
    raghu = 0
    sayan = 0
    for y in range(0, n):
        if raghu + int(dish[y]) < a:
            raghu = raghu + int(dish[y])
        if sayan + int(dish[y]) < b:
            sayan = sayan + int(dish[y])
    if raghu > sayan:
        print "Raghu Won"
    if sayan > raghu:
        print "Sayan Won"
    if raghu == sayan:
        print "Tie"
