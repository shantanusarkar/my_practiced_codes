test_case = int(raw_input())
strength = raw_input()
strength = strength.split()
strength = sorted(strength)
calories = raw_input()
calories = calories.split()
calories = sorted(calories)
value = 0
for x in range(0, test_case):
    value = value + (int(strength[x])*int(calories[x]))
print value