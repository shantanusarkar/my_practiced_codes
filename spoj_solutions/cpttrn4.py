## link to the question: http://www.spoj.com/BSCPROG/problems/CPTTRN4/
## Author: Shantanu Sarkar
import sys
t = int(raw_input())
for x in range(0, t):
    a = raw_input()
    a = a.split(' ')
    l = int(a[0])
    c = int(a[1])
    d = int(a[2])
    e = int(a[3])
    for y in range(0, (l*(d+1))+1):
        for z in range(0, (c*(e+1))+1):
            if y == 0 or y % (d+1) == 0 or z == 0 or z % (e+1) == 0:
                sys.stdout.write('*')
            else:
                sys.stdout.write('.')
        print "\n"
    print "\n"

