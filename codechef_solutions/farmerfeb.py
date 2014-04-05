##Farmer Feb has three fields with potatoes planted in them. He harvested x
##potatoes from the first field, y potatoes from the second field and is yet
##to harvest potatoes from the third field. Feb is very superstitious and
##believes that if the sum of potatoes he harvests from the three fields is a
##prime number (http://en.wikipedia.org/wiki/Prime_number), he'll make a huge
##profit. Please help him by calculating for him the minimum number of
##potatoes that if harvested from the third field will make the sum of
##potatoes prime. At least one potato should be harvested from the third field.
##
##Input
##The first line of the input contains an integer T denoting the number of 
##test cases. Each of the next T lines contain 2 integers separated by single
##space: x and y.
## 
##Output
##For each test case, output a single line containing the answer.
## 
##Constraints
##1 ≤ T ≤ 1000
##1 ≤ x ≤ 1000
##1 ≤ y ≤ 1000

def isprime(n):
    for x in xrange(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True

t = int(raw_input())
for x in range(0, t):
    a = raw_input()
    a = a.split()
    sum = int(a[0]) + int(a[1])
    check = False
    while check == False:
        check = isprime(sum + 1)
        if check == False:
            sum += 1
    result = (sum +1) - (int(a[0]) + int(a[1]))
    print result
