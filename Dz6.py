list = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(list)):
    list[i - 1] = list[i]
list.pop()
print(''.join([str(i) for i in list]))