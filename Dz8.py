month = int(input('Введите номер месяца:'))

def season(num):
    if month == 1 or month == 2 or month == 12:
        print('Зима')
        if month == 1:
            print('Январь')
        elif month == 2:
            print('Февраль')
        else:
            print('Декабрь')
    elif month == 3 or month == 4 or month == 5:
        print('Весна')
        if month == 3:
            print('Март')
        elif month == 4:
            print('Апрель')
        else:
            print('Май')
    elif month == 6 or month == 7 or month == 8:
        print('Лето')
        if month == 6:
            print('Июнь')
        elif month == 7:
            print('Июль')
        else:
            print('Август')
    elif month == 9 or month == 10 or month == 11:
        print('Осень')
        if month == 9:
            print('Сентябрь')
        elif month == 10:
            print('Октябрь')
        else:
            print('Ноябрь')
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