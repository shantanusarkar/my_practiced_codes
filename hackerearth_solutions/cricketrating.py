##India is a cricket crazy nation. Chang also loves cricket and computations
##related to cricket. Chang has created a Cricket app.This app analyses the
##performance of a cricketer. If a cricketer under-performs, then a negative
##rating is awarded. If performance is good, then positive rating is awarded
##to the cricketer.Chang wants to analyse the performance of a cricketer over
##a period of N matches. Chang wants to find consistency of a cricketer. So
##he wants to find out the maximum consistent sum of cricket rating of a
##batsman or a bowler only if his overall rating is positive over that period.
##Help chang in doing so.
##
##Input
##The first line contain number of matches "N" over which the analysis is to
##be done. The second line contains those ratings of a batsman/bowler in those
##N matches.
##
##Output
##Print a single integer ie. the maximum consistent sum of rating of the
##cricketer if it is positive otherwise output 0 (zero).
##
##Constraint
##0 <= N(matches) <= 10^5
##-100 <= rating <= +100

n = int(raw_input())
ratings = raw_input()
ratings = ratings.split()
a = 0
b = 0
y = len(ratings)
for x in range(0, y):
    if int(ratings[x]) > 0:
        a = x
        break
for x in range(0, y):
    if int(ratings[x]) > 0:
        b = x
sum = 0
for x in range(a, b+1):
    sum = sum + int(ratings[x])
if sum < 0:
    print '0'
else:
    print sum
