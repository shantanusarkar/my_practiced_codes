number = 0
while(number != eof)
    number = int(raw_input())
    part_1 = int(number/2) + int(number/3) + int(number/4)
    if part_1 > number:
        print part_1
    else:
        print number