##Levy's conjecture, named after Hyman Levy, states that all odd integers
##greater than 5 can be represented as the sum of an odd prime number and an
##even semiprime. To put it algebraically, 2n + 1 = p + 2q always has a
##solution in primes p and q (not necessary to be distinct) for n > 2.
##In this problem, given a positive integer N (not necessary to be odd integer
##greater than 5). Your task is to calculate how many distinct ordered pairs
##(p, q) such that N = p + 2q, where p and q are primes.
##
##Input
##The first line of input contains an integer T, denoting the number of test
##cases. Then T test cases follow.
##Each test case consists of exactly one line containing an integer N.
##
##Constraints
##1 ≤ T ≤ 100000 (105)
##1 ≤ N ≤ 10000 (104)
##
##Output
##For each test case, output the number of ordered pairs (p, q) of primes
##such that N = p + 2q.

def primes(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

t = int(raw_input())
for x in range(0, t):
    num = int(raw_input())
    l = primes(num)
    total = len(l)
    result = []
    for y in range(0, total):
        for z in range(0, total):
            if int(l[y]) + (2 * int(l[z])) == num:
                if l[y] and l[z] not in result:
                    result.append(l[y])
                    result.append(l[z])
    print len(result) / 2
