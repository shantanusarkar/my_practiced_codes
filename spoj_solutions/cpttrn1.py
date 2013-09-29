## link to the question: http://www.spoj.com/BSCPROG/problems/CPTTRN1/
## Author: Shantanu Sarkar
import sys
a = []
b = []
s = 0
c = '*'
d = '.'
t = int(raw_input())
for x in range(0,t):
    a = raw_input()
    a = a.split()
    for z in a:
       b.append(z)
for x in range(0,t):
    for x in range(0, int(b[s])):
        for y in range(0, int(b[s+1])):
            if (x+y)%2 == 0:
                sys.stdout.write(c)
            else:
                sys.stdout.write(d)
        print("\n")
    s+=2
    
