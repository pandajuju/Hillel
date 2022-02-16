N = int(input())
two_to_the_power = 2
power = 1
while two_to_the_power <= N:
    two_to_the_power *= 2
    power += 1
print(power - 1, two_to_the_power // 2)