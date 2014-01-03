## link to the question: http://www.spoj.com/BSCPROG/problems/CPTTRN2/
## Author: Shantanu Sarkar
import sys
t = int(raw_input())
for x in range(0, t):
    a = raw_input()
    a = a.split(' ')
    l = int(a[0])
    c = int(a[1])
    for y in range(0, l):
        for z in range(0, c):
            if y == 0 or y == l-1 or z == 0 or z == c-1:
                sys.stdout.write('*')
            else:
                sys.stdout.write('.')
        print "\n"
    print "\n"
