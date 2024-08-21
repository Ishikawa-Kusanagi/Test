def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

def list_of_numbers(n: int) -> list:
    i = 1
    my_str = []
    for i in range(i, n + 1):
        my_str.append(i)
    return my_str

def check_month(month: int):
    if month == 9 or month == 10 or month == 11:
        result = 'Осень'
    elif month == 1 or month == 2 or month == 12:
        result = 'Зима'
    elif month == 3 or month == 4 or month == 5:
        result = 'Весна'
    elif month == 6 or month == 7 or month == 8:
        result = 'Лето'
    else:
        result = 'Некорректный номер месяца'
    return result
