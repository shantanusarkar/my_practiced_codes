def palindrome(num):
    if num[::-1] == num:
       return True
    else:
       return False
n = int(raw_input())
for x in range(0, n):
    a = raw_input()
    a = a.split()
    m = int(a[0])
    n = int(a[1])
    count = 0
    for y in range(m, n+1):
        if palindrome(str(y)) == True:
            count += 1
    print count