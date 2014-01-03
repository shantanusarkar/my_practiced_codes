# link to question: http://www.hackerearth.com/problem/algorithm/complete-string-4/
# Author: Shantanu Sarkar

#!/usr/bin/env python
t = int(raw_input())
for x in range(0,t):
    a = raw_input()
    if len(a) < 26:
        print 'NO'
    else:
        bet = 'a'
        check = True
        for y in range(0,26):
            check = a.__contains__(bet)
            bet = chr(ord(bet) + 1)
            if check == False:
                break
        if check == True:
            print 'YES'
        else:
            print 'NO'
