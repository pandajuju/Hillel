numbers = int(input())
number_1 = numbers//100
number_2 = (numbers%100)//10
number_3 = numbers%10
print(number_3, number_2, number_1, sep = '')