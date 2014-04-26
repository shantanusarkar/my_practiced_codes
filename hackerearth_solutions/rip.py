t = int(raw_input())
for x in range(0, t):
    a = raw_input()
    if a.__contains__('21') == True or int(a) % 21 == 0:
        print "The streak is broken!"
    else:
        print "The streak lives still in our heart!"