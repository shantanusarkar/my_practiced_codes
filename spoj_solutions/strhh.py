## link to question: http://www.spoj.com/BSCPROG/problems/STRHH/
## Author: Shantanu Sarkar
t = int(raw_input())
for x in range(0,t):
    a = raw_input()
    l = len(a)
    a = a.strip()
    h = l/2
    print a[:h:2]
