month = int(input('Введите номер месяца:'))

def season(num):
    if month == 1 or month == 2 or month == 12:
        print('Зима')
    elif month == 3 or month == 4 or month == 5:
        print('Весна')
    elif month == 6 or month == 7 or month == 8:
        print('Лето')
    elif month == 9 or month == 10 or month == 11:
        print('Осень')
    else:
        print('ОШИБКА. Введите число от 1 до 12')

season(month)

# def season(month):
#     if month == 1 or month == 2 or month == 12:
#         return "Зима"
#     elif month == 3 or month == 4 or month == 5:
#         return "Весна"
#     elif month == 6 or month == 7 or month == 8:
#         return "Лето"
#     elif month == 9 or month == 10 or month == 11:
#         return "Осень"
#     else:
#         return 'ОШИБКА. Введите число от 1 до 12'
#
# print(season(month))